from django_filters import rest_framework as filters
from study.models import Payment


class PaymentFilter(filters.FilterSet):
    course = filters.NumberFilter(field_name='paid_course__id')
    lesson = filters.NumberFilter(field_name='paid_lesson__id')
    payment_method = filters.ChoiceFilter(field_name='payment_method', choices=Payment.payment_method_choices)

    class Meta:
        model = Payment
        fields = []
