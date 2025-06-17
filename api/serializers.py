from rest_framework import serializers
from Notes.models import Note


class NoteUpload(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Note
        fields = ['file', 'title', 'uploaded_at', 'user']
        read_only_fields = ['uploaded_at', 'user', 'title']

