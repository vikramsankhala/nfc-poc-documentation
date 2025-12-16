"""
eKYC (Electronic Know Your Customer) Page
Identity Verification with NFC and Document Upload
"""

import streamlit as st
from utils.ai_simulation import simulate_kyc_verification, simulate_nfc_reading
import json

def show():
    st.markdown('<h1 class="main-header">🛡️ eKYC & Identity Verification</h1>', unsafe_allow_html=True)
    st.markdown("Verify your identity using NFC passport reading and document upload.")
    
    # Check if onboarding is complete
    if not st.session_state.get('customer_data'):
        st.warning("⚠️ Please complete the **Onboarding** form first before proceeding with eKYC.")
        return
    
    st.markdown("---")
    
    # Initialize KYC status
    if 'kyc_status' not in st.session_state:
        st.session_state.kyc_status = {}
    
    # NFC Passport Reading Section
    st.markdown("### 📱 NFC Passport Reading")
    st.markdown("Simulate NFC chip reading from your passport. In production, this would use native NFC hardware.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info("""
        **How it works:**
        - Tap your passport on the device (simulated)
        - NFC chip data is read securely
        - Personal information is extracted
        - Data is cross-referenced with application form
        """)
    
    with col2:
        if st.button("🔍 Read NFC Passport", use_container_width=True, type="primary"):
            with st.spinner("Reading NFC chip..."):
                # Simulate NFC reading
                nfc_data = simulate_nfc_reading(st.session_state.customer_data)
                
                if nfc_data:
                    st.session_state.kyc_status['nfc_data'] = nfc_data
                    st.session_state.kyc_status['nfc_verified'] = True
                    st.success("✅ NFC passport read successfully!")
                    
                    with st.expander("View NFC Data", expanded=True):
                        st.json(nfc_data)
                else:
                    st.error("❌ Failed to read NFC chip. Please try again.")
    
    # Display NFC status
    if st.session_state.kyc_status.get('nfc_verified'):
        st.markdown("**NFC Status:** ✅ Verified")
        nfc_data = st.session_state.kyc_status.get('nfc_data', {})
        if nfc_data:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Passport Number", nfc_data.get('passport_number', 'N/A'))
            with col2:
                st.metric("Nationality", nfc_data.get('nationality', 'N/A'))
            with col3:
                st.metric("Date of Birth", nfc_data.get('date_of_birth', 'N/A'))
    
    st.markdown("---")
    
    # Document Upload Section
    st.markdown("### 📄 Document Upload")
    st.markdown("Upload identity documents for OCR and verification.")
    
    doc_type = st.selectbox(
        "Document Type",
        ["Passport", "Driving License", "National ID Card"],
        index=0
    )
    
    uploaded_file = st.file_uploader(
        "Upload Document Image",
        type=['png', 'jpg', 'jpeg'],
        help="Upload a clear image of your identity document"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Document", use_container_width=True)
        
        if st.button("🔍 Verify Document", use_container_width=True, type="primary"):
            with st.spinner("Processing document with AI..."):
                # Simulate document verification
                doc_verification = simulate_kyc_verification(
                    st.session_state.customer_data,
                    doc_type,
                    uploaded_file.name
                )
                
                if doc_verification:
                    st.session_state.kyc_status['document_verified'] = True
                    st.session_state.kyc_status['document_data'] = doc_verification
                    
                    st.success("✅ Document verified successfully!")
                    
                    # Display verification results
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("#### Verification Results")
                        st.json(doc_verification.get('extracted_data', {}))
                    
                    with col2:
                        st.markdown("#### Match Status")
                        match_status = doc_verification.get('match_status', {})
                        
                        for field, status in match_status.items():
                            icon = "✅" if status else "❌"
                            color = "#22c55e" if status else "#ef4444"
                            st.markdown(f"""
                            <div style="padding: 0.5rem; margin: 0.25rem 0; border-left: 3px solid {color};">
                                {icon} <strong>{field}</strong>
                            </div>
                            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Sanctions & Fraud Screening
    st.markdown("### 🔍 Sanctions & Fraud Screening")
    
    if st.button("🚀 Run Screening Checks", use_container_width=True, type="primary"):
        with st.spinner("Running sanctions and fraud checks..."):
            # Simulate screening
            screening_results = {
                'sanctions_check': {
                    'status': 'CLEAR',
                    'matches': 0,
                    'checked_databases': ['OFAC', 'UN Sanctions', 'EU Sanctions', 'UK Sanctions']
                },
                'pep_check': {
                    'status': 'CLEAR',
                    'is_pep': False,
                    'risk_level': 'LOW'
                },
                'fraud_check': {
                    'status': 'CLEAR',
                    'fraud_score': 0.12,
                    'risk_level': 'LOW',
                    'checks_performed': [
                        'Identity verification',
                        'Document authenticity',
                        'Device fingerprinting',
                        'Behavioral analysis'
                    ]
                },
                'adverse_media': {
                    'status': 'CLEAR',
                    'matches': 0
                }
            }
            
            st.session_state.kyc_status['screening'] = screening_results
            st.session_state.kyc_status['screening_complete'] = True
            
            st.success("✅ Screening checks completed!")
            
            # Display results
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                sanctions = screening_results['sanctions_check']
                st.metric("Sanctions", sanctions['status'], delta=f"{sanctions['matches']} matches")
            
            with col2:
                pep = screening_results['pep_check']
                pep_status = "CLEAR" if not pep['is_pep'] else "FLAG"
                st.metric("PEP Check", pep_status, delta=pep['risk_level'])
            
            with col3:
                fraud = screening_results['fraud_check']
                st.metric("Fraud Score", f"{fraud['fraud_score']:.2f}", delta=f"Risk: {fraud['risk_level']}")
            
            with col4:
                media = screening_results['adverse_media']
                st.metric("Adverse Media", media['status'], delta=f"{media['matches']} matches")
            
            # Detailed results
            with st.expander("View Detailed Screening Results", expanded=False):
                st.json(screening_results)
    
    # Display screening status
    if st.session_state.kyc_status.get('screening_complete'):
        st.info("✅ All screening checks have been completed.")
    
    st.markdown("---")
    
    # Overall KYC Status
    st.markdown("### 📊 Overall KYC Status")
    
    nfc_ok = st.session_state.kyc_status.get('nfc_verified', False)
    doc_ok = st.session_state.kyc_status.get('document_verified', False)
    screening_ok = st.session_state.kyc_status.get('screening_complete', False)
    
    if nfc_ok and doc_ok and screening_ok:
        st.session_state.kyc_status['status'] = 'APPROVED'
        st.session_state.kyc_status['overall_status'] = 'COMPLETE'
        
        st.success("""
        ### ✅ KYC Verification Complete!
        
        All identity verification checks have passed:
        - ✅ NFC passport verified
        - ✅ Document verified and matched
        - ✅ Sanctions & fraud screening cleared
        
        You can now proceed to **Asset Valuation**.
        """)
    else:
        pending = []
        if not nfc_ok:
            pending.append("NFC Passport Reading")
        if not doc_ok:
            pending.append("Document Verification")
        if not screening_ok:
            pending.append("Screening Checks")
        
        st.warning(f"⚠️ Pending: {', '.join(pending)}")
        
        progress = (nfc_ok + doc_ok + screening_ok) / 3
        st.progress(progress)
        st.caption(f"KYC Progress: {int(progress * 100)}%")

