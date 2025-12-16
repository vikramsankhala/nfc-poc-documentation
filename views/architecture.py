"""
Architecture & Technical Overview Page
"""

import streamlit as st

def show():
    st.markdown('<h1 class="main-header">🏗️ Architecture & Technical Overview</h1>', unsafe_allow_html=True)
    st.markdown("Technical architecture and system design overview.")
    
    st.markdown("---")
    
    # High-Level Architecture
    st.markdown("### 🏛️ High-Level Architecture")
    
    st.markdown("""
    The application follows a modern, AI-augmented architecture designed for banking and financial services:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Frontend Layer**
        - Streamlit web application (this POC)
        - React Native mobile app (production)
        - Responsive UI components
        - Real-time data visualization
        """)
        
        st.markdown("""
        **Integration Layer**
        - NFC passport reading
        - Camera integration
        - Document upload & OCR
        - WebView communication bridge
        """)
    
    with col2:
        st.markdown("""
        **Backend Services**
        - FastAPI orchestration layer
        - Agentic AI engine
        - LLM gateway (LiteLLM)
        - Data processing services
        """)
        
        st.markdown("""
        **AI & ML Services**
        - Computer vision analysis
        - Document OCR & extraction
        - Risk scoring models
        - Fraud detection
        """)
    
    st.markdown("---")
    
    # Agentic AI Architecture
    st.markdown("### 🤖 Agentic AI Architecture")
    
    st.markdown("""
    The system uses autonomous AI agents to handle different aspects of the onboarding process:
    """)
    
    agents = [
        {
            "name": "IDV Agent",
            "description": "Identity Verification Agent",
            "capabilities": [
                "ID OCR and extraction",
                "Liveness detection",
                "Face matching",
                "Document authenticity verification"
            ]
        },
        {
            "name": "Screening Agent",
            "description": "Compliance & Screening Agent",
            "capabilities": [
                "Sanctions list checking",
                "PEP (Politically Exposed Person) screening",
                "Adverse media monitoring",
                "Fuzzy name matching"
            ]
        },
        {
            "name": "Fraud Agent",
            "description": "Fraud Detection Agent",
            "capabilities": [
                "Fraud history checking",
                "Device/IP anomaly detection",
                "Suspicious pattern recognition",
                "Deduplication checks"
            ]
        },
        {
            "name": "Risk Score Agent",
            "description": "Risk Assessment Agent",
            "capabilities": [
                "Credit risk calculation",
                "Asset risk evaluation",
                "Compliance risk assessment",
                "Aggregated risk scoring"
            ]
        },
        {
            "name": "Asset Valuation Agent",
            "description": "Asset Analysis Agent",
            "capabilities": [
                "Image analysis (condition assessment)",
                "Market data integration (CAP HPI)",
                "DVLA VES cross-checking",
                "Real-time valuation"
            ]
        }
    ]
    
    for agent in agents:
        with st.expander(f"🔹 {agent['name']} - {agent['description']}", expanded=False):
            st.markdown(f"**Capabilities:**")
            for capability in agent['capabilities']:
                st.markdown(f"- {capability}")
    
    st.markdown("---")
    
    # Workflow Diagram
    st.markdown("### 🔄 System Workflow")
    
    st.markdown("""
    ```
    Customer Onboarding
         ↓
    [Form Submission] → Data Collection
         ↓
    [eKYC Process]
         ├─→ NFC Passport Reading → IDV Agent
         ├─→ Document Upload → OCR → IDV Agent
         └─→ Screening Agent → Fraud Agent
         ↓
    [Asset Valuation]
         ├─→ Photo Upload → Asset Valuation Agent
         ├─→ V5C Upload → DVLA Verification
         └─→ Market Data Integration
         ↓
    [Loan Application]
         ├─→ Risk Score Agent
         ├─→ Automated Decisioning
         └─→ Loan Offer Generation
         ↓
    [Results & Analytics]
         └─→ Dashboard & Reporting
    ```
    """)
    
    st.markdown("---")
    
    # Technology Stack
    st.markdown("### 💻 Technology Stack")
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.markdown("""
        **Frontend**
        - Streamlit (POC)
        - React Native (Production)
        - Plotly (Visualizations)
        - Material-UI Components
        
        **Backend**
        - Python 3.10+
        - FastAPI
        - LangChain
        - LiteLLM Gateway
        """)
    
    with tech_col2:
        st.markdown("""
        **AI/ML**
        - OpenAI GPT-4 / Claude
        - Computer Vision Models
        - OCR Services
        - Risk Scoring Models
        
        **Infrastructure**
        - AWS SageMaker (Current)
        - On-Premise AI (Planned)
        - Langfuse (Logging/Tracing)
        - SQLite / PostgreSQL
        """)
    
    st.markdown("---")
    
    # Security & Compliance
    st.markdown("### 🔒 Security & Compliance")
    
    compliance_items = [
        ("GDPR Compliance", "Data minimization, retention policies, right to deletion"),
        ("KYC/AML", "Know Your Customer and Anti-Money Laundering compliance"),
        ("Consumer Duty", "UK Consumer Duty regulations adherence"),
        ("SCA", "Strong Customer Authentication (biometric/2FA)"),
        ("Data Protection", "Encryption at rest and in transit (TLS 1.3, SSE-KMS)"),
        ("Operational Resilience", "High availability, disaster recovery, monitoring"),
        ("SM&CR", "Senior Managers & Certification Regime compliance")
    ]
    
    for title, description in compliance_items:
        st.markdown(f"""
        <div style="padding: 0.75rem; margin: 0.5rem 0; border-left: 4px solid #1f77b4; background-color: #f8f9fa; border-radius: 4px;">
            <strong>{title}</strong><br>
            <span style="color: #666; font-size: 0.9rem;">{description}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Key Features
    st.markdown("### ✨ Key Technical Features")
    
    feature_col1, feature_col2 = st.columns(2)
    
    with feature_col1:
        st.markdown("""
        **Real-Time Processing**
        - Instant asset valuation
        - Automated loan decisioning
        - Live risk scoring
        
        **AI-Powered Analysis**
        - Computer vision for document/asset analysis
        - Natural language processing for data extraction
        - Machine learning for risk assessment
        """)
    
    with feature_col2:
        st.markdown("""
        **Native Integration**
        - NFC chip reading (passport)
        - Camera integration (liveness, photos)
        - Biometric authentication
        
        **Scalability**
        - Microservices architecture
        - Horizontal scaling capability
        - Cloud-native design
        """)
    
    st.markdown("---")
    
    # API Endpoints (Example)
    st.markdown("### 🔌 API Endpoints (Example)")
    
    with st.expander("View API Structure", expanded=False):
        st.code("""
        POST /api/v1/onboarding/submit
        POST /api/v1/ekyc/verify-nfc
        POST /api/v1/ekyc/verify-document
        POST /api/v1/ekyc/screening
        POST /api/v1/asset/valuate
        POST /api/v1/loan/apply
        GET  /api/v1/loan/decision/{application_id}
        GET  /api/v1/analytics/dashboard
        """, language="text")
    
    st.markdown("---")
    
    # Deployment
    st.markdown("### 🚀 Deployment")
    
    st.markdown("""
    **Streamlit Community Cloud (POC)**
    - This application is deployed on Streamlit Community Cloud
    - Public URL for investor demonstration
    - No authentication required (demo mode)
    
    **Production Deployment (Planned)**
    - On-premise infrastructure
    - Private cloud deployment
    - Full security and authentication
    - High availability setup
    """)
    
    st.info("""
    **Note:** This is a Proof of Concept application. Production implementation would include 
    additional security measures, authentication, and integration with actual banking systems.
    """)

