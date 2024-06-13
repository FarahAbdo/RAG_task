Follow these steps to set up your development environment:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/rag_chatbot_project.git
   cd rag_chatbot_project
  
2. **Create a virtual environment**:

  ```bash
  python -m venv venv
  ```
3. **Activate the virtual environment**:

- On Windows:
 ```bash
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```
4. **Install the required packages**:

  ```bash
  pip install -r docs/requirements.txt
  ```
5. **Set up environment variables**:
Create a .env file in the root directory with the following content:

OPENAI_API_KEY=your_openai_api_key

6. **Run the application**:

  ```bash
  streamlit run src/main.py
  ```

Additional Information
Python version: Ensure you are using Python 3.7 or higher.
Dependencies: The required dependencies are listed in docs/requirements.txt.
Troubleshooting: If you encounter any issues, ensure all dependencies are correctly installed and environment variables are set.
