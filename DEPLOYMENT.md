# Deployment Instructions

## Option 1: Heroku (Recommended for Flask)

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
