from django.db import models

gender_choices =(
    ("MALE","MALE"),
    ("FEMALE","FEMALE"),
    ("OTHERS","OTHERS")
)



class basic_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)    
    firstname= models.CharField(max_length=100,null=True)
    lastname= models.CharField(max_length=100,null=True)
    emailaddress= models.CharField(max_length=100,null=True)
    mobilenumber= models.CharField(max_length=100,null=True)
    DOB= models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=20,choices=gender_choices,default='MALE')
    
class other_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)    
    fathername= models.CharField(max_length=100,null=True)
    mothername= models.CharField(max_length=100,null=True)
    address= models.CharField(max_length=100,null=True)
    city= models.CharField(max_length=100,null=True)
    pincode= models.CharField(max_length=100,null=True)
    aadharnumber= models.CharField(max_length=100,null=True)
    drivinglicencenumber= models.CharField(max_length=100,null=True)
    emergencycontactname= models.CharField(max_length=100,null=True)
    emergencycontactnumber= models.CharField(max_length=100,null=True)

class education_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    qualification=models.CharField(max_length=100,null=True)
    institute=models.CharField(max_length=100,null=True)
    year=models.IntegerField(null=True)
    percent=models.IntegerField(null=True)

class experience_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    company=models.CharField(max_length=100,null=True)
    from_date=models.CharField(max_length=100,null=True)
    to_date=models.CharField(max_length=100,null=True)
    position=models.CharField(max_length=100,null=True)
    reason=models.CharField(max_length=100,null=True)

    
    

class salary1(models.Model): 
    employee_id=models.CharField(max_length=100,null=True)    
    Designation=models.CharField(max_length=100,null=True)
    salary=models.CharField(max_length=100,null=True)
    dateofjoin=models.CharField(max_length=100,null=True)


class salary2(models.Model):
    employee_id=models.CharField(max_length=100,null=True)    
    Accountnumber=models.CharField(max_length=100,null=True)
    Bankname=models.CharField(max_length=100,null=True)
    Bankaddress=models.CharField(max_length=100,null=True)
    IFSCcode=models.CharField(max_length=100,null=True)


"""class lead(models.Model):
    Companyname= models.CharField(max_length=100,null=True)
    Companynumber= models.CharField(max_length=100,null=True)
    Companywebsite= models.CharField(max_length=100,null=True)
    Firstname= models.CharField(max_length=100,null=True)
    Lastname= models.CharField(max_length=100,null=True)
    Designation= models.CharField(max_length=100,null=True)
    Phonenumber= models.CharField(max_length=100,null=True)
    CompanyCategory= models.CharField(max_length=100,null=True)
    CompanyType= models.CharField(max_length=100,null=True)
    CompanySize= models.CharField(max_length=100,null=True)
    CompanyRevenue= models.CharField(max_length=100,null=True)
    FacebookLink= models.CharField(max_length=100,null=True)
    TwitterLink= models.CharField(max_length=100,null=True)
    LinkedIN= models.CharField(max_length=100,null=True)
    DetailFrom= models.CharField(max_length=100,null=True)"""

