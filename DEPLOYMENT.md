# Streamlit Community Cloud Deployment Guide

## Quick Deployment Steps

### 1. Prepare Your Repository
- Ensure all files are committed to Git (GitHub, GitLab, or Bitbucket)
- Verify `app.py` is in the root directory
- Verify `requirements.txt` exists with all dependencies

### 2. Deploy to Streamlit Cloud

1. **Sign in**: Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your Git provider

2. **Create New App**:
   - Click "New app"
   - Select your repository
   - Select the branch (usually `main` or `master`)
   - Set main file path: `app.py`
   - Set app URL (optional, auto-generated if not provided)

3. **Deploy**:
   - Click "Deploy"
   - Wait for the build to complete (usually 1-2 minutes)

### 3. Verify Deployment

- The app will be available at: `https://your-app-name.streamlit.app`
- Check the logs for any errors
- Test all pages to ensure functionality

## File Structure Requirements

```
your-repo/
├── app.py                 # Main entry point (required)
├── requirements.txt       # Python dependencies (required)
├── pages/                 # Page modules (required)
│   ├── home.py
│   ├── onboarding.py
│   ├── ekyc.py
│   ├── asset_valuation.py
│   ├── loan_application.py
│   ├── results.py
│   └── architecture.py
├── utils/                 # Utility modules (required)
│   ├── helpers.py
│   └── ai_simulation.py
└── .streamlit/           # Configuration (optional but recommended)
    └── config.toml
```

## Common Issues & Solutions

### Issue: App fails to start
**Solution**: Check that:
- `app.py` exists in root directory
- All imports are correct
- `requirements.txt` includes all dependencies

### Issue: Module not found errors
**Solution**: 
- Verify all files in `pages/` and `utils/` directories exist
- Check import statements in `app.py`
- Ensure no typos in file names

### Issue: Styling not applied
**Solution**: 
- Verify `.streamlit/config.toml` exists
- Check theme configuration in config file

### Issue: Slow loading
**Solution**:
- This is normal for first load on Streamlit Cloud
- Subsequent loads will be faster due to caching

## Environment Variables (Optional)

If you need to add API keys or secrets later:

1. Go to your app settings on Streamlit Cloud
2. Click "Secrets"
3. Add secrets in TOML format:
```toml
[secrets]
api_key = "your-api-key"
```

Access in code:
```python
import streamlit as st
api_key = st.secrets["api_key"]
```

## Updating Your App

1. Make changes to your code
2. Commit and push to your repository
3. Streamlit Cloud will automatically redeploy
4. Wait for the new deployment to complete

## Support

- Streamlit Community: [discuss.streamlit.io](https://discuss.streamlit.io)
- Streamlit Docs: [docs.streamlit.io](https://docs.streamlit.io)
- GitHub Issues: Create an issue in your repository

---

**Note**: This is a POC application. For production use, consider:
- Adding authentication
- Implementing proper error handling
- Adding data persistence
- Setting up monitoring and logging

