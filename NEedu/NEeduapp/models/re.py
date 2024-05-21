from django.db import models
from NEeduapp.models.course import Course
from NEeduapp.models.course import Mentor

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)  # Rating out of 5
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.course.name} by {self.mentor.name}"


class Testimonial(models.Model):
    course = models.ForeignKey(Course,null=True, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Testimonial for {self.course.name}"

