#!/usr/bin/env python3
"""
WotNot Backend - Simple Startup Script for Render
Starts FastAPI Backend directly
"""

import os
import sys

def main():
    """Simple startup function for production"""
    print("=" * 60)
    print("🚀 WotNot Backend - Simple Startup")
    print("=" * 60)
    print()
    
    # Get port from environment (Render provides this)
    port = os.getenv('PORT', '8000')
    host = '0.0.0.0'  # Render requires binding to 0.0.0.0
    
    print(f"🌐 Starting FastAPI server on {host}:{port}")
    print("=" * 60)
    print()
    
    # Start FastAPI Backend directly (this will block and keep the process alive)
    os.execvp("python", ["python", "-m", "uvicorn", "wati.main:app", "--host", host, "--port", port])

if __name__ == "__main__":
    main()
