from gensim.models import Word2Vec

# Sample sentences (tokenized)
sentences = [
    ["i", "love", "natural", "language", "processing"],
    ["language", "processing", "is", "fun"],
    ["deep", "learning", "advances", "artificial", "intelligence"],
    ["python", "is", "great", "for", "machine", "learning"]
]

# Train a Word2Vec model
model = Word2Vec(
    sentences, 
    vector_size=50,  # embedding dimension
    window=3,        # context window
    min_count=1,     # include all words
    workers=2,       # threads
    sg=1             # skip-gram model
)

# Ensure the vocabulary is built
model.build_vocab(sentences, progress_per=1)
model.train(sentences, total_examples=model.corpus_count, epochs=10)

# Helper function to safely get vectors and similarities
def safe_most_similar(word, topn=5):
    if word in model.wv:
        return model.wv.most_similar(word, topn=topn)
    else:
        return f"'{word}' not in vocabulary"

def safe_similarity(word1, word2):
    if word1 in model.wv and word2 in model.wv:
        return model.wv.similarity(word1, word2)
    else:
        return f"One of the words ('{word1}' or '{word2}') not in vocabulary"

# Explore embeddings
print("Vector for 'language':\n", model.wv.get_vector("language"))
print("\nMost similar to 'learning':", safe_most_similar("learning"))
print("\nSimilarity between 'python' and 'language':", safe_similarity("python", "language"))
