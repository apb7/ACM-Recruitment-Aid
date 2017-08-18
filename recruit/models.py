from django.db import models

class Recruit(models.Model):
    name=models.CharField(max_length=200)
    student_id=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=20)
    skills=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Member(models.Model):
    recruit=models.ForeignKey(Recruit, on_delete=models.CASCADE,blank=True,null=True)
    remarks=models.CharField(max_length=1000)
    grilled_by=models.CharField(max_length=200)
    task=models.CharField(max_length=200)
    task_status=models.BooleanField(default=False)
    def __str__(self):
        return self.grilled_by
