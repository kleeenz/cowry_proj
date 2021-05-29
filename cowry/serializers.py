from rest_framework import serializers
from . models import unique_field


class fieldserializers(serializers.ModelSerializer):
    class Meta:
        model = unique_field
        fields = "__all__"



