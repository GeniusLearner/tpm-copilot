# TPM Co-Pilot: Deployment & Setup Guide

Complete guide for deploying TPM Co-Pilot locally and to the cloud.

---

## Table of Contents

1. [Local Development Setup](#local-development-setup)
2. [Cloud Deployment (Streamlit Cloud)](#cloud-deployment-streamlit-cloud)
3. [Alternative Deployments](#alternative-deployments)
4. [Troubleshooting](#troubleshooting)
5. [Production Considerations](#production-considerations)

---

## Local Development Setup

### Prerequisites

Before starting, ensure you have:

- **Python 3.9 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package installer, comes with Python)
- **Git** (for cloning the repository)
- **Anthropic API Key** ([Get one here](https://console.anthropic.com/))

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/GeniusLearner/tpm-copilot.git
cd tpm-copilot
```

#### 2. Create Virtual Environment (Recommended)

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `anthropic` - Claude API client
- `streamlit` - Web UI framework
- `python-dotenv` - Environment variable management

#### 4. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env
```

Edit `.env` file and add your API key:

```bash
# Open in your preferred editor
nano .env   # or vim .env, or code .env
```

Replace the placeholder with your actual API key:

```
ANTHROPIC_API_KEY=sk-ant-api03-your-actual-key-here
```

**How to get your Anthropic API key:**
1. Go to [https://console.anthropic.com/](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to "API Keys"
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-api03-...`)

#### 5. Test the Installation

Run the core agent test:

```bash
python tpm_agent.py
```

You should see output like:
```
🤖 TPM Co-Pilot - Testing Core Functions
============================================================

1. Testing Meeting Agenda Generator...
# Sprint Planning Meeting...

2. Testing Thread Summarizer...
# Thread Summary...

✅ All core functions working!
```

If you see errors, check:
- API key is correct in `.env`
- Python version is 3.9+
- All dependencies are installed

#### 6. Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

**If it doesn't open automatically:**
1. Look for the URL in the terminal output
2. Copy and paste it into your browser

#### 7. Verify Everything Works

1. Navigate to "Meeting Agenda Generator"
2. Enter some sample text
3. Click "Generate Agenda"
4. You should see a structured agenda appear in ~10 seconds

**Success!** You're now running TPM Co-Pilot locally.

---

## Cloud Deployment (Streamlit Cloud)

Deploy TPM Co-Pilot to the cloud for free using Streamlit Cloud.

### Prerequisites

- GitHub account
- Anthropic API key
- TPM Co-Pilot code pushed to GitHub

### Step-by-Step Deployment

#### 1. Push Code to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: TPM Co-Pilot"

# Create a new repository on GitHub (via web UI)
# Then link it:
git remote add origin https://github.com/GeniusLearner/tpm-copilot.git
git branch -M main
git push -u origin main
```

#### 2. Deploy to Streamlit Cloud

1. **Go to [share.streamlit.io](https://share.streamlit.io/)**

2. **Click "New app"**

3. **Fill in deployment settings:**
   - **Repository:** `GeniusLearner/tpm-copilot`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL:** `tpm-copilot` (or your preferred name)

4. **Add secrets (API key):**
   - Click "Advanced settings"
   - In "Secrets" section, add:
     ```toml
     ANTHROPIC_API_KEY = "sk-ant-api03-your-actual-key-here"
     ```

5. **Click "Deploy"**

Streamlit Cloud will:
- Clone your repository
- Install dependencies from `requirements.txt`
- Start the app
- Provide a public URL like `https://tpm-copilot.streamlit.app/`

#### 3. Verify Deployment

1. Visit your app URL
2. Test all 5 tools
3. Ensure API key is working (no errors)

**Your app is now live!** 🎉

### Updating the Deployed App

Any time you push changes to GitHub, Streamlit Cloud will automatically redeploy:

```bash
# Make changes to code
git add .
git commit -m "Update: improved prompts"
git push

# Streamlit Cloud will auto-deploy in ~2 minutes
```

### Monitoring Usage

**Streamlit Cloud Free Tier Limits:**
- Unlimited apps
- 1 GB RAM per app
- Limited CPU
- Apps sleep after inactivity (wake up on first request)

**Claude API Free Tier:**
- Check usage at [console.anthropic.com](https://console.anthropic.com/)
- Monitor costs (typically $0.02-0.05 per generation)

---

## Alternative Deployments

### Option 1: Heroku

```bash
# Install Heroku CLI
brew install heroku/brew/heroku  # macOS
# or download from heroku.com

# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Create runtime.txt
echo "python-3.9.16" > runtime.txt

# Deploy
heroku create tpm-copilot
heroku config:set ANTHROPIC_API_KEY=your-key-here
git push heroku main
heroku open
```

### Option 2: AWS EC2

```bash
# SSH into EC2 instance
ssh -i key.pem ubuntu@your-ec2-ip

# Install dependencies
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt

# Set environment variable
export ANTHROPIC_API_KEY=your-key-here

# Run with screen (keeps running after disconnect)
screen -S tpm-copilot
streamlit run app.py --server.port=80 --server.address=0.0.0.0
# Press Ctrl+A, then D to detach
```

### Option 3: Docker

```dockerfile
# Create Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
# Build and run
docker build -t tpm-copilot .
docker run -p 8501:8501 -e ANTHROPIC_API_KEY=your-key tpm-copilot
```

### Option 4: Google Cloud Run

```bash
# Install gcloud CLI
gcloud init

# Build container
gcloud builds submit --tag gcr.io/your-project/tpm-copilot

# Deploy
gcloud run deploy tpm-copilot \
  --image gcr.io/your-project/tpm-copilot \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars ANTHROPIC_API_KEY=your-key
```

---

## Troubleshooting

### Common Issues

#### Issue 1: "ANTHROPIC_API_KEY not found"

**Symptom:**
```
ValueError: ANTHROPIC_API_KEY not found. Please set it in .env file.
```

**Solution:**
1. Ensure `.env` file exists in project root
2. Check API key is correctly formatted:
   ```
   ANTHROPIC_API_KEY=sk-ant-api03-xxxxx
   ```
3. Restart the app: `streamlit run app.py`

---

#### Issue 2: "Module not found" Error

**Symptom:**
```
ModuleNotFoundError: No module named 'anthropic'
```

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

---

#### Issue 3: Slow Generation Times

**Symptom:**
Generations take >30 seconds

**Possible causes:**
1. **Slow internet connection** - Claude API requires internet
2. **API rate limits** - You've hit your usage limit
3. **High API load** - Anthropic's servers are busy

**Solutions:**
- Check internet connection
- Verify API key is valid at console.anthropic.com
- Wait a few minutes and try again

---

#### Issue 4: "Error calling Claude API"

**Symptom:**
```
Error calling Claude API: [error message]
```

**Common causes:**
1. **Invalid API key** - Check it's correct
2. **Exceeded quota** - Check usage at console.anthropic.com
3. **Network issues** - Check internet connection

**Debug:**
```bash
# Test API key directly
python
>>> from anthropic import Anthropic
>>> client = Anthropic(api_key="your-key")
>>> message = client.messages.create(
...     model="claude-3-5-sonnet-20241022",
...     max_tokens=100,
...     messages=[{"role": "user", "content": "Hi"}]
... )
>>> print(message.content[0].text)
```

---

#### Issue 5: App Won't Start

**Symptom:**
```
streamlit: command not found
```

**Solution:**
```bash
# Check Python/pip installation
python --version  # Should be 3.9+
pip --version

# Reinstall streamlit
pip install streamlit

# Check it's in PATH
which streamlit
```

---

### Getting Help

**If you're still stuck:**

1. **Check the logs:**
   ```bash
   # Streamlit logs are in terminal
   # Look for error messages
   ```

2. **Test components individually:**
   ```bash
   python tpm_agent.py  # Test core agent
   streamlit hello      # Test Streamlit works
   ```

3. **Ask for help:**
   - Open an issue on GitHub
   - Include error message, OS, Python version

---

## Production Considerations

### Security

**For Production Deployment:**

1. **Never commit `.env` file**
   ```bash
   # Check .gitignore includes:
   .env
   ```

2. **Use environment variables**
   - Streamlit Cloud: Use Secrets
   - Heroku: `heroku config:set`
   - AWS: Use AWS Secrets Manager
   - Docker: Use `-e` flag or docker-compose secrets

3. **Rotate API keys regularly**
   - Generate new key every 90 days
   - Revoke old keys

4. **Monitor API usage**
   - Set up billing alerts
   - Track costs daily

### Performance

**Optimization Tips:**

1. **Caching:**
   ```python
   # Add to app.py for common queries
   @st.cache_data
   def generate_common_agenda(context):
       return st.session_state.copilot.generate_agenda(context)
   ```

2. **Rate limiting:**
   - Implement user-level rate limits
   - Prevent abuse

3. **Async processing:**
   - For high-traffic apps, use task queue
   - Return results via webhook

### Monitoring

**What to Track:**

1. **Usage metrics:**
   - Generations per day
   - Error rate
   - Average generation time

2. **Cost metrics:**
   - Claude API spend
   - Hosting costs

3. **User metrics:**
   - Active users
   - Feature usage breakdown

**Tools:**
- Streamlit Analytics (built-in)
- Google Analytics
- Custom logging to database

### Scaling

**If you outgrow Streamlit Cloud:**

1. **Upgrade to dedicated hosting**
   - AWS EC2 / Google Cloud Run
   - More RAM, CPU

2. **Add database**
   - Store user history
   - Save templates
   - Track analytics

3. **Implement authentication**
   - User accounts
   - Usage quotas
   - Payment system

4. **Build API**
   - RESTful API for programmatic access
   - Webhooks for async processing

---

## Cost Estimation

### Monthly Costs (estimated)

**Personal Use (10-50 generations/month):**
- Anthropic API: $1-5
- Streamlit Cloud: $0 (free tier)
- **Total: $1-5/month**

**Team Use (500 generations/month):**
- Anthropic API: $50-100
- Streamlit Cloud: $0 (free tier sufficient)
- **Total: $50-100/month**

**Production (5000+ generations/month):**
- Anthropic API: $500-1000
- Hosting (AWS/GCP): $50-200
- Database: $20-50
- Monitoring: $20
- **Total: $590-1270/month**

**Price breakdown:**
- Claude API: ~$0.01-0.02 per generation (varies by length)
- Streamlit Cloud: Free tier generous
- Upgrades only needed at scale

---

## Next Steps

**You're all set!** 🚀

**After deployment:**
1. ✅ Share the URL with beta testers
2. ✅ Gather feedback
3. ✅ Iterate on prompts
4. ✅ Add to your resume/portfolio
5. ✅ Use in interviews!

**For more help:**
- Read [Streamlit Docs](https://docs.streamlit.io/)
- Read [Anthropic API Docs](https://docs.anthropic.com/)
- Check the [GitHub Issues](https://github.com/GeniusLearner/tpm-copilot/issues)

---

*Last updated: January 2025*
