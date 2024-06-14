from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
from rest_framework import generics
from rest_framework import viewsets, mixins

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


class CourseAPIViewSet(ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class TeacherAPIViewSet(ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer


class StartCourseAPIViewSet(ModelViewSet):
    queryset = models.StartCourse.objects.all()
    serializer_class = serializers.StartCourseSerializer


class LessonAPIViewSet(ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer



class LessonVideoAPIViewSet(ModelViewSet):
    queryset = models.LessonVideo.objects.all()
    serializer_class = serializers.LessonVideoSerializer


class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Camment.objects.all()
    serializer_class = serializers.CommentSerializer


class Filter(APIView):
    def get(self, request: Request):
        word = str(request.query_params.get('word'))
        lessons = models.Lesson.objects.filter(name__icontains=word)
        return Response({'lessons': serializers.LessonSerializer(lessons, many=True).data})
    

class LikeAPIview(APIView):
    def get(self, request):
        serializer = serializers.LikeSerializer()
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = serializers.LikeSerializer(data=request.data)
        serializer.is_valid()

        if serializer.validated_data.get('like') == True:
            value = True
        else:
            value = False
        lesson_id = serializer.validated_data.get('lesson')
        lesson = models.Lesson.objects.get(pk=lesson_id)


        try:
            like = models.Like.objects.get(
                lesson=lesson,
                user=request.user
            )
            like.delete()
        except:
            pass

        models.Like.objects.create(
            lesson=lesson,
            user=request.user,
            like_or_dislike=value
        )

        return Response()