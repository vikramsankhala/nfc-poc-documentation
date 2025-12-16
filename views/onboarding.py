"""
Customer Onboarding Page
"""

import streamlit as st
from datetime import date, timedelta

def show():
    st.markdown('<h1 class="main-header">👤 Customer Onboarding</h1>', unsafe_allow_html=True)
    st.markdown("Complete the application form to begin the onboarding process.")
    
    st.markdown("---")
    
    # Initialize session state for customer data
    if 'customer_data' not in st.session_state:
        st.session_state.customer_data = {}
    
    with st.form("onboarding_form"):
        st.markdown("### Personal Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input(
                "First Name *",
                value=st.session_state.customer_data.get('first_name', ''),
                placeholder="Enter your first name"
            )
            
            last_name = st.text_input(
                "Last Name *",
                value=st.session_state.customer_data.get('last_name', ''),
                placeholder="Enter your last name"
            )
            
            date_of_birth = st.date_input(
                "Date of Birth *",
                value=st.session_state.customer_data.get('date_of_birth', date(1990, 1, 1)),
                max_value=date.today() - timedelta(days=365*18),
                min_value=date(1920, 1, 1)
            )
            
            nationality = st.selectbox(
                "Nationality *",
                ["United Kingdom", "United States", "Canada", "Australia", "Germany", "France", "Other"],
                index=0 if not st.session_state.customer_data.get('nationality') else 
                ["United Kingdom", "United States", "Canada", "Australia", "Germany", "France", "Other"].index(
                    st.session_state.customer_data.get('nationality', 'United Kingdom')
                )
            )
        
        with col2:
            email = st.text_input(
                "Email Address *",
                value=st.session_state.customer_data.get('email', ''),
                placeholder="your.email@example.com"
            )
            
            phone = st.text_input(
                "Phone Number *",
                value=st.session_state.customer_data.get('phone', ''),
                placeholder="+44 20 1234 5678"
            )
            
            address_line1 = st.text_input(
                "Address Line 1 *",
                value=st.session_state.customer_data.get('address_line1', ''),
                placeholder="Street address"
            )
            
            address_line2 = st.text_input(
                "Address Line 2",
                value=st.session_state.customer_data.get('address_line2', ''),
                placeholder="Apartment, suite, etc."
            )
        
        col3, col4 = st.columns(2)
        
        with col3:
            city = st.text_input(
                "City *",
                value=st.session_state.customer_data.get('city', ''),
                placeholder="City"
            )
            
            postcode = st.text_input(
                "Postcode *",
                value=st.session_state.customer_data.get('postcode', ''),
                placeholder="SW1A 1AA"
            )
        
        with col4:
            country = st.selectbox(
                "Country *",
                ["United Kingdom", "United States", "Canada", "Australia", "Germany", "France"],
                index=0 if not st.session_state.customer_data.get('country') else 
                ["United Kingdom", "United States", "Canada", "Australia", "Germany", "France"].index(
                    st.session_state.customer_data.get('country', 'United Kingdom')
                )
            )
        
        st.markdown("---")
        st.markdown("### Employment Information")
        
        col5, col6 = st.columns(2)
        
        with col5:
            employment_status = st.selectbox(
                "Employment Status *",
                ["Employed", "Self-Employed", "Unemployed", "Retired", "Student"],
                index=0 if not st.session_state.customer_data.get('employment_status') else
                ["Employed", "Self-Employed", "Unemployed", "Retired", "Student"].index(
                    st.session_state.customer_data.get('employment_status', 'Employed')
                )
            )
            
            employer_name = st.text_input(
                "Employer Name",
                value=st.session_state.customer_data.get('employer_name', ''),
                placeholder="Company name",
                disabled=(employment_status not in ["Employed", "Self-Employed"])
            )
        
        with col6:
            annual_income = st.number_input(
                "Annual Income (£) *",
                min_value=0,
                value=int(st.session_state.customer_data.get('annual_income', 30000)),
                step=1000,
                format="%d"
            )
            
            years_employed = st.number_input(
                "Years at Current Employment",
                min_value=0,
                max_value=50,
                value=int(st.session_state.customer_data.get('years_employed', 2)),
                step=1,
                disabled=(employment_status not in ["Employed", "Self-Employed"])
            )
        
        st.markdown("---")
        st.markdown("### Loan Requirements")
        
        col7, col8 = st.columns(2)
        
        with col7:
            loan_purpose = st.selectbox(
                "Loan Purpose *",
                ["Vehicle Purchase", "Home Improvement", "Debt Consolidation", "Business", "Other"],
                index=0 if not st.session_state.customer_data.get('loan_purpose') else
                ["Vehicle Purchase", "Home Improvement", "Debt Consolidation", "Business", "Other"].index(
                    st.session_state.customer_data.get('loan_purpose', 'Vehicle Purchase')
                )
            )
        
        with col8:
            requested_amount = st.number_input(
                "Requested Loan Amount (£) *",
                min_value=1000,
                max_value=100000,
                value=int(st.session_state.customer_data.get('requested_amount', 15000)),
                step=1000,
                format="%d"
            )
        
        st.markdown("---")
        
        # Submit button
        submitted = st.form_submit_button("Submit Application", use_container_width=True)
        
        if submitted:
            # Validate required fields
            required_fields = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'address_line1': address_line1,
                'city': city,
                'postcode': postcode,
                'annual_income': annual_income
            }
            
            missing_fields = [k for k, v in required_fields.items() if not v]
            
            if missing_fields:
                st.error(f"Please fill in all required fields: {', '.join(missing_fields)}")
            else:
                # Save to session state
                st.session_state.customer_data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'date_of_birth': date_of_birth,
                    'nationality': nationality,
                    'email': email,
                    'phone': phone,
                    'address_line1': address_line1,
                    'address_line2': address_line2,
                    'city': city,
                    'postcode': postcode,
                    'country': country,
                    'employment_status': employment_status,
                    'employer_name': employer_name,
                    'annual_income': annual_income,
                    'years_employed': years_employed,
                    'loan_purpose': loan_purpose,
                    'requested_amount': requested_amount,
                    'submitted_at': date.today().isoformat()
                }
                
                st.success("✅ Application submitted successfully!")
                st.info("📋 Please proceed to the **eKYC** page to complete identity verification.")
                
                # Show summary
                with st.expander("View Application Summary", expanded=False):
                    st.json(st.session_state.customer_data)
    
    # Display current data if exists
    if st.session_state.customer_data and not submitted:
        st.markdown("---")
        st.markdown("### 📄 Current Application Data")
        st.json(st.session_state.customer_data)

