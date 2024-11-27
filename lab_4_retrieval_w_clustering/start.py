"""
Laboratory Work #4 starter.
"""

# pylint:disable=duplicate-code, too-many-locals, too-many-statements, unused-variable

from lab_4_retrieval_w_clustering.main import (
    BM25Vectorizer,
    ClusteringSearchEngine,
    DocumentVectorDB,
    get_paragraphs,
    VectorDBSearchEngine,
)


def open_files() -> tuple[list[str], list[str]]:
    """
    # stubs: keep.

    Open files.

    Returns:
        tuple[list[str], list[str]]: Documents and stopwords.
    """
    paths_to_texts = [
        "assets/texts/Master_and_Margarita_chapter1.txt",
        "assets/texts/Master_and_Margarita_chapter2.txt",
        "assets/texts/Master_and_Margarita_chapter3.txt",
        "assets/texts/Master_and_Margarita_chapter4.txt",
        "assets/texts/Master_and_Margarita_chapter5.txt",
        "assets/texts/Master_and_Margarita_chapter6.txt",
        "assets/texts/Master_and_Margarita_chapter7.txt",
        "assets/texts/Master_and_Margarita_chapter8.txt",
        "assets/texts/Master_and_Margarita_chapter9.txt",
        "assets/texts/Master_and_Margarita_chapter10.txt",
        "assets/texts/War_and_Peace_chapter1.txt",
        "assets/texts/War_and_Peace_chapter2.txt",
        "assets/texts/War_and_Peace_chapter3.txt",
        "assets/texts/War_and_Peace_chapter4.txt",
        "assets/texts/War_and_Peace_chapter5.txt",
        "assets/texts/War_and_Peace_chapter6.txt",
        "assets/texts/War_and_Peace_chapter7.txt",
        "assets/texts/War_and_Peace_chapter8.txt",
        "assets/texts/War_and_Peace_chapter9.txt",
        "assets/texts/War_and_Peace_chapter10.txt",
    ]
    documents = []
    for path in sorted(paths_to_texts):
        with open(path, "r", encoding="utf-8") as file:
            documents.append(file.read())
    with open("assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    return documents, stopwords


def main() -> None:
    """
    Launch an implementation.
    """
    documents, stopwords = open_files()
    document_paragraphs = []
    for document in documents:
        paragraphs = get_paragraphs(document)
        document_paragraphs.append(paragraphs)

    vectorizer = BM25Vectorizer()
    vectorizer.set_tokenized_corpus(document_paragraphs)
    vectorizer.build()
    document_vector = vectorizer.vectorize(document_paragraphs[0])

    database = DocumentVectorDB(stopwords)
    database.put_corpus(documents)

    database_searcher = VectorDBSearchEngine(database)
    relevant_documents = database_searcher.retrieve_relevant_documents(
        "Первый был не кто иной, как Михаил Александрович Берлиоз, председатель правления", 3)

    clustering_searcher = ClusteringSearchEngine(database)
    more_relevant_documents = clustering_searcher.retrieve_relevant_documents(
        "Первый был не кто иной, как Михаил Александрович Берлиоз, председатель правления", 5)

    result = more_relevant_documents
    print(document_vector)
    print()
    for relevant_document in relevant_documents:
        print(relevant_document)
    print()
    for more_relevant_document in more_relevant_documents:
        print(more_relevant_document)
    assert result, "Result is None"


if __name__ == "__main__":
    main()
