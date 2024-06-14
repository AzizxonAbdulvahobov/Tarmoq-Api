from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()    
    price = models.FloatField(help_text="Bir oylik kurs narxi")
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.name 
    
    
    def total_price(self):
        """Total price of the course"""
        return self.price * self.duration

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    phone  = models.CharField(max_length=13)
    experience = models.IntegerField()
    img = models.ImageField(upload_to='teacher/img/', null=True, blank=True)

    def __str__(self):
        return self.full_name
    

class StartCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(User)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
   
    def __str__(self):
        return self.course.name

class Lesson(models.Model):
    course = models.ForeignKey(StartCourse, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class LessonVideo(models.Model):
    """Dars videolari uchun"""
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    video = models.FileField(upload_to='lesson/videos/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'WMV'])
    ])


class Camment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()


class Like(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like_or_dislike = models.BooleanField()