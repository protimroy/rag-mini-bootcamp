from workshop_code.common_components.vectorizers import Vectorizer
from workshop_code.common_components.vectordb_client_adapters import PineconeClientAdapter

class NaiveRetriever:
  
  def __init__(self, vectorizer: Vectorizer):
    self._client_adapter = PineconeClientAdapter()
    self._vectorizer = vectorizer
    
  def retrieve(self, query: str) -> str:
    query_vector = self._vectorizer.vectorize_query(query)
    retrieved_chunks_list = self._client_adapter.retrieve(query_vector, k=5)
    formatted_chunks = "\n\n".join(chunk for chunk in retrieved_chunks_list)
    return formatted_chunks