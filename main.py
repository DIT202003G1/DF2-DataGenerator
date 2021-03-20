from generators import DummyGenerator, QueriesGenerator

def main():
    QueriesGenerator.insert_patients(DummyGenerator.generatePatient())

    queries = QueriesGenerator.get_queries()
    with open("queries.sql", "w") as queries_file:
        for query in queries:
            queries_file.write(query + "\n")

if __name__ == "__main__":
    main()
