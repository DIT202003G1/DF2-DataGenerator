"""
TODO:
    - generate staff manager id
"""

from generators import dummy_generator, queries_generator
import json

def main():
    patients = dummy_generator.generatePatient()
    staffs = dummy_generator.generateStaff()
    clinics = dummy_generator.generateClinics()
    wards = dummy_generator.generateWards(clinics, staffs)
    beds = dummy_generator.generateBeds(wards)
    ipts, opts, appointments = dummy_generator.generateOPTIPTAppointment(patients, staffs)
    queries_generator.insert_ipts(ipts, wards, beds)
    queries_generator.insert_opts(opts)
    queries_generator.insert_appointments(appointments)

    print(json.dumps(ipts, indent=4))
    queries = queries_generator.get_queries()
    with open("queries.sql", "w", encoding="utf8") as queries_file:
        for query in queries:
            queries_file.write(query + "\n")

if __name__ == "__main__":
    main()
