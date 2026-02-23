# ☁️ Cloud Deployment Guide

This project is now "Cloud Ready"! Here is how you can deploy it to the internet for free using **Streamlit Community Cloud**.

## Step 1: Push to GitHub
1.  Create a new repository on [GitHub](https://github.com/new).
2.  Upload (or push) your project files to that repository.
    > [!IMPORTANT]
    > My updated `.gitignore` will ensure your private `SETTINGS` folder and `.env` files are NOT uploaded.

## Step 2: Deploy to Streamlit Cloud
1.  Go to [share.streamlit.io](https://share.streamlit.io) and log in with GitHub.
2.  Click **"New app"**.
3.  Select your repository, the branch (usually `main`), and the main file path: **`app.py`**.

## Step 3: Set Your API Key (Secrets)
Before clicking "Deploy", click **"Advanced settings..."** (or go to the app settings after deploying):
1.  In the **Secrets** section, paste the following:
    ```toml
    GEMINI_API_KEY = "YOUR_NEW_API_KEY_HERE"
    MODEL_NAME = "gemini-flash-latest"
    ```
2.  Save and deploy!

## Why This Works?
I've updated the code in `agents.py` to automatically detect if it's running in the cloud. It will prioritize the key you enter in the Streamlit Dashboard over local files.

---

### Alternative: Deployment on Render / Hugging Face
If you prefer other platforms, ensure you set the **`GEMINI_API_KEY`** and **`MODEL_NAME`** as **Environment Variables** in their respective dashboards.
