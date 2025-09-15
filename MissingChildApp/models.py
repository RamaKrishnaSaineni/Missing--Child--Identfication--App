from django.db import models

# Gender choices
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

# Status choices
STATUS_CHOICES = (
    ('Missing', 'Missing'),
    ('Found', 'Found'),
)

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    last_seen = models.DateField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Missing')
    photo = models.ImageField(upload_to='child_photos/', blank=True, null=True)

    def _str_(self):
        return self.name

class Report(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    reporter_name = models.CharField(max_length=100)
    reporter_contact = models.CharField(max_length=15)
    report_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"Report for {self.child.name} by {self.reporter_name}"