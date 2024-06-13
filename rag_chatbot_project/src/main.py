import os
import tempfile
import streamlit as st
from dotenv import load_dotenv  
from embedchain_config import embedchain_bot

load_dotenv()

st.title("Athina AI RAG-based chatbot Task")

openai_access_token = os.getenv("OPENAI_API_KEY")

if openai_access_token:
    db_path = tempfile.mkdtemp()
    app = embedchain_bot(db_path, openai_access_token)

    # Path to the default PDF file
    default_pdf_path = os.path.join('data', 'pdf_documents', 'policy-booklet-0923.pdf')

    # Load default PDF if no file is uploaded
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

    if pdf_file is None:
        st.warning("No PDF uploaded, using default PDF.")
        if os.path.exists(default_pdf_path):
            app.add(default_pdf_path, data_type="pdf_file")
            st.success(f"Loaded default PDF: policy-booklet-0923.pdf")
        else:
            st.error("Default PDF not found.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            f.write(pdf_file.getvalue())
            app.add(f.name, data_type="pdf_file")
        os.remove(f.name)
        st.success(f"Added {pdf_file.name} to knowledge base!")

    prompt = st.text_input("Ask a question about the PDF")

    if prompt:
        answer = app.chat(prompt)
        st.write(answer)

st.markdown("Built by Farah")
