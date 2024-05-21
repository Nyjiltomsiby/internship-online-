from django.db import models
from NEeduapp.models import Course
from NEeduapp.models.course import Mentor

class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=100, null=False)
    is_preview = models.BooleanField(default=False)
    duration_hours = models.IntegerField(default=0)  # Duration field for hours
    duration_minutes = models.IntegerField(default=0)  # Duration field for minutes


    def __str__(self):
        return self.title
