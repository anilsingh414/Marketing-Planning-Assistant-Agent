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

# 🔘 Alternative: Deploy on Render.com

Render is a great alternative to Streamlit Cloud. Here is how to use the "Blueprint" I just created for you:

## Step 1: Link your Repo
1.  Go to [dashboard.render.com](https://dashboard.render.com) and log in with GitHub.
2.  Click **"New +"** -> **"Blueprint"**.
3.  Select your `Marketing-Planning-Assistant-Agent` repository.

## Step 2: Configure Environment
Render will automatically detect the `render.yaml` file I added.
1.  It will ask you for a **`GEMINI_API_KEY`**.
2.  Paste your key: `AIzaSyA8Pb96OqYx1FijR3aB8zcweS4uO2F4E7Q`
3.  Click **"Apply"**.

## Step 3: Wait for Build
Render will install your dependencies and start the app. Once finished, you will get a URL like `https://marketing-planner.onrender.com`.

> [!TIP]
> **Important for Render Free Tier**:
> The first time you visit the site, it might take a minute to "wake up" the server if it hasn't been used recently. This is normal for the free tier.
