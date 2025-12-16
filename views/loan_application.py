"""
Loan Application Page
Final loan application submission and automated decisioning
"""

import streamlit as st
from utils.ai_simulation import simulate_loan_decision
from datetime import datetime

def show():
    st.markdown('<h1 class="main-header">💼 Loan Application</h1>', unsafe_allow_html=True)
    st.markdown("Review your application and submit for automated loan decision.")
    
    # Check prerequisites
    if not st.session_state.get('customer_data'):
        st.warning("⚠️ Please complete the **Onboarding** form first.")
        return
    
    if not st.session_state.get('kyc_status', {}).get('overall_status') == 'COMPLETE':
        st.warning("⚠️ Please complete **eKYC** verification first.")
        return
    
    if not st.session_state.get('asset_data', {}).get('market_value'):
        st.warning("⚠️ Please complete **Asset Valuation** first.")
        return
    
    st.markdown("---")
    
    # Application Summary
    st.markdown("### 📋 Application Summary")
    
    customer_data = st.session_state.customer_data
    asset_data = st.session_state.asset_data
    kyc_status = st.session_state.kyc_status
    
    # Customer Info
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Customer Information")
        st.markdown(f"""
        - **Name:** {customer_data.get('first_name', '')} {customer_data.get('last_name', '')}
        - **Email:** {customer_data.get('email', '')}
        - **Annual Income:** £{customer_data.get('annual_income', 0):,.0f}
        - **Employment:** {customer_data.get('employment_status', 'N/A')}
        """)
    
    with col2:
        st.markdown("#### 🚗 Asset Information")
        st.markdown(f"""
        - **Asset Type:** {asset_data.get('type', 'N/A')}
        - **Market Value:** £{asset_data.get('market_value', 0):,.0f}
        - **Condition:** {asset_data.get('condition_rating', 'N/A')}
        - **LTV Ratio:** {asset_data.get('ltv_ratio', 0.7)*100:.0f}%
        """)
    
    st.markdown("---")
    
    # Loan Details
    st.markdown("### 💰 Loan Details")
    
    requested_amount = customer_data.get('requested_amount', 0)
    asset_value = asset_data.get('market_value', 0)
    max_loan = asset_value * asset_data.get('ltv_ratio', 0.7)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Requested Amount", f"£{requested_amount:,.0f}")
    
    with col2:
        st.metric("Maximum Loan", f"£{max_loan:,.0f}")
    
    with col3:
        ltv_requested = (requested_amount / asset_value * 100) if asset_value > 0 else 0
        st.metric("Requested LTV", f"{ltv_requested:.1f}%")
    
    # Loan Terms
    st.markdown("---")
    st.markdown("### 📝 Proposed Loan Terms")
    
    # Calculate loan terms based on amount and risk
    annual_income = customer_data.get('annual_income', 0)
    debt_to_income = (requested_amount / annual_income * 100) if annual_income > 0 else 0
    
    # Simulate interest rate based on risk
    base_rate = 5.5
    risk_adjustment = 0
    if debt_to_income > 40:
        risk_adjustment += 1.5
    if ltv_requested > 80:
        risk_adjustment += 1.0
    
    interest_rate = base_rate + risk_adjustment
    loan_term_years = st.slider("Loan Term (Years)", 1, 7, 5)
    loan_term_months = loan_term_years * 12
    
    # Calculate monthly payment (simplified)
    monthly_rate = interest_rate / 100 / 12
    if monthly_rate > 0:
        monthly_payment = requested_amount * (monthly_rate * (1 + monthly_rate)**loan_term_months) / ((1 + monthly_rate)**loan_term_months - 1)
    else:
        monthly_payment = requested_amount / loan_term_months
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Interest Rate", f"{interest_rate:.2f}%")
    
    with col2:
        st.metric("Loan Term", f"{loan_term_years} years")
    
    with col3:
        st.metric("Monthly Payment", f"£{monthly_payment:,.2f}")
    
    with col4:
        total_payable = monthly_payment * loan_term_months
        st.metric("Total Payable", f"£{total_payable:,.0f}")
    
    st.markdown("---")
    
    # Risk Assessment Preview
    st.markdown("### ⚠️ Risk Assessment Preview")
    
    risk_factors = []
    
    # Income risk
    if debt_to_income > 40:
        risk_factors.append(("High Debt-to-Income Ratio", f"{debt_to_income:.1f}%", "HIGH"))
    elif debt_to_income > 30:
        risk_factors.append(("Moderate Debt-to-Income Ratio", f"{debt_to_income:.1f}%", "MEDIUM"))
    else:
        risk_factors.append(("Debt-to-Income Ratio", f"{debt_to_income:.1f}%", "LOW"))
    
    # LTV risk
    if ltv_requested > 80:
        risk_factors.append(("High LTV Ratio", f"{ltv_requested:.1f}%", "HIGH"))
    elif ltv_requested > 70:
        risk_factors.append(("Moderate LTV Ratio", f"{ltv_requested:.1f}%", "MEDIUM"))
    else:
        risk_factors.append(("LTV Ratio", f"{ltv_requested:.1f}%", "LOW"))
    
    # KYC risk
    fraud_score = kyc_status.get('screening', {}).get('fraud_check', {}).get('fraud_score', 0.1)
    if fraud_score > 0.3:
        risk_factors.append(("Fraud Risk Score", f"{fraud_score:.2f}", "HIGH"))
    elif fraud_score > 0.15:
        risk_factors.append(("Fraud Risk Score", f"{fraud_score:.2f}", "MEDIUM"))
    else:
        risk_factors.append(("Fraud Risk Score", f"{fraud_score:.2f}", "LOW"))
    
    # Asset condition
    condition_score = asset_data.get('condition_score', 7)
    if condition_score < 5:
        risk_factors.append(("Asset Condition", f"{condition_score}/10", "HIGH"))
    elif condition_score < 7:
        risk_factors.append(("Asset Condition", f"{condition_score}/10", "MEDIUM"))
    else:
        risk_factors.append(("Asset Condition", f"{condition_score}/10", "LOW"))
    
    for factor, value, risk in risk_factors:
        color = "#ef4444" if risk == "HIGH" else "#f59e0b" if risk == "MEDIUM" else "#22c55e"
        st.markdown(f"""
        <div style="padding: 0.75rem; margin: 0.5rem 0; border-left: 4px solid {color}; background-color: #f8f9fa; border-radius: 4px;">
            <strong>{factor}:</strong> {value} <span style="color: {color}; font-weight: bold;">[{risk}]</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Submit Application
    st.markdown("### 🚀 Submit Application")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("📄 Review Full Application", use_container_width=True):
            with st.expander("Full Application Data", expanded=True):
                st.json({
                    'customer': customer_data,
                    'kyc': kyc_status,
                    'asset': asset_data,
                    'loan_terms': {
                        'requested_amount': requested_amount,
                        'interest_rate': interest_rate,
                        'term_years': loan_term_years,
                        'monthly_payment': monthly_payment
                    }
                })
    
    with col2:
        if st.button("✅ Submit for Decision", use_container_width=True, type="primary"):
            with st.spinner("Processing application with AI decision engine..."):
                # Prepare application data
                application_data = {
                    'customer': customer_data,
                    'kyc': kyc_status,
                    'asset': asset_data,
                    'loan_request': {
                        'amount': requested_amount,
                        'term_years': loan_term_years,
                        'interest_rate': interest_rate,
                        'monthly_payment': monthly_payment
                    },
                    'risk_factors': risk_factors
                }
                
                # Simulate AI loan decision
                decision = simulate_loan_decision(application_data)
                
                if decision:
                    st.session_state.loan_decision = decision
                    st.session_state.loan_decision['submitted_at'] = datetime.now().isoformat()
                    
                    st.success("✅ Application submitted successfully!")
                    st.balloons()
                    
                    # Show decision
                    if decision.get('status') == 'APPROVED':
                        st.success(f"""
                        ### 🎉 Loan Approved!
                        
                        **Approved Amount:** £{decision.get('approved_amount', 0):,.0f}
                        **Interest Rate:** {decision.get('interest_rate', 0):.2f}%
                        **Term:** {decision.get('term_years', 0)} years
                        **Monthly Payment:** £{decision.get('monthly_payment', 0):,.2f}
                        
                        Please proceed to **Results** page to view detailed analysis.
                        """)
                    else:
                        st.warning(f"""
                        ### ⚠️ Loan Decision: {decision.get('status', 'PENDING')}
                        
                        **Reason:** {decision.get('reason', 'Under review')}
                        **Risk Score:** {decision.get('risk_score', 0):.2f}
                        
                        Please proceed to **Results** page for detailed analysis.
                        """)
    
    # Display existing decision if available
    if st.session_state.get('loan_decision'):
        st.markdown("---")
        st.markdown("### 📊 Current Decision Status")
        
        decision = st.session_state.loan_decision
        
        if decision.get('status') == 'APPROVED':
            st.success(f"✅ **Status:** {decision.get('status')}")
            st.metric("Approved Amount", f"£{decision.get('approved_amount', 0):,.0f}")
        else:
            st.warning(f"⚠️ **Status:** {decision.get('status', 'PENDING')}")
        
        st.info("View detailed results on the **Results** page.")

