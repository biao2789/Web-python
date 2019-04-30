from rest_framework import serializers
from applications.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'version', 'released_at', 'file')


class FileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField("get_file_absolute_url")

    def get_file_absolute_url(self, obj):
        return obj.file.url