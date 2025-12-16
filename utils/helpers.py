"""
Helper utility functions
"""

import streamlit as st

def get_progress_status():
    """Get progress status for workflow steps"""
    progress = {
        'step_0': bool(st.session_state.get('customer_data', {}).get('submitted_at')),
        'step_1': st.session_state.get('kyc_status', {}).get('overall_status') == 'COMPLETE',
        'step_2': bool(st.session_state.get('asset_data', {}).get('market_value')),
        'step_3': bool(st.session_state.get('loan_decision')),
        'step_4': bool(st.session_state.get('loan_decision', {}).get('status') == 'APPROVED')
    }
    return progress

