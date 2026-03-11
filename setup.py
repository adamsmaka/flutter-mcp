#!/usr/bin/env python3
"""Setup script for Flutter MCP Server - for backward compatibility only.
Please use pip install with pyproject.toml for modern installations."""

from setuptools import setup, find_packages

# Read long description from README
with open("docs/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flutter-mcp-server",
    version="0.1.0",
    author="Flutter MCP Contributors",
    description="MCP server providing real-time Flutter/Dart documentation to AI assistants",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flutter-mcp/flutter-mcp",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=3.10",
    install_requires=[
        "aiofiles>=24.1.0",
        "beautifulsoup4>=4.13.4",
        "httpx>=0.28.1",
        "mcp>=1.25,<2",
        "platformdirs>=4.0.0",
        "structlog>=25.4.0",
    ],
    entry_points={
        "console_scripts": [
            "flutter-mcp=flutter_mcp.cli:main",
        ],
    },
)