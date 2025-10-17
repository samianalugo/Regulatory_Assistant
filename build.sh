#!/bin/bash
set -e

echo "Starting build process..."
echo "Current directory: $(pwd)"
echo "Listing files:"
ls -la

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Building frontend..."
cd frontend
npm install
npm run build

echo "Build completed successfully!"
