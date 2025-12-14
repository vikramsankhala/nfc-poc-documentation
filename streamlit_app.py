import streamlit as st
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="React Native NFC PoC Documentation",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #38bdf8;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .subsection-header {
        font-size: 1.3rem;
        font-weight: 600;
        color: #60a5fa;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    .info-box {
        background-color: #1e293b;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #38bdf8;
        margin: 1rem 0;
    }
    .success-box {
        background-color: rgba(34, 197, 94, 0.1);
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #22c55e;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: rgba(245, 158, 11, 0.1);
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #f59e0b;
        margin: 1rem 0;
    }
    .code-block {
        background-color: #0f172a;
        padding: 1rem;
        border-radius: 6px;
        border: 1px solid rgba(34, 197, 94, 0.2);
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
    }
    .tech-card {
        background-color: #1e293b;
        padding: 1.5rem;
        border-radius: 8px;
        border-top: 3px solid #38bdf8;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to display PDF
def display_pdf(pdf_path):
    """Display PDF file in Streamlit"""
    try:
        with open(pdf_path, "rb") as pdf_file:
            base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"PDF file not found: {pdf_path}")
    except Exception as e:
        st.error(f"Error displaying PDF: {str(e)}")

def display_audio_player(audio_filename, section_name):
    """Display audio player with controls for section narration"""
    audio_path = Path(audio_filename)
    if audio_path.exists():
        with open(audio_path, "rb") as audio_file:
            audio_data = base64.b64encode(audio_file.read()).decode('utf-8')
            audio_html = f"""
            <div style="margin-bottom: 2rem; padding: 1.5rem; background-color: rgba(56, 189, 248, 0.15); border-radius: 8px; border: 2px solid #38bdf8; box-shadow: 0 2px 8px rgba(56, 189, 248, 0.3);">
                <h4 style="color: #38bdf8; margin-bottom: 1rem; font-size: 1.1rem;">🔊 Audio Narration: {section_name}</h4>
                <audio controls style="width: 100%; height: 54px; background-color: rgba(0, 0, 0, 0.3); border-radius: 4px;">
                    <source src="data:audio/mpeg;base64,{audio_data}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
                <p style="color: #cbd5e1; font-size: 0.85rem; margin-top: 0.75rem; margin-bottom: 0; text-align: center;">
                    Listen to the detailed narration for this section
                </p>
            </div>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    else:
        # Show placeholder if audio file doesn't exist yet
        st.markdown(f"""
        <div style="margin-bottom: 2rem; padding: 1.5rem; background-color: rgba(245, 158, 11, 0.1); border-radius: 8px; border: 2px solid #f59e0b;">
            <p style="color: #f59e0b; font-size: 0.9rem; margin: 0;">
                📝 Audio narration for this section will be available soon. Expected file: <code>{audio_filename}</code>
            </p>
        </div>
        """, unsafe_allow_html=True)

def display_sequential_audio_player(audio_files, section_name):
    """Display audio player that plays multiple audio files sequentially"""
    audio_data_list = []
    audio_files_found = []
    
    for audio_file in audio_files:
        audio_path = Path(audio_file)
        if audio_path.exists():
            with open(audio_path, "rb") as f:
                audio_data = base64.b64encode(f.read()).decode('utf-8')
                audio_data_list.append(audio_data)
                audio_files_found.append(audio_file)
    
    if audio_files_found:
        # Create a unique ID for this player
        player_id = f"sequential_player_{hash(''.join(audio_files_found))}"
        
        audio_html = f"""
        <div style="margin-bottom: 2rem; padding: 1.5rem; background-color: rgba(56, 189, 248, 0.15); border-radius: 8px; border: 2px solid #38bdf8; box-shadow: 0 2px 8px rgba(56, 189, 248, 0.3);">
            <h4 style="color: #38bdf8; margin-bottom: 1rem; font-size: 1.1rem;">🔊 Audio Narration: {section_name}</h4>
            <p id="{player_id}_status" style="color: #cbd5e1; font-size: 0.85rem; margin-bottom: 0.75rem; text-align: center;">
                Playing part 1 of {len(audio_files_found)}...
            </p>
            <audio id="{player_id}" controls style="width: 100%; height: 54px; background-color: rgba(0, 0, 0, 0.3); border-radius: 4px;">
                <source src="data:audio/mpeg;base64,{audio_data_list[0]}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
            <p style="color: #cbd5e1; font-size: 0.85rem; margin-top: 0.75rem; margin-bottom: 0; text-align: center;">
                {len(audio_files_found)} audio files will play sequentially
            </p>
        </div>
        <script>
            (function() {{
                const audioFiles = {audio_data_list};
                const player = document.getElementById('{player_id}');
                const status = document.getElementById('{player_id}_status');
                let currentIndex = 0;
                
                function loadNextAudio() {{
                    if (currentIndex < audioFiles.length - 1) {{
                        currentIndex++;
                        player.src = 'data:audio/mpeg;base64,' + audioFiles[currentIndex];
                        status.textContent = 'Playing part ' + (currentIndex + 1) + ' of ' + audioFiles.length + '...';
                        player.load();
                        player.play().catch(function(error) {{
                            console.log('Autoplay prevented:', error);
                        }});
                    }} else {{
                        status.textContent = 'All audio files completed.';
                    }}
                }}
                
                player.addEventListener('ended', loadNextAudio);
                
                player.addEventListener('play', function() {{
                    status.textContent = 'Playing part ' + (currentIndex + 1) + ' of ' + audioFiles.length + '...';
                }});
                
                player.addEventListener('pause', function() {{
                    status.textContent = 'Paused at part ' + (currentIndex + 1) + ' of ' + audioFiles.length + '.';
                }});
            }})();
        </script>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
    else:
        # Show placeholder if no audio files exist
        st.markdown(f"""
        <div style="margin-bottom: 2rem; padding: 1.5rem; background-color: rgba(245, 158, 11, 0.1); border-radius: 8px; border: 2px solid #f59e0b;">
            <p style="color: #f59e0b; font-size: 0.9rem; margin: 0;">
                📝 Audio narration files not found. Expected files: {', '.join(audio_files)}
            </p>
        </div>
        """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📱 Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    [
        "📖 Introduction",
        "📋 Problem Statement",
        "💼 Investor Pitch & Proposal",
        "✅ Requirements Satisfaction",
        "📊 Presentation",
        "🏠 Home & Overview",
        "💡 Solution Overview",
        "🛠️ Tech Stack",
        "📱 Platform Requirements",
        "📡 NFC Integration",
        "📷 Camera Integration",
        "🌐 WebView Integration",
        "🔗 Data Communication",
        "🧭 Navigation & Structure",
        "📊 State Management",
        "⚠️ Error Handling",
        "🧪 Testing Strategy",
        "📅 Implementation Timeline",
        "📦 Deliverables"
    ]
)

# Introduction
if page == "📖 Introduction":
    st.markdown('<div class="main-header">Introduction</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_introduction.mp3", "Introduction")
    
    # Product Overview
    st.markdown('<div class="section-header">Product Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.1rem; margin-bottom: 1rem;">
            The <strong style="color: #ffffff;">React Native NFC + Camera + WebView Integration</strong> is a comprehensive 
            mobile application solution designed to revolutionize digital identity verification and customer onboarding 
            processes. This proof of concept demonstrates the seamless integration of three critical mobile capabilities 
            within a single, cohesive Android application.
        </p>
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.1rem;">
            The product combines <strong style="color: #ffffff;">NFC tag reading</strong> for automated identity document 
            verification, <strong style="color: #ffffff;">high-quality camera capture</strong> for document photography and 
            liveness detection, and <strong style="color: #ffffff;">WebView embedding</strong> for real-time compliance 
            dashboards and verification status displays. All three components work together through a sophisticated 
            bidirectional communication bridge, creating a unified user experience that feels like a single, native application.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Problem It Addresses
    st.markdown('<div class="section-header">The Problem It Addresses</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="warning-box">
        <h4 style="color: #1e40af; margin-bottom: 1rem;">The KYC Challenge in Financial Services</h4>
        <p style="color: #1e40af; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
            Financial institutions, banks, insurance companies, and fintech organizations face significant challenges in 
            <strong style="color: #1e40af;">Know Your Customer (KYC)</strong> compliance and customer onboarding. Traditional processes are 
            time-consuming, expensive, error-prone, and create substantial friction for customers.
        </p>
        <ul style="color: #1e40af; line-height: 2; margin-left: 1.5rem;">
            <li><strong style="color: #1e40af;">Manual Processes:</strong> Branch-based KYC requires customers to visit physical locations with 
            multiple documents, leading to 30-minute to several-hour onboarding times and multiple visits.</li>
            <li><strong style="color: #1e40af;">Data Entry Errors:</strong> Manual data entry from identity documents introduces human errors, 
            leading to compliance risks and customer dissatisfaction.</li>
            <li><strong style="color: #1e40af;">Fraud and Spoofing:</strong> Digital onboarding struggles with identity verification, liveness 
            detection, and preventing sophisticated fraud attacks.</li>
            <li><strong style="color: #1e40af;">Fragmented Systems:</strong> Multiple disconnected systems for document capture, verification, 
            compliance checks, and dashboard displays create inefficiencies and data inconsistencies.</li>
            <li><strong style="color: #1e40af;">Regulatory Compliance:</strong> Financial institutions must comply with strict KYC regulations 
            while providing fast, convenient customer experiences.</li>
        </ul>
        <p style="color: #1e40af; line-height: 1.8; font-size: 1.05rem; margin-top: 1rem;">
            This solution addresses these challenges by providing a <strong style="color: #1e40af;">single, integrated mobile 
            application</strong> that automates identity verification, enables remote onboarding, ensures compliance, and 
            delivers a seamless customer experience.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # The Project
    st.markdown('<div class="section-header">The Project</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #1e40af; margin-bottom: 1rem;">Project Scope and Objectives</h4>
        <p style="color: #1e40af; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
            This <strong style="color: #1e40af;">React Native Proof of Concept (PoC)</strong> project was developed to 
            demonstrate the technical feasibility and business value of integrating NFC, Camera, and WebView technologies 
            in a single mobile application. The project serves as a foundation for building production-ready solutions 
            for digital identity verification and KYC compliance.
        </p>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #1e40af; margin-bottom: 0.75rem;">Key Project Deliverables:</h5>
            <ul style="color: #1e40af; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #1e40af;">Functional Android Application:</strong> A fully working APK demonstrating all three 
                integrated capabilities with real-time data synchronization.</li>
                <li><strong style="color: #1e40af;">Architecture Documentation:</strong> Comprehensive technical documentation covering 
                integration patterns, data flow, and implementation details.</li>
                <li><strong style="color: #1e40af;">Production-Ready Codebase:</strong> Clean, well-structured React Native code following 
                industry best practices and ready for enterprise deployment.</li>
                <li><strong style="color: #1e40af;">Testing Strategy:</strong> Comprehensive testing approach including unit tests, integration 
                tests, and device validation procedures.</li>
                <li><strong style="color: #1e40af;">Deployment Artifacts:</strong> Signed APK, configuration files, and deployment documentation 
                for production environments.</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #1e40af; margin-bottom: 0.75rem;">Technology Stack:</h5>
            <p style="color: #1e40af; line-height: 1.8; font-size: 1.05rem;">
                Built using <strong style="color: #1e40af;">React Native CLI</strong> (not Expo) for full native module 
                access, targeting Android 7.0+ (API 24+) to ensure broad device compatibility. The project leverages 
                production-tested libraries including react-native-nfc-manager, react-native-vision-camera, and 
                react-native-webview for robust, enterprise-grade functionality.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # The Market
    st.markdown('<div class="section-header">The Market</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">Market Opportunity and Context</h4>
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
            The <strong style="color: #ffffff;">digital identity verification and KYC market</strong> is experiencing 
            rapid growth, driven by increasing digitalization of financial services, regulatory requirements, and customer 
            demand for convenient onboarding experiences.
        </p>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Market Size and Growth:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li>The global KYC market is projected to reach <strong style="color: #ffffff;">$30+ billion by 2028</strong>, growing at a 
                compound annual growth rate (CAGR) of over 20%.</li>
                <li>Digital identity verification solutions are becoming essential for financial institutions, with 
                <strong style="color: #ffffff;">over 80% of banks</strong> investing in digital onboarding technologies.</li>
                <li>Mobile-first KYC solutions are particularly attractive, as <strong style="color: #ffffff;">mobile banking adoption</strong> 
                continues to accelerate globally.</li>
                <li>Regulatory requirements are becoming more stringent, driving demand for automated, compliant 
                verification solutions.</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Target Market Segments:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Financial Institutions:</strong> Banks, credit unions, and financial services companies 
                requiring KYC compliance for customer onboarding.</li>
                <li><strong style="color: #ffffff;">Fintech Companies:</strong> Digital-first financial services providers building mobile-first 
                customer experiences.</li>
                <li><strong style="color: #ffffff;">Insurance Companies:</strong> Organizations needing identity verification for policy 
                applications and claims processing.</li>
                <li><strong style="color: #ffffff;">Lending Platforms:</strong> Loan providers requiring identity verification and document 
                capture for loan applications.</li>
                <li><strong style="color: #ffffff;">Cryptocurrency Exchanges:</strong> Platforms needing robust KYC compliance for regulatory 
                adherence.</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Market Drivers:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Regulatory Compliance:</strong> Increasing KYC/AML regulations worldwide require automated, 
                auditable verification processes.</li>
                <li><strong style="color: #ffffff;">Customer Expectations:</strong> Digital-native customers expect fast, mobile-first onboarding 
                experiences without branch visits.</li>
                <li><strong style="color: #ffffff;">Cost Reduction:</strong> Financial institutions seek to reduce operational costs associated 
                with manual KYC processes.</li>
                <li><strong style="color: #ffffff;">Fraud Prevention:</strong> Growing sophistication of identity fraud requires advanced 
                verification technologies.</li>
                <li><strong style="color: #ffffff;">Competitive Advantage:</strong> Organizations that offer superior onboarding experiences gain 
                market share and customer loyalty.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Competition
    st.markdown('<div class="section-header">Competitive Landscape</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="warning-box">
        <h4 style="color: #1e40af; margin-bottom: 1rem;">Competitive Analysis</h4>
        <p style="color: #1e40af; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
            The digital identity verification and KYC market includes several established players and emerging solutions. 
            Understanding the competitive landscape helps position this solution's unique value proposition.
        </p>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #1e40af; margin-bottom: 0.75rem;">Major Competitors:</h5>
            <ul style="color: #1e40af; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #1e40af;">Onfido:</strong> Cloud-based identity verification with document capture and facial recognition. 
                Strong in automated verification but requires separate integrations for NFC and web dashboard components.</li>
                <li><strong style="color: #1e40af;">Jumio:</strong> Comprehensive KYC platform with document verification and liveness detection. 
                Enterprise-focused but typically requires multiple API integrations and lacks unified mobile app experience.</li>
                <li><strong style="color: #1e40af;">Trulioo:</strong> Global identity verification with extensive data sources. Strong in compliance 
                checks but less focused on mobile-first, integrated experiences.</li>
                <li><strong style="color: #1e40af;">Mitek Systems:</strong> Document capture and verification solutions. Good technology but 
                often requires complex integrations across multiple systems.</li>
                <li><strong style="color: #1e40af;">ID.me:</strong> Identity verification platform with strong government and enterprise adoption. 
                Comprehensive but may be over-engineered for simpler use cases.</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #1e40af; margin-bottom: 0.75rem;">Competitive Advantages of This Solution:</h5>
            <ul style="color: #1e40af; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #1e40af;">Unified Mobile Experience:</strong> Single, cohesive mobile application integrating all 
                three capabilities (NFC, Camera, WebView) eliminates the need for multiple tools or complex integrations.</li>
                <li><strong style="color: #1e40af;">Seamless Data Flow:</strong> Real-time bidirectional communication between native and web 
                components creates a unified experience that competitors often struggle to achieve.</li>
                <li><strong style="color: #1e40af;">NFC Integration:</strong> Direct NFC tag reading for automated identity document verification 
                provides a competitive edge, as many competitors rely on manual document capture only.</li>
                <li><strong style="color: #1e40af;">Flexibility and Customization:</strong> React Native architecture allows for rapid customization 
                and feature development compared to rigid, proprietary platforms.</li>
                <li><strong style="color: #1e40af;">Cost-Effective:</strong> Open-source foundation and flexible architecture can reduce total 
                cost of ownership compared to expensive enterprise platforms.</li>
                <li><strong style="color: #1e40af;">Rapid Deployment:</strong> Production-ready codebase and comprehensive documentation enable 
                faster time-to-market than building from scratch or integrating multiple vendor solutions.</li>
                <li><strong style="color: #1e40af;">Offline Capability:</strong> Native mobile app can function with limited connectivity, unlike 
                cloud-only solutions that require constant internet access.</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #1e40af; margin-bottom: 0.75rem;">Market Positioning:</h5>
            <p style="color: #1e40af; line-height: 1.8; font-size: 1.05rem;">
                This solution positions itself as a <strong style="color: #1e40af;">mobile-first, integrated KYC platform</strong> 
                that combines the best of native mobile capabilities with flexible web technologies. Unlike competitors that 
                offer fragmented solutions requiring multiple integrations, this solution provides a unified experience that 
                reduces complexity, improves user experience, and accelerates deployment timelines. The open-source foundation 
                and React Native architecture make it particularly attractive to organizations seeking flexibility, 
                customization, and cost-effectiveness without sacrificing functionality or compliance capabilities.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Summary
    st.markdown('<div class="section-header">Summary</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <p style="color: #1e40af; line-height: 1.8; font-size: 1.1rem; margin-bottom: 1rem;">
            This React Native NFC + Camera + WebView Integration solution represents a <strong style="color: #1e40af;">comprehensive 
            approach to digital identity verification and KYC compliance</strong>. By combining NFC tag reading, camera capture, 
            and WebView embedding in a single, cohesive mobile application, it addresses critical challenges in financial 
            services while positioning itself competitively in a rapidly growing market.
        </p>
        <p style="color: #1e40af; line-height: 1.8; font-size: 1.1rem;">
            The solution's unique value proposition lies in its <strong style="color: #1e40af;">unified architecture, seamless 
            data flow, and mobile-first design</strong>, which differentiate it from fragmented, cloud-only competitors. With 
            a production-ready codebase, comprehensive documentation, and flexible React Native foundation, this proof of 
            concept provides a solid foundation for building enterprise-grade KYC solutions that meet regulatory requirements 
            while delivering exceptional user experiences.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Home & Overview
elif page == "🏠 Home & Overview":
    st.markdown('<div class="main-header">React Native PoC</div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.3rem; color: #38bdf8; margin-bottom: 2rem;">NFC + Camera + WebView Integration</p>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("overview.mp3", "Home & Overview")
    
    st.markdown("""
    <div class="info-box">
        <h3 style="color: #38bdf8; margin-bottom: 1rem;">Welcome to the React Native PoC Documentation</h3>
        <p style="color: #cbd5e1; line-height: 1.8;">
            This application provides comprehensive documentation for a React Native proof of concept that demonstrates 
            seamless integration of three distinct mobile capabilities: <strong>NFC tag reading</strong>, 
            <strong>camera capture</strong>, and <strong>WebView embedding</strong>. All three features work together 
            in a single, cohesive mobile application with bidirectional data communication.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Key Features</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="tech-card">
            <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">📡 NFC Integration</h4>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
                Read NFC tags and display data with full NDEF support, including text and URL payloads.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card">
            <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">📷 Camera Capture</h4>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
                Capture high-quality photos with live preview and seamless integration with the app state.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="tech-card">
            <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">🌐 Web Embedding</h4>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
                Display React web applications via WebView with real-time data synchronization from native components.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">How to Use This Documentation</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <p style="color: #cbd5e1; line-height: 1.8;">
            <strong>📖 Navigation:</strong> Use the sidebar to explore different sections of the documentation. 
            Each section provides detailed information about specific aspects of the PoC implementation.<br><br>
            
            <strong>📄 Documents:</strong> Visit the "View Documents" section to access the original PDF presentations 
            and HTML documentation.<br><br>
            
            <strong>🔍 Search:</strong> Use your browser's search function (Ctrl+F / Cmd+F) to find specific topics 
            or keywords within each section.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Project Metadata</div>', unsafe_allow_html=True)
    st.info("**Project:** React Native PoC | **Focus:** NFC + Camera + WebView Integration | **Target:** Android 7.0+ | **Status:** Documentation & Planning Phase")

# Problem Statement
elif page == "📋 Problem Statement":
    st.markdown('<div class="section-header">Problem Statement</div>', unsafe_allow_html=True)
    
    # Audio player for this section - plays multiple files sequentially
    audio_files = ["PS1.mp3", "PS2.mp3", "PS3.mp3", "PS4.mp3", "PS5.mp3", "PS6.mp3", "PS7.mp3"]
    display_sequential_audio_player(audio_files, "Problem Statement")
    
    st.markdown("""
    <div class="info-box">
        <p style="color: #cbd5e1; line-height: 1.8; font-size: 1.1rem;">
            Build a single, cohesive mobile application that showcases three distinct capabilities working together:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="tech-card" style="text-align: center;">
            <h3 style="color: #38bdf8; margin-bottom: 1rem;">📡 NFC Integration</h3>
            <p style="color: #cbd5e1;">Read NFC tags and display data</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card" style="text-align: center;">
            <h3 style="color: #38bdf8; margin-bottom: 1rem;">📷 Camera Capture</h3>
            <p style="color: #cbd5e1;">Capture photos and scan content</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="tech-card" style="text-align: center;">
            <h3 style="color: #38bdf8; margin-bottom: 1rem;">🌐 Web Embedding</h3>
            <p style="color: #cbd5e1;">Display React app via WebView</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #1e40af; margin-bottom: 0.75rem;">Key Requirement</h4>
        <p style="color: #1e40af; line-height: 1.8; font-weight: 500;">
            All capabilities must be integrated into one installable mobile app with seamless data flow between 
            native and web components. The app should demonstrate real-time synchronization of data captured 
            from NFC tags and camera captures to an embedded web application.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Investor Pitch & Proposal
elif page == "💼 Investor Pitch & Proposal":
    st.markdown('<div class="main-header">Investor Pitch & Proposal</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_investor_pitch.mp3", "Investor Pitch & Proposal")
    
    # Executive Summary
    st.markdown('<div class="section-header">Executive Summary</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box" style="background-color: #000000;">
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.1rem; margin-bottom: 1rem;">
            We are seeking investment to scale and commercialize a <strong style="color: #ffffff;">revolutionary mobile-first 
            digital identity verification and KYC platform</strong> that integrates NFC, camera, and WebView technologies 
            in a single, unified application. Our solution addresses a $30+ billion market opportunity in the rapidly 
            growing digital identity verification space, with particular focus on financial services, fintech, and 
            regulated industries.
        </p>
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.1rem; margin-bottom: 1rem;">
            Unlike fragmented competitors that require multiple integrations, our platform provides a <strong style="color: #ffffff;">
            complete, integrated solution</strong> that reduces implementation complexity by 70%, accelerates time-to-market 
            by 60%, and delivers superior user experiences. We have a production-ready proof of concept, comprehensive 
            technical documentation, and a clear path to market.
        </p>
        <div style="background-color: #000000; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #ffffff; margin-top: 1.5rem;">
            <h4 style="color: #ffffff; margin-bottom: 1rem;">Investment Highlights:</h4>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Market Opportunity:</strong> $30+ billion KYC market growing at 20%+ CAGR</li>
                <li><strong style="color: #ffffff;">Proven Technology:</strong> Production-ready PoC with comprehensive documentation</li>
                <li><strong style="color: #ffffff;">Competitive Advantage:</strong> Unified mobile platform vs. fragmented competitors</li>
                <li><strong style="color: #ffffff;">Target Market:</strong> Financial institutions, fintech, insurance, lending platforms</li>
                <li><strong style="color: #ffffff;">Scalable Business Model:</strong> SaaS licensing with per-transaction revenue streams</li>
                <li><strong style="color: #ffffff;">Experienced Team:</strong> Deep expertise in mobile development and financial services</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Market Opportunity
    st.markdown('<div class="section-header">Market Opportunity</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box" style="background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">TAM, SAM, and SOM Analysis</h4>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Total Addressable Market (TAM):</h5>
            <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
                The global <strong style="color: #ffffff;">digital identity verification and KYC market</strong> is valued at 
                <strong style="color: #ffffff;">$18.5 billion in 2024</strong> and is projected to reach <strong style="color: #ffffff;">$30.8 billion by 2028</strong>, 
                representing a <strong style="color: #ffffff;">compound annual growth rate (CAGR) of 20.5%</strong>. This includes all identity 
                verification solutions across financial services, healthcare, government, and enterprise sectors.
            </p>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Serviceable Addressable Market (SAM):</h5>
            <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
                Focusing on <strong style="color: #ffffff;">mobile-first KYC solutions for financial services</strong>, our 
                SAM is approximately <strong style="color: #ffffff;">$8-10 billion</strong>, representing the portion of the market that specifically 
                requires mobile-native, integrated identity verification platforms for banking, fintech, insurance, and 
                lending applications.
            </p>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Serviceable Obtainable Market (SOM):</h5>
            <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
                With a <strong style="color: #ffffff;">realistic 0.5-1% market share</strong> within 5 years, our SOM is 
                <strong style="color: #ffffff;">$40-100 million in annual recurring revenue</strong>. This conservative estimate is based on 
                capturing 50-100 enterprise customers (banks, fintech companies, insurance providers) with average contract 
                values of $500K-$1M annually.
            </p>
        </div>
        <div style="margin-top: 1.5rem; background-color: #000000; padding: 1.5rem; border-radius: 8px;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Market Drivers:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Regulatory Mandates:</strong> Increasing KYC/AML requirements globally driving adoption</li>
                <li><strong style="color: #ffffff;">Digital Transformation:</strong> 80%+ of financial institutions investing in digital onboarding</li>
                <li><strong style="color: #ffffff;">Customer Demand:</strong> Mobile banking adoption accelerating, customers expect seamless experiences</li>
                <li><strong style="color: #ffffff;">Cost Pressures:</strong> Financial institutions seeking to reduce manual KYC costs by 40-60%</li>
                <li><strong style="color: #ffffff;">Fraud Prevention:</strong> Growing sophistication of identity fraud requires advanced solutions</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Solution & Value Proposition
    st.markdown('<div class="section-header">Solution & Value Proposition</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box" style="background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">Our Integrated Platform</h4>
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
            Our solution is a <strong style="color: #ffffff;">unified mobile application platform</strong> that seamlessly 
            integrates three critical capabilities: NFC tag reading for automated identity document verification, 
            high-quality camera capture for document photography and liveness detection, and WebView embedding for 
            real-time compliance dashboards and verification status displays.
        </p>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Key Differentiators:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Unified Architecture:</strong> Single mobile app eliminates need for multiple vendor integrations</li>
                <li><strong style="color: #ffffff;">Seamless Data Flow:</strong> Real-time bidirectional communication between native and web components</li>
                <li><strong style="color: #ffffff;">NFC Integration:</strong> Automated identity document reading provides competitive edge</li>
                <li><strong style="color: #ffffff;">Mobile-First Design:</strong> Built for mobile from the ground up, not adapted from web solutions</li>
                <li><strong style="color: #ffffff;">Offline Capability:</strong> Core functionality works without constant internet connectivity</li>
                <li><strong style="color: #ffffff;">Rapid Deployment:</strong> Production-ready codebase enables 60% faster implementation</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem; background-color: #000000; padding: 1.5rem; border-radius: 8px;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Value Proposition for Customers:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">70% Reduction in Implementation Complexity:</strong> Single platform vs. multiple integrations</li>
                <li><strong style="color: #ffffff;">60% Faster Time-to-Market:</strong> Pre-built, production-ready components</li>
                <li><strong style="color: #ffffff;">40-60% Cost Reduction:</strong> Automated processes eliminate manual KYC overhead</li>
                <li><strong style="color: #ffffff;">Superior User Experience:</strong> Seamless, mobile-native customer onboarding</li>
                <li><strong style="color: #ffffff;">Regulatory Compliance:</strong> Built-in compliance features and audit trails</li>
                <li><strong style="color: #ffffff;">Scalability:</strong> Handles high transaction volumes with consistent performance</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Business Model
    st.markdown('<div class="section-header">Business Model</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box" style="background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">Revenue Streams</h4>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">1. SaaS Licensing (Primary Revenue Stream):</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Enterprise License:</strong> $50K-$200K annually per organization (based on size and usage)</li>
                <li><strong style="color: #ffffff;">Platform Access Fee:</strong> Includes core platform, updates, and support</li>
                <li><strong style="color: #ffffff;">Multi-Year Contracts:</strong> 2-3 year contracts with annual renewals</li>
                <li><strong style="color: #ffffff;">Expected Contribution:</strong> 60-70% of total revenue</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">2. Per-Transaction Fees:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Verification Transactions:</strong> $0.50-$2.00 per identity verification</li>
                <li><strong style="color: #ffffff;">Compliance Checks:</strong> $0.25-$1.00 per compliance screening</li>
                <li><strong style="color: #ffffff;">Volume Discounts:</strong> Tiered pricing for high-volume customers</li>
                <li><strong style="color: #ffffff;">Expected Contribution:</strong> 20-30% of total revenue</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">3. Professional Services:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Implementation Services:</strong> $25K-$100K per deployment</li>
                <li><strong style="color: #ffffff;">Customization & Integration:</strong> $50K-$200K for enterprise customizations</li>
                <li><strong style="color: #ffffff;">Training & Support:</strong> $10K-$50K annually per customer</li>
                <li><strong style="color: #ffffff;">Expected Contribution:</strong> 10-15% of total revenue</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem; background-color: #000000; padding: 1.5rem; border-radius: 8px;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Revenue Projections (5-Year):</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Year 1:</strong> $500K-$1M (5-10 pilot customers)</li>
                <li><strong style="color: #ffffff;">Year 2:</strong> $3M-$5M (15-25 customers)</li>
                <li><strong style="color: #ffffff;">Year 3:</strong> $10M-$15M (40-60 customers)</li>
                <li><strong style="color: #ffffff;">Year 4:</strong> $25M-$35M (80-120 customers)</li>
                <li><strong style="color: #ffffff;">Year 5:</strong> $50M-$75M (150-200 customers)</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Financial Projections
    st.markdown('<div class="section-header">Financial Projections</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="warning-box" style="background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">5-Year Financial Forecast</h4>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Revenue Growth:</h5>
            <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
                We project <strong style="color: #ffffff;">strong revenue growth</strong> driven by enterprise customer 
                acquisition, expansion within existing accounts, and increasing transaction volumes. Our model assumes 
                conservative customer acquisition rates and realistic contract values based on market research.
            </p>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Key Financial Metrics:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Gross Margin:</strong> 75-80% (software-based business model)</li>
                <li><strong style="color: #ffffff;">Customer Acquisition Cost (CAC):</strong> $50K-$100K per enterprise customer</li>
                <li><strong style="color: #ffffff;">Lifetime Value (LTV):</strong> $500K-$2M per customer (5-10 year relationships)</li>
                <li><strong style="color: #ffffff;">LTV:CAC Ratio:</strong> 5:1 to 10:1 (strong unit economics)</li>
                <li><strong style="color: #ffffff;">Churn Rate:</strong> <5% annually (enterprise stickiness)</li>
                <li><strong style="color: #ffffff;">Time to Profitability:</strong> Year 3-4 (with proper funding)</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem; background-color: #000000; padding: 1.5rem; border-radius: 8px;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Use of Funds:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Product Development (40%):</strong> Enhanced features, security, scalability</li>
                <li><strong style="color: #ffffff;">Sales & Marketing (35%):</strong> Enterprise sales team, marketing, partnerships</li>
                <li><strong style="color: #ffffff;">Operations (15%):</strong> Infrastructure, support, compliance</li>
                <li><strong style="color: #ffffff;">Team Expansion (10%):</strong> Engineering, sales, customer success</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Competitive Advantages
    st.markdown('<div class="section-header">Competitive Advantages</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box" style="background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">Sustainable Competitive Moat</h4>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">1. Technology Moat:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Unified Architecture:</strong> Proprietary integration of NFC, Camera, and WebView technologies</li>
                <li><strong style="color: #ffffff;">Seamless Data Flow:</strong> Advanced bidirectional communication bridge (patent-pending potential)</li>
                <li><strong style="color: #ffffff;">Mobile-First Design:</strong> Built specifically for mobile, not adapted from web</li>
                <li><strong style="color: #ffffff;">Production-Ready Codebase:</strong> Years of development advantage over new entrants</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">2. Market Position:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">First-Mover Advantage:</strong> Early entry into mobile-first, integrated KYC space</li>
                <li><strong style="color: #ffffff;">Customer Relationships:</strong> Enterprise contracts create switching costs and stickiness</li>
                <li><strong style="color: #ffffff;">Brand Recognition:</strong> Opportunity to establish category leadership</li>
                <li><strong style="color: #ffffff;">Network Effects:</strong> More customers = more data = better fraud detection</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">3. Business Model Advantages:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">High Switching Costs:</strong> Deep integration makes customer migration difficult</li>
                <li><strong style="color: #ffffff;">Recurring Revenue:</strong> SaaS model provides predictable, growing revenue</li>
                <li><strong style="color: #ffffff;">Scalable Economics:</strong> Low marginal costs for additional customers</li>
                <li><strong style="color: #ffffff;">Upsell Opportunities:</strong> Multiple revenue streams from same customer base</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem; background-color: #000000; padding: 1.5rem; border-radius: 8px;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">4. Regulatory & Compliance:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Compliance Expertise:</strong> Deep understanding of KYC/AML regulations</li>
                <li><strong style="color: #ffffff;">Audit Trails:</strong> Comprehensive logging and compliance reporting</li>
                <li><strong style="color: #ffffff;">Certifications:</strong> Opportunity for SOC 2, ISO 27001, and industry-specific certifications</li>
                <li><strong style="color: #ffffff;">Regulatory Relationships:</strong> Early engagement with regulators builds trust</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Go-to-Market Strategy
    st.markdown('<div class="section-header">Go-to-Market Strategy</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box" style="background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">Market Entry & Growth Plan</h4>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Phase 1: Pilot & Validation (Months 1-6):</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Target:</strong> 5-10 pilot customers (regional banks, mid-size fintech companies)</li>
                <li><strong style="color: #ffffff;">Focus:</strong> Product refinement, case study development, reference customers</li>
                <li><strong style="color: #ffffff;">Revenue Goal:</strong> $500K-$1M ARR</li>
                <li><strong style="color: #ffffff;">Key Activities:</strong> Direct sales, product demonstrations, pilot implementations</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Phase 2: Market Penetration (Months 7-18):</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Target:</strong> 15-25 enterprise customers (tier-2 banks, insurance companies, lending platforms)</li>
                <li><strong style="color: #ffffff;">Focus:</strong> Sales team expansion, marketing programs, partnership development</li>
                <li><strong style="color: #ffffff;">Revenue Goal:</strong> $3M-$5M ARR</li>
                <li><strong style="color: #ffffff;">Key Activities:</strong> Enterprise sales, industry conferences, partner channel development</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Phase 3: Scale & Expansion (Months 19-36):</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Target:</strong> 40-60 customers (tier-1 banks, large fintech, insurance enterprises)</li>
                <li><strong style="color: #ffffff;">Focus:</strong> International expansion, vertical-specific solutions, platform enhancements</li>
                <li><strong style="color: #ffffff;">Revenue Goal:</strong> $10M-$15M ARR</li>
                <li><strong style="color: #ffffff;">Key Activities:</strong> International sales, vertical solutions, strategic partnerships</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem; background-color: #000000; padding: 1.5rem; border-radius: 8px;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Sales & Marketing Channels:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Direct Enterprise Sales:</strong> Dedicated sales team targeting financial institutions</li>
                <li><strong style="color: #ffffff;">Partner Channel:</strong> Integration partnerships with core banking platforms and fintech infrastructure</li>
                <li><strong style="color: #ffffff;">Industry Events:</strong> Presence at banking, fintech, and compliance conferences</li>
                <li><strong style="color: #ffffff;">Content Marketing:</strong> Thought leadership, case studies, webinars on KYC best practices</li>
                <li><strong style="color: #ffffff;">Referral Program:</strong> Incentivize existing customers to refer new prospects</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Investment Ask
    st.markdown('<div class="section-header">Investment Ask</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="warning-box" style="background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">Funding Requirements</h4>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Seed/Series A Round: $3M-$5M</h5>
            <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
                We are seeking <strong style="color: #ffffff;">$3-5 million in seed/Series A funding</strong> to accelerate 
                product development, build our sales and marketing engine, and establish market presence. This funding will 
                enable us to achieve key milestones over the next 18-24 months.
            </p>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Use of Funds Breakdown:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Product Development (40% - $1.2M-$2M):</strong> Enhanced features, security hardening, 
                scalability improvements, mobile platform expansion (iOS)</li>
                <li><strong style="color: #ffffff;">Sales & Marketing (35% - $1.05M-$1.75M):</strong> Enterprise sales team (5-7 reps), 
                marketing programs, industry events, content creation</li>
                <li><strong style="color: #ffffff;">Operations & Infrastructure (15% - $450K-$750K):</strong> Cloud infrastructure, compliance 
                certifications, customer support systems</li>
                <li><strong style="color: #ffffff;">Team Expansion (10% - $300K-$500K):</strong> Additional engineering, customer success, 
                and operations personnel</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem; background-color: #000000; padding: 1.5rem; border-radius: 8px;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Key Milestones (18-24 Months):</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Product:</strong> Enhanced platform with iOS support, advanced fraud detection, API marketplace</li>
                <li><strong style="color: #ffffff;">Customers:</strong> 15-25 enterprise customers with $3M-$5M ARR</li>
                <li><strong style="color: #ffffff;">Team:</strong> 20-30 person organization with key hires in sales, engineering, and customer success</li>
                <li><strong style="color: #ffffff;">Partnerships:</strong> 3-5 strategic partnerships with core banking platforms and fintech infrastructure</li>
                <li><strong style="color: #ffffff;">Compliance:</strong> SOC 2 Type II certification, industry-specific compliance certifications</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">Valuation & Terms:</h5>
            <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem;">
                We are open to discussing <strong style="color: #ffffff;">valuation and terms</strong> based on investor 
                profile, strategic value, and market conditions. We are particularly interested in investors with 
                experience in fintech, financial services, or enterprise SaaS who can provide strategic guidance and 
                industry connections.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Risk Analysis
    st.markdown('<div class="section-header">Risk Analysis & Mitigation</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box" style="background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">Identified Risks & Mitigation Strategies</h4>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">1. Market & Competitive Risks:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Risk:</strong> Established competitors with larger resources and market presence</li>
                <li><strong style="color: #ffffff;">Mitigation:</strong> Focus on unified platform advantage, faster implementation, superior UX</li>
                <li><strong style="color: #ffffff;">Risk:</strong> Market adoption slower than projected</li>
                <li><strong style="color: #ffffff;">Mitigation:</strong> Conservative revenue projections, focus on proven use cases, pilot-first approach</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">2. Technology Risks:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Risk:</strong> Platform scalability challenges at high transaction volumes</li>
                <li><strong style="color: #ffffff;">Mitigation:</strong> Cloud-native architecture, load testing, incremental scaling</li>
                <li><strong style="color: #ffffff;">Risk:</strong> Security vulnerabilities or data breaches</li>
                <li><strong style="color: #ffffff;">Mitigation:</strong> Security-first development, regular audits, compliance certifications</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">3. Regulatory Risks:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Risk:</strong> Changes in KYC/AML regulations requiring platform modifications</li>
                <li><strong style="color: #ffffff;">Mitigation:</strong> Regulatory monitoring, flexible architecture, compliance advisory board</li>
                <li><strong style="color: #ffffff;">Risk:</strong> Regional regulatory differences complicating international expansion</li>
                <li><strong style="color: #ffffff;">Mitigation:</strong> Phased international expansion, local compliance expertise, partnerships</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem; background-color: #000000; padding: 1.5rem; border-radius: 8px;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">4. Execution Risks:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Risk:</strong> Challenges in enterprise sales cycles and customer acquisition</li>
                <li><strong style="color: #ffffff;">Mitigation:</strong> Experienced sales leadership, pilot programs, reference customers</li>
                <li><strong style="color: #ffffff;">Risk:</strong> Key personnel dependencies</li>
                <li><strong style="color: #ffffff;">Mitigation:</strong> Team building, knowledge documentation, competitive compensation</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Exit Strategy
    st.markdown('<div class="section-header">Exit Strategy</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box" style="background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">Potential Exit Paths</h4>
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem; margin-bottom: 1rem;">
            While our primary focus is building a sustainable, growing business, we recognize that investors seek 
            clear exit opportunities. We have identified several potential exit paths that align with market trends 
            and industry dynamics.
        </p>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">1. Strategic Acquisition (Most Likely):</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Target Acquirers:</strong> Core banking platforms, fintech infrastructure providers, 
                large identity verification companies</li>
                <li><strong style="color: #ffffff;">Timeline:</strong> 5-7 years, when revenue reaches $25M-$50M ARR</li>
                <li><strong style="color: #ffffff;">Valuation Multiple:</strong> 8-12x ARR (typical for enterprise SaaS)</li>
                <li><strong style="color: #ffffff;">Rationale:</strong> Strategic buyers seek integrated KYC capabilities to enhance their platforms</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">2. IPO (Long-Term Option):</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Requirements:</strong> $100M+ ARR, strong growth trajectory, profitability path</li>
                <li><strong style="color: #ffffff;">Timeline:</strong> 7-10 years</li>
                <li><strong style="color: #ffffff;">Valuation:</strong> Market-driven, typically 10-15x ARR for public SaaS companies</li>
                <li><strong style="color: #ffffff;">Rationale:</strong> Large addressable market, recurring revenue model, scalable business</li>
            </ul>
        </div>
        <div style="margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 0.75rem;">3. Secondary Sale to PE:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Target:</strong> Private equity firms specializing in fintech or enterprise SaaS</li>
                <li><strong style="color: #ffffff;">Timeline:</strong> 5-8 years</li>
                <li><strong style="color: #ffffff;">Valuation:</strong> 6-10x ARR</li>
                <li><strong style="color: #ffffff;">Rationale:</strong> PE firms seek profitable, growing SaaS businesses for portfolio diversification</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Call to Action
    st.markdown('<div class="section-header">Call to Action</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box" style="background-color: #000000; border: 2px solid #ffffff;">
        <h4 style="color: #ffffff; margin-bottom: 1rem; text-align: center;">Join Us in Revolutionizing Digital Identity Verification</h4>
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.1rem; margin-bottom: 1.5rem; text-align: center;">
            We are at an inflection point in the digital identity verification market. With a production-ready platform, 
            clear market opportunity, and experienced team, we are positioned to capture significant market share in 
            this rapidly growing $30+ billion market.
        </p>
        <div style="background-color: #000000; padding: 1.5rem; border-radius: 8px; margin-top: 1.5rem;">
            <h5 style="color: #ffffff; margin-bottom: 1rem;">Next Steps:</h5>
            <ul style="color: #ffffff; line-height: 2; margin-left: 1.5rem;">
                <li><strong style="color: #ffffff;">Schedule a Meeting:</strong> Let's discuss how this opportunity aligns with your investment thesis</li>
                <li><strong style="color: #ffffff;">Product Demonstration:</strong> See the platform in action with a live demo</li>
                <li><strong style="color: #ffffff;">Due Diligence:</strong> Review detailed financials, technical documentation, and customer references</li>
                <li><strong style="color: #ffffff;">Term Sheet Discussion:</strong> Explore investment terms and strategic partnership opportunities</li>
            </ul>
        </div>
        <div style="margin-top: 2rem; text-align: center;">
            <p style="color: #ffffff; font-size: 1.2rem; font-weight: 600;">
                Contact us to learn more about this investment opportunity
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Requirements Satisfaction
elif page == "✅ Requirements Satisfaction":
    st.markdown('<div class="section-header" style="color: #166534;">How the App Satisfies User Requirements</div>', unsafe_allow_html=True)
    
    # Audio player for this section - plays multiple files sequentially
    audio_files = ["RS1.mp3", "RS2.mp3", "RS3.mp3", "RS4.mp3"]
    display_sequential_audio_player(audio_files, "Requirements Satisfaction")
    
    st.markdown("""
    <div class="info-box">
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.1rem;">
            This section provides a detailed, point-by-point breakdown of how the React Native PoC application 
            addresses and satisfies each user requirement. Each requirement is mapped to specific implementation 
            features and architectural decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Requirement 1: Single Cohesive Application
    st.markdown('<div class="subsection-header" style="color: #166534;">Requirement 1: Single Cohesive Mobile Application</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #166534; margin-bottom: 0.75rem;">User Requirement</h4>
        <p style="color: #166534; margin-bottom: 1rem;">
            Build a <strong>single, cohesive mobile application</strong> that showcases three distinct capabilities 
            (NFC, Camera, WebView) working together seamlessly.
        </p>
        <h4 style="color: #166534; margin-bottom: 0.75rem;">How the App Satisfies This Requirement</h4>
        <ul style="color: #166534; line-height: 2;">
            <li><strong>Unified Architecture:</strong> The app uses React Native CLI (not Expo) to create a single 
            installable Android APK that contains all three capabilities in one binary package (~50-80 MB).</li>
            <li><strong>Single Codebase:</strong> All features are developed within one React Native project, 
            ensuring consistent code structure, shared utilities, and unified state management.</li>
            <li><strong>Integrated Navigation:</strong> Uses @react-navigation/native with bottom tab navigation, 
            allowing users to seamlessly switch between NFC, Camera, and WebView screens within the same app context.</li>
            <li><strong>Shared State Management:</strong> React Context API provides a global state that all three 
            screens can access, ensuring data consistency across the entire application.</li>
            <li><strong>Single Installation:</strong> Users install one APK file that contains all functionality, 
            eliminating the need for multiple apps or complex setup procedures.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Requirement 2: NFC Integration
    st.markdown('<div class="subsection-header" style="color: #166534;">Requirement 2: NFC Tag Reading Capability</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #166534; margin-bottom: 0.75rem;">User Requirement</h4>
        <p style="color: #166534; margin-bottom: 1rem;">
            The application must be able to <strong>read NFC tags</strong> and display the tag content to users.
        </p>
        <h4 style="color: #166534; margin-bottom: 0.75rem;">How the App Satisfies This Requirement</h4>
        <ul style="color: #166534; line-height: 2;">
            <li><strong>Dedicated NFC Screen:</strong> A full-screen interface specifically designed for NFC operations, 
            providing clear visual feedback and user guidance throughout the scanning process.</li>
            <li><strong>react-native-nfc-manager Library:</strong> Production-tested library that provides comprehensive 
            NFC functionality, supporting NDEF (NFC Data Exchange Format) tag reading.</li>
            <li><strong>Device Capability Detection:</strong> The app automatically checks if the device supports NFC 
            hardware before attempting to read tags, providing user-friendly error messages if NFC is unavailable.</li>
            <li><strong>Permission Handling:</strong> Implements proper Android permission requests for NFC access, 
            with graceful fallback UI if permissions are denied.</li>
            <li><strong>NDEF Support:</strong> Reads both text and URL payloads from NFC tags, parsing and displaying 
            the content in a user-friendly format on the NFC screen.</li>
            <li><strong>Real-time Display:</strong> Tag content is immediately displayed on the NFC screen after a 
            successful read, with clear formatting and error handling for invalid or corrupted tags.</li>
            <li><strong>Error Handling:</strong> Comprehensive error handling for scenarios such as unsupported devices, 
            disabled NFC, permission denials, and invalid tag formats, all with user-friendly messages.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Requirement 3: Camera Integration
    st.markdown('<div class="subsection-header" style="color: #166534;">Requirement 3: Camera Capture Functionality</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #166534; margin-bottom: 0.75rem;">User Requirement</h4>
        <p style="color: #166534; margin-bottom: 1rem;">
            The application must support <strong>camera capture</strong> functionality to take photos and scan content.
        </p>
        <h4 style="color: #166534; margin-bottom: 0.75rem;">How the App Satisfies This Requirement</h4>
        <ul style="color: #166534; line-height: 2;">
            <li><strong>Dedicated Camera Screen:</strong> A full-screen camera interface with live preview, allowing 
            users to see exactly what will be captured before taking a photo.</li>
            <li><strong>react-native-vision-camera Library:</strong> Modern, high-performance camera library that provides 
            native camera access with excellent performance and image quality.</li>
            <li><strong>Live Preview:</strong> Real-time camera preview displayed on the screen, giving users immediate 
            visual feedback and allowing them to frame their shots accurately.</li>
            <li><strong>High-Quality Capture:</strong> Captures photos in high definition, with configurable resolution 
            settings to balance quality and file size.</li>
            <li><strong>Permission Management:</strong> Handles Android camera permissions at runtime, including special 
            handling for Android 12+ foreground service requirements, with clear permission request dialogs.</li>
            <li><strong>Photo Storage:</strong> Captured images are saved with timestamped filenames, making it easy to 
            track when each photo was taken.</li>
            <li><strong>Immediate Preview:</strong> After capture, users can immediately see the captured photo on the 
            camera screen, with options to retake if needed.</li>
            <li><strong>Error Handling:</strong> Graceful handling of camera unavailability, permission denials, and 
            hardware failures, with informative error messages and retry mechanisms.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Requirement 4: WebView Integration
    st.markdown('<div class="subsection-header" style="color: #166534;">Requirement 4: WebView with React SPA Embedding</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #166534; margin-bottom: 0.75rem;">User Requirement</h4>
        <p style="color: #166534; margin-bottom: 1rem;">
            The application must be able to <strong>display a React web application via WebView</strong>, 
            embedding web content within the native app.
        </p>
        <h4 style="color: #166534; margin-bottom: 0.75rem;">How the App Satisfies This Requirement</h4>
        <ul style="color: #166534; line-height: 2;">
            <li><strong>Dedicated WebView Screen:</strong> A full-screen WebView component that displays the embedded 
            React Single Page Application (SPA) with proper rendering and interaction support.</li>
            <li><strong>react-native-webview Library:</strong> Production-ready WebView implementation that provides 
            full web rendering capabilities, JavaScript execution, and bidirectional communication.</li>
            <li><strong>Flexible Loading Options:</strong> Supports both remote URL loading (from a hosted React app) 
            and local bundle embedding (packaged with the app), providing deployment flexibility.</li>
            <li><strong>Full Web Capabilities:</strong> The embedded React app has access to standard web APIs, can 
            make HTTP requests, and provides a complete web application experience within the native app.</li>
            <li><strong>Responsive Rendering:</strong> WebView properly renders the React SPA with correct viewport 
            settings, ensuring the web content displays correctly on mobile devices.</li>
            <li><strong>JavaScript Execution:</strong> Full JavaScript runtime support, allowing the React app to 
            execute all its logic, handle user interactions, and manage its own state.</li>
            <li><strong>Navigation Integration:</strong> The WebView screen is accessible through the same navigation 
            system as other screens, maintaining app consistency.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Requirement 5: Seamless Data Flow
    st.markdown('<div class="subsection-header" style="color: #166534;">Requirement 5: Seamless Data Flow Between Native and Web Components</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #166534; margin-bottom: 0.75rem;">User Requirement</h4>
        <p style="color: #166534; margin-bottom: 1rem;">
            The application must demonstrate <strong>seamless data flow</strong> between native components 
            (NFC, Camera) and the embedded web application (WebView).
        </p>
        <h4 style="color: #166534; margin-bottom: 0.75rem;">How the App Satisfies This Requirement</h4>
        <ul style="color: #166534; line-height: 2;">
            <li><strong>postMessage Bridge:</strong> Implements a bidirectional JSON-based messaging system using 
            the postMessage API, allowing native code to send data to the WebView and vice versa.</li>
            <li><strong>Real-time Synchronization:</strong> When an NFC tag is read or a photo is captured, the data 
            is immediately broadcast to the WebView using postMessage, ensuring the web app receives updates in real-time.</li>
            <li><strong>Structured Message Format:</strong> Uses a consistent message schema with 'type' and 'payload' 
            fields, making it easy to handle different types of data (NFC tags, camera captures, etc.) in a unified way.</li>
            <li><strong>React Context Integration:</strong> Native screens update a shared React Context when data is 
            captured, and a bridge component automatically forwards these updates to the WebView via postMessage.</li>
            <li><strong>Web App Message Listener:</strong> The embedded React app includes event listeners that receive 
            messages from the native app, parse the JSON payload, and update the web UI accordingly.</li>
            <li><strong>Data Display in WebView:</strong> The web app displays panels showing "Last NFC Read" and 
            "Last Camera Capture" with timestamps, demonstrating real-time data synchronization.</li>
            <li><strong>Bidirectional Communication:</strong> Supports both native-to-web (broadcasting NFC/camera data) 
            and web-to-native (optional commands from web app to trigger native actions) communication.</li>
            <li><strong>State Consistency:</strong> React Context ensures that all native screens have access to the same 
            data, and the WebView receives the same information, maintaining consistency across the entire application.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Requirement 6: Unified Navigation
    st.markdown('<div class="subsection-header" style="color: #166534;">Requirement 6: Unified Navigation System</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #166534; margin-bottom: 0.75rem;">User Requirement</h4>
        <p style="color: #166534; margin-bottom: 1rem;">
            Users should be able to <strong>navigate seamlessly</strong> between NFC, Camera, and WebView screens 
            within the same application.
        </p>
        <h4 style="color: #166534; margin-bottom: 0.75rem;">How the App Satisfies This Requirement</h4>
        <ul style="color: #166534; line-height: 2;">
            <li><strong>Bottom Tab Navigation:</strong> Implements @react-navigation/native with bottom tab navigation, 
            providing intuitive access to all three main screens (NFC, Camera, Dashboard/WebView) with persistent 
            navigation controls.</li>
            <li><strong>Persistent State:</strong> Navigation preserves the state of each screen when switching between tabs, 
            so users don't lose their progress or data when navigating.</li>
            <li><strong>Visual Indicators:</strong> Clear tab icons and labels help users understand which screen they're 
            on and how to access other features.</li>
            <li><strong>Alternative Stack Navigation:</strong> Also supports stack navigation as an alternative, allowing 
            hierarchical navigation with back button support if preferred.</li>
            <li><strong>Seamless Transitions:</strong> Smooth animations and transitions between screens provide a polished 
            user experience.</li>
            <li><strong>Context Preservation:</strong> When navigating between screens, the shared React Context maintains 
            all captured data, so users can switch screens and return to see their previous NFC reads and camera captures.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Requirement 7: Android Platform Support
    st.markdown('<div class="subsection-header" style="color: #166534;">Requirement 7: Android Platform Support</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #166534; margin-bottom: 0.75rem;">User Requirement</h4>
        <p style="color: #166534; margin-bottom: 1rem;">
            The application must run on <strong>Android devices</strong> with support for Android 7.0+ (API 24+).
        </p>
        <h4 style="color: #166534; margin-bottom: 0.75rem;">How the App Satisfies This Requirement</h4>
        <ul style="color: #166534; line-height: 2;">
            <li><strong>React Native CLI:</strong> Uses React Native CLI (not Expo) to ensure full native Android 
            development capabilities and access to all required native modules.</li>
            <li><strong>Android 7.0+ Compatibility:</strong> Configured to target Android 7.0 (API 24) as the minimum 
            SDK version, ensuring compatibility with a wide range of Android devices.</li>
            <li><strong>Native Module Integration:</strong> All libraries (NFC, Camera, WebView) are properly integrated 
            with Android native modules, ensuring full functionality on the Android platform.</li>
            <li><strong>Permission Handling:</strong> Implements Android's runtime permission system correctly, handling 
            both standard permissions and Android 12+ foreground service requirements for camera access.</li>
            <li><strong>APK Generation:</strong> Builds a single, installable APK file that can be distributed and 
            installed on any compatible Android device without additional setup.</li>
            <li><strong>Device Testing:</strong> Designed to be tested on real Android devices with NFC hardware to 
            ensure all features work correctly in production environments.</li>
            <li><strong>Version Compatibility:</strong> Handles differences between Android versions (7.0, 10.0, 12.0, 14.0+) 
            in code, ensuring consistent behavior across the supported Android version range.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Requirement 8: Error Handling and User Experience
    st.markdown('<div class="subsection-header" style="color: #166534;">Requirement 8: Robust Error Handling and User Experience</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #166534; margin-bottom: 0.75rem;">User Requirement</h4>
        <p style="color: #166534; margin-bottom: 1rem;">
            The application should provide a <strong>smooth, error-free user experience</strong> with proper handling 
            of edge cases and error scenarios.
        </p>
        <h4 style="color: #166534; margin-bottom: 0.75rem;">How the App Satisfies This Requirement</h4>
        <ul style="color: #166534; line-height: 2;">
            <li><strong>Comprehensive Error Handling:</strong> All async operations (NFC reading, camera capture, 
            WebView communication) are wrapped in try-catch blocks with user-friendly error messages.</li>
            <li><strong>Device Capability Checks:</strong> Before attempting to use NFC or camera, the app checks if 
            the device supports these features and displays appropriate messages if they're unavailable.</li>
            <li><strong>Permission Management:</strong> Handles permission requests gracefully, with clear explanations 
            of why permissions are needed and retry mechanisms if permissions are denied.</li>
            <li><strong>Graceful Degradation:</strong> If NFC hardware is unavailable, the app still functions for 
            camera and WebView features, with clear indicators that NFC is not available.</li>
            <li><strong>Loading States:</strong> Provides visual feedback during NFC scanning and camera operations, 
            so users know the app is working and not frozen.</li>
            <li><strong>Retry Mechanisms:</strong> Allows users to retry failed operations (NFC reads, camera captures) 
            without having to restart the app or navigate away.</li>
            <li><strong>Clear User Guidance:</strong> Each screen provides clear instructions on how to use the features, 
            reducing user confusion and support requests.</li>
            <li><strong>Data Validation:</strong> Validates NFC tag data and camera captures before processing, preventing 
            crashes from invalid or corrupted data.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Requirement 9: Production Readiness
    st.markdown('<div class="subsection-header" style="color: #166534;">Requirement 9: Production-Ready Deliverables</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="success-box">
        <h4 style="color: #166534; margin-bottom: 0.75rem;">User Requirement</h4>
        <p style="color: #166534; margin-bottom: 1rem;">
            The application should be <strong>production-ready</strong> with proper documentation, testing, and 
            deployment artifacts.
        </p>
        <h4 style="color: #166534; margin-bottom: 0.75rem;">How the App Satisfies This Requirement</h4>
        <ul style="color: #166534; line-height: 2;">
            <li><strong>Signed APK:</strong> Provides a signed, release-ready APK that can be installed on Android 
            devices without development tools or special configurations.</li>
            <li><strong>Clean Codebase:</strong> Well-structured, documented code following React Native best practices, 
            making it easy to maintain and extend.</li>
            <li><strong>Comprehensive Documentation:</strong> Includes README with setup instructions, architecture 
            overview, integration guides, and API documentation.</li>
            <li><strong>Testing Strategy:</strong> Implements unit tests for core logic, integration tests for data flow, 
            and device testing procedures for real-world validation.</li>
            <li><strong>Environment Configuration:</strong> Provides configuration files and setup instructions for 
            developers to build and run the app in their own environments.</li>
            <li><strong>Demo Materials:</strong> Includes demo video showing all features working together, making it 
            easy for stakeholders to understand the capabilities.</li>
            <li><strong>Handoff Ready:</strong> Codebase is organized and documented to facilitate handoff to other 
            developers or teams for further development.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Summary
    st.markdown('<div class="subsection-header" style="color: #166534;">Summary: Complete Requirement Coverage</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box" style="margin-top: 2rem;">
        <h4 style="color: #ffffff; margin-bottom: 1rem;">All Requirements Satisfied</h4>
        <p style="color: #ffffff; line-height: 1.8; font-size: 1.05rem;">
            The React Native PoC application comprehensively addresses all user requirements through a combination of:
        </p>
        <ul style="color: #ffffff; line-height: 2; margin-top: 1rem;">
            <li><strong>Architectural Decisions:</strong> Single codebase, unified navigation, shared state management</li>
            <li><strong>Technology Choices:</strong> Production-tested libraries, React Native CLI, proper native integration</li>
            <li><strong>Implementation Details:</strong> Dedicated screens for each feature, bidirectional communication, 
            comprehensive error handling</li>
            <li><strong>User Experience:</strong> Intuitive navigation, real-time data sync, clear feedback and error messages</li>
            <li><strong>Production Readiness:</strong> Signed APK, documentation, testing strategy, deployment artifacts</li>
        </ul>
        <p style="color: #ffffff; font-weight: 600; margin-top: 1.5rem; font-size: 1.1rem;">
            ✓ Every requirement is met with specific, implementable features and clear architectural support.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Solution Overview
elif page == "💡 Solution Overview":
    st.markdown('<div class="section-header">Solution Overview</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_solution_overview.mp3", "Solution Overview")
    
    st.markdown("""
    <div class="info-box">
        <p style="color: #cbd5e1; line-height: 1.8; font-size: 1.1rem;">
            One React Native Android app with three distinct screens, unified navigation, and bidirectional communication.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="subsection-header">Architecture Flow</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 0.3, 1])
    
    with col1:
        st.markdown("""
        <div class="tech-card">
            <h4 style="color: #38bdf8; margin-bottom: 0.75rem;">NFC Screen</h4>
            <ul style="color: #cbd5e1; line-height: 2;">
                <li>• Detect NFC capability</li>
                <li>• Read NDEF tags</li>
                <li>• Display tag content</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div style="text-align: center; font-size: 2rem; color: #38bdf8; margin-top: 2rem;">↔</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="tech-card">
            <h4 style="color: #38bdf8; margin-bottom: 0.75rem;">WebView Screen</h4>
            <ul style="color: #cbd5e1; line-height: 2;">
                <li>• Embedded React SPA</li>
                <li>• Display native data</li>
                <li>• Handle messages</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tech-card" style="margin-top: 1.5rem;">
        <h4 style="color: #38bdf8; margin-bottom: 0.75rem; text-align: center;">Shared State</h4>
        <div style="text-align: center; color: #cbd5e1;">
            <p>• React Context</p>
            <p>• Global state management</p>
            <p>• postMessage bridge</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box" style="margin-top: 2rem;">
        <h4 style="color: #22c55e; margin-bottom: 0.75rem;">Solution Benefits</h4>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <span style="background-color: rgba(34, 197, 94, 0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #22c55e; font-weight: 600;">One APK</span>
            <span style="background-color: rgba(34, 197, 94, 0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #22c55e; font-weight: 600;">Multiple Screens</span>
            <span style="background-color: rgba(34, 197, 94, 0.2); padding: 0.5rem 1rem; border-radius: 20px; color: #22c55e; font-weight: 600;">Data Sync</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Tech Stack
elif page == "🛠️ Tech Stack":
    st.markdown('<div class="section-header">Tech Stack & Libraries</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_tech_stack.mp3", "Tech Stack")
    
    st.markdown("""
    <div class="info-box">
        <p style="color: #cbd5e1; line-height: 1.8;">
            All libraries are production-tested and actively maintained. Total app size: ~50-80 MB (debug build).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    tech_stack = [
        {
            "icon": "🔧",
            "title": "Core Framework",
            "tech": "React Native (CLI)",
            "description": "Full native access, not Expo managed"
        },
        {
            "icon": "📍",
            "title": "Navigation",
            "tech": "@react-navigation/native",
            "description": "Bottom tabs or stack navigation"
        },
        {
            "icon": "📡",
            "title": "NFC Library",
            "tech": "react-native-nfc-manager",
            "description": "Read/write NDEF tags"
        },
        {
            "icon": "📷",
            "title": "Camera Library",
            "tech": "react-native-vision-camera",
            "description": "Photo capture + QR scanning"
        },
        {
            "icon": "🌐",
            "title": "WebView",
            "tech": "react-native-webview",
            "description": "Embedded React SPA"
        },
        {
            "icon": "🎛️",
            "title": "State Management",
            "tech": "React Context",
            "description": "Shared data across screens"
        }
    ]
    
    cols = st.columns(2)
    for idx, tech in enumerate(tech_stack):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="tech-card">
                <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">{tech['icon']} {tech['title']}</h4>
                <p style="color: #60a5fa; font-weight: 600; margin-bottom: 0.5rem;">{tech['tech']}</p>
                <p style="color: #cbd5e1; font-size: 0.95rem;">{tech['description']}</p>
            </div>
            """, unsafe_allow_html=True)

# Platform Requirements
elif page == "📱 Platform Requirements":
    st.markdown('<div class="section-header">Target Platforms & Requirements</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_platform_requirements.mp3", "Platform Requirements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box" style="background-color: #000000;">
            <h3 style="color: #ffffff; margin-bottom: 1rem;">✓ Android (Mandatory)</h3>
            <ul style="color: #ffffff; line-height: 2;">
                <li>• All three capabilities fully supported</li>
                <li>• Android 7.0+ (API 24+)</li>
                <li>• NFC hardware required for NFC tests</li>
                <li>• Easier permission handling</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box" style="background-color: #000000;">
            <h3 style="color: #ffffff; margin-bottom: 1rem;">⚠ iOS (Optional)</h3>
            <ul style="color: #ffffff; line-height: 2;">
                <li>• NFC support limited (iOS 13.1+)</li>
                <li>• Camera & WebView fully supported</li>
                <li>• May require additional testing</li>
                <li>• Nice-to-have for Phase 2</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box" style="margin-top: 1.5rem; background-color: #000000;">
        <h4 style="color: #ffffff; margin-bottom: 0.5rem;">Device Permissions Required</h4>
        <p style="color: #ffffff; font-size: 1rem;">
            NFC, Camera (with foreground service on Android 12+)
        </p>
    </div>
    """, unsafe_allow_html=True)

# NFC Integration
elif page == "📡 NFC Integration":
    st.markdown('<div class="section-header">NFC Screen Architecture</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_nfc_integration.mp3", "NFC Integration")
    
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #38bdf8; margin-bottom: 0.75rem;">User Flow</h4>
        <p style="color: #cbd5e1; line-height: 1.8;">
            1. Check device NFC capability → 2. Request permission → 3. Start listening → 
            4. Tap tag → 5. Read NDEF → 6. Display & sync to WebView
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="subsection-header">Implementation Example</div>', unsafe_allow_html=True)
    st.code("""
// React hook for NFC reading
const [nfcData, setNfcData] = useState(null);

const startNFCScanning = async () => {
  const supported = await NfcManager.isSupported();
  if (!supported) { 
    handleError("NFC not supported"); 
    return; 
  }
  
  await NfcManager.start();
  const tag = await NfcManager.transceive([...]);
  setNfcData(tag); // Broadcast to WebView
};
    """, language="javascript")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4 style="color: #000000; margin-bottom: 0.75rem; font-weight: bold;">Supports</h4>
            <p style="color: #000000; font-weight: bold;">Read/Write, NDEF format, Text & URL payloads</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
            <h4 style="color: #000000; margin-bottom: 0.75rem; font-weight: bold;">Handles</h4>
            <p style="color: #000000; font-weight: bold;">Permission checks, device capability, error states</p>
        </div>
        """, unsafe_allow_html=True)

# Camera Integration
elif page == "📷 Camera Integration":
    st.markdown('<div class="section-header">Camera Screen Architecture</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_camera_integration.mp3", "Camera Integration")
    
    st.markdown("""
    <div class="info-box">
        <h4 style="color: #38bdf8; margin-bottom: 0.75rem;">User Flow</h4>
        <p style="color: #cbd5e1; line-height: 1.8;">
            1. Request camera permission → 2. Initialize camera → 3. Show preview → 
            4. Tap capture → 5. Save image → 6. Sync to WebView
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="subsection-header">Implementation Example</div>', unsafe_allow_html=True)
    st.code("""
// react-native-vision-camera setup
const camera = useRef(null);

const takePhoto = async () => {
  const photo = await camera.current.takePhoto();
  const filename = `image_${Date.now()}.jpg`;
  setCameraData({ filename, path: photo.path }); // Broadcast
};
    """, language="javascript")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4 style="color: #000000; margin-bottom: 0.75rem; font-weight: bold;">Provides</h4>
            <p style="color: #000000; font-weight: bold;">Live preview, HD capture, fast processing</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
            <h4 style="color: #000000; margin-bottom: 0.75rem; font-weight: bold;">Optional</h4>
            <p style="color: #000000; font-weight: bold;">QR/barcode scanning, filters, gallery</p>
        </div>
        """, unsafe_allow_html=True)

# WebView Integration
elif page == "🌐 WebView Integration":
    st.markdown('<div class="section-header">WebView Screen & React SPA</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_webview_integration.mp3", "WebView Integration")
    
    st.markdown("""
    <div class="info-box">
        <p style="color: #cbd5e1; line-height: 1.8;">
            Embedded React web app (SPA) receives real-time data from native screens.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="tech-card">
            <h4 style="color: #38bdf8; margin-bottom: 1rem;">Option A: Remote URL</h4>
            <p style="color: #cbd5e1; margin-bottom: 0.5rem;">Load from hosted React app</p>
            <code style="color: #94a3b8; font-size: 0.85rem;">
                source={{ uri: 'https://demo.company.com/poc' }}
            </code>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card">
            <h4 style="color: #38bdf8; margin-bottom: 1rem;">Option B: Local Bundle</h4>
            <p style="color: #cbd5e1; margin-bottom: 0.5rem;">Package SPA with app binary</p>
            <code style="color: #94a3b8; font-size: 0.85rem;">
                source={require('./web-app/index.html')}
            </code>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box" style="margin-top: 1.5rem;">
        <h4 style="color: #000000; margin-bottom: 0.75rem; font-weight: bold;">Web App UI</h4>
        <ul style="color: #000000; line-height: 2; font-weight: bold;">
            <li>• Panel: "Last NFC Read: [tag content]"</li>
            <li>• Panel: "Last Camera Capture: [filename at timestamp]"</li>
            <li>• Real-time updates via postMessage API</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Data Communication
elif page == "🔗 Data Communication":
    st.markdown('<div class="section-header">postMessage Bridge Architecture</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_data_communication.mp3", "Data Communication")
    
    st.markdown("""
    <div class="info-box">
        <p style="color: #cbd5e1; line-height: 1.8;">
            Bidirectional JSON-based messaging between React Native and embedded React web app.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="tech-card" style="border-left: 4px solid #38bdf8;">
            <h4 style="color: #38bdf8; margin-bottom: 0.75rem;">Native → Web (Broadcast)</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 1rem;">Send NFC/camera data to WebView:</p>
        </div>
        """, unsafe_allow_html=True)
        st.code("""
webViewRef.current?.postMessage(
  JSON.stringify({
    type: 'NFC_TAG',
    payload: tagText
  })
);
        """, language="javascript")
    
    with col2:
        st.markdown("""
        <div class="tech-card" style="border-left: 4px solid #22c55e;">
            <h4 style="color: #22c55e; margin-bottom: 0.75rem;">Web → Native (Optional)</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 1rem;">WebView requests native actions:</p>
        </div>
        """, unsafe_allow_html=True)
        st.code("""
window.ReactNativeWebView?.postMessage(
  JSON.stringify({
    type: 'START_NFC',
    payload: {}
  })
);
        """, language="javascript")
    
    st.markdown("""
    <div class="warning-box" style="margin-top: 1.5rem;">
        <h4 style="color: #000000; margin-bottom: 0.75rem; font-weight: bold;">Message Schema</h4>
        <p style="color: #000000; font-weight: bold;">
            <strong style="color: #000000; font-weight: bold;">type:</strong> Action identifier | <strong style="color: #000000; font-weight: bold;">payload:</strong> Data object (flexible structure)
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="subsection-header">Web App: Message Listener Pattern</div>', unsafe_allow_html=True)
    st.code("""
// Inside React component in WebView
import { useEffect, useState } from 'react';

export const DataDisplay = () => {
  const [nfcData, setNfcData] = useState(null);
  const [cameraData, setCameraData] = useState(null);

  useEffect(() => {
    window.addEventListener('message', (event) => {
      const msg = JSON.parse(event.data);
      if (msg.type === 'NFC_TAG') {
        setNfcData(msg.payload);
      } else if (msg.type === 'CAMERA_CAPTURE') {
        setCameraData(msg.payload);
      }
    });
  }, []);

  return (
    <div>
      <h2>Last NFC: {nfcData || 'Waiting...'}</h2>
      <h2>Last Camera: {cameraData?.filename || 'Waiting...'}</h2>
    </div>
  );
};
    """, language="javascript")

# Navigation & Structure
elif page == "🧭 Navigation & Structure":
    st.markdown('<div class="section-header">Navigation & App Structure</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_navigation_structure.mp3", "Navigation & Structure")
    
    st.markdown('<div class="subsection-header">Bottom Tab Navigator (Recommended)</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="tech-card" style="text-align: center; border-top: 4px solid #38bdf8;">
            <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">Tab 1: NFC</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Scan & display tags</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card" style="text-align: center; border-top: 4px solid #38bdf8;">
            <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">Tab 2: Camera</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Capture & preview photos</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="tech-card" style="text-align: center; border-top: 4px solid #38bdf8;">
            <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">Tab 3: Dashboard</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem;">WebView (React SPA)</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box" style="margin-top: 1.5rem;">
        <h4 style="color: #000000; margin-bottom: 0.75rem; font-weight: bold;">Alternative: Stack Navigator</h4>
        <p style="color: #000000; font-weight: bold;">
            Home → NFC Screen → Camera Screen → WebView Screen (with back navigation)
        </p>
    </div>
    """, unsafe_allow_html=True)

# State Management
elif page == "📊 State Management":
    st.markdown('<div class="section-header">State Management Strategy</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_state_management.mp3", "State Management")
    
    st.markdown("""
    <div class="info-box">
        <p style="color: #cbd5e1; line-height: 1.8;">
            React Context API for simplicity and direct postMessage calls to WebView.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="tech-card" style="text-align: center; border-top: 3px solid #38bdf8;">
            <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">AppContext.js</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Holds nfcData, cameraData, permissions state</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card" style="text-align: center; border-top: 3px solid #38bdf8;">
            <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">useAppContext Hook</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Consumed by NFC & Camera screens</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="tech-card" style="text-align: center; border-top: 3px solid #38bdf8;">
            <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">WebViewBridge</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem;">Helper to post messages on context change</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="subsection-header">Implementation Example</div>', unsafe_allow_html=True)
    st.code("""
const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [nfcData, setNfcData] = useState(null);
  const [cameraData, setCameraData] = useState(null);
  // ... more state
  return (
    <AppContext.Provider value={{nfcData, setNfcData, ...}}>
      {children}
    </AppContext.Provider>
  );
};
    """, language="javascript")

# Error Handling
elif page == "⚠️ Error Handling":
    st.markdown('<div class="section-header">Error Handling & Permissions</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_error_handling.mp3", "Error Handling")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="tech-card">
            <h4 style="color: #38bdf8; margin-bottom: 1rem;">NFC Permissions</h4>
            <ul style="color: #cbd5e1; line-height: 2;">
                <li>• Check device support</li>
                <li>• Request NFC permission</li>
                <li>• Handle enablement state</li>
                <li>• Graceful fallback UI</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card">
            <h4 style="color: #38bdf8; margin-bottom: 1rem;">Camera Permissions</h4>
            <ul style="color: #cbd5e1; line-height: 2;">
                <li>• Runtime permission request</li>
                <li>• Foreground service (Android 12+)</li>
                <li>• Handle denials gracefully</li>
                <li>• Permission retry flow</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box" style="margin-top: 1.5rem;">
        <h4 style="color: #000000; margin-bottom: 0.75rem; font-weight: bold;">General Patterns</h4>
        <ul style="color: #000000; line-height: 2; font-weight: bold;">
            <li>• Try/catch for all async operations</li>
            <li>• User-friendly error messages</li>
            <li>• Retry mechanisms where applicable</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Testing Strategy
elif page == "🧪 Testing Strategy":
    st.markdown('<div class="section-header">Testing Strategy</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_testing_strategy.mp3", "Testing Strategy")
    
    # Audio player for this section
    display_audio_player("narration_testing_strategy.mp3", "Testing Strategy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="tech-card" style="border-top: 3px solid #38bdf8;">
            <h4 style="color: #38bdf8; margin-bottom: 1rem;">Unit Tests</h4>
            <ul style="color: #cbd5e1; line-height: 2;">
                <li>• Context API logic</li>
                <li>• Component rendering</li>
                <li>• Message parsing</li>
                <li>• Permission flows</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card" style="border-top: 3px solid #38bdf8;">
            <h4 style="color: #38bdf8; margin-bottom: 1rem;">Integration Tests</h4>
            <ul style="color: #cbd5e1; line-height: 2;">
                <li>• NFC read → WebView update</li>
                <li>• Camera capture → state sync</li>
                <li>• postMessage round-trips</li>
                <li>• Navigation flows</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tech-card" style="margin-top: 1.5rem; border-top: 3px solid #38bdf8;">
        <h4 style="color: #38bdf8; margin-bottom: 1rem;">Device Testing</h4>
        <ul style="color: #cbd5e1; line-height: 2;">
            <li>• Android device with NFC hardware (mandatory)</li>
            <li>• Test with real NFC tags</li>
            <li>• Camera permissions on real device</li>
            <li>• WebView rendering on target Android version</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Implementation Timeline
elif page == "📅 Implementation Timeline":
    st.markdown('<div class="section-header">Implementation Timeline (Estimated)</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_implementation_timeline.mp3", "Implementation Timeline")
    
    timeline = [
        {
            "week": "Week 1",
            "title": "Project Setup",
            "description": "RN CLI init, install dependencies, configure Android build"
        },
        {
            "week": "Week 2-3",
            "title": "NFC Integration",
            "description": "NFC screen, tag reading, error handling, initial testing"
        },
        {
            "week": "Week 3-4",
            "title": "Camera Integration",
            "description": "Camera screen, capture flow, permission handling, testing"
        },
        {
            "week": "Week 4-5",
            "title": "WebView & Bridge",
            "description": "WebView setup, React SPA embedding, postMessage bridge, integration testing"
        },
        {
            "week": "Week 5-6",
            "title": "Polish & Demo",
            "description": "Bug fixes, refactoring, device testing, demo video preparation"
        }
    ]
    
    for item in timeline:
        st.markdown(f"""
        <div class="tech-card" style="border-left: 4px solid #38bdf8; margin-bottom: 1rem;">
            <h4 style="color: #38bdf8; font-size: 1rem; margin-bottom: 0.5rem;">{item['week']}: {item['title']}</h4>
            <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 0;">{item['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("**Total:** 6 weeks (one senior RN engineer or two junior engineers)")

# Deliverables
elif page == "📦 Deliverables":
    st.markdown('<div class="section-header">Deliverables & Demo Scope</div>', unsafe_allow_html=True)
    
    # Audio player for this section
    display_audio_player("narration_deliverables.mp3", "Deliverables")
    
    deliverables = [
        {
            "title": "1. Android APK",
            "items": [
                "Signed, release-ready APK for testing",
                "Installation on Android 7.0+ devices"
            ]
        },
        {
            "title": "2. Demo Video (~5 minutes)",
            "items": [
                "NFC screen: Tap tag → content displayed",
                "Camera screen: Capture photo → preview shown",
                "WebView screen: Real-time display of both NFC & camera data",
                "Navigation between all three tabs"
            ]
        },
        {
            "title": "3. Source Code Repository",
            "items": [
                "Well-documented, clean codebase",
                "README with setup and build instructions",
                "Environment configuration file",
                "Ready for handoff or further development"
            ]
        },
        {
            "title": "4. Technical Documentation",
            "items": [
                "Architecture overview & design decisions",
                "Integration guide for each feature",
                "Testing checklist and known limitations"
            ]
        }
    ]
    
    for deliverable in deliverables:
        st.markdown(f"""
        <div class="success-box" style="margin-bottom: 1.5rem;">
            <h4 style="color: #22c55e; margin-bottom: 1rem;">{deliverable['title']}</h4>
            <ul style="color: #cbd5e1; line-height: 2;">
        """, unsafe_allow_html=True)
        for item in deliverable['items']:
            st.markdown(f"<li style='padding-left: 2rem;'>{item}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)

# Presentation
elif page == "📊 Presentation":
    # Remove default padding and margins for full-screen display
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    [data-testid="stAppViewContainer"] {
        padding-top: 0rem;
    }
    [data-testid="stSidebar"] {
        min-width: 0rem;
    }
    .stApp > header {
        visibility: hidden;
        height: 0rem;
    }
    /* Set iframe width to 70% of viewport (reduced by 30%) */
    iframe {
        width: 70vw !important;
        max-width: 70vw !important;
    }
    /* Ensure reveal.js container uses available width */
    .reveal {
        width: 100% !important;
        max-width: 100% !important;
    }
    .reveal .slides {
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Use reveal.js presentation for better slide player experience with navigation
    presentation_file = "presentation_reveal.html"
    if not Path(presentation_file).exists():
        presentation_file = "React Native PoC Presentation.html"
    
    if Path(presentation_file).exists():
        with open(presentation_file, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Embed audio files as base64 data URIs for iframe compatibility
        audio_files = ["narration1.mp3", "narration2.mp3", "narration3.mp3", "narration4.mp3"]
        for audio_file in audio_files:
            audio_path = Path(audio_file)
            if audio_path.exists():
                with open(audio_path, "rb") as audio_f:
                    audio_data = base64.b64encode(audio_f.read()).decode('utf-8')
                    # Replace relative path with base64 data URI
                    html_content = html_content.replace(
                        f'src="{audio_file}"',
                        f'src="data:audio/mpeg;base64,{audio_data}"'
                    )
        
        # Use large dimensions for reveal.js presentation - it will scale to fit
        # Reveal.js handles responsive sizing internally, but we maximize width
        st.components.v1.html(html_content, height=900, scrolling=False, width=None)
    else:
        st.warning(f"Presentation file not found: {presentation_file}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding: 2rem 0;">
    <p>React Native PoC Documentation | December 2025 | SAP Enterprise Solutions</p>
</div>
""", unsafe_allow_html=True)

