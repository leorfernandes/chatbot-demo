# 🚀 Quick Render Deployment Guide

## Step-by-Step Instructions

### 1. Go to Render
- Visit [render.com](https://render.com)
- Click "Get Started for Free"
- Sign up with your GitHub account

### 2. Create New Web Service
- Click "New +" button
- Select "Web Service"
- Choose "Connect a repository"
- Find and select: `leorfernandes/chatbot-demo`

### 3. Configure Your Service
Fill in these settings exactly (copy and paste to avoid typos):

```
Name: family-compatibility-demo
Root Directory: (leave blank)
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: cd backend && python app.py
Instance Type: Free
```

⚠️ **IMPORTANT**: Make sure "Start Command" is exactly: `cd backend && python app.py`
(Double-check there's no typo like "backedn")

### 4. Deploy
- Click "Create Web Service"
- Wait 3-5 minutes for deployment
- You'll get a URL like: `https://family-compatibility-demo.onrender.com`

### 5. Test Your App
- Visit your URL
- Click "Start Onboarding Demo"
- Test the full flow!

## 🎯 For Your Interview

### Before the Demo:
1. **Wake up your app** - Visit the URL 2-3 minutes before your interview
2. **Test it quickly** - Make sure everything works
3. **Have the URL ready** - Share screen and navigate to your live demo

### During the Demo:
- Show the live, deployed application
- Explain the technology stack
- Walk through the matching algorithm
- Demonstrate the explainable AI features

## 📋 Troubleshooting

**If deployment fails:**
1. Check the build logs in Render dashboard
2. Ensure all files are pushed to GitHub
3. Verify the start command: `cd backend && python app.py`

**If app seems slow:**
- This is normal for free tier after 15 minutes of inactivity
- Simply wait 30-60 seconds for it to wake up

Your chatbot demo is now live and ready for interviews! 🎉
