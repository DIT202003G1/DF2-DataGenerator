CREATE DATABASE SunwayGCH;

USE SunwayGCH;

CREATE TABLE Certification(
    cert_id char(8),
    cert_name varchar(256) NOT NULL,
    cert_type varchar(256) NOT NULL,
    PRIMARY KEY (cert_id)
);

CREATE TABLE Cert_Staff(
    cert_id char(8),
    sf_id char(8),
    cersf_date date NOT NULL,
    crtsf_institude varchar(256) NOT NULL,
    PRIMARY KEY (cert_id, sf_id)
);

CREATE TABLE WorkingExp(
    sf_id char(8),
    wexp_index int(8),
    wexp_organization varchar(256) NOT NULL,
    wexp_position varchar(256) NOT NULL,
    wexp_start_date date NOT NULL,
    wexp_time int(4),
    PRIMARY KEY (sf_id, wexp_index)
);

CREATE TABLE Staff(
    sf_id char(8),
    sf_first_name varchar(256) NOT NULL,
    sf_last_name varchar(256) NOT NULL,
    sf_address varchar(256) NOT NULL,
    sf_telephone varchar(11) NOT NULL,
    sf_birth_date date NOT NULL,
    sf_gender varchar(6) NOT NULL,
    sf_NIN char(9) NOT NULL,
    sf_position varchar(128) NOT NULL,
    sf_salary decimal(10,2) NOT NULL,
    sf_salary_scale decimal(10,2),
    PRIMARY KEY (sf_id)
);

CREATE TABLE Staff_Personnel_Officer(
    sf_id char(8),
    PRIMARY KEY (sf_id)
);

CREATE TABLE Staff_Nurse(
    sf_id char(8),
    PRIMARY KEY (sf_id)
);

CREATE TABLE Staff_Medical_Director(
    sf_id char(8),
    PRIMARY KEY (sf_id)
);

CREATE TABLE Staff_Long_Term(
    sf_id char(8),
    sflt_start_date date NOT NULL,
    PRIMARY KEY (sf_id)
);

CREATE TABLE Staff_Short_Term(
    sf_id char(8),
    sfst_start_date date,
    sfst_duration int(4),
    PRIMARY KEY (sf_id)
);

CREATE TABLE Patient(
    pt_id char(8),
    pt_first_name varchar(256) NOT NULL,
    pt_last_name varchar(256) NOT NULL,
    pt_address varchar(256) NOT NULL,
    pt_telephone varchar(11) NOT NULL,
    pt_birth_date date NOT NULL,
    pt_gender varchar(6) NOT NULL,
    pt_marital_status varchar(8) NOT NULL,
    pt_register_date date NOT NULL,
    PRIMARY KEY (pt_id)
);

CREATE TABLE pt_ntk(
    pt_id char(8),
    pt_ntx_index int(8),
    pt_ntx_first_name varchar(256) NOT NULL,
    pt_ntx_last_name varchar(256) NOT NULL,
    pt_ntx_relationship varchar(256) NOT NULL,
    pt_ntx_address varchar(256) NOT NULL,
    pt_ntx_telephone varchar(11) NOT NULL,
    PRIMARY KEY (pt_id, pt_ntx_index)
);

CREATE TABLE Out_Patient(
    pt_id char(8),
    opt_date date,
    opt_reason longtext NOT NULL,
    opt_is_done bit(1) NOT NULL DEFAULT 1,
    opt_clinic char(8) NOT NULL,
    PRIMARY KEY (opt_clinic)
);

CREATE TABLE In_Patient(
    pt_id char(8),
    ipt_wait_date date NOT NULL,
    ipt_in_date date,
    ipt_expected_duration int(4),
    ipt_out_date date,
    ipt_bed char(8),
    PRIMARY KEY (pt_id)
);

CREATE TABLE Patient_Appointment(
    pa_id char(8),
    pa_date date NOT NULL,
    pa_time time NOT NULL,
    pa_patient char(8) NOT NULL,
    pa_consultant char(8) NOT NULL,
    PRIMARY KEY (pa_id)
);

CREATE TABLE Patient_Treatment(
    ptr_id char(8),
    ptr_units_per_day int(2) NOT NULL,
    ptr_start_date date NOT NULL,
    ptr_duration int(4) NOT NULL,
    ptr_drug char(8) NOT NULL,
    ptr_patient char(8) NOT NULL,
    PRIMARY KEY (ptr_id)
);

CREATE TABLE Suppliers(
    splr_id char(8),
    splr_name varchar(256) NOT NULL,
    splr_address varchar(256) NOT NULL,
    splr_telephone varchar(11) NOT NULL,
    splr_fax varchar(11) NOT NULL,
    PRIMARY KEY (splr_id)
);

CREATE TABLE Supply(
    sply_id char(8),
    sply_quantity int(4) NOT NULL,
    sply_reorder_level int(4),
    sply_cost decimal(10,2) NOT NULL,
    sply_splr char(8) NOT NULL,
    sply_director char(8) NOT NULL,
    PRIMARY KEY (sply_id)
);

CREATE TABLE Supply_Equipment(
    sply_id char(8),
    eqm_type varchar(256) NOT NULL,
    eqm_size varchar(64) NOT NULL,
    PRIMARY KEY (sply_id)
);

CREATE TABLE Supply_Drug(
    sply_id char(8),
    drug_type_method varchar(64) NOT NULL,
    drug_dose_per_unit decimal(10,2) NOT NULL,
    PRIMARY KEY (sply_id)
);

CREATE TABLE Room(
    room_id char(8),
    room_location varchar(64) NOT NULL,
    PRIMARY KEY (room_id)
);

CREATE TABLE Bed(
    bed_id char(8),
    bed_type varchar(64) NOT NULL,
    room_id char(8) NOT NULL,
    PRIMARY KEY (bed_id)
);

CREATE TABLE Clinic(
    room_id char(8),
    PRIMARY KEY (room_id)
);

CREATE TABLE Ward(
    room_id char(8),
    room_nurse char(8) NOT NULL,
    PRIMARY KEY (room_id)
);