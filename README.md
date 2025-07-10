



## Dataset Structure

### hosp

All of the relevent features must be tied to a subject_id,
the patient

#### admissions.csv

**subject_id** : specific patient (couldnt have multipul hadm_id)
Integer

**hadm_id** : specific encounter id 
Integer

**Admission_type** : 
one-hot [EW EMER., EU OBSERVATION, URGENT, OBSERVATION ADMIT, SURGICAL SAME DAY ADMISSION, EU OBSERVATION, OTHER]

#### drgcodes.csv

