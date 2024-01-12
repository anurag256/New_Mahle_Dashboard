#!/bin/bash

source ./venv/bin/Activate.ps1

./venv/lib/python3.11/site-packages/streamlit run ./App.py --server.enableCORS false --server.enableWebsocketCompression false --server.enableXsrfProtection false --server.sslKeyFile key.pem --server.sslCertFile cert.pem
