"""
AI Simulation Module
Simulates AI processing for demonstration purposes
"""

import random
import uuid
from datetime import datetime, date

def simulate_nfc_reading(customer_data):
    """Simulate NFC passport chip reading"""
    if not customer_data:
        return None
    
    # Simulate reading passport data
    passport_data = {
        'passport_number': f"GB{random.randint(100000000, 999999999)}",
        'nationality': customer_data.get('nationality', 'United Kingdom'),
        'date_of_birth': str(customer_data.get('date_of_birth', date(1990, 1, 1))),
        'first_name': customer_data.get('first_name', ''),
        'last_name': customer_data.get('last_name', ''),
        'gender': random.choice(['M', 'F']),
        'expiry_date': str(date.today().replace(year=date.today().year + 5)),
        'issuing_authority': 'UKPA',
        'mrz_line1': f"P<GBR{customer_data.get('last_name', '').upper()}<{customer_data.get('first_name', '').upper()}",
        'mrz_line2': f"{passport_data['passport_number']}GBR{random.randint(100000, 999999)}",
        'chip_authenticated': True,
        'read_timestamp': datetime.now().isoformat()
    }
    
    return passport_data

def simulate_kyc_verification(customer_data, doc_type, filename):
    """Simulate document verification with OCR"""
    if not customer_data:
        return None
    
    # Simulate OCR extraction
    extracted_data = {
        'document_type': doc_type,
        'document_number': f"{random.choice(['P', 'DL', 'ID'])}{random.randint(100000, 999999)}",
        'first_name': customer_data.get('first_name', ''),
        'last_name': customer_data.get('last_name', ''),
        'date_of_birth': str(customer_data.get('date_of_birth', '')),
        'nationality': customer_data.get('nationality', 'United Kingdom'),
        'address': customer_data.get('address_line1', ''),
        'expiry_date': str(date.today().replace(year=date.today().year + 3)),
        'issuing_authority': 'UKPA' if doc_type == 'Passport' else 'DVLA',
        'extraction_confidence': round(random.uniform(0.85, 0.99), 2)
    }
    
    # Simulate matching with application form
    match_status = {
        'first_name': True,
        'last_name': True,
        'date_of_birth': True,
        'nationality': True,
        'address': random.choice([True, True, True, False]),  # Mostly match
        'document_authentic': True,
        'not_expired': True,
        'image_quality': 'GOOD',
        'liveness_detected': True
    }
    
    return {
        'extracted_data': extracted_data,
        'match_status': match_status,
        'verification_status': 'VERIFIED' if all(match_status.values()) else 'REVIEW_REQUIRED',
        'confidence_score': round(random.uniform(0.88, 0.98), 2),
        'processed_at': datetime.now().isoformat()
    }

def simulate_asset_valuation(asset_info, uploaded_photos):
    """Simulate AI-powered asset valuation"""
    if not asset_info or not uploaded_photos:
        return None
    
    asset_type = asset_info.get('type', 'Vehicle')
    
    # Base market value (simulated)
    if asset_type == 'Vehicle':
        make = asset_info.get('make', 'BMW')
        model = asset_info.get('model', '320d')
        year = asset_info.get('year', 2020)
        mileage = asset_info.get('mileage', 50000)
        condition = asset_info.get('condition', 'Good')
        
        # Simulate market value based on inputs
        base_value = 25000
        age_depreciation = (2025 - year) * 2000
        mileage_depreciation = (mileage / 10000) * 500
        
        condition_multipliers = {
            'Excellent': 1.1,
            'Very Good': 1.0,
            'Good': 0.9,
            'Fair': 0.75,
            'Poor': 0.6
        }
        
        market_value = max(1000, (base_value - age_depreciation - mileage_depreciation) * 
                          condition_multipliers.get(condition, 0.9))
        
        # Simulate condition score from AI analysis
        condition_scores = {
            'Excellent': (9, 10),
            'Very Good': (8, 9),
            'Good': (6, 8),
            'Fair': (4, 6),
            'Poor': (2, 4)
        }
        
        score_range = condition_scores.get(condition, (6, 8))
        condition_score = round(random.uniform(score_range[0], score_range[1]), 1)
        
        # DVLA verification
        dvla_verification = {
            'verified': True,
            'status': 'VERIFIED',
            'make_match': 'MATCH',
            'model_match': 'MATCH',
            'registration_valid': 'VALID',
            'mileage_check': 'CONSISTENT',
            'stolen_check': 'CLEAR',
            'written_off': False
        }
        
        # Market data
        market_data = {
            'avg_price': market_value * 1.05,
            'min_price': market_value * 0.85,
            'max_price': market_value * 1.15,
            'trend': random.choice(['Stable', 'Increasing', 'Decreasing']),
            'comparables': random.randint(15, 50),
            'source': 'CAP HPI'
        }
        
    else:
        # Generic asset
        market_value = random.randint(5000, 50000)
        condition_score = round(random.uniform(6, 9), 1)
        dvla_verification = None
        market_data = {
            'avg_price': market_value,
            'min_price': market_value * 0.8,
            'max_price': market_value * 1.2,
            'trend': 'Stable',
            'comparables': random.randint(5, 20),
            'source': 'Market Data'
        }
    
    # Condition details from AI analysis
    condition_details = {
        'exterior_condition': round(random.uniform(6, 10), 1),
        'interior_condition': round(random.uniform(6, 10), 1),
        'mechanical_condition': round(random.uniform(6, 10), 1),
        'overall_quality': condition_score
    }
    
    # LTV ratio based on condition
    if condition_score >= 8:
        ltv_ratio = 0.75
    elif condition_score >= 6:
        ltv_ratio = 0.70
    else:
        ltv_ratio = 0.65
    
    condition_rating = 'Excellent' if condition_score >= 9 else \
                      'Very Good' if condition_score >= 8 else \
                      'Good' if condition_score >= 6 else \
                      'Fair' if condition_score >= 4 else 'Poor'
    
    return {
        'market_value': round(market_value, 2),
        'value_range': round(market_value * 0.15, 2),
        'condition_score': condition_score,
        'condition_rating': condition_rating,
        'condition_details': condition_details,
        'ltv_ratio': ltv_ratio,
        'market_data': market_data,
        'dvla_verification': dvla_verification,
        'analysis_summary': f"AI analysis of {len(uploaded_photos)} photos indicates {condition_rating.lower()} condition. "
                          f"Market valuation based on comparable assets and current market trends. "
                          f"Asset verified against official databases.",
        'photos_analyzed': len(uploaded_photos),
        'valuation_timestamp': datetime.now().isoformat()
    }

def simulate_loan_decision(application_data):
    """Simulate AI-powered loan decision"""
    if not application_data:
        return None
    
    customer = application_data.get('customer', {})
    asset = application_data.get('asset', {})
    kyc = application_data.get('kyc', {})
    loan_request = application_data.get('loan_request', {})
    
    requested_amount = loan_request.get('amount', 0)
    asset_value = asset.get('market_value', 0)
    annual_income = customer.get('annual_income', 0)
    
    # Calculate risk factors
    debt_to_income = (requested_amount / annual_income * 100) if annual_income > 0 else 100
    ltv_ratio = (requested_amount / asset_value * 100) if asset_value > 0 else 100
    
    # Risk scoring
    credit_risk = min(1.0, debt_to_income / 50)  # Higher DTI = higher risk
    asset_risk = max(0.0, (ltv_ratio - 60) / 40) if ltv_ratio > 60 else 0.1  # Higher LTV = higher risk
    
    fraud_score = kyc.get('screening', {}).get('fraud_check', {}).get('fraud_score', 0.1)
    fraud_risk = min(1.0, fraud_score * 2)
    
    condition_score = asset.get('condition_score', 7)
    condition_risk = max(0.0, (7 - condition_score) / 7)  # Lower condition = higher risk
    
    # Risk breakdown
    risk_breakdown = {
        'credit_risk': round(credit_risk, 2),
        'asset_risk': round(asset_risk, 2),
        'fraud_risk': round(fraud_risk, 2),
        'compliance_risk': round(random.uniform(0.05, 0.15), 2)
    }
    
    # Overall risk score (weighted average)
    overall_risk = (
        risk_breakdown['credit_risk'] * 0.3 +
        risk_breakdown['asset_risk'] * 0.3 +
        risk_breakdown['fraud_risk'] * 0.25 +
        risk_breakdown['compliance_risk'] * 0.15
    )
    
    # Decision logic
    approved = overall_risk < 0.6 and ltv_ratio <= 80 and debt_to_income <= 45
    
    if approved:
        # Calculate approved amount (may be less than requested)
        max_loan = asset_value * asset.get('ltv_ratio', 0.7)
        approved_amount = min(requested_amount, max_loan)
        
        # Interest rate based on risk
        base_rate = 5.5
        risk_adjustment = overall_risk * 2.5
        interest_rate = base_rate + risk_adjustment
        
        # Loan terms
        term_years = loan_request.get('term_years', 5)
        monthly_rate = interest_rate / 100 / 12
        monthly_payment = approved_amount * (monthly_rate * (1 + monthly_rate)**(term_years*12)) / \
                         ((1 + monthly_rate)**(term_years*12) - 1) if monthly_rate > 0 else \
                         approved_amount / (term_years * 12)
        
        status = 'APPROVED'
        reason = 'Application meets all criteria. Loan approved based on risk assessment.'
        conditions = []
        
        if ltv_ratio > 70:
            conditions.append('Higher LTV ratio - standard terms apply')
        if debt_to_income > 35:
            conditions.append('Moderate debt-to-income ratio - monitoring recommended')
        
    else:
        approved_amount = 0
        interest_rate = 0
        term_years = 0
        monthly_payment = 0
        status = 'REJECTED'
        
        reasons = []
        if overall_risk >= 0.6:
            reasons.append('High overall risk score')
        if ltv_ratio > 80:
            reasons.append('Loan-to-value ratio exceeds maximum')
        if debt_to_income > 45:
            reasons.append('Debt-to-income ratio too high')
        
        reason = '; '.join(reasons) if reasons else 'Application does not meet approval criteria'
        conditions = []
    
    return {
        'application_id': f"APP-{uuid.uuid4().hex[:8].upper()}",
        'status': status,
        'approved_amount': round(approved_amount, 2),
        'requested_amount': requested_amount,
        'interest_rate': round(interest_rate, 2),
        'term_years': term_years,
        'monthly_payment': round(monthly_payment, 2),
        'risk_score': round(overall_risk, 2),
        'risk_breakdown': risk_breakdown,
        'reason': reason,
        'conditions': conditions,
        'decision_date': datetime.now().isoformat(),
        'risk_analysis': {
            'debt_to_income': round(debt_to_income, 1),
            'ltv_ratio': round(ltv_ratio, 1),
            'asset_value': asset_value,
            'annual_income': annual_income,
            'condition_score': condition_score
        }
    }

