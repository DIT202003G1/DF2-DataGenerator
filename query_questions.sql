select ipt.*, w.ward_name 
from (in_patient as ipt), (ward as w) 
where ipt.ipt_in_date is null 
and w.ward_id = ipt.ipt_expected_ward;

select w.ward_id, w.ward_name,COUNT(pt_id)
from (ward as w), (in_patient as ipt), (bed as b) 
where ipt.ipt_bed = b.bed_id 
and b.bed_ward = w.ward_id
group by w.ward_id;

select w.ward_id, w.ward_name, COUNT(b.bed_id)
from (ward as w), (bed as b), (
	select w.ward_id, b.bed_id
	from (in_patient as ipt), (ward as w), (bed as b) 
	where ipt_in_date is not null
	and ipt_out_date is null
	and w.ward_id = b.bed_ward
	and b.bed_id = ipt.ipt_bed
) as tmp
where w.ward_id = b.bed_ward
and b.bed_id != tmp.bed_id
group by w.ward_id;

select *
from patient
where pt_gender = "Male"
and (pt_birth_date between "1981-03-21" and "1991-03-21")
order by pt_first_name, pt_gender;

select pa.pa_id, pt.pt_id, pt.pt_first_name, pt.pt_last_name, s.sf_id, s.sf_first_name, s.sf_last_name
from (patient_appointment as pa), (patient as pt), (staff as s)
where pa.pa_patient = pt.pt_id
and pa.pa_consultant = s.sf_id
and (
	s.sf_first_name like "J%"
	or s.sf_first_name like "A%"
);

select ptr.ptr_id, p.pt_id, s.sply_description, ptr.ptr_units_per_day
from (supply as s), (supply_drug as d), (patient_treatment as ptr), (patient as p)
where s.sply_id = d.sply_id
and ptr.ptr_drug = d.sply_id
and ptr.ptr_patient = p.pt_id