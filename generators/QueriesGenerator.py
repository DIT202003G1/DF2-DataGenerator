queries = []

def format_date(date):
    return "-".join(map(str, date))

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
    patients_value_list = []
    patient_ntks_value_list = []

    for id, patient_data in patients.items():
        patients_value_list.append(
            '("{}", "{}", "{}", "{}", {}, "{}", "{}", "{}", "{}")'.format(
                id,
                patient_data.get("firstName"),
                patient_data.get("lastName"),
                patient_data.get("address"),
                format_telephone(patient_data.get("telephone")),
                format_date(patient_data.get("birthdate")),
                patient_data.get("gender"),
                patient_data.get("marital"),
                format_date(patient_data.get("register")),
            )
        )
        
        for ntk in patient_data.get("ntk"):
            global ntk_index
            patient_ntks_value_list.append(
                '("{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(
                    id,
                    ntk_index,
                    ntk.get("firstName"),
                    ntk.get("lastName"),
                    ntk.get("relationship"),
                    ntk.get("address"),
                    ntk.get("telephone")
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
                staff_data.get("firstName"),
                staff_data.get("lastName"),
                staff_data.get("address"),
                format_telephone(staff_data.get("telephone")),
                format_date(staff_data.get("birthdate")),
                staff_data.get("gender"),
                staff_data.get("NIN"),
                staff_data.get("position"),
                staff_data.get("salary"),
                staff_data.get("salaryScale"),
                "SF000000"
            )
        )

        for wexp in staff_data.get("wexp"):
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

def get_queries():
    return queries
