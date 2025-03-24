import React, { useState } from 'react';
import { 
  Container, 
  TextField, 
  Select, 
  MenuItem, 
  FormControl,
  InputLabel,
  Card,
  CardContent,
  Typography,
  Button,
  Stack,
  Snackbar,
  Alert,
  CircularProgress
} from '@mui/material';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';

interface Tweet {
  content: string;
  title: string;
  url: string;
}

function App() {
  const [channelId, setChannelId] = useState('');
  const [aiProvider, setAiProvider] = useState('claude');
  const [apiKey, setApiKey] = useState('');
  const [tweets, setTweets] = useState<Tweet[]>([]);
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');
  const [snackbarSeverity, setSnackbarSeverity] = useState<'success' | 'error'>('success');
  const [loading, setLoading] = useState(false);

  const showNotification = (message: string, severity: 'success' | 'error') => {
    setSnackbarMessage(message);
    setSnackbarSeverity(severity);
    setSnackbarOpen(true);
  };

  const handleGenerateTweets = async () => {
    setLoading(true);
    try {
      // First check if the server is running
      const healthCheck = await fetch('http://localhost:8000/');
      if (!healthCheck.ok) {
        throw new Error('Server is not responding');
      }

      const response = await fetch('http://localhost:8000/generate-tweets', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          channelId,
          provider: aiProvider,
          apiKey,
        }),
      });
      
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.error || 'Failed to generate tweets');
      }
      
      setTweets(data.tweets);
      showNotification('Tweets generated successfully!', 'success');
    } catch (error) {
      console.error('Error generating tweets:', error);
      showNotification(error instanceof Error ? error.message : 'An error occurred', 'error');
      setTweets([]);
    } finally {
      setLoading(false);
    }
  };

  const handleCopyTweet = (content: string) => {
    navigator.clipboard.writeText(content);
    showNotification('Tweet copied to clipboard!', 'success');
  };

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        YouTube Tweet Generator
      </Typography>
      
      <Stack spacing={3}>
        <TextField
          fullWidth
          label="YouTube Channel ID"
          value={channelId}
          onChange={(e) => setChannelId(e.target.value)}
          placeholder="Enter YouTube Channel ID"
          disabled={loading}
        />
        
        <FormControl fullWidth>
          <InputLabel>AI Provider</InputLabel>
          <Select
            value={aiProvider}
            label="AI Provider"
            onChange={(e) => setAiProvider(e.target.value)}
            disabled={loading}
          >
            <MenuItem value="claude">Claude</MenuItem>
            <MenuItem value="deepseek">DeepSeek</MenuItem>
          </Select>
        </FormControl>
        
        <TextField
          fullWidth
          label="API Key"
          type="password"
          value={apiKey}
          onChange={(e) => setApiKey(e.target.value)}
          placeholder={`Enter ${aiProvider === 'claude' ? 'Claude' : 'DeepSeek'} API Key`}
          disabled={loading}
        />
        
        <Button 
          variant="contained" 
          onClick={handleGenerateTweets}
          disabled={!channelId || !apiKey || loading}
          startIcon={loading ? <CircularProgress size={20} color="inherit" /> : null}
        >
          {loading ? 'Generating...' : 'Generate Tweets'}
        </Button>
        
        {tweets.map((tweet, index) => (
          <Card key={index}>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                {tweet.title}
              </Typography>
              <Typography variant="body1" sx={{ mb: 2 }}>
                {tweet.content}
              </Typography>
              <Button
                startIcon={<ContentCopyIcon />}
                onClick={() => handleCopyTweet(tweet.content)}
                variant="outlined"
                disabled={loading}
              >
                Copy Tweet
              </Button>
            </CardContent>
          </Card>
        ))}
      </Stack>

      <Snackbar
        open={snackbarOpen}
        autoHideDuration={3000}
        onClose={() => setSnackbarOpen(false)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert 
          onClose={() => setSnackbarOpen(false)} 
          severity={snackbarSeverity}
          sx={{ width: '100%' }}
        >
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </Container>
  );
}

export default App; 