"""
Home/Dashboard Page
"""

import streamlit as st
from utils.helpers import get_progress_status

def show():
    st.markdown('<h1 class="main-header">🏦 AI-Augmented Customer Onboarding</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Proof of Concept - Investor Demonstration</p>', unsafe_allow_html=True)
    
    # Overview section
    st.markdown("---")
    st.markdown("## 📋 Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **Customer Onboarding**
        - Seamless application process
        - Digital form submission
        - Real-time validation
        """)
    
    with col2:
        st.info("""
        **eKYC & Identity Verification**
        - NFC passport reading (simulated)
        - Document OCR & validation
        - Sanctions & fraud screening
        """)
    
    with col3:
        st.info("""
        **Asset Valuation & Loan Processing**
        - AI-powered asset analysis
        - Real-time market valuation
        - Automated loan decisioning
        """)
    
    # Workflow visualization
    st.markdown("---")
    st.markdown("## 🔄 Customer Onboarding Workflow")
    
    workflow_steps = [
        ("1️⃣", "Customer Onboarding", "Fill application form with personal details"),
        ("2️⃣", "eKYC Verification", "Identity verification via NFC/document scan"),
        ("3️⃣", "Asset Valuation", "Upload asset photos for AI-powered valuation"),
        ("4️⃣", "Loan Application", "Review terms and submit loan application"),
        ("5️⃣", "Results & Decision", "View automated decision and loan offer")
    ]
    
    # Display workflow with progress indicators
    progress = get_progress_status()
    
    for icon, title, description in workflow_steps:
        step_num = int(icon[0]) - 1
        is_complete = progress.get(f"step_{step_num}", False)
        
        status_icon = "✅" if is_complete else "⏳"
        status_color = "#22c55e" if is_complete else "#94a3b8"
        
        st.markdown(f"""
        <div style="padding: 1rem; margin: 0.5rem 0; border-left: 4px solid {status_color}; background-color: #f8f9fa; border-radius: 4px;">
            <strong>{status_icon} {icon} {title}</strong><br>
            <span style="color: #666;">{description}</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Key Features
    st.markdown("---")
    st.markdown("## ✨ Key Features")
    
    feature_col1, feature_col2 = st.columns(2)
    
    with feature_col1:
        st.markdown("""
        **🤖 Agentic AI Engine**
        - Autonomous agents for data extraction
        - Computer vision analysis
        - Real-time decision making
        
        **🔒 Security & Compliance**
        - GDPR compliant data handling
        - KYC/AML compliance checks
        - Secure document processing
        """)
    
    with feature_col2:
        st.markdown("""
        **📱 Native Integration**
        - NFC passport chip reading
        - Camera for liveness checks
        - Asset photo capture
        
        **⚡ Real-Time Processing**
        - Instant asset valuation
        - Automated risk scoring
        - Immediate loan decisions
        """)
    
    # Quick Start
    st.markdown("---")
    st.markdown("## 🚀 Quick Start")
    
    st.markdown("""
    Navigate through the workflow using the sidebar menu:
    1. Start with **Onboarding** to fill in customer details
    2. Proceed to **eKYC** for identity verification
    3. Use **Asset Valuation** to evaluate collateral
    4. Complete **Loan Application** for final submission
    5. View **Results** to see the automated decision
    """)
    
    # Statistics (if data exists)
    if st.session_state.get('customer_data'):
        st.markdown("---")
        st.markdown("## 📊 Current Session Status")
        
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
        
        with stat_col1:
            st.metric("Application Status", "In Progress" if not st.session_state.get('loan_decision') else "Completed")
        
        with stat_col2:
            kyc_status = st.session_state.get('kyc_status', {}).get('status', 'Pending')
            st.metric("KYC Status", kyc_status)
        
        with stat_col3:
            asset_val = st.session_state.get('asset_data', {}).get('valuation', 0)
            st.metric("Asset Valuation", f"£{asset_val:,.0f}" if asset_val else "Not Set")
        
        with stat_col4:
            loan_amt = st.session_state.get('loan_decision', {}).get('approved_amount', 0)
            st.metric("Loan Offer", f"£{loan_amt:,.0f}" if loan_amt else "Pending")

