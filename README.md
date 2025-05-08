# CureCrafter
##📁 Repository Structure
```plaintext
curecrafter/
├── paper_miner/
│   └── paper_miner.py
├── bio_graph/
│   └── bio_graph.py
├── requirements.txt
├── README.md
└── LICENSE
```

**CureCrafter** is an AI-powered tool designed to automate the extraction of biomedical relationships from research abstracts and suggest potential drug repurposing opportunities using knowledge graphs.

## 🚀 Features

- **PaperMinerAgent**: Extracts gene–drug–disease triples from biomedical abstracts using OpenAI's GPT-4.
- **BioGraphAgent**: Constructs a knowledge graph from extracted triples and suggests drug repurposing candidates.

## 🛠️ Technologies Used

- Python
- FastAPI
- OpenAI API
- NetworkX

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/curecrafter.git
   cd curecrafter
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
 **🧪 Usage**
**Start PaperMinerAgent**
 ```bash
uvicorn paper_miner.paper_miner:app --reload --port 8000
```
**Start BioGraphAgent**
 ```bash
uvicorn bio_graph.bio_graph:app --reload --port 8001
```

**📬 API Endpoints**
1. **Extract Triples**
Endpoint: /extract-triples

Method: POST

Payload:
 ```bash
{
  "abstract": "EGFR mutations are targeted by gefitinib in lung cancer treatment.",
  "api_key": "your-openai-api-key"
}
```

Response:
```bash
{
  "triples": [
    ["EGFR", "Gefitinib", "Lung Cancer"]
  ]
}
```

**📈 Future Enhancements**
Integrate additional biomedical databases for enriched graph construction.

Develop a user-friendly frontend interface.

Implement advanced graph algorithms for more accurate repurposing suggestions.

**📄 License**
This project is licensed under the MIT License - see the LICENSE file for details.

---

### 📄 `LICENSE` (MIT License)

```txt
MIT License

Copyright (c) 2025 CureCrafter

Permission is hereby granted, free of charge, to any person obtaining a copy
...
```
