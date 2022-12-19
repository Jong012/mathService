from rest_framework import serializers


class AddCalcSerializer(serializers.Serializer):
    numbers = serializers.ListField(
        number=serializers.FloatField(
            max_value=1000000.0,
            help_text='최대 숫자는 1000000 입니다.')
    )


def save(self, **kwargs):
    validated_data
