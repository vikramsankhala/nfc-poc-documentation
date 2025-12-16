"""
AI-Augmented Customer Onboarding POC
Streamlit Application for Investor Demonstration
"""

import streamlit as st
from streamlit_option_menu import option_menu
import views.home as home_page
import views.onboarding as onboarding_page
import views.ekyc as ekyc_page
import views.asset_valuation as asset_valuation_page
import views.loan_application as loan_application_page
import views.results as results_page
import views.architecture as architecture_page

# Page configuration
st.set_page_config(
    page_title="AI-Augmented Customer Onboarding",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7f7f7f;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #1565c0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'customer_data' not in st.session_state:
    st.session_state.customer_data = {}
if 'kyc_status' not in st.session_state:
    st.session_state.kyc_status = {}
if 'asset_data' not in st.session_state:
    st.session_state.asset_data = {}
if 'loan_decision' not in st.session_state:
    st.session_state.loan_decision = {}

# Sidebar navigation
with st.sidebar:
    st.image("https://via.placeholder.com/200x60/1f77b4/ffffff?text=FPT+Banking", use_container_width=True)
    
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Onboarding", "eKYC", "Asset Valuation", "Loan Application", "Results", "Architecture"],
        icons=["house", "person-plus", "shield-check", "image", "file-earmark-text", "graph-up", "diagram-3"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "#1f77b4", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#1f77b4"},
        }
    )

# Route to appropriate page
if selected == "Home":
    home_page.show()
elif selected == "Onboarding":
    onboarding_page.show()
elif selected == "eKYC":
    ekyc_page.show()
elif selected == "Asset Valuation":
    asset_valuation_page.show()
elif selected == "Loan Application":
    loan_application_page.show()
elif selected == "Results":
    results_page.show()
elif selected == "Architecture":
    architecture_page.show()

