# 🎯 Simple RAGAS Evaluation with EPAM DIAL

A comprehensive toolkit for evaluating Retrieval-Augmented Generation (RAG) systems using RAGAS (Retrieval-Augmented Generation Assessment) metrics with EPAM DIAL models.

## 📋 Overview

This project provides a complete solution for evaluating RAG systems using industry-standard RAGAS metrics. It integrates seamlessly with EPAM DIAL's Azure OpenAI endpoints to provide accurate and reliable evaluation results.

**🔒 Access Requirements:**
- EPAM VPN connection (required for DIAL API access)
- Valid EPAM DIAL API key
- Access to EPAM's internal AI infrastructure

## 🚀 Features

- **RAGAS Integration**: Complete implementation of RAGAS evaluation metrics
- **EPAM DIAL Support**: Native integration with EPAM DIAL Azure OpenAI endpoints
- **LangChain Compatibility**: Wrapper functions for seamless LangChain integration
- **Comprehensive Metrics**: Context Recall, Context Precision, Faithfulness, and Answer Correctness
- **Easy Setup**: Simple configuration and quick start guide
- **Results Export**: CSV export for further analysis and reporting

## 📊 RAGAS Metrics Evaluated

| Metric | Description | Range |
|--------|-------------|-------|
| **Context Recall** | How complete is the retrieved context? | 0-1 |
| **Context Precision** | How relevant is the retrieved context? | 0-1 |
| **Faithfulness** | Is the answer grounded in the context? | 0-1 |
| **Answer Correctness** | How accurate is the answer compared to ground truth? | 0-1 |

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd simple-ragas-evaluation
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DIAL_API_KEY=your_epam_dial_api_key
   AZURE_ENDPOINT=https://ai-proxy.lab.epam.com
   API_VERSION=2024-02-01
   ```

   **⚠️ Important Notes:**
   - This project uses **EPAM DIAL API keys** and requires **EPAM VPN connection**
   - You must be connected to EPAM's VPN to access the DIAL endpoints
   - If you want to use your own API keys, modify the configuration in `utils/langchain_wrappers.py` and `utils/model_explorer.py`

## 🎮 Quick Start

### Option 1: Jupyter Notebook (Recommended)
1. Open `rag-eval-demo.ipynb` in Jupyter
2. Run all cells to see a complete evaluation example
3. Results will be saved to `ragas_evaluation_results.csv`

### Option 2: Python Script
```python
from utils import create_ragas_dataset, create_langchain_llm, create_langchain_embeddings
from ragas import evaluate
from ragas.metrics import context_recall, context_precision, faithfulness, answer_correctness

# Load dataset
dataset = create_ragas_dataset()

# Configure models
llm = create_langchain_llm("gpt-4.1-mini-2025-04-14")
embeddings = create_langchain_embeddings("text-embedding-3-small-1")

# Run evaluation
result = evaluate(
    dataset,
    metrics=[context_recall, context_precision, faithfulness, answer_correctness],
    llm=llm,
    embeddings=embeddings
)

print(result)
```

## 📁 Project Structure

```
simple-ragas-evaluation/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── rag-eval-demo.ipynb         # Interactive demo notebook
├── ragas_evaluation_results.csv # Sample evaluation results
└── utils/                       # Utility modules
    ├── __init__.py             # Package initialization
    ├── dataset_creator.py      # Dataset creation utilities
    ├── langchain_wrappers.py   # LangChain model wrappers
    └── model_explorer.py       # Model exploration tools
```

## 🔧 Configuration

### Available Models

Use the model explorer to discover available deployments:

```bash
python utils/model_explorer.py
```

### Custom Dataset

Replace the fake dataset with your own RAG evaluation data:

```python
from datasets import Dataset

# Your custom dataset
custom_data = [
    {
        "question": "Your question here",
        "answer": "Generated answer",
        "context": "Retrieved context",
        "ground_truth": "Expected answer",
        "retrieved_contexts": ["Context 1", "Context 2"]
    }
    # ... more examples
]

dataset = Dataset.from_list(custom_data)
```

## 📈 Understanding Results

### Score Interpretation

- **0.0-0.3**: Poor performance, needs significant improvement
- **0.3-0.6**: Moderate performance, some optimization needed
- **0.6-0.8**: Good performance, minor improvements possible
- **0.8-1.0**: Excellent performance, well-optimized system

### Sample Results

```
Overall Scores:
{
    'context_recall': 1.0000,      # Perfect context retrieval
    'context_precision': 1.0000,   # Perfect context relevance
    'faithfulness': 0.7000,        # Good grounding in context
    'answer_correctness': 0.6708    # Moderate accuracy
}
```

## 🛠️ Advanced Usage

### Custom Metrics

Add additional RAGAS metrics:

```python
from ragas.metrics import answer_relevancy, context_utilization

metrics = [
    context_recall,
    context_precision,
    faithfulness,
    answer_correctness,
    answer_relevancy,      # Additional metric
    context_utilization    # Additional metric
]
```

### Batch Evaluation

For larger datasets:

```python
# Process in batches to avoid memory issues
batch_size = 10
for i in range(0, len(dataset), batch_size):
    batch = dataset.select(range(i, min(i + batch_size, len(dataset))))
    result = evaluate(batch, metrics=metrics, llm=llm, embeddings=embeddings)
    # Process batch results
```

## 🔍 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure `DIAL_API_KEY` is set in your `.env` file
2. **VPN Connection Required**: You must be connected to EPAM VPN to access DIAL endpoints
3. **Model Not Found**: Check available deployments with `model_explorer.py`
4. **Timeout Errors**: Increase timeout values for large datasets
5. **Memory Issues**: Use batch processing for large datasets
6. **Authentication Failed**: Verify your EPAM DIAL API key is valid and active

### Debug Mode

Enable verbose logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 Resources

- [RAGAS Documentation](https://docs.ragas.io/)
- [EPAM DIAL Documentation](https://dial.epam.com/)
- [LangChain Azure Integration](https://python.langchain.com/docs/integrations/llms/azure_openai)
- [HuggingFace Datasets](https://huggingface.co/docs/datasets/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [RAGAS](https://github.com/explodinggradients/ragas) for the evaluation framework
- [EPAM DIAL](https://dial.epam.com/) for providing the AI infrastructure
- [LangChain](https://langchain.com/) for the integration framework

---

**Happy Evaluating! 🎉**

For questions or support, please open an issue or contact the development team.
