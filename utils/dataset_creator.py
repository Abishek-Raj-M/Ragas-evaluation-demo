"""
Dataset Creator Utility for RAGAS Evaluation
Contains functions to create fake datasets for testing RAGAS metrics
"""

import pandas as pd

def create_fake_ragas_dataset():
    """
    Create a fake dataset with diverse examples covering different RAG evaluation scenarios
    This demonstrates various combinations of RAGAS metrics
    """
    
    # Define diverse dataset scenarios
    data = [
        # Example 1: PERFECT SCORES - All metrics should be high
        {
            "question": "What is the capital of France?",
            "answer": "The capital of France is Paris.",
            "context": "France is a country located in Western Europe. Its capital and largest city is Paris, which is situated in the north-central part of the country along the Seine River. Paris is known for landmarks like the Eiffel Tower and Louvre Museum.",
            "ground_truth": "Paris",
            "retrieved_contexts": ["France is a country located in Western Europe. Its capital and largest city is Paris, which is situated in the north-central part of the country along the Seine River. Paris is known for landmarks like the Eiffel Tower and Louvre Museum."]
        },
        
        # Example 2: LOW CONTEXT RECALL - Missing important information
        {
            "question": "What are the main ingredients in pizza?",
            "answer": "Pizza contains dough, tomato sauce, cheese, and toppings.",
            "context": "Pizza is a popular Italian dish.",  # Very incomplete context
            "ground_truth": "Dough, tomato sauce, cheese, and various toppings",
            "retrieved_contexts": ["Pizza is a popular Italian dish."]  # Missing detailed ingredient info
        },
        
        # Example 3: LOW CONTEXT PRECISION - Irrelevant context retrieved
        {
            "question": "How does photosynthesis work?",
            "answer": "Plants use sunlight, water, and carbon dioxide to produce glucose and oxygen through photosynthesis.",
            "context": "Cooking is a great hobby. Many people enjoy preparing meals at home. There are various cooking techniques like frying, baking, and grilling. Plants also do photosynthesis.",  # Mostly irrelevant
            "ground_truth": "Plants convert sunlight, water, and CO2 into glucose and oxygen",
            "retrieved_contexts": ["Cooking is a great hobby. Many people enjoy preparing meals at home. There are various cooking techniques like frying, baking, and grilling. Plants also do photosynthesis."]
        },
        
        # Example 4: LOW FAITHFULNESS - Answer not grounded in context (hallucination)
        {
            "question": "What is the population of Tokyo?",
            "answer": "Tokyo has approximately 50 million people and is the largest city in the world.",  # Wrong info not in context
            "context": "Tokyo is the capital city of Japan. It is known for its modern technology and traditional culture. The city has excellent public transportation including the famous bullet trains.",
            "ground_truth": "37 million (Greater Tokyo Area)",
            "retrieved_contexts": ["Tokyo is the capital city of Japan. It is known for its modern technology and traditional culture. The city has excellent public transportation including the famous bullet trains."]
        },
        
        # Example 5: LOW ANSWER CORRECTNESS - Wrong answer despite good context
        {
            "question": "Who wrote Romeo and Juliet?",
            "answer": "Charles Dickens wrote Romeo and Juliet in 1850.",  # Completely wrong
            "context": "Romeo and Juliet is a tragic play written by William Shakespeare in the early part of his career, around 1595-1596. It tells the story of two young lovers whose deaths ultimately unite their feuding families. Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language.",
            "ground_truth": "William Shakespeare",
            "retrieved_contexts": ["Romeo and Juliet is a tragic play written by William Shakespeare in the early part of his career, around 1595-1596. It tells the story of two young lovers whose deaths ultimately unite their feuding families. Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language."]
        },
        
        # Example 6: MIXED SCENARIO - Good context but partial answer
        {
            "question": "What are the benefits of exercise?",
            "answer": "Exercise improves cardiovascular health and builds muscle strength.",
            "context": "Regular exercise provides numerous health benefits including improved cardiovascular health, stronger muscles, better mental health, reduced risk of chronic diseases, enhanced sleep quality, and increased energy levels. It also helps with weight management and bone density.",
            "ground_truth": "Improved cardiovascular health, stronger muscles, better mental health, reduced disease risk, better sleep, increased energy, weight management, stronger bones",
            "retrieved_contexts": ["Regular exercise provides numerous health benefits including improved cardiovascular health, stronger muscles, better mental health, reduced risk of chronic diseases, enhanced sleep quality, and increased energy levels. It also helps with weight management and bone density."]
        },
        
        # Example 7: PARTIAL CONTEXT RECALL - Some relevant info missing
        {
            "question": "What is machine learning?",
            "answer": "Machine learning is a subset of artificial intelligence that enables computers to learn from data.",
            "context": "Machine learning is a subset of artificial intelligence.",  # Missing key details
            "ground_truth": "Machine learning is a subset of AI that enables computers to learn and improve from experience without being explicitly programmed",
            "retrieved_contexts": ["Machine learning is a subset of artificial intelligence."]
        },
        
        # Example 8: HIGH PRECISION, LOW RECALL - Very relevant but incomplete
        {
            "question": "What is the speed of light?",
            "answer": "The speed of light is approximately 299,792,458 meters per second.",
            "context": "The speed of light in vacuum is exactly 299,792,458 meters per second.",  # Precise but minimal
            "ground_truth": "299,792,458 meters per second in vacuum",
            "retrieved_contexts": ["The speed of light in vacuum is exactly 299,792,458 meters per second."]
        }
    ]
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    return df

def create_ragas_dataset():
    """
    Create a RAGAS-compatible dataset with diverse scenarios to demonstrate different metric combinations
    This dataset includes examples that will show:
    - High/Low Context Recall (completeness of retrieved context)
    - High/Low Context Precision (relevance of retrieved context) 
    - High/Low Faithfulness (grounding in context)
    - High/Low Answer Correctness (accuracy vs ground truth)
    """
    from datasets import Dataset
    
    # Define diverse dataset scenarios
    data = [
        # Example 1: PERFECT SCORES - All metrics should be high
        {
            "question": "What is the capital of France?",
            "answer": "The capital of France is Paris.",
            "context": "France is a country located in Western Europe. Its capital and largest city is Paris, which is situated in the north-central part of the country along the Seine River. Paris is known for landmarks like the Eiffel Tower and Louvre Museum.",
            "ground_truth": "Paris",
            "retrieved_contexts": ["France is a country located in Western Europe. Its capital and largest city is Paris, which is situated in the north-central part of the country along the Seine River. Paris is known for landmarks like the Eiffel Tower and Louvre Museum."]
        },
        
        # Example 2: LOW CONTEXT RECALL - Missing important information
        {
            "question": "What are the main ingredients in pizza?",
            "answer": "Pizza contains dough, tomato sauce, cheese, and toppings.",
            "context": "Pizza is a popular Italian dish.",  # Very incomplete context
            "ground_truth": "Dough, tomato sauce, cheese, and various toppings",
            "retrieved_contexts": ["Pizza is a popular Italian dish."]  # Missing detailed ingredient info
        },
        
        # Example 3: LOW CONTEXT PRECISION - Irrelevant context retrieved
        {
            "question": "How does photosynthesis work?",
            "answer": "Plants use sunlight, water, and carbon dioxide to produce glucose and oxygen through photosynthesis.",
            "context": "Cooking is a great hobby. Many people enjoy preparing meals at home. There are various cooking techniques like frying, baking, and grilling. Plants also do photosynthesis.",  # Mostly irrelevant
            "ground_truth": "Plants convert sunlight, water, and CO2 into glucose and oxygen",
            "retrieved_contexts": ["Cooking is a great hobby. Many people enjoy preparing meals at home. There are various cooking techniques like frying, baking, and grilling. Plants also do photosynthesis."]
        },
        
        # Example 4: LOW FAITHFULNESS - Answer not grounded in context (hallucination)
        {
            "question": "What is the population of Tokyo?",
            "answer": "Tokyo has approximately 50 million people and is the largest city in the world.",  # Wrong info not in context
            "context": "Tokyo is the capital city of Japan. It is known for its modern technology and traditional culture. The city has excellent public transportation including the famous bullet trains.",
            "ground_truth": "37 million (Greater Tokyo Area)",
            "retrieved_contexts": ["Tokyo is the capital city of Japan. It is known for its modern technology and traditional culture. The city has excellent public transportation including the famous bullet trains."]
        },
        
        # Example 5: LOW ANSWER CORRECTNESS - Wrong answer despite good context
        {
            "question": "Who wrote Romeo and Juliet?",
            "answer": "Charles Dickens wrote Romeo and Juliet in 1850.",  # Completely wrong
            "context": "Romeo and Juliet is a tragic play written by William Shakespeare in the early part of his career, around 1595-1596. It tells the story of two young lovers whose deaths ultimately unite their feuding families. Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language.",
            "ground_truth": "William Shakespeare",
            "retrieved_contexts": ["Romeo and Juliet is a tragic play written by William Shakespeare in the early part of his career, around 1595-1596. It tells the story of two young lovers whose deaths ultimately unite their feuding families. Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language."]
        },
        
        # Example 6: MIXED SCENARIO - Good context but partial answer
        {
            "question": "What are the benefits of exercise?",
            "answer": "Exercise improves cardiovascular health and builds muscle strength.",
            "context": "Regular exercise provides numerous health benefits including improved cardiovascular health, stronger muscles, better mental health, reduced risk of chronic diseases, enhanced sleep quality, and increased energy levels. It also helps with weight management and bone density.",
            "ground_truth": "Improved cardiovascular health, stronger muscles, better mental health, reduced disease risk, better sleep, increased energy, weight management, stronger bones",
            "retrieved_contexts": ["Regular exercise provides numerous health benefits including improved cardiovascular health, stronger muscles, better mental health, reduced risk of chronic diseases, enhanced sleep quality, and increased energy levels. It also helps with weight management and bone density."]
        },
        
        # Example 7: PARTIAL CONTEXT RECALL - Some relevant info missing
        {
            "question": "What is machine learning?",
            "answer": "Machine learning is a subset of artificial intelligence that enables computers to learn from data.",
            "context": "Machine learning is a subset of artificial intelligence.",  # Missing key details
            "ground_truth": "Machine learning is a subset of AI that enables computers to learn and improve from experience without being explicitly programmed",
            "retrieved_contexts": ["Machine learning is a subset of artificial intelligence."]
        },
        
        # Example 8: HIGH PRECISION, LOW RECALL - Very relevant but incomplete
        {
            "question": "What is the speed of light?",
            "answer": "The speed of light is approximately 299,792,458 meters per second.",
            "context": "The speed of light in vacuum is exactly 299,792,458 meters per second.",  # Precise but minimal
            "ground_truth": "299,792,458 meters per second in vacuum",
            "retrieved_contexts": ["The speed of light in vacuum is exactly 299,792,458 meters per second."]
        }
    ]
    
    # Create HuggingFace Dataset directly
    dataset = Dataset.from_list(data)
    
    return dataset

def save_dataset(df, filename="fake_ragas_data.csv"):
    """Save the dataset to a CSV file"""
    df.to_csv(filename, index=False)
    print(f"Dataset saved as {filename}")
    print(f"Dataset shape: {df.shape}")
    return filename
