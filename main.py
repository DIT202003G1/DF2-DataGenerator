"""
TODO:
    - generate staff manager id
"""

from generators import DummyGenerator, QueriesGenerator
import json

def main():
    patients = DummyGenerator.generatePatient()
    staffs = DummyGenerator.generateStaff()
    clinics = DummyGenerator.generateClinics()
    wards = DummyGenerator.generateWards(clinics, staffs)
    beds = DummyGenerator.generateBeds(wards)
    ipts, opts, appointments = DummyGenerator.generateOPTIPTAppointment(patients, staffs)
    QueriesGenerator.insert_ipts(ipts, wards, beds)
    QueriesGenerator.insert_opts(opts)
    QueriesGenerator.insert_appointments(appointments)

    print(json.dumps(ipts, indent=4))
    queries = QueriesGenerator.get_queries()
    with open("queries.sql", "w", encoding="utf8") as queries_file:
        for query in queries:
            queries_file.write(query + "\n")

if __name__ == "__main__":
    main()
