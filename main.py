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
    treatments = dummy_generator.generateTreatmentDrug(ipts, opts)

    queries_generator.insert_patients(patients)
    queries_generator.insert_staffs(staffs)
    queries_generator.insert_clinics(clinics)
    queries_generator.insert_wards(wards)
    queries_generator.insert_beds(beds)
    queries_generator.insert_ipts(ipts, wards, beds)
    queries_generator.insert_opts(opts)
    queries_generator.insert_appointments(appointments)
    queries_generator.insert_treatments(treatments)
    
    queries = queries_generator.get_queries()
    with open("queries.sql", "w", encoding="utf8") as queries_file:
        for query in queries:
            queries_file.write(query + "\n")

if __name__ == "__main__":
    main()
