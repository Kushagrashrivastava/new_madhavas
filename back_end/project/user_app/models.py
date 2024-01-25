from django.db import models
from main_app.models import CustomUser
from main_app.models import gender_choices

# Create your models here.


document_choice = (
    ('Aadhar Card', 'Aadhar Card'),
    ('Pan Card', 'Pan Card'),
    ('Voter Id', 'Voter Id'),
    ('Health Card', 'Health Card'),
    ('ABC', 'ABC'),
    ('Driving Licience', 'Driving Licience'),
    ('10th Marksheet', '10th Marksheet'),
    ('12th Marksheet', '12th Marksheet'),
    ('Migration', 'Migration'),
    ('Trancerfer Certificate', 'Trancerfer Certificate'),
    ('Marksheet', 'Marksheet'),
    ('GAP Certificate', 'GAP Certificate'),
    ('Admission Slip', 'Admission Slip'),
    ('Domacile', 'Domacile'),
    ('Income', 'Income'),
    ('Caste', 'Caste'),
    ('Samagra', 'Samagra'),
    ('Bank Passbook', 'Bank Passbook'),

)


class UploadForm(models.Model):

    document_type = models.CharField(max_length=100, choices=document_choice)

    document_number = models.BigIntegerField()

    document = models.FileField(upload_to='documents')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('document_type', 'user')


form_status = (
    ('1', 'Filled'),
    ('2', 'Institute Verified'),
    ('3', 'Government Verified'),
    ('4', 'Money Scentioned'),
    ('5', 'Money Deposited')
)

class ScolarShipFormModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Personal Information
    highersecondarypercentage = models.IntegerField()

    transfercertificate = models.IntegerField()

    gapcertificate = models.IntegerField()

    secondaryclasspercentage = models.IntegerField()
    
    lastyearmarksheet = models.IntegerField()
    accountholdername = models.CharField(max_length=200)
    accountnumber = models.IntegerField()
        
    isfcnumber = models.CharField(max_length=200)
    
    name = models.CharField(max_length=200)

    dateOfBirth = models.DateField()

    Fathername = models.CharField(max_length=200)

    Gender = models.CharField(max_length=200, choices=gender_choices)

    Address = models.CharField(max_length=200)

    PinCode = models.IntegerField()

    MobileNUmber = models.IntegerField()

    EmailAddress = models.EmailField()

    MaritalStatus = models.CharField(max_length=200)
      
    CasteCertificate = models.CharField(max_length=200)

    CasteCertificateUpload = models.FileField(upload_to='scholarship')

    DomicileCertificate = models.CharField(max_length=200)

    DomicileCertificateUpload = models.FileField(upload_to='scholarship')

    VOterID = models.CharField(max_length=200)

    PanCard = models.CharField(max_length=200)

    SSmID = models.CharField(max_length=200)

    IncomeCertificate = models.CharField(max_length=200)

    IncomeCertificateUpload = models.FileField(upload_to='scholarship')

    status = models.CharField(max_length=10, choices=form_status, default='1')
