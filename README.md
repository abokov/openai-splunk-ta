# ⚡ Zero to Splunk TA: GenAI Deployment Framework

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-black.svg)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

**Zero to Splunk TA** is an AI deployment accelerator built to help Systems Integrators (SIs) and enterprise engineering teams transform API documentation into production-ready Splunk Technology Add-ons (TAs) in minutes, not days. 

By leveraging the **OpenAI API** and advanced prompt chaining, this framework codifies architectural best practices into a repeatable, automated pipeline. It mentors technical teams toward self-sufficiency by removing the friction of manual Python scripting and regex formulation, accelerating customer time-to-value for complex data ingest pipelines.

## 🏗️ Architectural Pattern

The framework utilizes a multi-pass agentic workflow to ensure deterministic, high-quality code generation.

```mermaid
graph TD
    A[Partner / SI Engineer] -->|Inputs API Specs/Docs| B(CLI Orchestrator: Python)
    
    subgraph OpenAI API Integration
    B -->|1. Extraction Prompt| C{OpenAI / Azure OpenAI}
    C -->|Returns JSON| D[Extracted Auth & Endpoint Schema]
    B -->|2. Generation Prompt + Schema| C
    end
    
    C -->|Yields Code| E[Python Ingestion Script]
    C -->|Yields Configs| F[props.conf & inputs.conf]
    
    E --> G((Deployment-Ready Splunk TA))
    F --> G
    
    classDef primary fill:#10a37f,stroke:#000,stroke-width:2px,color:#fff;
    class C primary;
```

## ✨ Key Features
Accelerated Deployment: Reduces the prototyping and implementation phase of custom Splunk integrations by 95%.

Agentic Prompt Chaining: Uses a two-pass approach with the OpenAI API—first extracting structured schema data, then generating the functional logic.

Production-Ready Artifacts: Automatically formats output into standard Splunk structures (inputs.conf, props.conf, and Modular Input Python scripts).

Provider Agnostic: Built on the official openai Python SDK, seamlessly adaptable between standard OpenAI endpoints and Azure OpenAI deployments.

## 🚀 Quick Start
Prerequisites
Python 3.9+

An active OpenAI API Key (or Azure OpenAI endpoint credentials)

### Installation
1. Clone the repository:
``` bash
git clone [https://github.com/abokov/zero-to-splunk-ta-openai.git](https://github.com/abokov/zero-to-splunk-ta-openai.git)
cd zero-to-splunk-ta-openai

2. Install dependencies:

```Bash
pip install -r requirements.txt
```
3. Configure your environment:

```Bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY```
```

4.  Usage
Run the CLI tool and pass the target API documentation or JSON spec:

```Bash
python src/main.py --spec ./examples/sample_api_doc.md --output ./build/MyCustomTA
```

The framework will process the spec and output a ready-to-deploy folder in the ./build directory.



###🧠 Why This Exists (Product Mindset)
Working directly with strategic SIs and enterprise customers, I identified a recurring bottleneck: deploying AI/ML analytics required ingesting niche data sources, which meant weeks of manual engineering for custom connectors. This tool is a codified solution package designed to eliminate that bottleneck, driving immediate business value and unlocking faster adoption of downstream AI/ML use cases.

### 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

Contact: alex@bokov.net




