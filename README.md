# AI-Augmented Customer Onboarding POC

A comprehensive Proof of Concept application for AI-augmented customer onboarding in banking and financial services, built with Streamlit for investor demonstration.

## 🎯 Overview

This application demonstrates a complete customer onboarding workflow with:
- **Customer Onboarding**: Digital form submission with real-time validation
- **eKYC Verification**: Identity verification via simulated NFC passport reading and document upload
- **Asset Valuation**: AI-powered asset analysis and market valuation
- **Loan Application**: Automated loan decisioning with risk assessment
- **Results Dashboard**: Comprehensive analytics and visualizations

## 🚀 Features

### Core Functionality
- ✅ Multi-page navigation with professional UI
- ✅ Complete customer onboarding form
- ✅ Simulated NFC passport reading
- ✅ Document upload and OCR simulation
- ✅ Sanctions and fraud screening
- ✅ AI-powered asset valuation
- ✅ Automated loan decisioning
- ✅ Interactive analytics dashboard
- ✅ Architecture and technical overview

### AI & Automation
- 🤖 Agentic AI engine simulation
- 📊 Real-time risk scoring
- 🔍 Automated compliance checks
- 💰 Market data integration simulation
- 📈 Data visualization with Plotly

## 📋 Prerequisites

- Python 3.10 or higher
- pip package manager

## 🛠️ Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏃 Running Locally

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## ☁️ Deployment to Streamlit Community Cloud

### Step 1: Prepare Repository
1. Ensure all files are committed to a Git repository (GitHub, GitLab, or Bitbucket)
2. Make sure `requirements.txt` is in the root directory
3. Ensure `app.py` is the main entry point

### Step 2: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub/GitLab/Bitbucket account
3. Click "New app"
4. Select your repository
5. Set the main file path to `app.py`
6. Click "Deploy"

### Step 3: Configuration
- The app will automatically detect `requirements.txt`
- Configuration is handled via `.streamlit/config.toml`
- No additional environment variables required for basic deployment

## 📁 Project Structure

```
.
├── app.py                      # Main Streamlit application
├── pages/                      # Page modules
│   ├── home.py                # Home/Dashboard page
│   ├── onboarding.py          # Customer onboarding form
│   ├── ekyc.py                # eKYC verification page
│   ├── asset_valuation.py     # Asset valuation page
│   ├── loan_application.py    # Loan application page
│   ├── results.py             # Results dashboard
│   └── architecture.py        # Technical overview
├── utils/                     # Utility modules
│   ├── helpers.py            # Helper functions
│   └── ai_simulation.py       # AI simulation logic
├── requirements.txt           # Python dependencies
├── .streamlit/
│   └── config.toml           # Streamlit configuration
└── README.md                  # This file
```

## 🎨 Application Flow

1. **Home**: Overview and navigation
2. **Onboarding**: Fill customer application form
3. **eKYC**: 
   - Simulate NFC passport reading
   - Upload and verify documents
   - Run sanctions and fraud screening
4. **Asset Valuation**:
   - Upload asset photos
   - AI analysis and valuation
   - Market data integration
5. **Loan Application**:
   - Review application summary
   - Submit for automated decision
6. **Results**: View comprehensive analytics and decision

## 🔧 Configuration

### Customization
- Modify `.streamlit/config.toml` for theme customization
- Update `utils/ai_simulation.py` to adjust simulation logic
- Customize pages in the `pages/` directory

### Adding Real AI Integration
To integrate with actual AI services:
1. Replace simulation functions in `utils/ai_simulation.py`
2. Add API client libraries to `requirements.txt`
3. Add environment variables for API keys
4. Update Streamlit Cloud secrets for production

## 📊 Key Technologies

- **Streamlit**: Web application framework
- **Plotly**: Interactive visualizations
- **Python**: Backend logic and AI simulation

## 🔒 Security Notes

This is a **Proof of Concept** application for demonstration purposes:
- No actual authentication required (demo mode)
- Simulated data processing (no real API calls)
- Suitable for investor demonstrations
- Production deployment would require additional security measures

## 📝 License

This is a demonstration application. Please ensure compliance with your organization's policies before deployment.

## 🤝 Support

For questions or issues:
1. Check the Architecture page in the application
2. Review the code comments
3. Consult Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)

## 🎯 Next Steps for Production

1. Integrate with actual AI/ML services
2. Add authentication and authorization
3. Connect to real databases
4. Implement actual NFC reading (mobile app)
5. Add comprehensive error handling
6. Set up monitoring and logging
7. Implement data persistence
8. Add unit and integration tests

---

**Built for Investor Demonstration** | FPT Software Banking Solutions

