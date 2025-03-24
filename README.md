# YouTube Tweet Generator

A web application that generates tweet suggestions based on YouTube channel content using AI (Claude or DeepSeek).

## Prerequisites

- Python 3.11 or higher
- Node.js (with npm)
- Virtual environment tool (venv)

## Setup

### Backend Setup

1. Create and activate a Python virtual environment:
```bash
python -m venv venv-3.11
source venv-3.11/bin/activate  # On Unix/macOS
# or
.\venv-3.11\Scripts\activate  # On Windows
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
Create a `.env` file in the root directory with:
```
DEEPSEEK_API_KEY=your_deepseek_api_key
CLAUDE_API_KEY=your_claude_api_key
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

## Running the Application

1. Start the Flask backend server (from the project root):
```bash
cd src
python server.py
```
The backend will run on http://localhost:8000

2. In a new terminal, start the React frontend (from the project root):
```bash
cd frontend
npm start
```
The frontend will run on http://localhost:3000

## Usage

1. Open your browser and navigate to http://localhost:3000
2. Enter a YouTube Channel ID in the input field
3. Select your preferred AI provider (Claude or DeepSeek)
4. Enter your API key for the selected provider
5. Click "Generate Tweets" to create tweet suggestions
6. Use the copy button on each tweet card to copy the content to your clipboard

## Features

- Generate tweet suggestions based on YouTube channel content
- Support for multiple AI providers (Claude and DeepSeek)
- Modern Material-UI interface
- Copy-to-clipboard functionality
- Real-time error handling and loading states
- Responsive design

## Development Notes

- The backend runs on port 8000 to avoid conflicts with macOS AirPlay
- Frontend development server uses legacy OpenSSL provider for compatibility
- Debug mode is enabled on the backend for development purposes

## Troubleshooting

- If port 8000 is in use, you can modify the port in `src/server.py`
- If you encounter OpenSSL issues with the frontend, the start script includes the necessary legacy provider flag
- Check the browser console and terminal for detailed error messages 