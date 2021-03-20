queries = []

def get_queries():
    return queries



def format_date(date):
    return "-".join(map(str, date))

def format_time(time):
    return ":".join(map(str, time))

def format_telephone(telephone):
    return f'"{telephone}"' if telephone else "null"

def format_queries(query_template, values):
    return query_template.format(",\n    ".join(values))



INSERT_PATIENT_NTK_TEMPLATE = """INSERT INTO pt_ntk VALUES
    {};"""

INSERT_PATIENTS_TEMPLATE = """INSERT INTO patient VALUES
    {};"""

ntk_index = 0
def insert_patients(patients = {}):
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



INSERT_STAFFS_TEMPLATE = """INSERT INTO staff VALUES
    {};"""

INSERT_WORKING_EXP_TEMPLATE = """INSERT INTO working_exp VALUES
    {};"""

def insert_staffs(staffs = {}):
    staffs_value_list = []
    working_experiences_value_list = []

    for id, staff_data in staffs.items():
        staffs_value_list.append(
            '("{}", "{}", "{}", "{}", {}, "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(
                id,
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
                "SF000000"
            )
        )

        for wexp in staff_data["wexp"]:
            org = wexp[0]
            pos = wexp[1]
            start = wexp[2]
            duration = wexp[3]

            working_experiences_value_list.append(
                '("{}", "{}", "{}", "{}", "{}")'.format(
                    id,
                    format_date(start),
                    org,
                    pos,
                    duration
                )
            )
    
    queries.append(format_queries(INSERT_STAFFS_TEMPLATE, staffs_value_list))
    queries.append(format_queries(INSERT_WORKING_EXP_TEMPLATE, working_experiences_value_list))



INSERT_OPTS_TEMPLATE = """INSERT INTO out_patient VALUES
    {};"""

opt_index = 0
def insert_opts(opts = []):
    global opt_index
    opts_value_list = []

    for opt in opts:
        opts_value_list.append(
            '("{}", "{}", "{}", "{}", "{}")'.format(
                opt["PID"],
                opt_index,
                format_date(opt["date"]),
                opt["reason"],
                opt["clinic"]
            )
        )
        
        opt_index += 1
    
    queries.append(format_queries(INSERT_OPTS_TEMPLATE, opts_value_list))



INSERT_IPTS_TEMPLATE = """INSERT INTO in_patient VALUES
    {};"""

def insert_ipts(ipts = {}, wards = {}, beds = {}):
    ipts_value_list = []

    for ipt in ipts:
        ward_id = random.choice(wards.keys())
        beds_in_ward = [bed_id for bed_id, bed_data in beds if bed_data["ward"] == ward_id]
        bed_id = random.choice(beds_in_ward)

        ipts_value_list.append(
            '("{}", "{}", "{}", "{}", "{}", "{}")'.format(
                ipt["PID"],
                format_date(ipt["waitDate"]),
                format_date(ipt["inDate"]),
                ipt["expectedDuration"],
                format_date(ipt["outDate"]),
                bed_id
            )
        )
    
    queries.append(format_queries(INSERT_IPTS_TEMPLATE, ipts_value_list))



INSERT_APPOINTMENTS_TEMPLATE = """INSERT INTO patient_appointment VALUES
    {};"""

def insert_appointments(appointments = {}):
    appointments_value_list = []

    for appointment_id, appointment_date in appointments:
        appointments_value_list.append(
            '("{}", "{}", "{}", "{}", "{}", "{}")'.format(
                appointment_id,
                appointment_date["date"],
                appointment_date["room"],
                format_time(appointment_date["time"]),
                appointment_date["PID"],
                appointment_date["SID"]
            )
        )
    
    queries.append(format_queries(INSERT_APPOINTMENTS_TEMPLATE, appointments_value_list))
