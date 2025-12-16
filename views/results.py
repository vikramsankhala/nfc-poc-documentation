"""
Results Dashboard Page
Comprehensive view of application results and analytics
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

def show():
    st.markdown('<h1 class="main-header">📊 Results & Analytics</h1>', unsafe_allow_html=True)
    st.markdown("Comprehensive view of your application results and decision analysis.")
    
    # Check if application is complete
    if not st.session_state.get('loan_decision'):
        st.warning("⚠️ Please complete the loan application process first.")
        st.info("Navigate through: Onboarding → eKYC → Asset Valuation → Loan Application")
        return
    
    st.markdown("---")
    
    # Decision Summary
    decision = st.session_state.loan_decision
    customer_data = st.session_state.customer_data
    asset_data = st.session_state.asset_data
    kyc_status = st.session_state.kyc_status
    
    st.markdown("### 🎯 Loan Decision Summary")
    
    if decision.get('status') == 'APPROVED':
        st.success(f"""
        ## ✅ LOAN APPROVED
        
        **Application ID:** {decision.get('application_id', 'N/A')}
        **Decision Date:** {decision.get('decision_date', 'N/A')}
        """)
    else:
        st.warning(f"""
        ## ⚠️ LOAN STATUS: {decision.get('status', 'PENDING')}
        
        **Application ID:** {decision.get('application_id', 'N/A')}
        **Decision Date:** {decision.get('decision_date', 'N/A')}
        """)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Approved Amount",
            f"£{decision.get('approved_amount', 0):,.0f}",
            delta=f"Requested: £{customer_data.get('requested_amount', 0):,.0f}"
        )
    
    with col2:
        st.metric(
            "Interest Rate",
            f"{decision.get('interest_rate', 0):.2f}%",
            delta="APR"
        )
    
    with col3:
        st.metric(
            "Monthly Payment",
            f"£{decision.get('monthly_payment', 0):,.2f}",
            delta=f"Term: {decision.get('term_years', 0)} years"
        )
    
    with col4:
        risk_score = decision.get('risk_score', 0)
        risk_level = "LOW" if risk_score < 0.3 else "MEDIUM" if risk_score < 0.6 else "HIGH"
        st.metric(
            "Risk Score",
            f"{risk_score:.2f}",
            delta=risk_level
        )
    
    st.markdown("---")
    
    # Visualizations
    st.markdown("### 📈 Analytics & Visualizations")
    
    # Risk Score Breakdown
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Risk Score Breakdown")
        
        risk_breakdown = decision.get('risk_breakdown', {
            'credit_risk': 0.2,
            'asset_risk': 0.15,
            'fraud_risk': 0.1,
            'compliance_risk': 0.05
        })
        
        fig = go.Figure(data=[
            go.Bar(
                x=list(risk_breakdown.keys()),
                y=list(risk_breakdown.values()),
                marker_color=['#ef4444', '#f59e0b', '#22c55e', '#3b82f6'],
                text=[f"{v:.2f}" for v in risk_breakdown.values()],
                textposition='auto'
            )
        ])
        fig.update_layout(
            title="Risk Components",
            xaxis_title="Risk Type",
            yaxis_title="Risk Score",
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Application Flow Status")
        
        flow_steps = [
            ("Onboarding", True),
            ("eKYC", kyc_status.get('overall_status') == 'COMPLETE'),
            ("Asset Valuation", bool(asset_data.get('market_value'))),
            ("Loan Application", bool(decision))
        ]
        
        fig = go.Figure(data=[
            go.Scatter(
                x=[i for i, _ in enumerate(flow_steps)],
                y=[1 if status else 0 for _, status in flow_steps],
                mode='lines+markers',
                marker=dict(size=15, color=['#22c55e' if status else '#ef4444' for _, status in flow_steps]),
                line=dict(color='#1f77b4', width=3),
                text=[name for name, _ in flow_steps],
                textposition="top center"
            )
        ])
        fig.update_layout(
            title="Process Completion",
            xaxis=dict(tickmode='array', tickvals=list(range(len(flow_steps))), 
                      ticktext=[name for name, _ in flow_steps]),
            yaxis=dict(range=[-0.2, 1.2], showticklabels=False),
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Asset Valuation vs Loan Amount
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Asset Value vs Loan Amount")
        
        asset_value = asset_data.get('market_value', 0)
        approved_amount = decision.get('approved_amount', 0)
        requested_amount = customer_data.get('requested_amount', 0)
        
        fig = go.Figure(data=[
            go.Bar(
                name='Asset Value',
                x=['Value'],
                y=[asset_value],
                marker_color='#3b82f6'
            ),
            go.Bar(
                name='Approved Loan',
                x=['Value'],
                y=[approved_amount],
                marker_color='#22c55e'
            ),
            go.Bar(
                name='Requested Loan',
                x=['Value'],
                y=[requested_amount],
                marker_color='#f59e0b'
            )
        ])
        fig.update_layout(
            title="Financial Overview",
            yaxis_title="Amount (£)",
            barmode='group',
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### LTV Analysis")
        
        ltv_approved = (approved_amount / asset_value * 100) if asset_value > 0 else 0
        ltv_requested = (requested_amount / asset_value * 100) if asset_value > 0 else 0
        max_ltv = asset_data.get('ltv_ratio', 0.7) * 100
        
        fig = go.Figure(data=[
            go.Bar(
                x=['LTV Ratios'],
                y=[ltv_approved],
                name='Approved LTV',
                marker_color='#22c55e'
            ),
            go.Bar(
                x=['LTV Ratios'],
                y=[ltv_requested],
                name='Requested LTV',
                marker_color='#f59e0b'
            ),
            go.Bar(
                x=['LTV Ratios'],
                y=[max_ltv],
                name='Maximum LTV',
                marker_color='#3b82f6'
            )
        ])
        fig.update_layout(
            title="Loan-to-Value Ratios",
            yaxis_title="LTV (%)",
            barmode='group',
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed Breakdown
    st.markdown("---")
    st.markdown("### 📋 Detailed Analysis")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Decision Details", "KYC Results", "Asset Analysis", "Risk Assessment"])
    
    with tab1:
        st.markdown("#### Loan Decision Details")
        st.json({
            'status': decision.get('status'),
            'approved_amount': decision.get('approved_amount'),
            'interest_rate': decision.get('interest_rate'),
            'term_years': decision.get('term_years'),
            'monthly_payment': decision.get('monthly_payment'),
            'total_payable': decision.get('monthly_payment', 0) * decision.get('term_years', 0) * 12,
            'reason': decision.get('reason', 'N/A'),
            'conditions': decision.get('conditions', [])
        })
    
    with tab2:
        st.markdown("#### KYC Verification Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Identity Verification**")
            st.success(f"✅ NFC Passport: {'Verified' if kyc_status.get('nfc_verified') else 'Pending'}")
            st.success(f"✅ Document: {'Verified' if kyc_status.get('document_verified') else 'Pending'}")
        
        with col2:
            st.markdown("**Screening Results**")
            screening = kyc_status.get('screening', {})
            st.info(f"Sanctions: {screening.get('sanctions_check', {}).get('status', 'N/A')}")
            st.info(f"PEP: {screening.get('pep_check', {}).get('status', 'N/A')}")
            st.info(f"Fraud Score: {screening.get('fraud_check', {}).get('fraud_score', 0):.2f}")
        
        with st.expander("Full KYC Data"):
            st.json(kyc_status)
    
    with tab3:
        st.markdown("#### Asset Valuation Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Market Value", f"£{asset_data.get('market_value', 0):,.0f}")
            st.metric("Condition Score", f"{asset_data.get('condition_score', 0)}/10")
            st.metric("Condition Rating", asset_data.get('condition_rating', 'N/A'))
        
        with col2:
            ltv = asset_data.get('ltv_ratio', 0.7)
            st.metric("LTV Ratio", f"{ltv*100:.0f}%")
            st.metric("Max Loan Value", f"£{asset_data.get('market_value', 0) * ltv:,.0f}")
        
        with st.expander("Full Asset Data"):
            st.json(asset_data)
    
    with tab4:
        st.markdown("#### Risk Assessment")
        
        risk_breakdown = decision.get('risk_breakdown', {})
        
        for risk_type, score in risk_breakdown.items():
            risk_level = "HIGH" if score > 0.5 else "MEDIUM" if score > 0.3 else "LOW"
            color = "#ef4444" if score > 0.5 else "#f59e0b" if score > 0.3 else "#22c55e"
            
            st.markdown(f"""
            <div style="padding: 1rem; margin: 0.5rem 0; border-left: 4px solid {color}; background-color: #f8f9fa; border-radius: 4px;">
                <strong>{risk_type.replace('_', ' ').title()}:</strong> {score:.2f} 
                <span style="color: {color}; font-weight: bold;">[{risk_level}]</span>
                <div style="margin-top: 0.5rem;">
                    <div style="background-color: #e5e7eb; height: 8px; border-radius: 4px; overflow: hidden;">
                        <div style="background-color: {color}; height: 100%; width: {score*100}%;"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("Full Risk Analysis"):
            st.json(decision.get('risk_analysis', {}))
    
    # Next Steps
    st.markdown("---")
    st.markdown("### 🎯 Next Steps")
    
    if decision.get('status') == 'APPROVED':
        st.success("""
        **Congratulations! Your loan has been approved.**
        
        Next steps:
        1. Review the loan terms and conditions
        2. Accept the loan offer
        3. Complete final documentation
        4. Funds will be transferred to your account
        
        For questions, please contact our customer service team.
        """)
    else:
        st.info("""
        **Your application is under review.**
        
        Our team will contact you shortly with additional information or requirements.
        You can also contact our customer service team for assistance.
        """)

