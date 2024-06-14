from . import models
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'


class StartCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StartCourse
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'


class LessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LessonVideo
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Camment
        fields = '__all__'

class LikeSerializer(serializers.Serializer):
    lesson = serializers.IntegerField()
    like = serializers.BooleanField()
    dislike = serializers.BooleanField()