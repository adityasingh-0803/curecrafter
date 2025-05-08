# BioGraphAgent — Build graph and suggest drug repurposing

from fastapi import FastAPI
from pydantic import BaseModel
import networkx as nx

app = FastAPI()

class Request(BaseModel):
    triples: list
    target_disease: str

@app.post("/suggest-repurposing")
def suggest(data: Request):
    G = nx.Graph()
    for gene, drug, disease in data.triples:
        G.add_node(gene, type='gene')
        G.add_node(drug, type='drug')
        G.add_node(disease, type='disease')
        G.add_edge(gene, drug, relation='targeted_by')
        G.add_edge(drug, disease, relation='treats')

    suggestions = []
    for drug in G.nodes:
        if G.nodes[drug].get('type') == 'drug':
            for neighbor in G.neighbors(drug):
                if G.nodes[neighbor].get('type') == 'disease' and neighbor != data.target_disease:
                    suggestions.append((drug, neighbor))

    return {"suggestions": list(set(suggestions))}
