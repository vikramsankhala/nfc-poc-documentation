"""
Investor Targeting Strategy Page
Best investors to approach for the startup
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def show():
    st.markdown('<h1 class="main-header">🎯 Investor Targeting Strategy</h1>', unsafe_allow_html=True)
    st.markdown("Strategic guide to identifying and approaching the best investors for your startup")
    
    st.markdown("---")
    
    # Navigation tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🏆 Top Priority Investors",
        "📊 Investor Categories",
        "🌍 Geographic Strategy",
        "💼 Investor Matching",
        "📈 Outreach Plan",
        "📋 Resources"
    ])
    
    with tab1:
        show_top_priority_investors()
    
    with tab2:
        show_investor_categories()
    
    with tab3:
        show_geographic_strategy()
    
    with tab4:
        show_investor_matching()
    
    with tab5:
        show_outreach_plan()
    
    with tab6:
        show_resources()


def show_top_priority_investors():
    st.markdown("## 🏆 Top 20 Priority Investors")
    
    # Tier 1 Investors
    st.markdown("### Tier 1: Highest Priority (Contact First)")
    
    tier1_data = {
        'Investor': [
            'QED Investors',
            'Ribbit Capital',
            'Andreessen Horowitz (a16z)',
            'Fintech Collective',
            'Anthemis Group',
            'JPMorgan Strategic Investments',
            'Goldman Sachs Principal Strategic Investments',
            'Citi Ventures',
            'Stripe',
            'PayPal Ventures'
        ],
        'Focus': [
            'Fintech specialist, banking expertise',
            'Early-stage fintech focus',
            'Fintech practice, strong brand',
            'B2B fintech focus',
            'Financial services technology',
            'Strategic + customer access',
            'Strategic value',
            'Banking technology focus',
            'Fintech ecosystem leader',
            'Payment and fintech expertise'
        ],
        'Why Ideal': [
            'Deep banking connections, RegTech portfolio',
            'Early-stage fintech specialist',
            'Strong brand, fintech practice',
            'B2B SaaS expertise',
            'Financial services focus',
            'Direct customer pipeline',
            'Strategic banking relationships',
            'Banking technology expertise',
            'Fintech ecosystem access',
            'Payment industry connections'
        ]
    }
    
    df_tier1 = pd.DataFrame(tier1_data)
    st.dataframe(df_tier1, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Tier 2 Investors
    st.markdown("### Tier 2: High Priority (Contact Second)")
    
    tier2_data = {
        'Investor': [
            'Nyca Partners',
            'Valar Ventures',
            'Canapi Ventures',
            'Point72 Ventures',
            'F-Prime Capital',
            'Microsoft M12',
            'Salesforce Ventures',
            'Mastercard Start Path',
            'Visa Ventures',
            'Illuminate Financial'
        ],
        'Focus': [
            'Fintech and financial services',
            'Fintech focus',
            'Banking technology',
            'Fintech practice',
            'Financial services technology',
            'Financial services cloud',
            'Financial services focus',
            'Payment and banking',
            'Financial services technology',
            'RegTech and compliance'
        ],
        'Why Ideal': [
            'Fintech expertise',
            'Fintech portfolio',
            'Banking technology specialist',
            'Fintech practice',
            'Financial services focus',
            'Enterprise + fintech',
            'CRM + financial services',
            'Payment ecosystem',
            'Payment technology',
            'RegTech specialist'
        ]
    }
    
    df_tier2 = pd.DataFrame(tier2_data)
    st.dataframe(df_tier2, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Visual Priority Map
    st.markdown("### Investor Priority Visualization")
    
    fig = go.Figure()
    
    # Tier 1
    fig.add_trace(go.Scatter(
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        mode='markers+text',
        marker=dict(size=20, color='#22c55e', symbol='star'),
        text=['QED', 'Ribbit', 'a16z', 'Fintech Coll', 'Anthemis', 'JPM', 'GS', 'Citi', 'Stripe', 'PayPal'],
        textposition="top center",
        textfont=dict(size=8),
        name='Tier 1',
        hovertemplate='<b>%{text}</b><extra></extra>'
    ))
    
    # Tier 2
    fig.add_trace(go.Scatter(
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        mode='markers+text',
        marker=dict(size=15, color='#f59e0b', symbol='diamond'),
        text=['Nyca', 'Valar', 'Canapi', 'P72', 'F-Prime', 'M12', 'SF', 'MC', 'Visa', 'Illuminate'],
        textposition="top center",
        textfont=dict(size=8),
        name='Tier 2',
        hovertemplate='<b>%{text}</b><extra></extra>'
    ))
    
    fig.update_layout(
        title="Investor Priority Map",
        xaxis=dict(showgrid=False, showticklabels=False, range=[0, 11]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[0.5, 2.5]),
        height=300,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def show_investor_categories():
    st.markdown("## 📊 Investor Categories & Profiles")
    
    categories = st.tabs([
        "Fintech VCs",
        "Strategic Investors",
        "RegTech Investors",
        "AI/ML VCs",
        "Enterprise SaaS VCs"
    ])
    
    with categories[0]:
        st.markdown("### 🏦 Fintech-Focused VCs (Highest Priority)")
        
        st.markdown("""
        **Why They're Ideal:**
        - ✅ Deep sector expertise in fintech
        - ✅ Portfolio synergies with banking tech
        - ✅ Regulatory knowledge and connections
        - ✅ Understanding of financial services market
        - ✅ Connections to banks and financial institutions
        
        **Key Characteristics:**
        - Portfolio includes banking/financial services tech
        - Experience with RegTech, KYC/AML, or compliance solutions
        - Understanding of financial services regulatory landscape
        - Track record in B2B fintech SaaS
        """)
        
        fintech_vcs = {
            'Firm': [
                'Andreessen Horowitz (a16z)',
                'Ribbit Capital',
                'QED Investors',
                'Fintech Collective',
                'Anthemis Group',
                'Nyca Partners',
                'Valar Ventures',
                'Canapi Ventures',
                'Point72 Ventures',
                'F-Prime Capital'
            ],
            'Location': [
                'San Francisco, CA',
                'Palo Alto, CA',
                'Alexandria, VA',
                'New York, NY',
                'London, UK',
                'New York, NY',
                'New York, NY',
                'Raleigh, NC',
                'New York, NY',
                'Cambridge, MA'
            ],
            'Focus': [
                'Fintech practice',
                'Early-stage fintech',
                'Fintech specialist',
                'B2B fintech',
                'Financial services tech',
                'Fintech & financial services',
                'Fintech focus',
                'Banking technology',
                'Fintech practice',
                'Financial services tech'
            ]
        }
        
        df_fintech = pd.DataFrame(fintech_vcs)
        st.dataframe(df_fintech, use_container_width=True, hide_index=True)
    
    with categories[1]:
        st.markdown("### 🏢 Strategic Corporate Investors (High Priority)")
        
        st.markdown("""
        **Why They're Ideal:**
        - ✅ Direct customer access and pipeline
        - ✅ Industry credibility and validation
        - ✅ Potential partnerships and integrations
        - ✅ Regulatory guidance
        - ✅ Potential acquisition path
        
        **Categories:**
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Banks & Financial Institutions:**
            - JPMorgan Strategic Investments
            - Goldman Sachs Principal Strategic Investments
            - Citi Ventures
            - Wells Fargo Strategic Capital
            - Bank of America Ventures
            - HSBC Ventures
            - Barclays Ventures
            - Santander InnoVentures
            - BBVA Ventures
            """)
        
        with col2:
            st.markdown("""
            **Fintech Companies:**
            - Stripe (Stripe Capital)
            - Square (Square Capital)
            - PayPal Ventures
            - Mastercard Start Path
            - Visa Ventures
            - FIS Ventures
            - Fiserv Ventures
            
            **Technology Companies:**
            - Microsoft M12
            - Google Ventures
            - Salesforce Ventures
            - IBM Ventures
            """)
    
    with categories[2]:
        st.markdown("### 🛡️ RegTech & Compliance-Focused Investors")
        
        st.markdown("""
        **Why They're Ideal:**
        - ✅ Specialized understanding of compliance market
        - ✅ Deep regulatory expertise
        - ✅ Connections to compliance officers
        - ✅ Understanding of KYC/AML pain points
        - ✅ RegTech portfolio companies
        
        **Target Firms:**
        - Fintech Ventures (RegTech focus)
        - Illuminate Financial (Financial services technology)
        - Fintech Innovation Lab (Banking technology accelerator)
        - Plug and Play Fintech (Fintech accelerator)
        - Techstars Fintech (Fintech accelerator program)
        """)
    
    with categories[3]:
        st.markdown("### 🤖 AI/ML-Focused VCs (Medium-High Priority)")
        
        st.markdown("""
        **Why They're Valuable:**
        - ✅ Technology validation and credibility
        - ✅ AI expertise and talent network
        - ✅ ML engineering expertise
        - ✅ Competitive advantage validation
        
        **Target Firms:**
        - AI Fund (AI-focused investments)
        - Data Collective / DCVC (AI and data science)
        - Two Sigma Ventures (AI/ML expertise)
        - Intel Capital (AI and financial services)
        - NEA (AI and enterprise software)
        - GV / Google Ventures (AI portfolio)
        """)
    
    with categories[4]:
        st.markdown("### 💼 Enterprise SaaS VCs (Medium Priority)")
        
        st.markdown("""
        **Why They're Relevant:**
        - ✅ SaaS business model expertise
        - ✅ Enterprise sales knowledge
        - ✅ Scaling B2B companies experience
        - ✅ Recurring revenue optimization
        
        **Target Firms:**
        - Bessemer Venture Partners (Enterprise SaaS)
        - Insight Partners (B2B software)
        - Accel (Enterprise software)
        - Sequoia Capital (Enterprise technology)
        - Lightspeed Venture Partners (Enterprise SaaS)
        """)


def show_geographic_strategy():
    st.markdown("## 🌍 Geographic Targeting Strategy")
    
    # Geographic Markets
    geo_data = {
        'Market': [
            'United States',
            'United Kingdom',
            'European Union',
            'Singapore',
            'Canada'
        ],
        'Tier': [
            'Tier 1',
            'Tier 1',
            'Tier 1',
            'Tier 2',
            'Tier 2'
        ],
        'Key Cities': [
            'New York, San Francisco, Boston, Chicago',
            'London',
            'Berlin, Amsterdam, Paris',
            'Singapore',
            'Toronto'
        ],
        'Why Important': [
            'Financial services hub, many fintech VCs',
            'Leading fintech hub globally, FCA regulatory environment',
            'Growing fintech scene, banking technology focus',
            'Regional fintech hub, gateway to APAC',
            'Financial services hub, growing fintech ecosystem'
        ],
        'Key Investors': [
            'QED, Ribbit, a16z, Fintech Collective',
            'Anthemis, Illuminate Financial',
            'Various EU fintech VCs',
            'Regional fintech funds',
            'Canadian fintech VCs'
        ]
    }
    
    df_geo = pd.DataFrame(geo_data)
    st.dataframe(df_geo, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Geographic Distribution Chart
    st.markdown("### Investor Geographic Distribution")
    
    fig = px.bar(
        x=['United States', 'United Kingdom', 'European Union', 'Singapore', 'Canada'],
        y=[10, 3, 4, 2, 1],
        labels={'x': 'Region', 'y': 'Number of Priority Investors'},
        title="Priority Investors by Geography",
        color=['United States', 'United Kingdom', 'European Union', 'Singapore', 'Canada'],
        color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    )
    
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


def show_investor_matching():
    st.markdown("## 💼 Investor Profile Matching")
    
    st.markdown("### Ideal Investor Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **✅ Must-Have Criteria:**
        
        1. **Fintech or Financial Services Portfolio**
           - Portfolio companies in banking/fintech
           - Understanding of financial services market
           
        2. **Series A Stage Experience**
           - Investments in $3M-$10M range
           - Experience with Series A rounds
           
        3. **B2B SaaS Business Model Understanding**
           - SaaS portfolio companies
           - Recurring revenue model expertise
           
        4. **Regulatory/Compliance Market Knowledge**
           - RegTech investments
           - KYC/AML understanding
           - Compliance expertise
           
        5. **Connections to Banks or Financial Institutions**
           - Banking relationships
           - Financial services network
        """)
    
    with col2:
        st.markdown("""
        **⭐ Nice-to-Have Criteria:**
        
        1. **AI/ML Portfolio Companies**
           - AI/ML investments
           - Technology expertise
           
        2. **International Expansion Experience**
           - Global portfolio
           - International market knowledge
           
        3. **Strategic Partnerships with Banks**
           - Banking partnerships
           - Strategic relationships
           
        4. **RegTech or KYC/AML Investments**
           - Compliance tech portfolio
           - Regulatory technology focus
           
        5. **Follow-on Funding Capability**
           - Multi-stage fund
           - Follow-on investment ability
        """)
    
    st.markdown("---")
    
    # Matching Score Calculator
    st.markdown("### Investor Matching Score")
    st.markdown("Evaluate potential investors based on fit criteria")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fintech_portfolio = st.selectbox(
            "Fintech Portfolio",
            ["Yes - Strong", "Yes - Moderate", "No"],
            index=0
        )
        
        series_a_experience = st.selectbox(
            "Series A Experience",
            ["Yes - Strong", "Yes - Moderate", "No"],
            index=0
        )
    
    with col2:
        b2b_saas = st.selectbox(
            "B2B SaaS Understanding",
            ["Yes - Strong", "Yes - Moderate", "No"],
            index=0
        )
        
        regulatory_knowledge = st.selectbox(
            "Regulatory Knowledge",
            ["Yes - Strong", "Yes - Moderate", "No"],
            index=0
        )
    
    with col3:
        banking_connections = st.selectbox(
            "Banking Connections",
            ["Yes - Strong", "Yes - Moderate", "No"],
            index=0
        )
        
        ai_ml_portfolio = st.selectbox(
            "AI/ML Portfolio",
            ["Yes", "No"],
            index=0
        )
    
    # Calculate score
    score = 0
    max_score = 0
    
    criteria = [
        (fintech_portfolio, 20),
        (series_a_experience, 20),
        (b2b_saas, 15),
        (regulatory_knowledge, 15),
        (banking_connections, 15),
        (ai_ml_portfolio, 15)
    ]
    
    for criterion, weight in criteria:
        max_score += weight
        if "Strong" in str(criterion):
            score += weight
        elif "Moderate" in str(criterion):
            score += weight * 0.5
        elif criterion == "Yes":
            score += weight * 0.7
    
    match_percentage = (score / max_score) * 100
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.metric("Investor Match Score", f"{match_percentage:.0f}%", f"{score:.0f}/{max_score}")
        
        if match_percentage >= 80:
            st.success("✅ Excellent Match - High Priority")
        elif match_percentage >= 60:
            st.info("✅ Good Match - Medium Priority")
        else:
            st.warning("⚠️ Moderate Match - Lower Priority")


def show_outreach_plan():
    st.markdown("## 📈 Outreach Strategy & Timeline")
    
    # Phases
    phases = st.tabs(["Phase 1", "Phase 2", "Phase 3", "Success Metrics"])
    
    with phases[0]:
        st.markdown("### Phase 1: Warm Introductions (Weeks 1-4)")
        
        st.markdown("""
        **Priority:** Fintech-focused VCs and strategic investors
        
        **Target:** 15-20 initial meetings
        
        **Approach:**
        1. Leverage existing network connections
        2. Use portfolio company introductions
        3. Engage with advisors and board members
        4. Attend fintech conferences and events
        
        **Focus Areas:**
        - Fintech-focused VCs (QED, Ribbit, a16z)
        - Strategic investors (JPMorgan, Goldman Sachs)
        - RegTech investors (Illuminate Financial)
        """)
        
        # Timeline visualization
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            y=[3, 8, 13, 18],
            mode='lines+markers',
            name='Cumulative Meetings',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="Phase 1: Meeting Targets",
            xaxis_title="Week",
            yaxis_title="Cumulative Meetings",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with phases[1]:
        st.markdown("### Phase 2: Direct Outreach (Weeks 5-8)")
        
        st.markdown("""
        **Priority:** RegTech investors and AI-focused VCs
        
        **Target:** 20-30 additional meetings
        
        **Approach:**
        1. Personalized email outreach
        2. LinkedIn connections
        3. Industry event meetings
        4. Accelerator/incubator programs
        
        **Focus Areas:**
        - RegTech specialists
        - AI/ML-focused VCs
        - Enterprise SaaS VCs
        - Geographic expansion (EU, UK)
        """)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=['Week 5', 'Week 6', 'Week 7', 'Week 8'],
            y=[20, 25, 28, 30],
            mode='lines+markers',
            name='Cumulative Meetings',
            line=dict(color='#ff7f0e', width=3),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="Phase 2: Meeting Targets",
            xaxis_title="Week",
            yaxis_title="Cumulative Meetings",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with phases[2]:
        st.markdown("### Phase 3: Strategic Partners (Weeks 9-12)")
        
        st.markdown("""
        **Priority:** Corporate strategic investors
        
        **Target:** 10-15 strategic discussions
        
        **Approach:**
        1. Partnership discussions
        2. Pilot program proposals
        3. Strategic investment conversations
        4. Joint go-to-market opportunities
        
        **Focus Areas:**
        - Banking strategic investors
        - Fintech company ventures
        - Technology company ventures
        - Partnership opportunities
        """)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=['Week 9', 'Week 10', 'Week 11', 'Week 12'],
            y=[32, 36, 40, 45],
            mode='lines+markers',
            name='Cumulative Meetings',
            line=dict(color='#2ca02c', width=3),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="Phase 3: Meeting Targets",
            xaxis_title="Week",
            yaxis_title="Cumulative Meetings",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with phases[3]:
        st.markdown("### Success Metrics & KPIs")
        
        metrics_data = {
            'Metric': [
                'Target Investor Meetings',
                'Term Sheets Received',
                'Meeting to Term Sheet Conversion',
                'Timeline to Close',
                'Valuation Target',
                'Follow-on Interest'
            ],
            'Target': [
                '40-50 meetings',
                '3-5 term sheets',
                '10-15%',
                '3-4 months',
                '$20M-$25M pre-money',
                'Multiple options'
            ],
            'Status': [
                'Track weekly',
                'Track monthly',
                'Monitor conversion',
                'Target Q1 2025',
                'Negotiate based on interest',
                'Maintain relationships'
            ]
        }
        
        df_metrics = pd.DataFrame(metrics_data)
        st.dataframe(df_metrics, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Overall timeline
        st.markdown("### Overall Timeline")
        
        timeline_data = {
            'Month': ['Month 1', 'Month 2', 'Month 3', 'Month 4'],
            'Key Activities': [
                'Initial outreach, warm introductions, 15-20 meetings',
                'Direct outreach, 20-30 meetings, initial term sheets',
                'Strategic discussions, term sheet negotiations, due diligence',
                'Final negotiations, closing, funding received'
            ],
            'Milestones': [
                'First term sheet',
                '3-5 term sheets',
                'Selected investor, LOI signed',
                'Series A closed'
            ]
        }
        
        df_timeline = pd.DataFrame(timeline_data)
        st.dataframe(df_timeline, use_container_width=True, hide_index=True)


def show_resources():
    st.markdown("## 📋 Investor Resources & Tools")
    
    resource_tabs = st.tabs(["Databases", "Events", "Accelerators", "Templates"])
    
    with resource_tabs[0]:
        st.markdown("### Investor Databases")
        
        databases = {
            'Platform': [
                'Crunchbase',
                'PitchBook',
                'CB Insights',
                'Fintech News',
                'AngelList'
            ],
            'Focus': [
                'Filter: Fintech, Series A',
                'Fintech sector, Series A stage',
                'Fintech market map',
                'Investor lists and news',
                'Angel investors and VCs'
            ],
            'Key Features': [
                'Company and investor profiles',
                'Deal flow and valuations',
                'Market intelligence',
                'Industry news and trends',
                'Startup and investor matching'
            ]
        }
        
        df_databases = pd.DataFrame(databases)
        st.dataframe(df_databases, use_container_width=True, hide_index=True)
    
    with resource_tabs[1]:
        st.markdown("### Industry Events")
        
        events = {
            'Event': [
                'Money20/20',
                'Fintech Week',
                'SIBOS',
                'Fintech Innovation Lab',
                'Web Summit',
                'Finovate'
            ],
            'Location': [
                'Las Vegas, Amsterdam',
                'London, New York',
                'Various',
                'New York, London',
                'Lisbon',
                'New York, London'
            ],
            'Focus': [
                'Fintech and payments',
                'Fintech ecosystem',
                'Banking technology',
                'Banking technology accelerator',
                'Technology and startups',
                'Financial technology'
            ],
            'Best For': [
                'Networking, investor meetings',
                'Industry connections',
                'Banking relationships',
                'Accelerator program',
                'General networking',
                'Product demos'
            ]
        }
        
        df_events = pd.DataFrame(events)
        st.dataframe(df_events, use_container_width=True, hide_index=True)
    
    with resource_tabs[2]:
        st.markdown("### Accelerators & Programs")
        
        accelerators = {
            'Program': [
                'Techstars Fintech',
                'Plug and Play Fintech',
                'Fintech Innovation Lab',
                'Y Combinator',
                '500 Startups'
            ],
            'Location': [
                'Various',
                'Silicon Valley',
                'New York, London',
                'San Francisco',
                'San Francisco'
            ],
            'Focus': [
                'Fintech startups',
                'Fintech accelerator',
                'Banking technology',
                'General (fintech companies)',
                'General (fintech track)'
            ],
            'Benefits': [
                'Mentorship, funding, network',
                'Corporate partnerships',
                'Banking connections',
                'Strong brand, network',
                'Global network'
            ]
        }
        
        df_accelerators = pd.DataFrame(accelerators)
        st.dataframe(df_accelerators, use_container_width=True, hide_index=True)
    
    with resource_tabs[3]:
        st.markdown("### Email Templates & Talking Points")
        
        st.markdown("#### Email Subject Lines:")
        st.code("""
- "Series A Opportunity: AI-Powered Customer Onboarding Platform"
- "Fintech Investment: $5M Series A in RegTech/KYC Automation"
- "Partnership Opportunity: Banking Technology Platform"
- "Introducing: AI-Augmented Customer Onboarding for Financial Services"
        """)
        
        st.markdown("#### Key Talking Points:")
        st.markdown("""
        1. **Market Opportunity:** $450B TAM, 12.5% CAGR
        2. **Traction:** $2.5M ARR, 45+ financial institutions
        3. **Technology:** AI-powered, 99.8% accuracy, <30 min processing
        4. **Team:** Experienced fintech and AI team
        5. **Competitive Advantage:** 10x faster, 60% cost reduction
        """)
        
        st.markdown("#### Pitch Deck Sections:")
        st.markdown("""
        - Problem & Solution (5 slides)
        - Market Opportunity (3 slides)
        - Product & Technology (5 slides)
        - Business Model (3 slides)
        - Traction & Metrics (3 slides)
        - Team (2 slides)
        - Financial Projections (3 slides)
        - Ask & Use of Funds (2 slides)
        """)

