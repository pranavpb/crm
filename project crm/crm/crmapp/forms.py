from django import forms
from .models import *

class basic_details_form(forms.ModelForm):   
    class Meta:
        model = basic_details
        fields=['firstname','lastname','mobilenumber','DOB','emailaddress','gender']
        widgets={
            
            'firstname': forms.TextInput(attrs={'class': 'form-control','placeholder':'firstname'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control','placeholder':'lastname'}),
            'emailaddress': forms.TextInput(attrs={'class': 'form-control','placeholder':'emailaddress'}),
            'mobilenumber': forms.TextInput(attrs={'class': 'form-control','placeholder':'mobilenumber'}),
            'DOB':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),
            'gender':forms.RadioSelect(choices=gender_choices,attrs={}),            
        }
class others_form(forms.ModelForm):
    class Meta:
        model = other_details
        fields=['fathername','mothername','address','city','pincode','aadharnumber','drivinglicencenumber','emergencycontactnumber','emergencycontactname']
        widgets={
            'fathername': forms.TextInput(attrs={'class': 'form-control','placeholder':'fathername'}),
            'mothername': forms.TextInput(attrs={'class': 'form-control','placeholder':'mothername'}),
            'address': forms.Textarea(attrs={'class': 'form-control','placeholder':'address','rows':'5'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'city'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control','placeholder':'pincode'}),
            'aadharnumber': forms.TextInput(attrs={'class': 'form-control','placeholder':'aadharnumber'}),
            'drivinglicencenumber': forms.TextInput(attrs={'class': 'form-control','placeholder':'drivinglicencenumber'}),
            'emergencycontactnumber': forms.TextInput(attrs={'class': 'form-control','placeholder':'emergencycontactnumber'}),
            'emergencycontactname': forms.TextInput(attrs={'class': 'form-control','placeholder':'emergencycontactname'}),

        } 
            
            
class salary1_details_form(forms.ModelForm):
    class Meta:
        model = salary1
        fields=['Designation','salary','dateofjoin']
        widgets={            
            'Designation': forms.TextInput(attrs={'class': 'form-control','placeholder':'Designation'}),
            'salary': forms.TextInput(attrs={'class': 'form-control','placeholder':'salary'}),
            'dateofjoin':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),            
        }
        
class salary2_details_form(forms.ModelForm):
    class Meta:
        model = salary2
        fields=['Accountnumber','IFSCcode','Bankname','Bankaddress']
        widgets={

            'Accountnumber': forms.TextInput(attrs={'class': 'form-control','placeholder':'AccountNumber'}),
            'IFSCcode': forms.TextInput(attrs={'class': 'form-control','placeholder':'IFSCcode'}),
            'Bankname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Bankname'}),
            'Bankaddress': forms.TextInput(attrs={'class': 'form-control','placeholder':'Bankaddress'}),
        }

"""CompanyCategory={
    ("public","public"),
    ("private","private"),
}
class lead_form(forms.ModelForm):
    class Meta:
        model = lead
        fields=['Firstname','Lastname','Companyname','Companynumber','Companywebsite','Designation','Phonenumber','CompanyCategory','CompanyType','CompanySize','CompanyRevenue','FacebookLink','TwitterLink','LinkedIN','DetailFrom']
        widgets={
        'Firstname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Firstname'}),
        'Lastname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Lastname'}),
        'Companyname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Companyname'}),
        'Companynumber': forms.TextInput(attrs={'class': 'form-control','placeholder':'Companynumber'}),
        'Companywebsite': forms.TextInput(attrs={'class': 'form-control','placeholder':'Companywebsite'}),
        'Designation': forms.TextInput(attrs={'class': 'form-control','placeholder':'Designation'}),
        'Phonenumber': forms.TextInput(attrs={'class': 'form-control','placeholder':'Phonenumber'}),
        'CompanyCategory': forms.Select(choices=CompanyCategory,attrs={'class': 'form-control','placeholder':'CompanyCategory'}),
        'CompanyType': forms.TextInput(attrs={'class': 'form-control','placeholder':'CompanyType'}),
        'CompanySize': forms.TextInput(attrs={'class': 'form-control','placeholder':'CompanySize'}),
        'CompanyRevenue': forms.TextInput(attrs={'class': 'form-control','placeholder':'CompanyRevenue'}),
        'FacebookLink': forms.TextInput(attrs={'class': 'form-control','placeholder':'FacebookLink'}),
        'TwitterLink': forms.TextInput(attrs={'class': 'form-control','placeholder':'TwitterLink'}),
        'LinkedIN': forms.TextInput(attrs={'class': 'form-control','placeholder':'LinkedIN'}),
        'DetailFrom': forms.TextInput(attrs={'class': 'form-control','placeholder':'DetailFrom'}),


            
        }"""
            

        


         
