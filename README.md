# RAGAS Evaluation Framework for EPAM DIAL

A demonstration toolkit for comprehensive evaluation of Retrieval-Augmented Generation (RAG) systems using RAGAS (Retrieval-Augmented Generation Assessment) metrics integrated with EPAM DIAL infrastructure.

> **⚠️ Educational Purpose Only**: This framework is designed for learning, understanding, and demonstration purposes. It is not intended for production use without proper validation and customization.

## Overview

This demonstration framework showcases evaluation capabilities for RAG systems using industry-standard RAGAS metrics. The solution integrates with EPAM DIAL's Azure OpenAI infrastructure to provide educational examples and learning resources for RAG evaluation methodologies.

### Prerequisites

- **EPAM VPN Connection**: Required for accessing DIAL API endpoints
- **Valid EPAM DIAL API Key**: Authentication credential for API access
- **EPAM Internal Network Access**: Access to EPAM's AI infrastructure

## Key Features

- **Educational RAGAS Implementation**: Complete demonstration of industry-standard evaluation metrics
- **EPAM DIAL Integration**: Example integration with EPAM DIAL Azure OpenAI endpoints
- **LangChain Compatibility**: Learning examples with LangChain ecosystem integration
- **Multi-Metric Demonstration**: Context Recall, Context Precision, Faithfulness, and Answer Correctness
- **Learning Configuration**: Simplified setup for educational purposes
- **Results Export**: CSV export functionality for analysis and learning workflows

## Evaluation Metrics

The framework implements the following RAGAS evaluation metrics:

| Metric | Description | Score Range |
|--------|-------------|-------------|
| **Context Recall** | Measures completeness of retrieved context relative to ground truth | 0.0 - 1.0 |
| **Context Precision** | Evaluates relevance of retrieved context to the query | 0.0 - 1.0 |
| **Faithfulness** | Assesses whether generated answers are grounded in provided context | 0.0 - 1.0 |
| **Answer Correctness** | Compares generated answers against ground truth for accuracy | 0.0 - 1.0 |

## Installation

### Prerequisites
- Python 3.8 or higher
- EPAM VPN connection
- Valid EPAM DIAL API credentials

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd simple-ragas-evaluation
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   Create a `.env` file in the project root:
   ```env
   DIAL_API_KEY=your_epam_dial_api_key
   AZURE_ENDPOINT=https://ai-proxy.lab.epam.com
   API_VERSION=2024-02-01
   ```

### Configuration Notes

- **Educational Purpose**: This framework is designed for learning and demonstration purposes
- **EPAM DIAL Integration**: Configured for EPAM DIAL infrastructure for educational examples
- **VPN Requirement**: EPAM VPN connection is mandatory for API access
- **Custom Configuration**: To use alternative API keys, modify configuration files in the `utils/` directory

## Quick Start

### Interactive Evaluation (Recommended)
1. Launch Jupyter Notebook and open `rag-eval-demo.ipynb`
2. Execute all cells to run a complete evaluation workflow
3. Results are automatically exported to `ragas_evaluation_results.csv`

### Programmatic Evaluation
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

## Learning Objectives

This demonstration framework helps you understand:

1. **RAGAS Metrics Implementation**: How to implement and configure RAGAS evaluation metrics
2. **EPAM DIAL Integration**: Connecting to EPAM's AI infrastructure for evaluation
3. **LangChain Wrappers**: Creating compatible wrappers for different AI services
4. **Evaluation Workflows**: End-to-end evaluation processes for RAG systems
5. **Results Analysis**: Interpreting and analyzing evaluation results

## Next Steps for Learning

1. **Experiment with Datasets**: Replace sample data with your own RAG system examples
2. **Explore Additional Metrics**: Implement additional RAGAS metrics for comprehensive evaluation
3. **Scale Evaluation**: Practice batch processing techniques for larger datasets
4. **Customize Configuration**: Modify the framework for different AI service providers
5. **Build Production Systems**: Use learnings to develop production-ready evaluation pipelines

## Troubleshooting

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

## Additional Resources

- [RAGAS Documentation](https://docs.ragas.io/) - Official RAGAS framework documentation
- [EPAM DIAL Documentation](https://dial.epam.com/) - EPAM DIAL platform information
- [LangChain Azure Integration](https://python.langchain.com/docs/integrations/llms/azure_openai) - LangChain Azure OpenAI integration guide
- [HuggingFace Datasets](https://huggingface.co/docs/datasets/) - Dataset handling documentation

## Contributing

Contributions to this educational framework are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/educational-enhancement`)
3. Commit your changes (`git commit -m 'Add educational enhancement'`)
4. Push to the branch (`git push origin feature/educational-enhancement`)
5. Open a Pull Request

## License

This educational project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [RAGAS](https://github.com/explodinggradients/ragas) for providing the evaluation framework
- [EPAM DIAL](https://dial.epam.com/) for providing access to AI infrastructure
- [LangChain](https://langchain.com/) for the integration framework and ecosystem

---

**Educational Framework for RAG Evaluation**

This demonstration toolkit is designed for learning and understanding RAG evaluation methodologies. For questions or support, please open an issue or contact the development team.
