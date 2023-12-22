
from django.db import models
from django.contrib.auth.models import User


class TestResult(models.Model):
    username = models.CharField(max_length=255)
    testname = models.CharField(max_length=255)
    result = models.IntegerField()

    def save_result(self):
        existing_entry = TestResult.objects.filter(username=self.username, testname=self.testname).first()
        if existing_entry:
            # If entry exists, update the result
            existing_entry.result = self.result
            existing_entry.save()
        else:
            # If entry doesn't exist, create a new one
            self.save()

    def __str__(self):
        return f"{self.username} - {self.testname} - {self.result}"




class TestResult1(models.Model):
    username1 = models.CharField(max_length=255)
    testname1 = models.CharField(max_length=255)
    result1 = models.IntegerField()

    def save_result1(self):
        existing_entry = TestResult1.objects.filter(username1=self.username1, testname1=self.testname1).first()
        if existing_entry:
            # If entry exists, update the result
            existing_entry.result1 = self.result1
            existing_entry.save()
        else:
            # If entry doesn't exist, create a new one
            self.save()

    def __str__(self):
        return f"{self.username1} - {self.testname1} - {self.result1}"
    

class TestResult2(models.Model):
    username2 = models.CharField(max_length=255)
    testname2 = models.CharField(max_length=255)
    result2 = models.IntegerField()

    def save_result2(self):
        existing_entry = TestResult2.objects.filter(username2=self.username2, testname2=self.testname2).first()
        if existing_entry:
            # If entry exists, update the result
            existing_entry.result2 = self.result2
            existing_entry.save()
        else:
            # If entry doesn't exist, create a new one
            self.save()

    def __str__(self):
        return f"{self.username2} - {self.testname2} - {self.result2}"
    


# class TestResult21(models.Model):
#     username21 = models.CharField(max_length=255)
#     testname21 = models.CharField(max_length=255)
#     result21 = models.IntegerField()

#     def save_result21(self):
#         existing_entry = TestResult21.objects.filter(username21=self.username21, testname21=self.testname21).first()
#         if existing_entry:
#             # If entry exists, update the result
#             existing_entry.result21 = self.result21
#             existing_entry.save()
#         else:
#             # If entry doesn't exist, create a new one
#             self.save()

#     def __str__(self):
#         return f"{self.username21} - {self.testname21} - {self.result21}"
    


# class TestResult22(models.Model):
#     username22 = models.CharField(max_length=255)
#     testname22 = models.CharField(max_length=255)
#     result22 = models.IntegerField()

#     def save_result22(self):
#         existing_entry = TestResult22.objects.filter(username22=self.username22, testname22=self.testname222).first()
#         if existing_entry:
#             # If entry exists, update the result
#             existing_entry.result22 = self.result22
#             existing_entry.save()
#         else:
#             # If entry doesn't exist, create a new one
#             self.save()

#     def __str__(self):
#         return f"{self.username22} - {self.testname22} - {self.result22}"
    
