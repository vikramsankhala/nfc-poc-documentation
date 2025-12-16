"""
Wireframes and Design Mockups Page
Visual representations of screen layouts and designs
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show():
    st.markdown('<h1 class="main-header">🎨 Wireframes & Design Mockups</h1>', unsafe_allow_html=True)
    st.markdown("Visual layouts and design mockups for the AI-Augmented Customer Onboarding application.")
    
    st.markdown("---")
    
    # Navigation tabs for different views
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📱 Mobile App Wireframes", 
        "💻 Web Application Layouts", 
        "🔄 User Flow Diagrams", 
        "🎯 Component Mockups",
        "📐 Architecture Diagrams"
    ])
    
    with tab1:
        st.markdown("### 📱 Mobile Application Wireframes")
        st.markdown("React Native mobile app screen designs and layouts.")
        
        # Mobile App Screens
        mobile_screens = [
            {
                "name": "Onboarding Screen",
                "description": "Customer registration and information collection",
                "components": ["Header with logo", "Form fields (Name, Email, Phone)", "Address input", "Employment details", "Loan requirements", "Submit button"]
            },
            {
                "name": "NFC Passport Reading",
                "description": "NFC chip reading interface",
                "components": ["NFC detection indicator", "Tap to read button", "Reading animation", "Passport data display", "Verification status"]
            },
            {
                "name": "Camera Screen",
                "description": "Document and asset photo capture",
                "components": ["Camera preview", "Capture button", "Gallery view", "Liveness check overlay", "Quality indicators"]
            },
            {
                "name": "Asset Valuation",
                "description": "Asset photo upload and analysis",
                "components": ["Photo grid", "Upload button", "AI analysis progress", "Valuation results", "Market data display"]
            },
            {
                "name": "Loan Application",
                "description": "Loan details and submission",
                "components": ["Application summary", "Loan terms", "Risk indicators", "Submit button", "Status tracker"]
            },
            {
                "name": "Results Dashboard",
                "description": "Decision and analytics view",
                "components": ["Decision card", "Charts and graphs", "Risk breakdown", "Loan details", "Next steps"]
            }
        ]
        
        for screen in mobile_screens:
            with st.expander(f"📱 {screen['name']}", expanded=False):
                st.markdown(f"**Description:** {screen['description']}")
                st.markdown("**Components:**")
                for component in screen['components']:
                    st.markdown(f"- {component}")
                
                # Visual mockup using HTML/CSS
                st.markdown("**Visual Mockup:**")
                create_mobile_mockup(screen['name'], screen['components'])
    
    with tab2:
        st.markdown("### 💻 Web Application Layouts")
        st.markdown("Streamlit web application page layouts and structure.")
        
        # Web Layouts
        web_layouts = [
            {
                "page": "Home Dashboard",
                "layout": "3-column grid with info cards, workflow visualization, and statistics",
                "sections": ["Header", "Overview cards (3 columns)", "Workflow steps", "Key features", "Quick start guide", "Session status metrics"]
            },
            {
                "page": "Customer Onboarding",
                "layout": "2-column form with grouped sections",
                "sections": ["Personal Information (2 columns)", "Address details", "Employment Information", "Loan Requirements", "Form validation", "Submit button"]
            },
            {
                "page": "eKYC Verification",
                "layout": "Multi-section with tabs for different verification methods",
                "sections": ["NFC Reading section", "Document Upload area", "Screening Results", "Status indicators", "Progress tracker"]
            },
            {
                "page": "Asset Valuation",
                "layout": "Split view: form on left, results on right",
                "sections": ["Asset information form", "Photo upload grid", "Valuation results (4 metrics)", "Detailed analysis tabs", "Market data display"]
            },
            {
                "page": "Loan Application",
                "layout": "Summary view with expandable sections",
                "sections": ["Application summary cards", "Loan terms display", "Risk assessment", "Terms and conditions", "Submit section"]
            },
            {
                "page": "Results Dashboard",
                "layout": "Dashboard with charts and detailed tabs",
                "sections": ["Decision summary banner", "Key metrics (4 columns)", "Visualizations (2x2 grid)", "Detailed tabs", "Next steps section"]
            }
        ]
        
        for layout in web_layouts:
            with st.expander(f"💻 {layout['page']}", expanded=False):
                st.markdown(f"**Layout Structure:** {layout['layout']}")
                st.markdown("**Page Sections:**")
                for section in layout['sections']:
                    st.markdown(f"- {section}")
                
                # Create visual layout representation
                create_web_layout_mockup(layout['page'], layout['sections'])
    
    with tab3:
        st.markdown("### 🔄 User Flow Diagrams")
        st.markdown("Complete user journey and workflow visualizations.")
        
        # User Flow
        st.markdown("#### Complete Customer Onboarding Flow")
        create_user_flow_diagram()
        
        st.markdown("---")
        
        # Decision Tree
        st.markdown("#### Loan Decision Flow")
        create_decision_flow_diagram()
        
        st.markdown("---")
        
        # KYC Process Flow
        st.markdown("#### eKYC Verification Process")
        create_kyc_flow_diagram()
    
    with tab4:
        st.markdown("### 🎯 Component Mockups")
        st.markdown("Detailed UI component designs and interactions.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Form Components")
            create_form_component_mockup()
            
            st.markdown("#### Navigation Components")
            create_navigation_mockup()
        
        with col2:
            st.markdown("#### Status Indicators")
            create_status_indicator_mockup()
            
            st.markdown("#### Data Visualization Components")
            create_chart_component_mockup()
    
    with tab5:
        st.markdown("### 📐 Architecture Diagrams")
        st.markdown("System architecture and component relationships.")
        
        st.markdown("#### High-Level System Architecture")
        create_architecture_diagram()
        
        st.markdown("---")
        
        st.markdown("#### Data Flow Diagram")
        create_data_flow_diagram()
        
        st.markdown("---")
        
        st.markdown("#### AI Agent Architecture")
        create_ai_agent_diagram()


def create_mobile_mockup(screen_name, components):
    """Create a visual mobile screen mockup"""
    mockup_html = f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 20px; margin: 20px 0;">
        <div style="background: white; border-radius: 15px; padding: 15px; max-width: 375px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
            <div style="background: #f0f0f0; height: 40px; border-radius: 10px 10px 0 0; display: flex; align-items: center; padding: 0 15px; margin: -15px -15px 15px -15px;">
                <div style="width: 8px; height: 8px; background: #ff5f57; border-radius: 50%; margin-right: 6px;"></div>
                <div style="width: 8px; height: 8px; background: #ffbd2e; border-radius: 50%; margin-right: 6px;"></div>
                <div style="width: 8px; height: 8px; background: #28ca42; border-radius: 50%;"></div>
                <div style="flex: 1; text-align: center; font-size: 12px; font-weight: bold; color: #333;">{screen_name}</div>
            </div>
            <div style="min-height: 500px; background: #fafafa; border-radius: 10px; padding: 20px;">
    """
    
    for i, component in enumerate(components[:5]):  # Show first 5 components
        mockup_html += f"""
            <div style="background: white; padding: 12px; margin: 10px 0; border-radius: 8px; border-left: 4px solid #667eea; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                <div style="font-size: 11px; color: #666;">{component}</div>
            </div>
        """
    
    mockup_html += """
            </div>
            <div style="background: #f0f0f0; height: 30px; border-radius: 0 0 10px 10px; margin: 15px -15px -15px -15px; display: flex; justify-content: space-around; align-items: center;">
                <div style="width: 60px; height: 4px; background: #667eea; border-radius: 2px;"></div>
            </div>
        </div>
    </div>
    """
    st.markdown(mockup_html, unsafe_allow_html=True)


def create_web_layout_mockup(page_name, sections):
    """Create a visual web page layout mockup"""
    layout_html = f"""
    <div style="background: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <div style="background: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <div style="background: #1f77b4; color: white; padding: 15px; border-radius: 5px; margin-bottom: 15px; font-weight: bold;">
                {page_name}
            </div>
    """
    
    # Create sections based on page type
    if "Dashboard" in page_name:
        layout_html += """
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 15px;">
                <div style="background: #e3f2fd; padding: 15px; border-radius: 5px; border-left: 4px solid #1f77b4;">Card 1</div>
                <div style="background: #e3f2fd; padding: 15px; border-radius: 5px; border-left: 4px solid #1f77b4;">Card 2</div>
                <div style="background: #e3f2fd; padding: 15px; border-radius: 5px; border-left: 4px solid #1f77b4;">Card 3</div>
            </div>
        """
    elif "Onboarding" in page_name:
        layout_html += """
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-bottom: 15px;">
                <div style="background: #f0f0f0; padding: 20px; border-radius: 5px; min-height: 100px;">Form Field 1</div>
                <div style="background: #f0f0f0; padding: 20px; border-radius: 5px; min-height: 100px;">Form Field 2</div>
            </div>
        """
    elif "Valuation" in page_name:
        layout_html += """
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                <div style="background: #f0f0f0; padding: 20px; border-radius: 5px; min-height: 200px;">Form Section</div>
                <div style="background: #e8f5e9; padding: 20px; border-radius: 5px; min-height: 200px;">Results Section</div>
            </div>
        """
    
    layout_html += """
            <div style="background: #f9f9f9; padding: 15px; border-radius: 5px; margin-top: 15px;">
                <div style="font-size: 12px; color: #666;">Additional Sections:</div>
        """
    
    for section in sections[:3]:
        layout_html += f'<div style="font-size: 11px; color: #888; margin-top: 5px;">• {section}</div>'
    
    layout_html += """
            </div>
        </div>
    </div>
    """
    st.markdown(layout_html, unsafe_allow_html=True)


def create_user_flow_diagram():
    """Create interactive user flow diagram"""
    fig = go.Figure()
    
    # Define flow steps
    steps = [
        ("Start", 0, 0),
        ("Browse Products", 1, 0),
        ("Onboarding Form", 2, 0),
        ("eKYC Verification", 3, 0),
        ("Asset Valuation", 4, 0),
        ("Loan Application", 5, 0),
        ("Decision", 6, 0),
        ("Complete", 7, 0)
    ]
    
    # Add nodes
    for i, (name, x, y) in enumerate(steps):
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers+text',
            marker=dict(size=80, color='#1f77b4', line=dict(width=2, color='white')),
            text=[name],
            textposition="middle center",
            textfont=dict(size=10, color='white'),
            name=name,
            hovertemplate=f'<b>{name}</b><extra></extra>'
        ))
    
    # Add arrows/connections
    for i in range(len(steps) - 1):
        fig.add_annotation(
            x=steps[i+1][1],
            y=steps[i+1][2],
            ax=steps[i][1],
            ay=steps[i][2],
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor="#666",
            axref="x",
            ayref="y",
            xref="x",
            yref="y"
        )
    
    fig.update_layout(
        title="Customer Onboarding User Flow",
        xaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, 7.5]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, 0.5]),
        height=200,
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def create_decision_flow_diagram():
    """Create loan decision flow diagram"""
    fig = go.Figure()
    
    # Decision tree structure
    nodes = [
        ("Application\nReceived", 0, 2),
        ("KYC\nCheck", 1, 2),
        ("Asset\nValuation", 2, 2),
        ("Risk\nAssessment", 3, 2),
        ("Approved", 4, 3),
        ("Rejected", 4, 1),
        ("Manual\nReview", 4, 2)
    ]
    
    # Add nodes with different colors
    colors = ['#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#22c55e', '#ef4444', '#f59e0b']
    
    for i, ((name, x, y), color) in enumerate(zip(nodes, colors)):
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers+text',
            marker=dict(size=100, color=color, line=dict(width=2, color='white')),
            text=[name],
            textposition="middle center",
            textfont=dict(size=9, color='white'),
            name=name
        ))
    
    # Add connections
    connections = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (3, 6)]
    for start, end in connections:
        fig.add_annotation(
            x=nodes[end][1],
            y=nodes[end][2],
            ax=nodes[start][1],
            ay=nodes[start][2],
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor="#666"
        )
    
    fig.update_layout(
        title="Loan Decision Flow",
        xaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, 4.5]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[0.5, 3.5]),
        height=300,
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def create_kyc_flow_diagram():
    """Create KYC process flow"""
    fig = make_subplots(rows=1, cols=1)
    
    # KYC steps
    steps = [
        ("NFC\nRead", 0, 0),
        ("Document\nUpload", 1, 0),
        ("OCR\nExtraction", 2, 0),
        ("Data\nMatching", 3, 0),
        ("Screening", 4, 0),
        ("Fraud\nCheck", 5, 0),
        ("Approved", 6, 0)
    ]
    
    for i, (name, x, y) in enumerate(steps):
        color = '#22c55e' if i == len(steps) - 1 else '#1f77b4'
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers+text',
            marker=dict(size=90, color=color, line=dict(width=2, color='white')),
            text=[name],
            textposition="middle center",
            textfont=dict(size=9, color='white'),
            name=name
        ))
    
    # Add arrows
    for i in range(len(steps) - 1):
        fig.add_annotation(
            x=steps[i+1][1],
            y=steps[i+1][2],
            ax=steps[i][1],
            ay=steps[i][2],
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor="#666"
        )
    
    fig.update_layout(
        title="eKYC Verification Process",
        xaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, 6.5]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, 0.5]),
        height=200,
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def create_form_component_mockup():
    """Create form component visualizations"""
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #ddd; margin: 10px 0;">
        <div style="margin-bottom: 15px;">
            <label style="display: block; font-weight: bold; margin-bottom: 5px; color: #333;">Text Input</label>
            <input type="text" placeholder="Enter text..." style="width: 100%; padding: 10px; border: 2px solid #1f77b4; border-radius: 5px; font-size: 14px;" disabled>
        </div>
        <div style="margin-bottom: 15px;">
            <label style="display: block; font-weight: bold; margin-bottom: 5px; color: #333;">Select Dropdown</label>
            <select style="width: 100%; padding: 10px; border: 2px solid #1f77b4; border-radius: 5px; font-size: 14px;" disabled>
                <option>Option 1</option>
                <option>Option 2</option>
            </select>
        </div>
        <div>
            <button style="width: 100%; padding: 12px; background: #1f77b4; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer;">Submit Button</button>
        </div>
    </div>
    """, unsafe_allow_html=True)


def create_navigation_mockup():
    """Create navigation component mockup"""
    st.markdown("""
    <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin: 10px 0;">
        <div style="background: #1f77b4; color: white; padding: 10px; border-radius: 5px; margin-bottom: 5px; font-weight: bold;">🏠 Home</div>
        <div style="background: white; padding: 10px; border-radius: 5px; margin-bottom: 5px;">👤 Onboarding</div>
        <div style="background: white; padding: 10px; border-radius: 5px; margin-bottom: 5px;">🛡️ eKYC</div>
        <div style="background: white; padding: 10px; border-radius: 5px;">💰 Results</div>
    </div>
    """, unsafe_allow_html=True)


def create_status_indicator_mockup():
    """Create status indicator components"""
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #ddd; margin: 10px 0;">
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <div style="width: 12px; height: 12px; background: #22c55e; border-radius: 50%; margin-right: 10px;"></div>
            <span style="font-weight: bold; color: #22c55e;">✅ Approved</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <div style="width: 12px; height: 12px; background: #f59e0b; border-radius: 50%; margin-right: 10px;"></div>
            <span style="font-weight: bold; color: #f59e0b;">⏳ Pending</span>
        </div>
        <div style="display: flex; align-items: center;">
            <div style="width: 12px; height: 12px; background: #ef4444; border-radius: 50%; margin-right: 10px;"></div>
            <span style="font-weight: bold; color: #ef4444;">❌ Rejected</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def create_chart_component_mockup():
    """Create chart component visualization"""
    # Create a sample chart
    fig = go.Figure(data=[
        go.Bar(
            x=['Risk Score', 'Credit Risk', 'Asset Risk', 'Fraud Risk'],
            y=[0.45, 0.3, 0.25, 0.15],
            marker_color=['#1f77b4', '#f59e0b', '#22c55e', '#ef4444']
        )
    ])
    fig.update_layout(
        title="Sample Risk Breakdown Chart",
        height=250,
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)


def create_architecture_diagram():
    """Create system architecture diagram"""
    fig = go.Figure()
    
    # Architecture layers
    layers = [
        ("Frontend\n(Streamlit/React Native)", 0, 3, '#1f77b4'),
        ("API Gateway\n(FastAPI)", 0, 2, '#667eea'),
        ("Orchestrator\n(LangChain)", 0, 1, '#764ba2'),
        ("AI Agents\n(IDV, Screening, etc.)", -1, 0, '#f59e0b'),
        ("AI Agents\n(Fraud, Risk, etc.)", 1, 0, '#f59e0b'),
        ("LLM Gateway\n(LiteLLM)", 0, -1, '#22c55e'),
        ("Data Storage\n(SQLite/PostgreSQL)", 0, -2, '#10b981')
    ]
    
    for name, x, y, color in layers:
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers+text',
            marker=dict(size=120, color=color, line=dict(width=3, color='white')),
            text=[name],
            textposition="middle center",
            textfont=dict(size=9, color='white'),
            name=name
        ))
    
    # Add connections
    connections = [
        (0, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 5), (5, 6)
    ]
    
    for start, end in connections:
        fig.add_annotation(
            x=layers[end][1],
            y=layers[end][2],
            ax=layers[start][1],
            ay=layers[start][2],
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor="#666"
        )
    
    fig.update_layout(
        title="System Architecture",
        xaxis=dict(showgrid=False, showticklabels=False, range=[-2, 2]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-3, 4]),
        height=500,
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def create_data_flow_diagram():
    """Create data flow diagram"""
    fig = go.Figure()
    
    # Data flow nodes
    nodes = [
        ("User\nInput", -2, 0),
        ("Form\nData", -1, 0),
        ("NFC\nData", -1, 1),
        ("Document\nData", -1, -1),
        ("Orchestrator", 0, 0),
        ("AI\nProcessing", 1, 0),
        ("Decision\nEngine", 2, 0),
        ("Results", 3, 0)
    ]
    
    colors = ['#1f77b4', '#667eea', '#667eea', '#667eea', '#764ba2', '#f59e0b', '#22c55e', '#10b981']
    
    for i, ((name, x, y), color) in enumerate(zip(nodes, colors)):
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers+text',
            marker=dict(size=100, color=color, line=dict(width=2, color='white')),
            text=[name],
            textposition="middle center",
            textfont=dict(size=9, color='white'),
            name=name
        ))
    
    # Add flow arrows
    flow_connections = [
        (0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 4),
        (4, 5), (5, 6), (6, 7)
    ]
    
    for start, end in flow_connections:
        fig.add_annotation(
            x=nodes[end][1],
            y=nodes[end][2],
            ax=nodes[start][1],
            ay=nodes[start][2],
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor="#666"
        )
    
    fig.update_layout(
        title="Data Flow Diagram",
        xaxis=dict(showgrid=False, showticklabels=False, range=[-3, 4]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-2, 2]),
        height=300,
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def create_ai_agent_diagram():
    """Create AI agent architecture diagram"""
    fig = go.Figure()
    
    # AI agents
    agents = [
        ("Orchestrator", 0, 2),
        ("IDV\nAgent", -2, 1),
        ("Screening\nAgent", -1, 1),
        ("Fraud\nAgent", 1, 1),
        ("Risk Score\nAgent", 2, 1),
        ("Asset\nValuation\nAgent", 0, 0),
        ("LLM\nGateway", 0, -1)
    ]
    
    colors = ['#764ba2', '#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#f59e0b', '#22c55e']
    
    for i, ((name, x, y), color) in enumerate(zip(agents, colors)):
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers+text',
            marker=dict(size=110, color=color, line=dict(width=2, color='white')),
            text=[name],
            textposition="middle center",
            textfont=dict(size=8, color='white'),
            name=name
        ))
    
    # Connect agents to orchestrator
    for i in range(1, len(agents)):
        fig.add_annotation(
            x=agents[i][1],
            y=agents[i][2],
            ax=agents[0][1],
            ay=agents[0][2],
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor="#666"
        )
    
    # Connect agents to LLM Gateway
    for i in range(1, len(agents) - 1):
        fig.add_annotation(
            x=agents[-1][1],
            y=agents[-1][2],
            ax=agents[i][1],
            ay=agents[i][2],
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1.5,
            arrowcolor="#999",
            linestyle="dash"
        )
    
    fig.update_layout(
        title="AI Agent Architecture",
        xaxis=dict(showgrid=False, showticklabels=False, range=[-3, 3]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-2, 3]),
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

