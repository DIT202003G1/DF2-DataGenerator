import random
from generators import dummy_generator

queries = []

def get_queries():
    return queries

def random_dict_element(d):
    key = random.choice(list(d.keys()))
    return key,d[key]

def format_date(date):
    return "-".join(map(str, date))

def format_nullable_date(date):
    if date:
        return f'"{format_date(date)}"'
    else:
        return "null"

def format_time(time):
    new_time = []
    for i in map(str, time):
        new_time.append("0"*(2 - len(i)) + i)
    return ":".join(new_time)

def format_telephone(telephone):
    return f'"{telephone}"' if telephone else "null"

def format_queries(query_template, values):
    return query_template.format(",\n    ".join(values))



INSERT_PATIENT_NTK_TEMPLATE = """INSERT INTO pt_ntk VALUES
    {};"""

INSERT_PATIENTS_TEMPLATE = """INSERT INTO patient VALUES
    {};"""

ntk_index = 0
def insert_patients(patients):
    global ntk_index
    patients_value_list = []
    patient_ntks_value_list = []

    for id, patient_data in patients.items():
        patients_value_list.append(
            '("{}", "{}", "{}", "{}", {}, "{}", "{}", "{}", "{}")'.format(
                id,
                patient_data["firstName"],
                patient_data["lastName"],
                patient_data["address"],
                format_telephone(patient_data["telephone"]),
                format_date(patient_data["birthdate"]),
                patient_data["gender"],
                patient_data["marital"],
                format_date(patient_data["register"]),
            )
        )
        
        for ntk in patient_data["ntk"]:
            patient_ntks_value_list.append(
                '("{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(
                    id,
                    ntk_index,
                    ntk["firstName"],
                    ntk["lastName"],
                    ntk["relationship"],
                    ntk["address"],
                    ntk["telephone"]
                )
            )

            ntk_index += 1
    
    queries.append(format_queries(INSERT_PATIENTS_TEMPLATE, patients_value_list))
    queries.append(format_queries(INSERT_PATIENT_NTK_TEMPLATE, patient_ntks_value_list))



INSERT_SUPPLIERS_TEMPLATE = """INSERT INTO suppliers VALUES
    {};"""

INSERT_SUPPLIES_TEMPLATE = """INSERT INTO supply VALUES
    {};"""

INSERT_DRUGS_TEMPLATE = """INSERT INTO supply_drug VALUES
    {};"""

INSERT_EQUIPMENTS_TEMPLATE = """INSERT INTO supply_equipment VALUES
    {};"""

def insert_suppliers(suppliers):
    suppliers_value_list = []

    for id, supplier_data in suppliers.items():
        suppliers_value_list.append(
            '("{}", "{}", "{}", "{}", "{}")'.format(
                id,
                supplier_data["name"],
                supplier_data["address"],
                supplier_data["telephone"],
                supplier_data["fax"],
            )
        )
    queries.append(format_queries(INSERT_SUPPLIERS_TEMPLATE, suppliers_value_list))

def insert_supplies(suppliers,staffs):
    supplies_value_list = []
    drugs_value_list = []
    equipments_value_list = []

    for supplier_id, supplier_data in suppliers.items():
        for equipment in supplier_data["equipments"]:
            """
               sply_id CHAR(8),
                eqm_size VARCHAR(128),
                eqm_type VARCHAR(128),
                PRIMARY KEY (sply_id)
            """
            while True:
                staff_director, staff_director_data = random_dict_element(staffs)
                if staff_director_data["position"] == "Medical Director":
                    break
            supplies_value_list.append(
                '("{}", "{}", {}, {}, "{}", "{}", "{}")'.format(
                    equipment[0],
                    equipment[2],
                    random.randint(100,500),
                    random.randint(1,5) * 100,
                    f"{random.randint(1,3)}{random.randint(0,9)}{random.randint(0,9)}.{random.randint(0,9)}{random.randint(0,9)}",
                    supplier_id,
                    staff_director,
                )
            )
            equipments_value_list.append(
                '("{}", "{}", "{}")'.format(
                    equipment[0],
                    equipment[1],
                    "First-aid",
                )
            )
        for drug in supplier_data["drugs"]:
            while True:
                staff_director, staff_director_data = random_dict_element(staffs)
                if staff_director_data["position"] == "Medical Director":
                    break
            supplies_value_list.append(
                '("{}","{}",{},{},"{}","{}","{}")'.format(
                    drug[0],
                    drug[1],
                    random.randint(1000,5000),
                    random.randint(1,5) * 1000,
                    f"{random.randint(1,3)}{random.randint(0,9)}{random.randint(0,9)}.{random.randint(0,9)}{random.randint(0,9)}",
                    supplier_id,
                    staff_director,
                )
            )
            drugs_value_list.append(
                '("{}", "{}", "{}")'.format(
                    drug[0],
                    random.choice(["Tablet","Liquid Ingestion","Liquid Injection","Topical"]),
                    drug[2],
                )
            )
    queries.append(format_queries(INSERT_SUPPLIES_TEMPLATE, supplies_value_list))
    queries.append(format_queries(INSERT_DRUGS_TEMPLATE, drugs_value_list))
    queries.append(format_queries(INSERT_EQUIPMENTS_TEMPLATE, equipments_value_list))



INSERT_STAFFS_TEMPLATE = """INSERT INTO staff VALUES
    {};"""

INSERT_WORKING_EXP_TEMPLATE = """INSERT INTO working_exp VALUES
    {};"""

INSERT_SHORT_TERM_STAFFS_TEMPLATE = """INSERT INTO staff_short_term VALUES
    {};"""

INSERT_LONG_TERM_STAFFS_TEMPLATE = """INSERT INTO staff_long_term VALUES
    {};"""

INSERT_CERT_STAFFS_TEMPLATE = """INSERT INTO cert_staff VALUES
    {};"""

def seperate_value_list(value_list):
    first_value_list = []
    second_value_list = []
    for value in value_list:
        if "null" in value:
            first_value_list.append(value)
        else:
            second_value_list.append(value)
    return first_value_list, second_value_list

def insert_staffs(staffs):
    staffs_value_list = []
    working_experiences_value_list = []
    short_term_staffs_value_list = []
    long_term_staffs_value_list = []
    cert_staffs_value_list = []

    for staff_id, staff_data in staffs.items():
        while True:
            staff_manager, staff_manager_data = random_dict_element(staffs)
            if staff_manager_data["position"] == "Personnel Officer":
                break
        
        staffs_value_list.append(
            '("{}", "{}", "{}", "{}", {}, "{}", "{}", "{}", "{}", "{}", "{}", {})'.format(
                staff_id,
                staff_data["firstName"],
                staff_data["lastName"],
                staff_data["address"],
                format_telephone(staff_data["telephone"]),
                format_date(staff_data["birthdate"]),
                staff_data["gender"],
                staff_data["NIN"],
                staff_data["position"],
                staff_data["salary"],
                staff_data["salaryScale"],
                f'"{staff_manager}"' if staff_data["position"] != "Personnel Officer" else "null",
            )
        )

        for wexp in staff_data["wexp"]:
            org = wexp[0]
            pos = wexp[1]
            start = wexp[2]
            duration = wexp[3]

            working_experiences_value_list.append(
                '("{}", "{}", "{}", "{}", "{}")'.format(
                    staff_id,
                    format_date(start),
                    org,
                    pos,
                    duration
                )
            )

        if staff_data["contract"] == "short":
            short_term_staffs_value_list.append(
                '("{}", "{}", "{}")'.format(
                    staff_id,
                    format_date(staff_data["contractStart"]),
                    staff_data["duration"]
                )
            )
        elif staff_data["contract"] == "long":
            long_term_staffs_value_list.append(
                '("{}", "{}")'.format(
                    staff_id,
                    format_date(staff_data["contractStart"])
                )
            )

        cert_staffs_value_list.append(
            '("{}", "{}", "{}", "{}")'.format(
                staff_id,
                format_date(staff_data["qualification_date"]),
                staff_data["qualification_institute"],
                staff_data["qualification_type"]
            )
        )
    
    first_staffs_value_list, second_staffs_value_list = seperate_value_list(staffs_value_list)
    queries.append(format_queries(INSERT_STAFFS_TEMPLATE, first_staffs_value_list))
    queries.append(format_queries(INSERT_STAFFS_TEMPLATE, second_staffs_value_list))
    queries.append(format_queries(INSERT_WORKING_EXP_TEMPLATE, working_experiences_value_list))
    queries.append(format_queries(INSERT_SHORT_TERM_STAFFS_TEMPLATE, short_term_staffs_value_list))
    queries.append(format_queries(INSERT_LONG_TERM_STAFFS_TEMPLATE, long_term_staffs_value_list))
    queries.append(format_queries(INSERT_CERT_STAFFS_TEMPLATE, cert_staffs_value_list))



INSERT_OPTS_TEMPLATE = """INSERT INTO out_patient VALUES
    {};"""

opt_index = 0
def insert_opts(opts):
    global opt_index
    opts_value_list = []

    for opt_id, opt_data in opts.items():
        opts_value_list.append(
            '("{}", "{}", "{}", "{}", "{}")'.format(
                opt_id,
                opt_index,
                format_date(opt_data["date"]),
                opt_data["reason"],
                opt_data["clinic"]
            )
        )
        
        opt_index += 1
    
    queries.append(format_queries(INSERT_OPTS_TEMPLATE, opts_value_list))



INSERT_IPTS_TEMPLATE = """INSERT INTO in_patient VALUES
    {};"""

def insert_ipts(ipts, wards, beds):
    ipts_value_list = []

    for ipt_id, ipt_data in ipts.items():
        ward_id = random.choice(list(wards.keys()))
        beds_in_ward = [bed_id for bed_id, bed_data in beds.items() if bed_data["ward"] == ward_id]
        bed_id = random.choice(beds_in_ward)
        if ipt_data["inDate"]:
            expected_ward = beds[bed_id]["ward"]
        else:
            expected_ward, _ = random_dict_element(wards)
        ipts_value_list.append(
            '("{}", "{}", {}, {}, "{}", {}, {})'.format(
                ipt_id,
                format_date(ipt_data["waitDate"]),
                format_nullable_date(ipt_data["inDate"]),
                ipt_data["expectedDuration"],
                expected_ward,
                format_nullable_date(ipt_data["outDate"]),
                f'"{bed_id}"' if ipt_data["inDate"] else "null"
            )
        )
    
    queries.append(format_queries(INSERT_IPTS_TEMPLATE, ipts_value_list))



INSERT_APPOINTMENTS_TEMPLATE = """INSERT INTO patient_appointment VALUES
    {};"""

def insert_appointments(appointments):
    appointments_value_list = []

    for appointment_id, appointment_date in appointments.items():
        appointments_value_list.append(
            '("{}", "{}", "{}", "{}", "{}", "{}")'.format(
                appointment_id,
                format_date(appointment_date["date"]),
                appointment_date["room"],
                format_time(appointment_date["time"]),
                appointment_date["PID"],
                appointment_date["SID"]
            )
        )
    
    queries.append(format_queries(INSERT_APPOINTMENTS_TEMPLATE, appointments_value_list))



INSERT_CLINICS_TEMPLATE = """INSERT INTO clinic VALUES
    {};"""

def insert_clinics(clinics):
    clinics_value_list = []

    for clinic_id, clinic_data in clinics.items():
        clinics_value_list.append(
            '("{}", "{}")'.format(
                clinic_id,
                clinic_data["name"]
            )
        )
    
    queries.append(format_queries(INSERT_CLINICS_TEMPLATE, clinics_value_list))



INSERT_WARDS_TEMPLATE = """INSERT INTO ward VALUES
    {};"""

def insert_wards(wards):
    wards_value_list = []

    for ward_id, ward_data in wards.items():
        wards_value_list.append(
            '("{}", "{}", "{}", "{}", "{}")'.format(
                ward_id,
                ward_data["ext"],
                ward_data["name"],
                ward_data["location"],
                ward_data["nurse"]
            )
        )
    
    queries.append(format_queries(INSERT_WARDS_TEMPLATE, wards_value_list))



INSERT_BEDS_TEMPLATE = """INSERT INTO bed VALUES
    {};"""

def insert_beds(beds):
    beds_value_list = []
    
    for bed_id, bed_data in beds.items():
        beds_value_list.append(
            '("{}", "{}", "{}")'.format(
                bed_id,
                bed_data["type"],
                bed_data["ward"]
            )
        )
    
    queries.append(format_queries(INSERT_BEDS_TEMPLATE, beds_value_list))



INSERT_TREATMENTS_TEMPLATE = """INSERT INTO patient_treatment VALUES
    {};"""

def insert_treatments(treatments):
    treatments_value_list = []

    for treatment_id, treatment_data in treatments.items():
        treatments_value_list.append(
            '("{}", "{}", "{}", "{}", "{}", "{}")'.format(
                treatment_id,
                treatment_data["unitsPerDay"],
                format_date(treatment_data["start"]),
                treatment_data["duration"],
                treatment_data["drug"],
                treatment_data["patient"]
            )
        )
    
    queries.append(format_queries(INSERT_TREATMENTS_TEMPLATE, treatments_value_list))
    