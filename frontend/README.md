# YouTube Tweet Generator Frontend

A React-based frontend for generating tweets from YouTube videos using AI.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm start
```

The app will be available at http://localhost:3000

## Features

- Enter YouTube Channel ID to fetch recent videos
- Choose between Claude and DeepSeek AI providers
- Securely input API keys
- Generate tweets for recent videos
- Copy tweets to clipboard with one click
- Modern Material UI interface

## Backend Setup

The frontend requires the Flask backend to be running. To start the backend:

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Start the Flask server:
```bash
python src/server.py
```

The backend will be available at http://localhost:5000

## Environment Variables

No environment variables are needed for the frontend as all configuration is handled through the UI.

## Development

This project was bootstrapped with Create React App and uses:

- React 18
- TypeScript
- Material UI
- React Hooks 