#!/bin/bash
session="start-streamlit"

# Create a new session named "start-streamlit"
tmux new-session -d -s "$session"
# Tmux will ensure that the app will be running in the background.
# Run streamlit app on its webserver on port 8081 
tmux send-keys -t "$session" "streamlit run /vagrant/app/main.py --server.port=8081" Enter

# Attach to session
# tmux attach -t "$session"

# Kill session
# tmux kill-session -t "$session"