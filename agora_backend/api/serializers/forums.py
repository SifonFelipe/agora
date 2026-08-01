from rest_framework import serializers

from forums.models import Forum

#NOTE: Serializers converts objects into JSON format for API responses

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'parent',
            'created_at',
        ]
