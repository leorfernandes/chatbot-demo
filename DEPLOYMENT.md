# Deployment Instructions

## Render Deployment (Recommended - Completely Free)

### Prerequisites
- GitHub account
- Git repository pushed to GitHub

### Steps

1. **Push to GitHub (if not already done):**
   ```bash
   git remote add origin https://github.com/yourusername/chatbot-demo.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub (no credit card required)
   - Click "New Web Service"
   - Connect your GitHub repository: `chatbot-demo`
   
3. **Configure deployment settings:**
   - **Name:** `firstep-chatbot-demo` (or your preferred name)
   - **Root Directory:** Leave blank (uses repository root)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `cd backend && python app.py`
   - **Instance Type:** `Free`

4. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - You'll get a live URL like: `https://your-app-name.onrender.com`

### Features of Render Free Tier:
- ✅ Completely free (no credit card required)
- ✅ 750 hours/month (plenty for demos)
- ✅ Custom domain support
- ✅ Automatic deploys from GitHub
- ⚠️ Apps sleep after 15 minutes of inactivity (30-60 second wake-up time)

### Pro Tips:
- **For interviews:** Visit your app URL 2-3 minutes before the demo to wake it up
- **Auto-deploy:** Any push to your main branch will automatically redeploy
- **Logs:** Check the Render dashboard for deployment logs if issues occur

## Alternative Options

### Railway (Paid - $5 monthly credit)
- Faster performance (no sleeping)
- Better for production use
- $5/month covers most demo applications

### Heroku (Paid - $7/month minimum)
- Traditional choice but requires payment
- Good documentation and ecosystem

### Prerequisites
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
- Git repository initialized

### Steps

1. **Initialize Git (if not already done):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create Heroku app:**
   ```bash
   heroku create your-chatbot-demo
   ```

3. **Deploy:**
   ```bash
   git push heroku main
   ```

4. **Open your app:**
   ```bash
   heroku open
   ```

### Files Added for Heroku:
- `Procfile`: Tells Heroku how to run your app
- `runtime.txt`: Specifies Python version
- Updated `app.py`: Uses PORT environment variable

## Option 2: Railway (Alternative)

1. **Connect to GitHub:**
   - Push code to GitHub repository
   - Connect Railway to your GitHub repo

2. **Deploy:**
   - Railway auto-detects Flask app
   - Uses requirements.txt automatically
   - Sets PORT environment variable

## Option 3: Render (Free tier available)

1. **Create Render account**
2. **Connect GitHub repository**
3. **Set build command:** `pip install -r backend/requirements.txt`
4. **Set start command:** `python backend/app.py`

## Note on Vercel

Vercel is optimized for frontend and Node.js serverless functions. While possible to deploy Python, it's not ideal for this Flask application structure. The recommended options above are better suited for Flask apps.

## Environment Variables

For production deployment, consider setting:
- `FLASK_ENV=production`
- `DEBUG=False` (already set in app.py)

## Static Files

Your frontend files are served by Flask from the `../frontend` directory, so no additional static file hosting is needed.
