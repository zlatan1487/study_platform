from rest_framework import serializers
from study.models import Course, Lesson, Payment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LessonSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.IntegerField(source='course.lesson_set.count', read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_number_of_lessons(self, obj):
        return obj.course.lessons.count()

    def to_representation(self, instance):
        data = super(LessonSerializer, self).to_representation(instance)
        data['number_of_lessons'] = self.get_number_of_lessons(instance)
        return data


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
