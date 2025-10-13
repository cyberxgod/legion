#!/bin/bash
echo "Starting frontend server on http://localhost:8081"
echo ""
echo "Open http://localhost:8081 in your browser"
echo ""
cd Shopifyweb.py
python3 -m http.server 8081
