#!/usr/bin/env python3
"""
Create a fake dataset for RAGAS evaluation learning
This script generates sample data with different scenarios to test RAGAS metrics
"""

import pandas as pd

def create_fake_ragas_dataset():
    """
    Create a fake dataset with 5 examples covering different RAG evaluation scenarios
    """
    
    # Define our fake dataset
    data = [
        {
            "question": "What is the capital of France?",
            "answer": "The capital of France is Paris.",
            "context": "France is a country located in Western Europe. Its capital and largest city is Paris, which is situated in the north-central part of the country along the Seine River.",
            "ground_truth": "Paris"
        },
        {
            "question": "What are the main ingredients in pizza?",
            "answer": "Pizza typically contains dough, tomato sauce, cheese, and various toppings like pepperoni, vegetables, or meat.",
            "context": "Pizza is a popular Italian dish consisting of a flat, round base of dough topped with tomato sauce, cheese, and various ingredients. Common toppings include pepperoni, mushrooms, onions, bell peppers, and sausage. The dough is usually made from flour, water, yeast, and salt.",
            "ground_truth": "Dough, tomato sauce, cheese, and toppings"
        },
        {
            "question": "How does photosynthesis work?",
            "answer": "Plants use sunlight, water, and carbon dioxide to produce glucose and oxygen through photosynthesis.",
            "context": "Photosynthesis is the process by which plants convert light energy into chemical energy. During this process, plants absorb sunlight through chlorophyll in their leaves, take in water from their roots, and carbon dioxide from the air. They produce glucose (sugar) and release oxygen as a byproduct.",
            "ground_truth": "Plants convert sunlight, water, and CO2 into glucose and oxygen"
        },
        {
            "question": "What is the population of Tokyo?",
            "answer": "Tokyo has approximately 14 million people.",
            "context": "Tokyo is the capital city of Japan and one of the most populous metropolitan areas in the world. The Greater Tokyo Area has a population of over 37 million people, making it the largest metropolitan area globally.",
            "ground_truth": "37 million (Greater Tokyo Area)"
        },
        {
            "question": "Who wrote Romeo and Juliet?",
            "answer": "William Shakespeare wrote Romeo and Juliet, one of his most famous plays.",
            "context": "Romeo and Juliet is a tragic play written by William Shakespeare in the early part of his career, around 1595-1596. It tells the story of two young lovers whose deaths ultimately unite their feuding families. Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language.",
            "ground_truth": "William Shakespeare"
        }
    ]
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    return df

def save_dataset(df, filename="fake_ragas_data.csv"):
    """Save the dataset to a CSV file"""
    df.to_csv(filename, index=False)
    print(f"Dataset saved as {filename}")
    print(f"Dataset shape: {df.shape}")
    return filename

if __name__ == "__main__":
    print("Creating fake RAGAS dataset...")
    
    # Create the dataset
    df = create_fake_ragas_dataset()
    
    # Display the dataset
    print("\nDataset Preview:")
    print("=" * 80)
    for i, row in df.iterrows():
        print(f"\nExample {i+1}:")
        print(f"Question: {row['question']}")
        print(f"Answer: {row['answer']}")
        print(f"Context: {row['context'][:100]}...")
        print(f"Ground Truth: {row['ground_truth']}")
        print("-" * 40)
    
    # Save to CSV
    filename = save_dataset(df)
    
    print(f"\nSuccess! Your fake dataset is ready at: {filename}")
    print("\nThis dataset includes:")
    print("• Simple factual questions (France capital)")
    print("• Multi-component questions (pizza ingredients)")
    print("• Complex process questions (photosynthesis)")
    print("• Questions with incomplete answers (Tokyo population)")
    print("• Literature questions (Shakespeare)")
