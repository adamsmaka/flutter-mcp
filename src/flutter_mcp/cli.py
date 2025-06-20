#!/usr/bin/env python3
"""CLI entry point for Flutter MCP Server"""

import sys
import argparse
import os
from typing import Optional
import asyncio

# Add version info
__version__ = "0.1.0"


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        prog='flutter-mcp',
        description='Flutter MCP Server - Real-time Flutter/Dart documentation for AI assistants',
        epilog='For more information, visit: https://github.com/flutter-mcp/flutter-mcp'
    )
    
    parser.add_argument(
        'command',
        choices=['start', 'serve', 'dev', 'version', 'help'],
        nargs='?',
        default='start',
        help='Command to run (default: start)'
    )
    
    parser.add_argument(
        '--cache-dir',
        default=None,
        help='Custom cache directory (default: platform-specific)'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug logging'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )
    
    args = parser.parse_args()
    
    # Handle commands
    if args.command == 'version':
        print(f"Flutter MCP Server v{__version__}", file=sys.stderr)
        sys.exit(0)
    
    elif args.command == 'help':
        parser.print_help(sys.stderr)
        sys.exit(0)
    
    elif args.command == 'dev':
        # Run with MCP Inspector
        print("🚀 Starting Flutter MCP Server with MCP Inspector...", file=sys.stderr)
        print("📝 Opening browser at http://localhost:5173", file=sys.stderr)
        print("⚡ Use Ctrl+C to stop the server\n", file=sys.stderr)
        
        import subprocess
        try:
            # Set environment variables
            env = os.environ.copy()
            if args.cache_dir:
                env['CACHE_DIR'] = args.cache_dir
            if args.debug:
                env['DEBUG'] = '1'
            
            subprocess.run(['mcp', 'dev', 'src/flutter_mcp/server.py'], env=env)
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped", file=sys.stderr)
        except FileNotFoundError:
            print("❌ Error: MCP CLI not found. Please install with: pip install 'mcp[cli]'", file=sys.stderr)
            sys.exit(1)
    
    else:  # start or serve
        # Run the server directly
        # Print cool header using rich
        from flutter_mcp.logging_utils import print_server_header
        print_server_header()
        
        from rich.console import Console
        console = Console(stderr=True)
        
        console.print(f"\n[bold green]🚀 Starting Flutter MCP Server v{__version__}[/bold green]")
        console.print("[cyan]📦 Using built-in SQLite cache[/cyan]")
        if args.cache_dir:
            console.print(f"[dim]💾 Cache directory: {args.cache_dir}[/dim]")
        
        console.print("[yellow]⚡ Server running - connect your AI assistant[/yellow]")
        console.print("[yellow]⚡ Use Ctrl+C to stop the server[/yellow]\n")
        
        # Set environment variables
        if args.cache_dir:
            os.environ['CACHE_DIR'] = args.cache_dir
        if args.debug:
            os.environ['DEBUG'] = '1'
        
        # Set flag to indicate we're running from CLI
        sys._flutter_mcp_cli = True
        
        try:
            # Import and run the server
            from . import main as server_main
            server_main()
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped", file=sys.stderr)
        except ImportError as e:
            print(f"❌ Error: Failed to import server: {e}", file=sys.stderr)
            print("Make sure you're in the correct directory and dependencies are installed", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()