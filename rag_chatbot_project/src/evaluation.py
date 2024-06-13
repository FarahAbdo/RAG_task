import pandas as pd
import logging
from sklearn.metrics import precision_score, recall_score, f1_score
from embedchain_config import embedchain_bot
import os
import tempfile
from dotenv import load_dotenv
import asyncio
import aiohttp

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

# Load the dataset
df = pd.read_csv('data/queries_responses.csv')
logging.info(f"Loaded dataset with {len(df)} entries")

# Initialize the chatbot
openai_access_token = os.getenv("OPENAI_API_KEY")
if not openai_access_token:
    logging.error("OpenAI API key not found in environment variables")
    exit()

db_path = tempfile.mkdtemp()
logging.info(f"Created temporary database path at {db_path}")

app = embedchain_bot(db_path, openai_access_token)
logging.info("Initialized the embedchain bot")

# Asynchronous function to get predictions
async def fetch_prediction(session, query):
    try:
        answer = await app.chat_async(query)  # Assuming the library supports async chat
        return answer
    except Exception as e:
        logging.error(f"Error generating prediction for query: {query} | Error: {e}")
        return ""

# Main function to handle asynchronous processing
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_prediction(session, query) for query in df['query']]
        predictions = await asyncio.gather(*tasks)

    # Check if predictions were generated
    if len(predictions) != len(df):
        logging.error("The number of predictions does not match the number of queries")
        exit()

    # Save predictions to a file for reference
    df['predictions'] = predictions
    df.to_csv('data/predictions.csv', index=False)
    logging.info(f"Saved predictions to data/predictions.csv")

    # Evaluate predictions
    ground_truth = df['response'].tolist()

    # Here we assume exact match is required; otherwise, you might need more complex text similarity measures
    # Converting the responses and predictions into a form suitable for sklearn metrics
    precision = precision_score(ground_truth, predictions, average='micro', zero_division=0)
    recall = recall_score(ground_truth, predictions, average='micro', zero_division=0)
    f1 = f1_score(ground_truth, predictions, average='micro', zero_division=0)

    logging.info(f"Evaluation Metrics - Precision: {precision}, Recall: {recall}, F1-Score: {f1}")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
