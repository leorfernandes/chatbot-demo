# Deployment Instructions

## Option 1: Railway (Recommended - Free $5 credit monthly)

### Prerequisites
- GitHub account
- Git repository pushed to GitHub

### Steps

1. **Push to GitHub first:**
   ```bash
   git remote add origin https://github.com/yourusername/chatbot-demo.git
   git push -u origin main
   ```

2. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "Deploy from GitHub repo"
   - Select your `chatbot-demo` repository
   - Railway auto-detects Flask and deploys!

3. **Your app will be live in minutes!**

## Option 2: Render (Completely Free)

### Steps

1. **Push to GitHub** (same as above)

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub
   - Click "New Web Service"
   - Connect your GitHub repo
   - Set configuration:
     - **Build Command:** `pip install -r backend/requirements.txt`
     - **Start Command:** `python backend/app.py`

3. **Deploy and get your URL!**

## Option 3: Heroku (Paid - $7/month minimum)

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
