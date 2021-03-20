CREATE DATABASE SunwayGCH;

USE SunwayGCH;

CREATE TABLE cert_staff (
    sf_id CHAR(8),
    cert_date DATE,
    cert_institute VARCHAR(128),
    cert_type VARCHAR(128),
    PRIMARY KEY (sf_id, cert_date)
);

CREATE TABLE working_exp (
    sf_id CHAR(8),
    wexp_index INT(4),
    wexp_oragnization VARCHAR(128),
    wexp_position VARCHAR(128),
    wexp_start_date DATE,
    wexp_time INT(5),
    PRIMARY KEY (sf_id, wexp_index)
);

CREATE TABLE staff (
    sf_id CHAR(8),
    sf_first_name VARCHAR(128),
    sf_last_name VARCHAR(128),
    sf_address VARCHAR(128),
    sf_telephone VARCHAR(11),
    sf_birth_date DATE,
    sf_gender VARCHAR(10),
    sf_NIN CHAR(8),
    sf_position VARCHAR(128),
    sf_salary DECIMAL(10, 2),
    sf_salary_scale CHAR(2),
    sf_manager CHAR(8),
    PRIMARY KEY (sf_id)
);

CREATE TABLE staff_long_term (
    sf_id CHAR(8),
    sflt_start_date DATE
);

CREATE TABLE staff_short_term (
    sf_id CHAR(8),
    sfst_start_date DATE,
    sfst_duration INT(5)
);

CREATE TABLE patient (
    pt_id CHAR(8),
    pt_first_name VARCHAR(128),
    pt_last_name VARCHAR(128),
    pt_address VARCHAR(128),
    pt_telephone VARCHAR(11),
    pt_birth_date DATE,
    pt_gender VARCHAR(10),
    pt_marital_status VARCHAR(10),
    pt_register_date DATE,
    PRIMARY KEY (pt_id)
);

CREATE TABLE pt_ntk (
    pt_id CHAR(8),
    pt_ntk_index INT(4),
    pt_ntk_first_name VARCHAR(128),
    pt_ntk_last_name VARCHAR(128),
    pt_ntk_relationship VARCHAR(128),
    pt_ntk_address VARCHAR(128),
    pt_ntk_telephone VARCHAR(11),
    PRIMARY KEY (pt_id, pt_ntk_index)
);

CREATE TABLE out_patient (
    pt_id CHAR(8),
    opt_date DATE,
    opt_reason VARCHAR(128),
    opt_clinic CHAR(8),
    PRIMARY KEY (pt_id)
);

CREATE TABLE in_patient (
    pt_id CHAR(8),
    ipt_wait_date DATE,
    ipt_in_date DATE,
    ipt_expected_duration INT(5),
    ipt_out_date DATE,
    ipt_bed CHAR(8),
    PRIMARY KEY (pt_id)
);

CREATE TABLE patient_appointment (
    pa_id CHAR(8),
    pa_date DATE,
    pa_room_number CHAR(8),
    pa_time TIME,
    pa_patient CHAR(8),
    pa_consultant CHAR(8),
    PRIMARY KEY (pa_id)
);

CREATE TABLE patient_treatment (
    ptr_id CHAR(8),
    ptr_units_per_day INT(2),
    ptr_start_date DATE,
    ptr_duration INT(5),
    ptr_drug CHAR(8),
    ptr_patient CHAR(8),
    PRIMARY KEY (ptr_id)
);

CREATE TABLE suppliers (
    splr_id CHAR(8),
    splr_name VARCHAR(128),
    splr_address VARCHAR(128),
    splr_telephone VARCHAR(11),
    splr_fax VARCHAR(10),
    PRIMARY KEY (splr_id)
);

CREATE TABLE supply (
    sply_id CHAR(8),
    sply_description VARCHAR(128),
    sply_quantity INT(4),
    sply_reorder_level INT(4),
    sply_cost DECIMAL(10, 2),
    sply_splr CHAR(8),
    sply_director CHAR(8),
    PRIMARY KEY (sply_id)
);

CREATE TABLE supply_equipment (
    sply_id CHAR(8),
    eqm_size VARCHAR(128),
    eqm_type VARCHAR(128),
    PRIMARY KEY (sply_id)
);

CREATE TABLE supply_drug (
    sply_id CHAR(8),
    drug_type_method VARCHAR(128),
    drug_dose_per_unit DECIMAL(7, 3),
    PRIMARY KEY (sply_id)
);

CREATE TABLE ward (
    ward_id CHAR(8),
    ward_ext CHAR(4),
    ward_name VARCHAR(128),
    ward_location VARCHAR(128),
    ward_nurse CHAR(8),
    PRIMARY KEY (ward_id)
);

CREATE TABLE clinic (
    clinic_id CHAR(8),
    clinic_name VARCHAR(128),
    PRIMARY KEY (clinic_id)
);

CREATE TABLE bed (
    bed_id CHAR(8),
    bed_type VARCHAR(128),
    bed_ward CHAR(8),
    PRIMARY KEY (bed_id)
);

ALTER TABLE cert_staff
ADD FOREIGN KEY (sf_id) REFERENCES staff(sf_id);

ALTER TABLE working_exp
ADD FOREIGN KEY (sf_id) REFERENCES staff(sf_id);

ALTER TABLE staff
ADD FOREIGN KEY (sf_manager) REFERENCES staff_personal_officer(sf_id);

ALTER TABLE staff_personal_officer
ADD FOREIGN KEY (sf_id) REFERENCES staff(sf_id);

ALTER TABLE staff_nurse
ADD FOREIGN KEY (sf_id) REFERENCES staff(sf_id);

ALTER TABLE staff_medical_director
ADD FOREIGN KEY (sf_id) REFERENCES staff(sf_id);

ALTER TABLE staff_long_term
ADD FOREIGN KEY (sf_id) REFERENCES staff(sf_id);

ALTER TABLE staff_short_term
ADD FOREIGN KEY (sf_id) REFERENCES staff(sf_id);

ALTER TABLE pt_ntk
ADD FOREIGN KEY (pt_id) REFERENCES patient(pt_id),
ADD FOREIGN KEY (pt_id) REFERENCES patient(pt_id);

ALTER TABLE out_patient
ADD FOREIGN KEY (opt_clinic) REFERENCES clinic(clinic_id);

ALTER TABLE in_patient
ADD FOREIGN KEY (ipt_bed) REFERENCES bed(bed_id);
ADD FOREIGN KEY (pt_id) REFERENCES patient(pt_id);

ALTER TABLE patient_appointment
ADD FOREIGN KEY (pa_patient) REFERENCES patient(pt_id),
ADD FOREIGN KEY (pa_consultant) REFERENCES out_patient(opt_clinic);

ALTER TABLE patient_treatment
ADD FOREIGN KEY (ptr_drug) REFERENCES supply_drug(sply_id),
ADD FOREIGN KEY (ptr_patient) REFERENCES patient(pt_id);

ALTER TABLE supply
ADD FOREIGN KEY (sply_splr) REFERENCES suppliers(splr_id),
ADD FOREIGN KEY (sply_director) REFERENCES staff_medical_director(sf_id);

ALTER TABLE supply_equipment
ADD FOREIGN KEY (sply_id) REFERENCES supply(sply_id);

ALTER TABLE supply_drug
ADD FOREIGN KEY (sply_id) REFERENCES supply(sply_id);

ALTER TABLE ward
ADD FOREIGN KEY (ward_nurse) REFERENCES staff_nurse(sf_id);

ALTER TABLE bed
ADD FOREIGN KEY (bed_ward) REFERENCES ward(ward_id);