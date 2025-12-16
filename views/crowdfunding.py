"""
Crowdfunding Guide Page
Best platforms and step-by-step process for crowdfunding
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def show():
    st.markdown('<h1 class="main-header">💰 Crowdfunding Strategy & Guide</h1>', unsafe_allow_html=True)
    st.markdown("Comprehensive guide to crowdfunding platforms and step-by-step process for fintech startups")
    
    st.markdown("---")
    
    # Navigation tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🏆 Best Platforms",
        "📋 Step-by-Step Process",
        "📊 Platform Comparison",
        "✅ Preparation Checklist",
        "💡 Best Practices",
        "📈 Success Metrics"
    ])
    
    with tab1:
        show_best_platforms()
    
    with tab2:
        show_step_by_step_process()
    
    with tab3:
        show_platform_comparison()
    
    with tab4:
        show_preparation_checklist()
    
    with tab5:
        show_best_practices()
    
    with tab6:
        show_success_metrics()


def show_best_platforms():
    st.markdown("## 🏆 Best Crowdfunding Platforms for Fintech Startups")
    
    st.markdown("### Top Recommendations for Your Startup")
    
    # Platform recommendations
    platforms = st.tabs([
        "Equity Crowdfunding",
        "Rewards-Based",
        "Debt Crowdfunding",
        "Reg CF Platforms"
    ])
    
    with platforms[0]:
        st.markdown("### 🏢 Equity Crowdfunding Platforms")
        st.markdown("**Best for:** Raising capital in exchange for equity")
        
        equity_platforms = {
            'Platform': [
                'Republic',
                'SeedInvest',
                'StartEngine',
                'Wefunder',
                'Netcapital',
                'EquityZen'
            ],
            'Best For': [
                'Fintech, diverse investor base',
                'High-quality startups, accredited investors',
                'Large campaigns, marketing support',
                'Community-focused, lower minimums',
                'Early-stage, flexible terms',
                'Secondary market, liquidity'
            ],
            'Min Raise': [
                '$25K',
                '$100K',
                '$10K',
                '$50K',
                '$10K',
                'N/A'
            ],
            'Max Raise (Reg CF)': [
                '$5M',
                '$5M',
                '$5M',
                '$5M',
                '$5M',
                'N/A'
            ],
            'Fees': [
                '2-6% + 2% payment processing',
                '7.5% success fee',
                '3.5-7% + payment processing',
                '7.5% + 2.9% payment',
                '6-8% success fee',
                'Transaction-based'
            ],
            'Investor Base': [
                '200K+ investors',
                'Accredited + non-accredited',
                '500K+ investors',
                'Community-driven',
                'Growing base',
                'Accredited investors'
            ]
        }
        
        df_equity = pd.DataFrame(equity_platforms)
        st.dataframe(df_equity, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.markdown("#### 🥇 Top Recommendation: **Republic**")
        st.markdown("""
        **Why Republic is ideal for your fintech startup:**
        
        - ✅ **Fintech Focus:** Strong track record with fintech companies
        - ✅ **Large Investor Base:** 200,000+ active investors
        - ✅ **Regulatory Compliance:** Full Reg CF compliance
        - ✅ **Marketing Support:** Built-in marketing tools and support
        - ✅ **Flexible Terms:** Can combine Reg CF with Reg A+
        - ✅ **Success Rate:** Higher success rate for fintech campaigns
        - ✅ **Community:** Active fintech investor community
        
        **Notable Fintech Successes:**
        - Robinhood (early stage)
        - Carta
        - Various RegTech companies
        """)
        
        st.info("💡 **Tip:** Republic has a dedicated fintech vertical and understands regulatory requirements for financial services companies.")
    
    with platforms[1]:
        st.markdown("### 🎁 Rewards-Based Crowdfunding")
        st.markdown("**Best for:** Pre-sales, product validation, community building")
        
        rewards_platforms = {
            'Platform': [
                'Kickstarter',
                'Indiegogo',
                'GoFundMe',
                'Patreon'
            ],
            'Best For': [
                'Product launches, all-or-nothing',
                'Flexible funding, international',
                'Personal/business fundraising',
                'Recurring revenue, subscriptions'
            ],
            'Fee Structure': [
                '5% + 3-5% payment processing',
                '5% + 2.9% payment processing',
                '2.9% + $0.30 per transaction',
                '5-12% based on plan'
            ],
            'Payment Model': [
                'All-or-nothing',
                'Flexible or fixed',
                'Keep what you raise',
                'Recurring monthly'
            ],
            'Best Use Case': [
                'Product pre-sales',
                'International campaigns',
                'Fundraising, donations',
                'Ongoing support'
            ]
        }
        
        df_rewards = pd.DataFrame(rewards_platforms)
        st.dataframe(df_rewards, use_container_width=True, hide_index=True)
        
        st.warning("⚠️ **Note:** Rewards-based crowdfunding may not be ideal for fintech due to regulatory restrictions. Consider equity or debt crowdfunding instead.")
    
    with platforms[2]:
        st.markdown("### 💳 Debt Crowdfunding (P2P Lending)")
        st.markdown("**Best for:** Raising debt capital from individual lenders")
        
        debt_platforms = {
            'Platform': [
                'Kiva',
                'Funding Circle',
                'LendingClub',
                'Prosper'
            ],
            'Focus': [
                'Small business loans',
                'Business loans',
                'Personal/business loans',
                'Personal loans'
            ],
            'Loan Amount': [
                '$1K-$10K',
                '$25K-$500K',
                '$1K-$40K',
                '$2K-$50K'
            ],
            'Interest Rates': [
                '0% (non-profit)',
                '4.99%-27.79%',
                '6.95%-35.89%',
                '6.95%-35.99%'
            ],
            'Best For': [
                'Small businesses, social impact',
                'Established businesses',
                'Personal/business use',
                'Personal loans'
            ]
        }
        
        df_debt = pd.DataFrame(debt_platforms)
        st.dataframe(df_debt, use_container_width=True, hide_index=True)
        
        st.info("💡 **Note:** Debt crowdfunding may have regulatory restrictions for fintech companies. Consult legal counsel.")
    
    with platforms[3]:
        st.markdown("### 📜 Regulation Crowdfunding (Reg CF) Platforms")
        st.markdown("**Best for:** Raising up to $5M from non-accredited investors")
        
        st.markdown("""
        **Reg CF Overview:**
        - Maximum raise: **$5 million** per 12-month period
        - Investor limits: Based on income/net worth
        - Required disclosures: Financial statements, business plan
        - Ongoing reporting: Annual reports required
        
        **Top Reg CF Platforms:**
        1. **Republic** - Best overall, fintech-friendly
        2. **SeedInvest** - High-quality startups
        3. **StartEngine** - Large campaigns, marketing
        4. **Wefunder** - Community-focused
        5. **Netcapital** - Early-stage friendly
        
        **Reg CF Advantages:**
        - ✅ Access to non-accredited investors
        - ✅ Marketing and advertising allowed
        - ✅ Online platform facilitation
        - ✅ Lower regulatory burden than IPO
        
        **Reg CF Requirements:**
        - ⚠️ Financial statement review/audit (based on raise amount)
        - ⚠️ Ongoing annual reporting
        - ⚠️ Investor communication requirements
        - ⚠️ Platform fees (typically 5-8%)
        """)


def show_step_by_step_process():
    st.markdown("## 📋 Step-by-Step Crowdfunding Process")
    
    # Process phases
    phases = st.tabs([
        "Pre-Launch (Weeks 1-4)",
        "Launch (Week 5)",
        "Campaign (Weeks 6-12)",
        "Post-Campaign"
    ])
    
    with phases[0]:
        st.markdown("### Phase 1: Pre-Launch Preparation (Weeks 1-4)")
        
        st.markdown("#### Week 1: Platform Selection & Legal Setup")
        
        week1_tasks = {
            'Task': [
                'Research and select platform',
                'Legal entity verification',
                'Regulatory compliance review',
                'Terms sheet preparation',
                'Platform application submission'
            ],
            'Details': [
                'Compare platforms, review terms, check fintech compatibility',
                'Ensure entity is properly registered and in good standing',
                'Review Reg CF requirements, securities law compliance',
                'Define equity terms, valuation, minimum investment',
                'Submit application to chosen platform(s)'
            ],
            'Owner': [
                'Founder/CEO',
                'Legal counsel',
                'Legal + Compliance',
                'Founder + Legal',
                'Founder'
            ],
            'Status': [
                'Required',
                'Required',
                'Required',
                'Required',
                'Required'
            ]
        }
        
        df_week1 = pd.DataFrame(week1_tasks)
        st.dataframe(df_week1, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.markdown("#### Week 2: Financial Preparation")
        
        st.markdown("""
        **Financial Documents Required:**
        
        1. **Financial Statements**
           - Balance sheet (last 2 years)
           - Income statement (last 2 years)
           - Cash flow statement
           - Financial projections (3-5 years)
        
        2. **Review Requirements (Based on Raise Amount):**
           - **$0-$124,999:** Financial statements reviewed by CPA
           - **$125,000-$499,999:** Financial statements reviewed by CPA
           - **$500,000-$5,000,000:** Financial statements audited by CPA
        
        3. **Tax Returns**
           - Last 2 years of business tax returns
        
        4. **Bank Statements**
           - Recent bank statements (3-6 months)
        """)
        
        st.markdown("---")
        
        st.markdown("#### Week 3: Campaign Materials Creation")
        
        campaign_materials = {
            'Material': [
                'Pitch video (2-3 minutes)',
                'Campaign page content',
                'Financial projections',
                'Team bios and photos',
                'Product demos/screenshots',
                'Market research data',
                'Customer testimonials',
                'Press kit and media assets'
            ],
            'Key Elements': [
                'Problem, solution, traction, ask',
                'Compelling narrative, visuals, data',
                'Revenue, expenses, growth assumptions',
                'Founder backgrounds, expertise',
                'Working product or prototype',
                'Market size, trends, opportunity',
                'Early customer feedback',
                'Logos, images, press releases'
            ],
            'Priority': [
                'Critical',
                'Critical',
                'Critical',
                'High',
                'High',
                'High',
                'Medium',
                'Medium'
            ]
        }
        
        df_materials = pd.DataFrame(campaign_materials)
        st.dataframe(df_materials, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.markdown("#### Week 4: Pre-Launch Marketing")
        
        st.markdown("""
        **Pre-Launch Activities:**
        
        1. **Email List Building**
           - Collect emails from website
           - Social media lead generation
           - Target: 1,000-5,000 pre-launch emails
        
        2. **Social Media Preparation**
           - Create campaign hashtags
           - Schedule posts
           - Build anticipation
        
        3. **Press Outreach**
           - Draft press release
           - Identify relevant journalists
           - Schedule embargoed briefings
        
        4. **Community Building**
           - Engage with potential investors
           - Share behind-the-scenes content
           - Build excitement
        """)
    
    with phases[1]:
        st.markdown("### Phase 2: Launch (Week 5)")
        
        launch_checklist = {
            'Time': [
                'T-1 Week',
                'T-3 Days',
                'T-1 Day',
                'Launch Day',
                'Day 1-3'
            ],
            'Action': [
                'Final review of all materials',
                'Send pre-launch email to list',
                'Social media teasers',
                'Go live on platform',
                'Intensive promotion push'
            ],
            'Key Activities': [
                'Legal review, compliance check, platform approval',
                'Announce launch date, build anticipation',
                'Countdown posts, final reminders',
                'Publish campaign, notify all contacts',
                'Email blasts, social media, press outreach'
            ],
            'Metrics to Track': [
                'Platform approval status',
                'Email open rates, click-through',
                'Social engagement',
                'Initial investment amount',
                'Daily investment rate'
            ]
        }
        
        df_launch = pd.DataFrame(launch_checklist)
        st.dataframe(df_launch, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.markdown("#### Launch Day Best Practices")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Morning (9 AM - 12 PM):**
            - ✅ Publish campaign live
            - ✅ Send launch email to full list
            - ✅ Post on all social channels
            - ✅ Notify personal network
            - ✅ Press release distribution
            
            **Afternoon (12 PM - 5 PM):**
            - ✅ Respond to investor questions
            - ✅ Share updates and milestones
            - ✅ Engage with comments
            - ✅ Media interviews (if scheduled)
            - ✅ Monitor investment flow
            """)
        
        with col2:
            st.markdown("""
            **Evening (5 PM - 9 PM):**
            - ✅ Thank early investors
            - ✅ Share day 1 results
            - ✅ Plan next day activities
            - ✅ Review metrics and feedback
            - ✅ Adjust strategy if needed
            
            **Key Metrics Day 1:**
            - Target: 10-20% of goal
            - First 48 hours critical
            - Momentum building essential
            - Social proof important
            """)
    
    with phases[2]:
        st.markdown("### Phase 3: Active Campaign (Weeks 6-12)")
        
        st.markdown("#### Weekly Campaign Activities")
        
        campaign_weeks = {
            'Week': [
                'Week 1',
                'Week 2',
                'Week 3-4',
                'Week 5-6',
                'Week 7-8',
                'Week 9-12'
            ],
            'Focus': [
                'Initial momentum',
                'Maintain engagement',
                'Mid-campaign push',
                'Re-engagement',
                'Final push preparation',
                'Closing sprint'
            ],
            'Key Activities': [
                'Daily updates, investor Q&A, social media',
                'New content, milestones, press coverage',
                'Webinars, demos, case studies',
                'Re-targeting, email campaigns',
                'Urgency messaging, final offers',
                'Last chance messaging, closing push'
            ],
            'Target %': [
                '20-30%',
                '40-50%',
                '60-70%',
                '75-85%',
                '90-95%',
                '100%+'
            ]
        }
        
        df_campaign = pd.DataFrame(campaign_weeks)
        st.dataframe(df_campaign, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Campaign timeline visualization
        st.markdown("#### Campaign Progress Timeline")
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=['Week 1', 'Week 2', 'Week 4', 'Week 6', 'Week 8', 'Week 12'],
            y=[25, 45, 65, 80, 92, 100],
            mode='lines+markers',
            name='Target Progress',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=10)
        ))
        
        fig.add_trace(go.Scatter(
            x=['Week 1', 'Week 2', 'Week 4', 'Week 6', 'Week 8', 'Week 12'],
            y=[30, 50, 70, 85, 95, 105],
            mode='lines+markers',
            name='Stretch Goal',
            line=dict(color='#22c55e', width=2, dash='dash'),
            marker=dict(size=8)
        ))
        
        fig.add_hline(y=100, line_dash="dot", line_color="red", annotation_text="100% Goal")
        
        fig.update_layout(
            title="Campaign Progress Timeline",
            xaxis_title="Campaign Week",
            yaxis_title="Percentage of Goal (%)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        st.markdown("#### Daily Campaign Activities")
        
        daily_activities = {
            'Activity': [
                'Respond to investor questions',
                'Post campaign updates',
                'Share on social media',
                'Email follow-ups',
                'Press/media outreach',
                'Engage with comments',
                'Track metrics and analytics',
                'Thank new investors'
            ],
            'Frequency': [
                'Real-time',
                'Daily',
                '2-3x daily',
                'Weekly batches',
                'Ongoing',
                'Real-time',
                'Daily',
                'Daily'
            ],
            'Time Required': [
                '1-2 hours',
                '30 minutes',
                '30 minutes',
                '1 hour',
                '1-2 hours',
                '30 minutes',
                '30 minutes',
                '30 minutes'
            ]
        }
        
        df_daily = pd.DataFrame(daily_activities)
        st.dataframe(df_daily, use_container_width=True, hide_index=True)
    
    with phases[3]:
        st.markdown("### Phase 4: Post-Campaign")
        
        st.markdown("#### Immediate Actions (Week 1 Post-Campaign)")
        
        post_campaign = {
            'Action': [
                'Thank all investors',
                'Distribute funds',
                'Issue securities',
                'Update investors',
                'Compliance reporting',
                'Plan next steps'
            ],
            'Timeline': [
                'Within 24 hours',
                'Within 1-2 weeks',
                'Within 30 days',
                'Weekly updates',
                'As required',
                'Ongoing'
            ],
            'Details': [
                'Personalized thank you messages',
                'Platform processes and distributes',
                'Legal documentation and certificates',
                'Progress updates, milestones',
                'Reg CF annual reporting',
                'Use of funds, growth plans'
            ]
        }
        
        df_post = pd.DataFrame(post_campaign)
        st.dataframe(df_post, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.markdown("#### Ongoing Investor Relations")
        
        st.markdown("""
        **Quarterly Updates:**
        - Financial performance
        - Key milestones achieved
        - Product development progress
        - Market traction
        - Challenges and solutions
        
        **Annual Requirements:**
        - Annual report (Reg CF requirement)
        - Financial statements
        - Business update
        - Use of funds report
        
        **Communication Channels:**
        - Email newsletters
        - Investor portal (if available)
        - Annual investor meeting
        - Regular updates via platform
        """)


def show_platform_comparison():
    st.markdown("## 📊 Platform Comparison & Selection Guide")
    
    # Detailed comparison
    comparison_data = {
        'Platform': [
            'Republic',
            'SeedInvest',
            'StartEngine',
            'Wefunder',
            'Netcapital'
        ],
        'Best For': [
            'Fintech, diverse campaigns',
            'High-quality startups',
            'Large campaigns',
            'Community-focused',
            'Early-stage companies'
        ],
        'Min Raise': [
            '$25K',
            '$100K',
            '$10K',
            '$50K',
            '$10K'
        ],
        'Max Raise (Reg CF)': [
            '$5M',
            '$5M',
            '$5M',
            '$5M',
            '$5M'
        ],
        'Success Fee': [
            '2-6%',
            '7.5%',
            '3.5-7%',
            '7.5%',
            '6-8%'
        ],
        'Payment Processing': [
            '2%',
            'Included',
            '2.9%',
            '2.9%',
            'Included'
        ],
        'Investor Base': [
            '200K+',
            'Accredited + Non-accredited',
            '500K+',
            'Community-driven',
            'Growing'
        ],
        'Marketing Support': [
            'High',
            'Medium',
            'High',
            'Medium',
            'Medium'
        ],
        'Fintech Experience': [
            'Excellent',
            'Good',
            'Good',
            'Good',
            'Fair'
        ]
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Visual comparison
    st.markdown("### Visual Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Success Fee Comparison
        fig_fees = go.Figure()
        
        fig_fees.add_trace(go.Bar(
            x=['Republic', 'SeedInvest', 'StartEngine', 'Wefunder', 'Netcapital'],
            y=[4, 7.5, 5.25, 7.5, 7],
            marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        ))
        
        fig_fees.update_layout(
            title="Success Fee Comparison (%)",
            xaxis_title="Platform",
            yaxis_title="Fee (%)",
            height=300
        )
        
        st.plotly_chart(fig_fees, use_container_width=True)
    
    with col2:
        # Investor Base Size
        fig_investors = go.Figure()
        
        fig_investors.add_trace(go.Bar(
            x=['Republic', 'SeedInvest', 'StartEngine', 'Wefunder', 'Netcapital'],
            y=[200, 50, 500, 100, 25],  # Estimated in thousands
            marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        ))
        
        fig_investors.update_layout(
            title="Investor Base Size (Thousands)",
            xaxis_title="Platform",
            yaxis_title="Investors (K)",
            height=300
        )
        
        st.plotly_chart(fig_investors, use_container_width=True)
    
    st.markdown("---")
    
    # Selection criteria
    st.markdown("### Platform Selection Criteria for Your Startup")
    
    criteria_scores = {
        'Criterion': [
            'Fintech Experience',
            'Investor Base Size',
            'Marketing Support',
            'Fee Structure',
            'Regulatory Compliance',
            'Platform Reputation',
            'Success Rate',
            'Ease of Use'
        ],
        'Republic': [
            10,
            9,
            9,
            8,
            10,
            9,
            8,
            9
        ],
        'SeedInvest': [
            8,
            7,
            7,
            6,
            10,
            9,
            9,
            8
        ],
        'StartEngine': [
            8,
            10,
            9,
            7,
            10,
            8,
            7,
            8
        ],
        'Wefunder': [
            7,
            8,
            7,
            6,
            10,
            8,
            8,
            9
        ],
        'Netcapital': [
            6,
            6,
            6,
            7,
            10,
            7,
            7,
            8
        ]
    }
    
    df_scores = pd.DataFrame(criteria_scores)
    st.dataframe(df_scores, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Recommendation
    st.markdown("### 🎯 Recommendation for Your Startup")
    
    st.success("""
    **Primary Recommendation: Republic**
    
    **Why Republic is the best fit:**
    
    1. ✅ **Fintech Expertise:** Strong track record with fintech and RegTech companies
    2. ✅ **Large Investor Base:** 200,000+ active investors, many interested in fintech
    3. ✅ **Marketing Support:** Comprehensive marketing tools and support
    4. ✅ **Regulatory Understanding:** Deep understanding of financial services regulations
    5. ✅ **Flexible Terms:** Can combine Reg CF with Reg A+ for larger raises
    6. ✅ **Success Rate:** Higher success rate for fintech campaigns
    7. ✅ **Community:** Active fintech investor community
    
    **Secondary Option: SeedInvest**
    
    - Better for high-quality, established startups
    - Strong focus on accredited investors
    - Higher success fee but more selective
    """)


def show_preparation_checklist():
    st.markdown("## ✅ Pre-Launch Preparation Checklist")
    
    checklist_tabs = st.tabs([
        "Legal & Compliance",
        "Financial Documents",
        "Campaign Materials",
        "Marketing Assets",
        "Platform Setup"
    ])
    
    with checklist_tabs[0]:
        st.markdown("### Legal & Compliance Requirements")
        
        legal_checklist = {
            'Item': [
                'Entity registration and good standing',
                'Reg CF compliance review',
                'Securities law compliance',
                'Terms sheet preparation',
                'Investor agreement templates',
                'Disclosure document review',
                'State blue sky law compliance',
                'FINRA registration (if applicable)',
                'Privacy policy and terms of service',
                'Intellectual property protection'
            ],
            'Status': [
                'Required',
                'Required',
                'Required',
                'Required',
                'Required',
                'Required',
                'Required',
                'Conditional',
                'Required',
                'Recommended'
            ],
            'Timeline': [
                'Before application',
                'Before application',
                'Before application',
                'Week 1',
                'Week 2',
                'Week 2',
                'Week 2',
                'If needed',
                'Before launch',
                'Ongoing'
            ]
        }
        
        df_legal = pd.DataFrame(legal_checklist)
        st.dataframe(df_legal, use_container_width=True, hide_index=True)
        
        st.warning("⚠️ **Important:** Consult with securities attorney familiar with Reg CF requirements. Legal compliance is critical.")
    
    with checklist_tabs[1]:
        st.markdown("### Financial Documents Required")
        
        financial_docs = {
            'Document': [
                'Balance sheet (2 years)',
                'Income statement (2 years)',
                'Cash flow statement (2 years)',
                'Financial projections (3-5 years)',
                'Tax returns (2 years)',
                'Bank statements (3-6 months)',
                'CPA review/audit (based on raise)',
                'Use of funds breakdown',
                'Cap table',
                'Valuation methodology'
            ],
            'Required For': [
                'All campaigns',
                'All campaigns',
                'All campaigns',
                'All campaigns',
                'All campaigns',
                'Platform verification',
                'Raises >$124,999',
                'All campaigns',
                'Equity campaigns',
                'Equity campaigns'
            ],
            'Review Level': [
                'Review required',
                'Review required',
                'Review required',
                'Review required',
                'Verification',
                'Verification',
                'Audit if >$500K',
                'Disclosure',
                'Disclosure',
                'Disclosure'
            ]
        }
        
        df_financial = pd.DataFrame(financial_docs)
        st.dataframe(df_financial, use_container_width=True, hide_index=True)
        
        st.info("💡 **Tip:** Start preparing financial documents early. CPA review/audit can take 2-4 weeks.")
    
    with checklist_tabs[2]:
        st.markdown("### Campaign Materials Checklist")
        
        materials_checklist = {
            'Material': [
                'Pitch video (2-3 min)',
                'Campaign page content',
                'Executive summary',
                'Business plan summary',
                'Financial projections',
                'Team bios and photos',
                'Product demo/screenshots',
                'Market research',
                'Customer testimonials',
                'Press kit'
            ],
            'Priority': [
                'Critical',
                'Critical',
                'Critical',
                'High',
                'Critical',
                'High',
                'High',
                'High',
                'Medium',
                'Medium'
            ],
            'Status': [
                'Required',
                'Required',
                'Required',
                'Required',
                'Required',
                'Recommended',
                'Recommended',
                'Recommended',
                'Optional',
                'Optional'
            ]
        }
        
        df_materials = pd.DataFrame(materials_checklist)
        st.dataframe(df_materials, use_container_width=True, hide_index=True)
    
    with checklist_tabs[3]:
        st.markdown("### Marketing Assets Checklist")
        
        marketing_assets = {
            'Asset': [
                'Email list (1K-5K contacts)',
                'Social media accounts',
                'Press release draft',
                'Media kit',
                'Investor FAQ document',
                'Social media content calendar',
                'Email templates',
                'Website landing page',
                'Investor presentation deck',
                'Case studies/testimonials'
            ],
            'Target': [
                '1,000-5,000 emails',
                'All major platforms',
                'Ready for distribution',
                'Complete package',
                'Comprehensive Q&A',
                '30-60 days of content',
                'Launch, updates, reminders',
                'Campaign-focused',
                '10-15 slides',
                '3-5 examples'
            ],
            'Timeline': [
                'Week 3-4',
                'Before launch',
                'Week 4',
                'Week 4',
                'Week 3',
                'Week 3-4',
                'Week 3-4',
                'Week 4',
                'Week 2-3',
                'Week 3'
            ]
        }
        
        df_marketing = pd.DataFrame(marketing_assets)
        st.dataframe(df_marketing, use_container_width=True, hide_index=True)
    
    with checklist_tabs[4]:
        st.markdown("### Platform Setup Checklist")
        
        platform_setup = {
            'Task': [
                'Platform account creation',
                'Company profile setup',
                'Campaign page draft',
                'Financial documents upload',
                'Legal documents upload',
                'Video upload',
                'Team information',
                'Terms and conditions',
                'Platform review submission',
                'Approval and launch prep'
            ],
            'Timeline': [
                'Week 1',
                'Week 1-2',
                'Week 2-3',
                'Week 2',
                'Week 2',
                'Week 3',
                'Week 2',
                'Week 2',
                'Week 3-4',
                'Week 4-5'
            ],
            'Status': [
                'Required',
                'Required',
                'Required',
                'Required',
                'Required',
                'Required',
                'Required',
                'Required',
                'Required',
                'Pending approval'
            ]
        }
        
        df_platform = pd.DataFrame(platform_setup)
        st.dataframe(df_platform, use_container_width=True, hide_index=True)


def show_best_practices():
    st.markdown("## 💡 Best Practices & Tips")
    
    practice_tabs = st.tabs([
        "Campaign Strategy",
        "Content Creation",
        "Marketing",
        "Investor Relations",
        "Common Mistakes"
    ])
    
    with practice_tabs[0]:
        st.markdown("### Campaign Strategy Best Practices")
        
        st.markdown("""
        **1. Set Realistic Goals**
        - Start with achievable target (70-80% of ideal)
        - Better to exceed goal than fall short
        - Consider stretch goals for momentum
        
        **2. Timing Matters**
        - Avoid holiday seasons
        - Launch on Tuesday-Thursday
        - Consider industry events/announcements
        
        **3. Build Momentum Early**
        - Secure 20-30% in first 48 hours
        - Pre-commit from friends/family/network
        - Create sense of urgency and FOMO
        
        **4. Tell a Compelling Story**
        - Focus on problem and solution
        - Show traction and validation
        - Demonstrate market opportunity
        - Highlight team expertise
        
        **5. Engage Continuously**
        - Daily updates and communication
        - Respond to all questions quickly
        - Share milestones and progress
        - Build community around campaign
        """)
    
    with practice_tabs[1]:
        st.markdown("### Content Creation Tips")
        
        st.markdown("""
        **Pitch Video (2-3 minutes):**
        - ✅ Hook in first 10 seconds
        - ✅ Clear problem statement
        - ✅ Compelling solution
        - ✅ Show traction/demo
        - ✅ Strong call to action
        - ✅ Professional but authentic
        
        **Campaign Page:**
        - ✅ Clear, scannable layout
        - ✅ Strong visuals and graphics
        - ✅ Data and metrics
        - ✅ Social proof
        - ✅ Easy to understand terms
        - ✅ Mobile-friendly design
        
        **Financial Projections:**
        - ✅ Conservative but ambitious
        - ✅ Clear assumptions
        - ✅ Multiple scenarios
        - ✅ Realistic timelines
        - ✅ Professional formatting
        """)
    
    with practice_tabs[2]:
        st.markdown("### Marketing Best Practices")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Email Marketing:**
            - Build list before launch
            - Segment by interest level
            - Personalize messages
            - Send at optimal times
            - Track open/click rates
            - A/B test subject lines
            
            **Social Media:**
            - Post 2-3x daily
            - Use relevant hashtags
            - Engage with comments
            - Share behind-the-scenes
            - Leverage video content
            - Cross-platform promotion
            """)
        
        with col2:
            st.markdown("""
            **Press & Media:**
            - Target fintech publications
            - Local business media
            - Industry blogs
            - Podcast appearances
            - Press release distribution
            - Media kit ready
            
            **Community Building:**
            - Engage potential investors
            - Answer questions promptly
            - Share progress updates
            - Create exclusivity
            - Build FOMO
            - Thank supporters
            """)
    
    with practice_tabs[3]:
        st.markdown("### Investor Relations Best Practices")
        
        st.markdown("""
        **During Campaign:**
        - Respond to questions within 24 hours
        - Provide regular updates
        - Be transparent about challenges
        - Share milestones and wins
        - Build trust and credibility
        
        **Post-Campaign:**
        - Thank all investors promptly
        - Provide quarterly updates
        - Share financial performance
        - Communicate challenges honestly
        - Deliver on promises
        - Build long-term relationships
        
        **Communication Channels:**
        - Email newsletters
        - Platform updates
        - Annual investor meeting
        - Investor portal (if available)
        - Social media updates
        """)
    
    with practice_tabs[4]:
        st.markdown("### Common Mistakes to Avoid")
        
        mistakes = {
            'Mistake': [
                'Setting goal too high',
                'Poor video quality',
                'Weak financial projections',
                'Insufficient marketing',
                'Not engaging with investors',
                'Unrealistic timelines',
                'Poor platform selection',
                'Inadequate preparation',
                'Ignoring compliance',
                'Overpromising results'
            ],
            'Impact': [
                'High',
                'High',
                'High',
                'High',
                'Medium',
                'Medium',
                'High',
                'High',
                'Critical',
                'High'
            ],
            'Solution': [
                'Set realistic, achievable target',
                'Invest in professional video',
                'Use conservative, data-driven projections',
                'Start marketing 4-6 weeks before launch',
                'Respond quickly, engage daily',
                'Set realistic milestones',
                'Research and choose carefully',
                'Follow checklist, allow 4-6 weeks',
                'Consult legal counsel early',
                'Be honest and transparent'
            ]
        }
        
        df_mistakes = pd.DataFrame(mistakes)
        st.dataframe(df_mistakes, use_container_width=True, hide_index=True)


def show_success_metrics():
    st.markdown("## 📈 Success Metrics & KPIs")
    
    metrics_tabs = st.tabs([
        "Campaign Metrics",
        "Financial Metrics",
        "Engagement Metrics",
        "Conversion Metrics"
    ])
    
    with metrics_tabs[0]:
        st.markdown("### Campaign Performance Metrics")
        
        campaign_metrics = {
            'Metric': [
                'Total Amount Raised',
                'Number of Investors',
                'Average Investment Size',
                'Campaign Duration',
                'Days to 50%',
                'Days to 100%',
                'Conversion Rate',
                'Platform Fee Paid'
            ],
            'Target': [
                '$500K - $5M',
                '50-500 investors',
                '$1K-$10K average',
                '60-90 days',
                '30-45 days',
                '60-90 days',
                '2-5%',
                '5-8% of raise'
            ],
            'How to Track': [
                'Platform dashboard',
                'Platform dashboard',
                'Total raised / # investors',
                'Campaign calendar',
                'Daily tracking',
                'Daily tracking',
                'Investors / Visitors',
                'Platform reporting'
            ]
        }
        
        df_campaign = pd.DataFrame(campaign_metrics)
        st.dataframe(df_campaign, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Success rate visualization
        st.markdown("### Campaign Success Rate by Platform")
        
        success_data = {
            'Platform': ['Republic', 'SeedInvest', 'StartEngine', 'Wefunder', 'Netcapital'],
            'Success Rate': [65, 70, 55, 60, 50]  # Estimated percentages
        }
        
        fig = px.bar(
            x=success_data['Platform'],
            y=success_data['Success Rate'],
            labels={'x': 'Platform', 'y': 'Success Rate (%)'},
            title="Estimated Campaign Success Rates",
            color=success_data['Platform'],
            color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with metrics_tabs[1]:
        st.markdown("### Financial Performance Metrics")
        
        financial_metrics = {
            'Metric': [
                'Funds Raised vs Goal',
                'Cost per Investor Acquisition',
                'Platform Fees',
                'Legal/Compliance Costs',
                'Marketing Costs',
                'Net Funds Received',
                'ROI on Campaign',
                'Time to Break-even'
            ],
            'Calculation': [
                'Raised / Goal × 100',
                'Total marketing cost / # investors',
                'Raise amount × platform fee %',
                'Legal fees + compliance costs',
                'Marketing spend',
                'Raised - fees - costs',
                'Net funds / Total costs',
                'Months to recover costs'
            ],
            'Target': [
                '100%+',
                '$50-$200',
                '5-8% of raise',
                '$10K-$50K',
                '$5K-$25K',
                '85-90% of raise',
                '5:1 or better',
                '6-12 months'
            ]
        }
        
        df_financial = pd.DataFrame(financial_metrics)
        st.dataframe(df_financial, use_container_width=True, hide_index=True)
    
    with metrics_tabs[2]:
        st.markdown("### Engagement Metrics")
        
        engagement_metrics = {
            'Metric': [
                'Campaign Page Views',
                'Video Views',
                'Email Open Rate',
                'Email Click-Through Rate',
                'Social Media Engagement',
                'Investor Questions',
                'Response Time',
                'Community Growth'
            ],
            'Target': [
                '10K-50K views',
                '5K-25K views',
                '20-30%',
                '3-5%',
                'High engagement',
                '50-200 questions',
                '<24 hours',
                '500-2K followers'
            ],
            'How to Improve': [
                'SEO, social sharing, press',
                'Compelling thumbnail, description',
                'Subject line optimization',
                'Clear CTAs, valuable content',
                'Regular posting, engagement',
                'Quick responses, transparency',
                'Set expectations, automate',
                'Valuable content, engagement'
            ]
        }
        
        df_engagement = pd.DataFrame(engagement_metrics)
        st.dataframe(df_engagement, use_container_width=True, hide_index=True)
    
    with metrics_tabs[3]:
        st.markdown("### Conversion Metrics")
        
        conversion_metrics = {
            'Stage': [
                'Visitor to Lead',
                'Lead to Investor',
                'Email to Investor',
                'Social to Investor',
                'Press to Investor',
                'Referral to Investor'
            ],
            'Conversion Rate': [
                '5-10%',
                '2-5%',
                '1-3%',
                '0.5-2%',
                '0.1-1%',
                '10-20%'
            ],
            'Optimization': [
                'Clear value proposition',
                'Compelling pitch, social proof',
                'Segmented campaigns',
                'Engaging content, CTAs',
                'Media coverage, credibility',
                'Incentivize referrals'
            ]
        }
        
        df_conversion = pd.DataFrame(conversion_metrics)
        st.dataframe(df_conversion, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Conversion funnel
        st.markdown("### Conversion Funnel Visualization")
        
        fig = go.Figure(go.Funnel(
            y=["Visitors", "Leads", "Interested", "Investors"],
            x=[10000, 1000, 200, 50],
            textposition="inside",
            textinfo="value+percent initial"
        ))
        
        fig.update_layout(
            title="Typical Campaign Conversion Funnel",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

