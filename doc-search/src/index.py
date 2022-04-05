import os
import codecs
from prometheus_client import Summary as prom_summary

REQUEST_TIME = prom_summary('request_processing_seconds','latency of requests')

class Index:
    # builds a naive, in efficient index
    
    def __init__(self, docs):
        self.docs = docs

    @staticmethod
    def new(data_path):
        
        docs = {}
        for path in os.listdir(data_path):
            if path.endswith('.xml'):
                doc_id = path.split(".")[0]

                with codecs.open(data_path + '/' + path, "r", encoding='utf-8', errors='ignore') as f:
                    data = f.read()
                    docs[doc_id] = data

        return Index(docs=docs)
    
    @REQUEST_TIME.time()
    def search(self, phrase):
        words = phrase.split()
        results = set()
        for doc, text in self.docs.items():
            found_all = True
            for word in words:
                if word not in text:
                    found_all = False
                    break
            if found_all:
                results.add(doc)
        return results

