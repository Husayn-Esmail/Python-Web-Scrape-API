#!/bin/bash
# This script starts the fastapi server
# sets the port and ip address host to 0.0.0.0:5000
export UVICORN_PORT=5000

uvicorn main:app --host 0.0.0.0 --reload
