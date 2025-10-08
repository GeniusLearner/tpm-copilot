# TPM Co-Pilot: Quick Start Guide

Get up and running in 5 minutes.

---

## ⚡ 5-Minute Setup

### 1. Install Python

**Check if you have Python 3.9+:**
```bash
python --version
```

**Don't have Python?** Download from [python.org](https://www.python.org/downloads/)

### 2. Clone & Install

```bash
# Clone repository
git clone https://github.com/GeniusLearner/tpm-copilot.git
cd tpm-copilot

# Install dependencies
pip install -r requirements.txt
```

### 3. Get API Key

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up (it's free)
3. Create an API key
4. Copy it (starts with `sk-ant-api03-...`)

### 4. Configure

```bash
# Copy example env file
cp .env.example .env

# Edit .env and paste your API key
# On Mac/Linux:
nano .env

# On Windows:
notepad .env
```

Add your key:
```
ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```

### 5. Run

```bash
streamlit run app.py
```

**Done!** App opens at `http://localhost:8501` 🎉

---

## 🚀 Your First Document

### Generate a Meeting Agenda

1. Click **"Meeting Agenda Generator"** in sidebar
2. Click **"See example templates"**
3. Select **"Sprint Planning"**
4. Click **"Generate Agenda"**
5. Wait ~10 seconds
6. **Download** the result

**Boom!** You just saved 30 minutes.

---

## 📚 What to Try Next

### 1. Thread Summarizer
- Copy a Slack or email thread
- Paste into "Thread Summarizer"
- Get instant TLDR + action items

### 2. Status Report Builder
- Write bullet points of your weekly updates
- Generate executive-ready report
- Send to your manager

### 3. Risk Analyzer
- Describe your project
- Get comprehensive risk analysis
- Use in project planning

### 4. Project Charter Creator
- Provide high-level project info
- Generate full charter
- Use in kickoff meetings

---

## 💡 Pro Tips

**1. Use Templates**
- Every tool has example templates
- Click "See example templates" to load them
- Modify the template for your use case

**2. Iterate**
- Generated output not perfect? No problem.
- Tweak your input and regenerate
- Usually get it right in 1-2 tries

**3. Download Everything**
- All outputs can be downloaded as .md or .txt
- Save to your docs folder
- Build a library of your best outputs

**4. Customize for Your Team**
- AI learns from the context you provide
- More specific input = better output
- Include your team's terminology

---

## 🎯 Use Cases

**Daily:**
- Summarize Slack threads before replying
- Generate agendas for recurring meetings

**Weekly:**
- Create status reports for leadership
- Review risks for ongoing projects

**Monthly:**
- Draft project charters for new initiatives
- Prepare quarterly business reviews

**Potential time saved:** 8-10 hours/week

---

## ❓ Troubleshooting

**"API key not found"**
- Check `.env` file exists
- Verify API key is correct
- Restart the app

**"Generation taking forever"**
- Check your internet connection
- Verify API key is valid
- Wait 30 seconds max (usually ~10 sec)

**"Module not found"**
- Run: `pip install -r requirements.txt`
- Make sure you're in the right directory

**Still stuck?**
- Read full [Deployment Guide](docs/deployment.md)
- Check [GitHub Issues](https://github.com/GeniusLearner/tpm-copilot/issues)

---

## 🌟 Next Steps

**After you've tried all the tools:**

1. **Share with colleagues**
   - Invite other TPMs to try it
   - Gather feedback

2. **Add to portfolio**
   - Include in resume
   - Use in job interviews

3. **Contribute**
   - Found a bug? Open an issue
   - Have an idea? Submit a PR
   - Help make it better!

---

## 📖 Additional Resources

- **[Full README](README.md)** - Complete documentation
- **[Example Outputs](docs/examples.md)** - See what's possible
- **[Deployment Guide](docs/deployment.md)** - Deploy to cloud

---

**Enjoy using TPM Co-Pilot!**

*Questions? Open an issue on GitHub.*
