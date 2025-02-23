#!/bin/bash

# Start the frontend development server
cd client && npm run dev &

# Start the backend server
cd ../server && npm start &

# Wait for any process to exit
wait

# Kill all processes on exit
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT 