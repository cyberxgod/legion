#!/bin/bash
echo "Installing required packages..."
pip install -r requirements.txt

echo ""
echo "Starting backend server on http://localhost:5001"
echo ""
python3 backend.py
