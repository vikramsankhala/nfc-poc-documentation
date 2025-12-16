"""
Investor Pitch & Proposal Page
Comprehensive investor presentation with financial instruments and funding details
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def show():
    st.markdown('<h1 class="main-header">💼 Investor Proposal & Pitch Deck</h1>', unsafe_allow_html=True)
    st.markdown("Comprehensive investment opportunity in AI-Augmented Customer Onboarding for Financial Services")
    
    st.markdown("---")
    
    # Navigation tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📊 Executive Summary",
        "💰 Financial Projections",
        "💵 Funding Instruments",
        "📈 Market Opportunity",
        "🎯 Business Model",
        "🚀 Growth Strategy",
        "📋 Investment Terms"
    ])
    
    with tab1:
        show_executive_summary()
    
    with tab2:
        show_financial_projections()
    
    with tab3:
        show_funding_instruments()
    
    with tab4:
        show_market_opportunity()
    
    with tab5:
        show_business_model()
    
    with tab6:
        show_growth_strategy()
    
    with tab7:
        show_investment_terms()


def show_executive_summary():
    st.markdown("## 📊 Executive Summary")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### The Opportunity
        
        **AI-Augmented Customer Onboarding Platform** is a revolutionary fintech solution that transforms 
        the traditional banking customer onboarding process through intelligent automation, reducing 
        processing time from days to minutes while ensuring regulatory compliance and fraud prevention.
        
        **Key Value Propositions:**
        - ⚡ **90% reduction** in onboarding time (from 5-7 days to <30 minutes)
        - 💰 **60% cost reduction** per customer acquisition
        - 🛡️ **99.8% accuracy** in fraud detection and KYC compliance
        - 📱 **Omnichannel solution** (Web + Mobile + API)
        - 🤖 **AI-powered** decisioning and risk assessment
        """)
    
    with col2:
        st.markdown("""
        ### Investment Highlights
        
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white; margin: 10px 0;">
            <div style="font-size: 32px; font-weight: bold; margin-bottom: 10px;">$5M</div>
            <div style="font-size: 14px;">Series A Funding</div>
        </div>
        
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 10px; color: white; margin: 10px 0;">
            <div style="font-size: 32px; font-weight: bold; margin-bottom: 10px;">$50M</div>
            <div style="font-size: 14px;">5-Year Revenue Target</div>
        </div>
        
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 10px; color: white; margin: 10px 0;">
            <div style="font-size: 32px; font-weight: bold; margin-bottom: 10px;">25%</div>
            <div style="font-size: 14px;">Target Market Share</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Key Metrics
    st.markdown("### Key Performance Indicators")
    
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    
    with metrics_col1:
        st.metric("Current ARR", "$2.5M", "+150% YoY")
    
    with metrics_col2:
        st.metric("Customer Base", "45+", "Financial Institutions")
    
    with metrics_col3:
        st.metric("Processed Applications", "250K+", "Annually")
    
    with metrics_col4:
        st.metric("Success Rate", "94%", "Approval Rate")
    
    st.markdown("---")
    
    # Problem Statement
    st.markdown("### The Problem We Solve")
    
    problem_col1, problem_col2 = st.columns(2)
    
    with problem_col1:
        st.markdown("""
        **Current Market Pain Points:**
        
        - 🐌 **Slow Processing**: Traditional onboarding takes 5-7 business days
        - 💸 **High Costs**: $500-800 per customer acquisition
        - ❌ **High Rejection Rates**: 30-40% manual error rate
        - 🔒 **Compliance Risk**: Manual processes prone to regulatory violations
        - 📱 **Poor UX**: Fragmented, multi-step customer experience
        - 🔍 **Limited Fraud Detection**: Reactive rather than proactive
        """)
    
    with problem_col2:
        st.markdown("""
        **Our Solution Delivers:**
        
        - ⚡ **Instant Processing**: <30 minutes end-to-end
        - 💰 **Cost Efficient**: $200-300 per customer (60% reduction)
        - ✅ **High Accuracy**: 99.8% automated decision accuracy
        - 🛡️ **Compliance First**: Built-in KYC/AML automation
        - 📱 **Seamless UX**: Single, intuitive interface
        - 🤖 **AI-Powered**: Proactive fraud detection and risk assessment
        """)


def show_financial_projections():
    st.markdown("## 💰 Financial Projections & Model")
    
    # Revenue Projections
    st.markdown("### Revenue Projections (5-Year Forecast)")
    
    years = ['2024', '2025', '2026', '2027', '2028']
    revenue_saas = [2.5, 8.5, 18.0, 32.0, 50.0]  # Million USD
    revenue_services = [0.5, 2.0, 5.0, 10.0, 15.0]
    revenue_total = [r + s for r, s in zip(revenue_saas, revenue_services)]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='SaaS Revenue',
        x=years,
        y=revenue_saas,
        marker_color='#1f77b4'
    ))
    
    fig.add_trace(go.Bar(
        name='Professional Services',
        x=years,
        y=revenue_services,
        marker_color='#ff7f0e'
    ))
    
    fig.add_trace(go.Scatter(
        name='Total Revenue',
        x=years,
        y=revenue_total,
        mode='lines+markers',
        line=dict(color='#2ca02c', width=3),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title="5-Year Revenue Projection (USD Millions)",
        xaxis_title="Year",
        yaxis_title="Revenue (USD Millions)",
        barmode='stack',
        height=400,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Financial Metrics Table
    st.markdown("### Financial Metrics")
    
    financial_data = {
        'Metric': [
            'Annual Recurring Revenue (ARR)',
            'Monthly Recurring Revenue (MRR)',
            'Gross Margin',
            'EBITDA Margin',
            'Customer Acquisition Cost (CAC)',
            'Lifetime Value (LTV)',
            'LTV:CAC Ratio',
            'Churn Rate',
            'Net Revenue Retention'
        ],
        '2024 (Actual)': [
            '$2.5M',
            '$208K',
            '78%',
            '-15%',
            '$45K',
            '$180K',
            '4:1',
            '8%',
            '115%'
        ],
        '2025 (Projected)': [
            '$8.5M',
            '$708K',
            '82%',
            '12%',
            '$38K',
            '$220K',
            '5.8:1',
            '6%',
            '125%'
        ],
        '2026 (Projected)': [
            '$18.0M',
            '$1.5M',
            '85%',
            '25%',
            '$32K',
            '$280K',
            '8.75:1',
            '5%',
            '135%'
        ]
    }
    
    import pandas as pd
    df_financial = pd.DataFrame(financial_data)
    st.dataframe(df_financial, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Unit Economics
    st.markdown("### Unit Economics Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Customer Economics
        fig_units = go.Figure()
        
        fig_units.add_trace(go.Bar(
            name='Revenue per Customer',
            x=['2024', '2025', '2026'],
            y=[55, 75, 95],  # Thousands
            marker_color='#22c55e'
        ))
        
        fig_units.add_trace(go.Bar(
            name='Cost per Customer',
            x=['2024', '2025', '2026'],
            y=[45, 38, 32],  # Thousands
            marker_color='#ef4444'
        ))
        
        fig_units.update_layout(
            title="Revenue vs Cost per Customer (USD Thousands)",
            xaxis_title="Year",
            yaxis_title="Amount (USD Thousands)",
            barmode='group',
            height=300
        )
        
        st.plotly_chart(fig_units, use_container_width=True)
    
    with col2:
        # Profitability Timeline
        fig_profit = go.Figure()
        
        fig_profit.add_trace(go.Scatter(
            x=['2024', '2025', '2026', '2027', '2028'],
            y=[-15, 12, 25, 32, 38],  # EBITDA Margin %
            mode='lines+markers',
            line=dict(color='#22c55e', width=4),
            marker=dict(size=12, color='#22c55e'),
            fill='tozeroy',
            fillcolor='rgba(34, 197, 94, 0.2)'
        ))
        
        fig_profit.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Break-even")
        
        fig_profit.update_layout(
            title="EBITDA Margin Projection (%)",
            xaxis_title="Year",
            yaxis_title="EBITDA Margin (%)",
            height=300
        )
        
        st.plotly_chart(fig_profit, use_container_width=True)
    
    st.markdown("---")
    
    # Use of Funds
    st.markdown("### Use of Funds - $5M Series A")
    
    fund_allocation = {
        'Category': [
            'Product Development & R&D',
            'Sales & Marketing',
            'Customer Success & Support',
            'Operations & Infrastructure',
            'Team Expansion',
            'Working Capital',
            'Regulatory & Compliance'
        ],
        'Amount (USD)': [
            '$1,500,000',
            '$1,200,000',
            '$800,000',
            '$600,000',
            '$500,000',
            '$300,000',
            '$100,000'
        ],
        'Percentage': [
            '30%',
            '24%',
            '16%',
            '12%',
            '10%',
            '6%',
            '2%'
        ]
    }
    
    df_funds = pd.DataFrame(fund_allocation)
    st.dataframe(df_funds, use_container_width=True, hide_index=True)
    
    # Visual representation
    fig_funds = px.pie(
        values=[30, 24, 16, 12, 10, 6, 2],
        names=fund_allocation['Category'],
        title="Use of Funds Distribution",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_funds.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_funds, use_container_width=True)


def show_funding_instruments():
    st.markdown("## 💵 Funding Instruments & Structures")
    
    st.markdown("### Available Investment Options")
    
    # Investment Instruments
    instrument_tabs = st.tabs(["Equity", "Convertible Notes", "SAFE", "Revenue Share", "Hybrid"])
    
    with instrument_tabs[0]:
        st.markdown("""
        ### 🏢 Equity Investment
        
        **Structure:** Preferred Stock (Series A)
        
        **Terms:**
        - **Investment Amount:** $500K - $5M
        - **Valuation:** $20M Pre-money / $25M Post-money
        - **Equity Stake:** 2% - 20% (proportional)
        - **Liquidation Preference:** 1x non-participating
        - **Anti-dilution:** Broad-based weighted average
        - **Board Seat:** Available for investments >$2M
        
        **Benefits:**
        - ✅ Direct equity ownership
        - ✅ Voting rights and board representation (if applicable)
        - ✅ Dividend rights (when declared)
        - ✅ Liquidation preference protection
        - ✅ Standard investor protections
        
        **Ideal For:** Strategic investors, VCs, family offices seeking long-term equity position
        """)
        
        st.info("💡 **Minimum Investment:** $500,000 | **Maximum Investment:** $5,000,000")
    
    with instrument_tabs[1]:
        st.markdown("""
        ### 📜 Convertible Notes
        
        **Structure:** Convertible Debt with Discount & Cap
        
        **Terms:**
        - **Investment Amount:** $100K - $2M
        - **Interest Rate:** 6% per annum (simple interest)
        - **Maturity:** 24 months
        - **Conversion Discount:** 20% discount on next equity round
        - **Valuation Cap:** $25M
        - **Conversion Trigger:** Next equity financing ≥$3M
        
        **Benefits:**
        - ✅ Lower initial valuation risk
        - ✅ Automatic conversion at discount
        - ✅ Interest accrual
        - ✅ Earlier investor advantage
        - ✅ Flexible conversion terms
        
        **Ideal For:** Angel investors, early-stage funds, bridge financing
        """)
        
        st.info("💡 **Minimum Investment:** $100,000 | **Maximum Investment:** $2,000,000")
    
    with instrument_tabs[2]:
        st.markdown("""
        ### 🚀 SAFE (Simple Agreement for Future Equity)
        
        **Structure:** Y Combinator Standard SAFE
        
        **Terms:**
        - **Investment Amount:** $50K - $1M
        - **Valuation Cap:** $22M
        - **Discount Rate:** 20%
        - **Most Favored Nation (MFN):** Yes
        - **Conversion:** Next equity financing or liquidity event
        
        **Benefits:**
        - ✅ Simple, standardized terms
        - ✅ No interest or maturity date
        - ✅ Automatic conversion
        - ✅ Lower legal costs
        - ✅ Fast execution
        
        **Ideal For:** Angel investors, accelerators, early supporters
        """)
        
        st.info("💡 **Minimum Investment:** $50,000 | **Maximum Investment:** $1,000,000")
    
    with instrument_tabs[3]:
        st.markdown("""
        ### 💰 Revenue Share Agreement
        
        **Structure:** Revenue-Based Financing
        
        **Terms:**
        - **Investment Amount:** $250K - $1.5M
        - **Return Multiple:** 1.5x - 2.0x (based on amount)
        - **Revenue Share:** 3-5% of monthly revenue
        - **Cap:** 1.5x - 2.0x of principal
        - **Term:** Until cap reached or 48 months (whichever first)
        
        **Benefits:**
        - ✅ No equity dilution
        - ✅ Aligned with revenue growth
        - ✅ Predictable returns
        - ✅ Flexible repayment
        - ✅ Lower risk for investors
        
        **Ideal For:** Debt-focused investors, revenue-based lenders, alternative financing
        """)
        
        st.info("💡 **Minimum Investment:** $250,000 | **Maximum Investment:** $1,500,000")
    
    with instrument_tabs[4]:
        st.markdown("""
        ### 🔀 Hybrid Instruments
        
        **Structure:** Customizable Investment Structures
        
        **Options:**
        1. **Equity + Revenue Share:** Lower equity stake with revenue participation
        2. **Convertible + Warrants:** Convertible note with equity warrants
        3. **Preferred + Options:** Preferred stock with employee option pool participation
        4. **Debt + Equity Kicker:** Senior debt with equity upside
        
        **Benefits:**
        - ✅ Tailored to investor needs
        - ✅ Risk/return optimization
        - ✅ Flexible terms
        - ✅ Multiple exit strategies
        
        **Ideal For:** Sophisticated investors, strategic partners, custom requirements
        """)
        
        st.info("💡 **Custom structures available - Contact for details**")
    
    st.markdown("---")
    
    # Comparison Table
    st.markdown("### Investment Instrument Comparison")
    
    comparison_data = {
        'Instrument': ['Equity', 'Convertible Notes', 'SAFE', 'Revenue Share'],
        'Min Investment': ['$500K', '$100K', '$50K', '$250K'],
        'Valuation Risk': ['Medium', 'Low', 'Low', 'None'],
        'Dilution': ['Immediate', 'Deferred', 'Deferred', 'None'],
        'Return Potential': ['High', 'High', 'High', 'Medium'],
        'Liquidity': ['Exit Event', 'Conversion/Exit', 'Conversion/Exit', 'Monthly'],
        'Term': ['Indefinite', '24 months', 'Until conversion', '48 months max']
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True, hide_index=True)


def show_market_opportunity():
    st.markdown("## 📈 Market Opportunity & TAM Analysis")
    
    # TAM, SAM, SOM
    st.markdown("### Total Addressable Market (TAM)")
    
    tam_data = {
        'Market Segment': [
            'Global Banking & Financial Services',
            'North American Market',
            'European Market',
            'APAC Market',
            'Target Addressable Market (TAM)',
            'Serviceable Available Market (SAM)',
            'Serviceable Obtainable Market (SOM)'
        ],
        'Market Size (USD)': [
            '$8.5 Trillion',
            '$2.1 Trillion',
            '$1.8 Trillion',
            '$2.5 Trillion',
            '$450 Billion',
            '$85 Billion',
            '$2.5 Billion'
        ],
        'CAGR': [
            '6.2%',
            '7.1%',
            '5.8%',
            '8.3%',
            '12.5%',
            '15.2%',
            '18.5%'
        ]
    }
    
    df_tam = pd.DataFrame(tam_data)
    st.dataframe(df_tam, use_container_width=True, hide_index=True)
    
    # Market Size Visualization
    fig_market = go.Figure()
    
    fig_market.add_trace(go.Bar(
        name='Market Size',
        x=['TAM', 'SAM', 'SOM'],
        y=[450, 85, 2.5],
        marker_color=['#1f77b4', '#ff7f0e', '#2ca02c'],
        text=['$450B', '$85B', '$2.5B'],
        textposition='outside'
    ))
    
    fig_market.update_layout(
        title="Market Size Analysis (USD Billions)",
        xaxis_title="Market Segment",
        yaxis_title="Market Size (USD Billions)",
        height=400
    )
    
    st.plotly_chart(fig_market, use_container_width=True)
    
    st.markdown("---")
    
    # Market Trends
    st.markdown("### Market Trends & Drivers")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Growth Drivers:**
        
        - 📱 **Digital Transformation:** 78% of banks prioritizing digital onboarding
        - 🤖 **AI Adoption:** $12B AI in fintech market by 2026
        - 🔒 **Regulatory Compliance:** Increasing KYC/AML requirements
        - 💰 **Cost Pressure:** Need for operational efficiency
        - 👥 **Customer Expectations:** Demand for instant, seamless experiences
        - 🌐 **Open Banking:** API-driven financial services growth
        """)
    
    with col2:
        st.markdown("""
        **Competitive Advantages:**
        
        - ⚡ **Speed:** 10x faster than competitors
        - 🎯 **Accuracy:** 99.8% vs industry average 85%
        - 💵 **Cost:** 60% lower than traditional solutions
        - 🛡️ **Compliance:** Built-in regulatory automation
        - 📊 **Analytics:** Advanced AI-powered insights
        - 🔌 **Integration:** Seamless API connectivity
        """)


def show_business_model():
    st.markdown("## 🎯 Business Model & Revenue Streams")
    
    # Revenue Model
    st.markdown("### Revenue Model")
    
    revenue_streams = {
        'Revenue Stream': [
            'SaaS Subscription (Core Platform)',
            'Transaction-Based Fees',
            'Professional Services',
            'API Usage Fees',
            'Premium Features & Add-ons',
            'White-Label Licensing',
            'Data & Analytics Services'
        ],
        'Description': [
            'Monthly/annual per-seat or per-institution pricing',
            'Per-application processed fee',
            'Implementation, customization, training',
            'Pay-per-API-call for third-party integrations',
            'Advanced AI features, premium support',
            'Licensing platform for large enterprises',
            'Aggregated insights and market intelligence'
        ],
        '2024 Revenue %': [
            '65%',
            '15%',
            '12%',
            '3%',
            '3%',
            '1%',
            '1%'
        ],
        '2026 Projected %': [
            '55%',
            '20%',
            '12%',
            '5%',
            '4%',
            '2%',
            '2%'
        ]
    }
    
    df_revenue = pd.DataFrame(revenue_streams)
    st.dataframe(df_revenue, use_container_width=True, hide_index=True)
    
    # Pricing Model
    st.markdown("---")
    st.markdown("### Pricing Model")
    
    pricing_col1, pricing_col2, pricing_col3 = st.columns(3)
    
    with pricing_col1:
        st.markdown("""
        <div style="background: #e3f2fd; padding: 20px; border-radius: 10px; border: 2px solid #1f77b4;">
            <h3 style="color: #1f77b4; margin-top: 0;">Starter</h3>
            <div style="font-size: 32px; font-weight: bold; color: #1f77b4;">$5K</div>
            <div style="color: #666; margin-bottom: 15px;">per month</div>
            <ul style="text-align: left; color: #333;">
                <li>Up to 1,000 applications/month</li>
                <li>Basic KYC/AML</li>
                <li>Standard support</li>
                <li>API access</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with pricing_col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; border: 2px solid #667eea; color: white;">
            <h3 style="color: white; margin-top: 0;">Professional</h3>
            <div style="font-size: 32px; font-weight: bold;">$15K</div>
            <div style="opacity: 0.9; margin-bottom: 15px;">per month</div>
            <ul style="text-align: left;">
                <li>Up to 10,000 applications/month</li>
                <li>Advanced AI features</li>
                <li>Priority support</li>
                <li>Custom integrations</li>
                <li>Analytics dashboard</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with pricing_col3:
        st.markdown("""
        <div style="background: #fff3e0; padding: 20px; border-radius: 10px; border: 2px solid #ff9800;">
            <h3 style="color: #ff9800; margin-top: 0;">Enterprise</h3>
            <div style="font-size: 32px; font-weight: bold; color: #ff9800;">Custom</div>
            <div style="color: #666; margin-bottom: 15px;">pricing</div>
            <ul style="text-align: left; color: #333;">
                <li>Unlimited applications</li>
                <li>Full AI suite</li>
                <li>Dedicated support</li>
                <li>White-label option</li>
                <li>On-premise deployment</li>
                <li>SLA guarantees</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


def show_growth_strategy():
    st.markdown("## 🚀 Growth Strategy & Roadmap")
    
    # Growth Phases
    st.markdown("### 12-Month Growth Roadmap")
    
    roadmap_data = {
        'Quarter': ['Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'],
        'Key Milestones': [
            'Series A close, team expansion (15→25), 3 new enterprise clients',
            'Product v2.0 launch, expand to 2 new markets, 10 new clients',
            'Strategic partnerships, API marketplace launch, 20 new clients',
            'Series B preparation, international expansion, 35+ total clients'
        ],
        'Revenue Target': [
            '$3.5M ARR',
            '$5.5M ARR',
            '$8.5M ARR',
            '$12M ARR'
        ],
        'Team Size': [
            '25',
            '35',
            '50',
            '65'
        ]
    }
    
    df_roadmap = pd.DataFrame(roadmap_data)
    st.dataframe(df_roadmap, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Growth Strategy
    st.markdown("### Growth Levers")
    
    growth_col1, growth_col2 = st.columns(2)
    
    with growth_col1:
        st.markdown("""
        **1. Product-Led Growth**
        - Self-service onboarding
        - Free trial programs
        - Viral referral mechanisms
        - API-first approach
        
        **2. Sales & Partnerships**
        - Direct enterprise sales
        - Channel partnerships
        - System integrator alliances
        - Fintech ecosystem integration
        
        **3. Market Expansion**
        - Geographic expansion (EU, APAC)
        - Vertical expansion (insurance, lending)
        - Use case expansion (KYC, AML, onboarding)
        """)
    
    with growth_col2:
        st.markdown("""
        **4. Technology Innovation**
        - Advanced AI/ML capabilities
        - Blockchain integration
        - Real-time processing
        - Enhanced security features
        
        **5. Customer Success**
        - High NPS scores (>70)
        - Expansion revenue (135% NRR)
        - Case studies & testimonials
        - Community building
        
        **6. Strategic M&A**
        - Complementary technology
        - Customer base acquisition
        - Talent acquisition
        - Market consolidation
        """)


def show_investment_terms():
    st.markdown("## 📋 Investment Terms & Conditions")
    
    # Key Terms
    st.markdown("### Key Investment Terms")
    
    terms_data = {
        'Term': [
            'Pre-Money Valuation',
            'Post-Money Valuation',
            'Investment Amount',
            'Equity Stake',
            'Liquidation Preference',
            'Anti-Dilution Protection',
            'Board Representation',
            'Voting Rights',
            'Information Rights',
            'Right of First Refusal',
            'Tag-Along Rights',
            'Drag-Along Rights'
        ],
        'Details': [
            '$20 Million',
            '$25 Million',
            '$5 Million',
            '20% (proportional)',
            '1x Non-Participating',
            'Broad-Based Weighted Average',
            '1 Board Seat (if >$2M investment)',
            'Proportional to equity stake',
            'Quarterly financials, annual audit',
            'Standard ROFR on new issuances',
            'Standard tag-along rights',
            'Standard drag-along rights'
        ]
    }
    
    df_terms = pd.DataFrame(terms_data)
    st.dataframe(df_terms, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Exit Strategy
    st.markdown("### Exit Strategy & Timeline")
    
    exit_col1, exit_col2 = st.columns(2)
    
    with exit_col1:
        st.markdown("""
        **Potential Exit Scenarios:**
        
        **1. Strategic Acquisition (3-5 years)**
        - Target: Large fintech, banks, or tech companies
        - Valuation: 8-12x revenue multiple
        - Probability: High (70%)
        
        **2. IPO (5-7 years)**
        - Target: NASDAQ or NYSE
        - Valuation: 10-15x revenue multiple
        - Probability: Medium (25%)
        
        **3. Secondary Sale (3-5 years)**
        - Target: Private equity or larger VCs
        - Valuation: 6-10x revenue multiple
        - Probability: Medium (30%)
        """)
    
    with exit_col2:
        st.markdown("""
        **Expected Returns:**
        
        **Conservative Scenario:**
        - 5-year exit at $150M valuation
        - 6x return on $5M investment
        - IRR: 43%
        
        **Base Case Scenario:**
        - 5-year exit at $250M valuation
        - 10x return on $5M investment
        - IRR: 58%
        
        **Optimistic Scenario:**
        - 5-year exit at $400M valuation
        - 16x return on $5M investment
        - IRR: 74%
        """)
    
    st.markdown("---")
    
    # Risk Factors
    st.markdown("### Risk Factors & Mitigation")
    
    risk_data = {
        'Risk Category': [
            'Market Competition',
            'Regulatory Changes',
            'Technology Disruption',
            'Customer Concentration',
            'Key Personnel',
            'Cybersecurity',
            'Economic Downturn'
        ],
        'Risk Level': [
            'Medium',
            'Medium',
            'Low',
            'Low',
            'Low',
            'Medium',
            'Medium'
        ],
        'Mitigation Strategy': [
            'Continuous innovation, first-mover advantage, strong IP',
            'Compliance-first design, regulatory partnerships, legal expertise',
            'R&D investment, technology partnerships, agile development',
            'Diversified customer base, long-term contracts, expansion revenue',
            'Equity incentives, strong culture, succession planning',
            'Enterprise-grade security, regular audits, insurance coverage',
            'Recurring revenue model, cost flexibility, market diversification'
        ]
    }
    
    df_risk = pd.DataFrame(risk_data)
    st.dataframe(df_risk, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Contact Information
    st.markdown("### Investment Contact")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; text-align: center;">
        <h2 style="color: white; margin-top: 0;">Ready to Invest?</h2>
        <p style="font-size: 18px; margin-bottom: 20px;">Contact our investment team to discuss opportunities</p>
        <div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 10px; margin: 20px 0;">
            <div style="font-size: 16px; margin: 10px 0;"><strong>📧 Email:</strong> investors@fptbanking.com</div>
            <div style="font-size: 16px; margin: 10px 0;"><strong>📞 Phone:</strong> +1 (555) 123-4567</div>
            <div style="font-size: 16px; margin: 10px 0;"><strong>🌐 Website:</strong> www.fptbanking.com/investors</div>
        </div>
        <p style="font-size: 14px; opacity: 0.9;">Confidentiality Agreement available upon request</p>
    </div>
    """, unsafe_allow_html=True)

