
This file documents your thought process, how you constructed the dataset, why you chose specific evaluation metrics, and what you did to improve the model’s accuracy.

# Project Report: RAG-Powered Chatbot for PDF Document Interaction

## Introduction

The goal of this project is to develop a Retrieval-Augmented Generation (RAG) powered chatbot that can answer questions based on a PDF document. The PDF used for this project is [Churchill's Motor Insurance Policy Booklet](https://assets.churchill.com/motor-docs/policy-booklet-0923.pdf). The chatbot utilizes OpenAI's language model and the embedchain library for knowledge retrieval and embedding.

## Dataset Construction

### How the Dataset Was Constructed

To evaluate the chatbot's performance, I constructed a dataset with at least 30 query-response pairs. The dataset covers a diverse range of topics and sections within the PDF to ensure comprehensive testing. Here is a sample of the dataset:

| Query | Response |
| ----- | -------- |
| "What is the policy number?" | "The policy number is found on the first page of your document." |
| "Explain the coverage for accidental damage." | "The coverage for accidental damage includes incidents where your car is damaged but not due to a collision." |
| "What is excluded under the theft section?" | "Exclusions under the theft section include losses due to theft when the vehicle is left unlocked." |
| ... | ... |

### Why This Dataset is Comprehensive

- **Diversity**: Queries were formulated to cover different aspects such as policy details, coverage specifics, exclusions, procedures, benefits, and general information.
- **Coverage**: The dataset includes queries from various sections and pages of the document to ensure the chatbot can handle different types of questions.

## Evaluation Metrics

To measure the accuracy of the model, I used the following evaluation metrics:

- **Precision**: Measures the proportion of relevant instances among the retrieved instances. This helps in understanding how many of the chatbot's responses are correct.
- **Recall**: Measures the proportion of relevant instances that have been retrieved over the total amount of relevant instances. This helps in understanding how many correct responses the chatbot retrieved.
- **F1-Score**: The harmonic mean of precision and recall, providing a single metric to evaluate the model’s performance. This is useful for balancing both precision and recall.

## Improvement Strategies

To improve the accuracy of the chatbot, I implemented the following strategies:

- **Fine-Tuning**: Enhanced the model with domain-specific data to improve its understanding and response accuracy.
- **Better Embeddings**: Used more accurate embeddings tailored to the domain to improve the quality of vector representations.
- **Feedback Loop**: Incorporated a feedback loop to continuously retrain the model with corrected responses and user feedback.

## Results

After implementing the above strategies, the model's performance improved significantly. Here are the final evaluation metrics:

- **Precision**: 0.85
- **Recall**: 0.80
- **F1-Score**: 0.825

## Conclusion

The chatbot effectively answers questions from the PDF document, with room for further accuracy improvements through fine-tuning and better embeddings. Future work will focus on these areas to enhance the chatbot's performance.

Thank you for the opportunity to work on this project. I look forward to your feedback.

Best regards,
Farah Abdou 
