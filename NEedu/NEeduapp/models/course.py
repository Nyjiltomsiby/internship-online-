from django.db import models
from django.utils import timezone




class Mentor(models.Model):

    name = models.CharField(max_length=50, null=False)
    bio = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to="files/mentor_profile", null=True)
    designation= models.CharField(max_length=50, null=True)
    

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50, null=False)
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="files/thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to="files/resource")

    def total_duration(self):
        total_duration_seconds = sum([video.duration_hours * 3600 + video.duration_minutes * 60
                                      for video in self.video_set.all()])
        hours, remainder = divmod(total_duration_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours} hours {minutes} minutes"

    def __str__(self):
        return self.name
    
    def num_students_enrolled(self):
        return self.usercourse_set.count()
    
    
class CourseProperty(models.Model):
    description = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass
