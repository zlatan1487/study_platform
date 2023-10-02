from rest_framework import serializers
from study.models import Course, Lesson, Payment, Subscription
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from study.validators import validate_youtube_links


class LessonSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.IntegerField(source='course.lesson_set.count', read_only=True)
    video_link = serializers.CharField(validators=[validate_youtube_links])

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


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
