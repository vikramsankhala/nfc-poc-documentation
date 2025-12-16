"""
Asset Valuation Page
AI-powered asset analysis and valuation
"""

import streamlit as st
from utils.ai_simulation import simulate_asset_valuation
import random

def show():
    st.markdown('<h1 class="main-header">🚗 Asset Valuation</h1>', unsafe_allow_html=True)
    st.markdown("Upload asset photos for AI-powered valuation and market analysis.")
    
    # Check prerequisites
    if not st.session_state.get('customer_data'):
        st.warning("⚠️ Please complete the **Onboarding** form first.")
        return
    
    if not st.session_state.get('kyc_status', {}).get('overall_status') == 'COMPLETE':
        st.warning("⚠️ Please complete **eKYC** verification first.")
        return
    
    st.markdown("---")
    
    # Initialize asset data
    if 'asset_data' not in st.session_state:
        st.session_state.asset_data = {}
    
    # Asset Information
    st.markdown("### 📋 Asset Information")
    
    asset_type = st.selectbox(
        "Asset Type *",
        ["Vehicle", "Property", "Equipment", "Other"],
        index=0
    )
    
    if asset_type == "Vehicle":
        col1, col2 = st.columns(2)
        
        with col1:
            make = st.text_input("Make", value=st.session_state.asset_data.get('make', 'BMW'))
            model = st.text_input("Model", value=st.session_state.asset_data.get('model', '320d'))
            year = st.number_input("Year", min_value=1990, max_value=2025, 
                                  value=int(st.session_state.asset_data.get('year', 2020)), step=1)
        
        with col2:
            mileage = st.number_input("Mileage", min_value=0, 
                                     value=int(st.session_state.asset_data.get('mileage', 50000)), step=1000)
            condition = st.selectbox(
                "Condition",
                ["Excellent", "Very Good", "Good", "Fair", "Poor"],
                index=2 if not st.session_state.asset_data.get('condition') else
                ["Excellent", "Very Good", "Good", "Fair", "Poor"].index(
                    st.session_state.asset_data.get('condition', 'Good')
                )
            )
            registration = st.text_input("Registration Number", 
                                        value=st.session_state.asset_data.get('registration', 'AB12 CDE'))
    
    elif asset_type == "Property":
        col1, col2 = st.columns(2)
        
        with col1:
            property_type = st.selectbox("Property Type", ["House", "Flat", "Commercial"])
            bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=3)
            bathrooms = st.number_input("Bathrooms", min_value=0, max_value=10, value=2)
        
        with col2:
            square_feet = st.number_input("Square Feet", min_value=0, value=1200)
            property_condition = st.selectbox(
                "Condition",
                ["Excellent", "Very Good", "Good", "Fair", "Poor"]
            )
    
    else:
        asset_description = st.text_area("Asset Description", height=100)
        estimated_value = st.number_input("Estimated Value (£)", min_value=0, value=10000)
    
    st.markdown("---")
    
    # Photo Upload Section
    st.markdown("### 📸 Asset Photos")
    st.markdown("Upload multiple photos of your asset for AI analysis. The AI will assess condition, authenticity, and market value.")
    
    uploaded_photos = st.file_uploader(
        "Upload Asset Photos",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True,
        help="Upload clear photos from multiple angles"
    )
    
    if uploaded_photos:
        st.markdown(f"**{len(uploaded_photos)} photo(s) uploaded**")
        
        # Display photos in a grid
        cols = st.columns(min(3, len(uploaded_photos)))
        for idx, photo in enumerate(uploaded_photos):
            with cols[idx % 3]:
                st.image(photo, caption=f"Photo {idx + 1}", use_container_width=True)
    
    st.markdown("---")
    
    # V5C Document Upload (for vehicles)
    if asset_type == "Vehicle":
        st.markdown("### 📄 V5C Document (Vehicle Registration)")
        st.markdown("Upload V5C document for verification and cross-referencing with DVLA database.")
        
        v5c_document = st.file_uploader(
            "Upload V5C Document",
            type=['png', 'jpg', 'jpeg', 'pdf'],
            help="Upload V5C registration document"
        )
        
        if v5c_document:
            st.success(f"✅ V5C document uploaded: {v5c_document.name}")
    
    st.markdown("---")
    
    # Valuation Button
    if st.button("🤖 Analyze & Value Asset", use_container_width=True, type="primary"):
        if not uploaded_photos:
            st.error("⚠️ Please upload at least one asset photo.")
        else:
            # Show visual analysis progress
            progress_container = st.container()
            with progress_container:
                st.markdown("### 🤖 AI Analysis in Progress")
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                analysis_steps = st.empty()
                
                import time
                
                # Step 1: Image Processing
                status_text.markdown("**Step 1/5:** Processing images...")
                analysis_steps.markdown("""
                <div style="background: #e3f2fd; padding: 10px; border-radius: 5px; margin: 5px 0;">
                    📸 Analyzing {0} photo(s) for quality and content...
                </div>
                """.format(len(uploaded_photos)), unsafe_allow_html=True)
                
                for i in range(20):
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)
                
                # Step 2: Computer Vision Analysis
                status_text.markdown("**Step 2/5:** Computer vision analysis...")
                analysis_steps.markdown("""
                <div style="background: #e3f2fd; padding: 10px; border-radius: 5px; margin: 5px 0;">
                    📸 Analyzing {0} photo(s) for quality and content...<br>
                    👁️ Computer vision: Detecting condition, damage, and features...
                </div>
                """.format(len(uploaded_photos)), unsafe_allow_html=True)
                
                for i in range(20, 40):
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)
                
                # Step 3: Market Data Integration
                status_text.markdown("**Step 3/5:** Fetching market data...")
                analysis_steps.markdown("""
                <div style="background: #e3f2fd; padding: 10px; border-radius: 5px; margin: 5px 0;">
                    📸 Analyzing {0} photo(s) for quality and content...<br>
                    👁️ Computer vision: Detecting condition, damage, and features...<br>
                    📊 Querying market databases (CAP HPI, DVLA)...
                </div>
                """.format(len(uploaded_photos)), unsafe_allow_html=True)
                
                for i in range(40, 70):
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)
                
                # Step 4: Valuation Calculation
                status_text.markdown("**Step 4/5:** Calculating valuation...")
                analysis_steps.markdown("""
                <div style="background: #e3f2fd; padding: 10px; border-radius: 5px; margin: 5px 0;">
                    📸 Analyzing {0} photo(s) for quality and content...<br>
                    👁️ Computer vision: Detecting condition, damage, and features...<br>
                    📊 Querying market databases (CAP HPI, DVLA)...<br>
                    💰 Calculating market value based on condition and market data...
                </div>
                """.format(len(uploaded_photos)), unsafe_allow_html=True)
                
                for i in range(70, 90):
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)
                
                # Step 5: Finalizing
                status_text.markdown("**Step 5/5:** Finalizing results...")
                analysis_steps.markdown("""
                <div style="background: #e8f5e9; padding: 10px; border-radius: 5px; margin: 5px 0;">
                    📸 Analyzing {0} photo(s) for quality and content...<br>
                    👁️ Computer vision: Detecting condition, damage, and features...<br>
                    📊 Querying market databases (CAP HPI, DVLA)...<br>
                    💰 Calculating market value based on condition and market data...<br>
                    ✅ Generating comprehensive valuation report...
                </div>
                """.format(len(uploaded_photos)), unsafe_allow_html=True)
                
                for i in range(90, 100):
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)
                
                # Prepare asset info
                asset_info = {
                    'type': asset_type,
                    'photos_count': len(uploaded_photos),
                    'has_v5c': v5c_document is not None if asset_type == "Vehicle" else False
                }
                
                if asset_type == "Vehicle":
                    asset_info.update({
                        'make': make,
                        'model': model,
                        'year': year,
                        'mileage': mileage,
                        'condition': condition,
                        'registration': registration
                    })
                
                # Simulate AI valuation
                valuation_result = simulate_asset_valuation(asset_info, uploaded_photos)
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                analysis_steps.empty()
                
                if valuation_result:
                    st.session_state.asset_data = {
                        **asset_info,
                        **valuation_result
                    }
                    
                    st.success("✅ Asset analysis complete!")
                    
                    # Display results
                    st.markdown("---")
                    st.markdown("### 💰 Valuation Results")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric(
                            "Market Value",
                            f"£{valuation_result['market_value']:,.0f}",
                            delta=f"±{valuation_result['value_range']:,.0f}"
                        )
                    
                    with col2:
                        st.metric(
                            "Condition Score",
                            f"{valuation_result['condition_score']}/10",
                            delta=f"{valuation_result['condition_rating']}"
                        )
                    
                    with col3:
                        ltv = valuation_result.get('ltv_ratio', 0.7)
                        st.metric(
                            "LTV Ratio",
                            f"{ltv*100:.0f}%",
                            delta="Standard"
                        )
                    
                    with col4:
                        max_loan = valuation_result['market_value'] * ltv
                        st.metric(
                            "Max Loan Value",
                            f"£{max_loan:,.0f}",
                            delta="Based on LTV"
                        )
                    
                    # Detailed Analysis
                    st.markdown("---")
                    st.markdown("### 🔍 Detailed Analysis")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("#### AI Analysis Summary")
                        st.info(valuation_result.get('analysis_summary', 'Analysis completed successfully.'))
                        
                        st.markdown("#### Condition Assessment")
                        condition_details = valuation_result.get('condition_details', {})
                        for aspect, score in condition_details.items():
                            st.progress(score / 10, text=f"{aspect}: {score}/10")
                    
                    with col2:
                        st.markdown("#### Market Data")
                        market_data = valuation_result.get('market_data', {})
                        
                        st.markdown(f"""
                        - **Average Market Price:** £{market_data.get('avg_price', 0):,.0f}
                        - **Price Range:** £{market_data.get('min_price', 0):,.0f} - £{market_data.get('max_price', 0):,.0f}
                        - **Market Trend:** {market_data.get('trend', 'Stable')}
                        - **Comparable Listings:** {market_data.get('comparables', 0)}
                        """)
                        
                        if asset_type == "Vehicle":
                            st.markdown("#### DVLA Verification")
                            dvla_status = valuation_result.get('dvla_verification', {})
                            status_icon = "✅" if dvla_status.get('verified') else "⚠️"
                            st.markdown(f"""
                            {status_icon} **Status:** {dvla_status.get('status', 'Pending')}
                            - **Make/Model Match:** {dvla_status.get('make_match', 'N/A')}
                            - **Registration Valid:** {dvla_status.get('registration_valid', 'N/A')}
                            - **Mileage Check:** {dvla_status.get('mileage_check', 'N/A')}
                            """)
                    
                    # Full JSON for debugging
                    with st.expander("View Full Valuation Data", expanded=False):
                        st.json(valuation_result)
                    
                    st.info("📋 You can now proceed to **Loan Application** to submit your loan request.")
    
    # Display existing valuation if available
    if st.session_state.asset_data.get('market_value'):
        st.markdown("---")
        st.markdown("### 📊 Current Valuation")
        
        val_col1, val_col2 = st.columns(2)
        
        with val_col1:
            st.metric("Asset Value", f"£{st.session_state.asset_data['market_value']:,.0f}")
            st.metric("Condition", st.session_state.asset_data.get('condition_rating', 'N/A'))
        
        with val_col2:
            ltv = st.session_state.asset_data.get('ltv_ratio', 0.7)
            max_loan = st.session_state.asset_data['market_value'] * ltv
            st.metric("Maximum Loan", f"£{max_loan:,.0f}")
            st.metric("LTV Ratio", f"{ltv*100:.0f}%")

