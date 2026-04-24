import os
import fitz  # PyMuPDF
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# 2. Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)

# 3. High-End Custom CSS
def apply_ultra_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono&display=swap');

        /* Background & Overall App Layout */
        .stApp {
            background: radial-gradient(circle at top right, #1e293b, #0f172a);
            color: #f8fafc;
            font-family: 'Inter', sans-serif;
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: rgba(15, 23, 42, 0.8) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Header Title with Gradient */
        .main-title {
            font-size: 4rem;
            font-weight: 800;
            background: linear-gradient(to right, #60a5fa, #a78bfa, #f472b6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            letter-spacing: -2px;
        }

        /* Custom Button */
        .stButton>button {
            background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%);
            color: white;
            border: none;
            padding: 15px 32px;
            border-radius: 12px;
            font-weight: 600;
            transition: 0.3s all ease;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
            width: 100%;
        }

        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6);
            border: none;
            color: white;
        }

        /* Content Cards */
        .custom-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 25px;
            min-height: 450px;
        }

        /* Text Area Styling */
        .stTextArea textarea {
            background-color: rgba(15, 23, 42, 0.5) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: #cbd5e1 !important;
            border-radius: 12px !important;
        }
        </style>
    """, unsafe_allow_html=True)


def extract_file_content(uploaded_file) -> str:
    """Extract plain text from txt, csv, or pdf uploads."""
    if uploaded_file.type == "application/pdf":
        pdf_bytes = uploaded_file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        pages_text = [page.get_text() for page in doc]
        doc.close()
        return "\n\n".join(pages_text)
    else:
        return uploaded_file.read().decode("utf-8")


def summarize_text_stream(text):
    try:
        return client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are BriefMind. Provide an elite, executive-level summary with clear headings and emojis.",
                },
                {"role": "user", "content": f"Summarize this:\n\n{text}"},
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            stream=True,
        )
    except Exception as e:
        st.error(f"Error: {e}")
        return None


def main():
    st.set_page_config(page_title="BriefMind | Next-Gen AI", page_icon="🧠", layout="wide")
    apply_ultra_theme()

    # --- SIDEBAR ---
    with st.sidebar:
        st.markdown("<h2 style='text-align: center; color: #60a5fa;'>🧠 BriefMind</h2>", unsafe_allow_html=True)
        st.markdown("---")
        st.write("🚀 **Engine:** Groq LPU")
        st.write("🤖 **Model:** Llama 3.3 70B")
        st.write("✨ **Mode:** Scalable Stream")
        st.markdown("---")
        st.write("📄 **Supported formats:**")
        st.write("&nbsp;&nbsp;• TXT &nbsp;• CSV &nbsp;• PDF")
        st.markdown("---")
        st.caption("Developed for professional document processing.")

    # --- HERO SECTION ---
    st.markdown("<h1 class='main-title'>BriefMind</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size: 1.2rem; color: #94a3b8;'>Executive document intelligence. Instant. Accurate. Beautiful.</p>",
        unsafe_allow_html=True,
    )
    st.divider()

    # --- UPLOADER SECTION ---
    uploaded_file = st.file_uploader(
        "Drop your file here",
        type=["txt", "csv", "pdf"],
        label_visibility="collapsed",
    )

    if uploaded_file:
        # Extract content based on file type
        with st.spinner("Reading document..."):
            try:
                file_content = extract_file_content(uploaded_file)
            except Exception as e:
                st.error(f"Failed to read file: {e}")
                return

        if not file_content.strip():
            st.warning("The document appears to be empty or could not be parsed.")
            return

        col1, col2 = st.columns([1, 1.2], gap="large")

        with col1:
            st.markdown("#### 📄 Document Input")
            container1 = st.container(border=True)
            with container1:
                st.text_area("input", file_content, height=450, label_visibility="collapsed")

        with col2:
            st.markdown("#### 📝 Intelligence Output")
            container2 = st.container(border=True)
            with container2:
                if st.button("✨ GENERATE INTELLIGENCE"):
                    if not GROQ_API_KEY:
                        st.error("API Key Missing — add GROQ_API_KEY to your .env file.")
                    else:
                        output_area = st.empty()
                        full_response = ""

                        response_stream = summarize_text_stream(file_content)
                        if response_stream:
                            for chunk in response_stream:
                                content = chunk.choices[0].delta.content
                                if content:
                                    full_response += content
                                    output_area.markdown(full_response + " ▎")

                            output_area.markdown(full_response)
                else:
                    st.info("Ready to summarize. Click the button above.")


if __name__ == "__main__":
    main()