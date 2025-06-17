from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, permissions
from .serializers import NoteUpload
from Notes.models import Note
from .generator import gen
from Notes.models import Quiz, Choice


class UploadFile(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Note.objects.all()
    serializer_class = NoteUpload
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file Uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        content = file_obj.read().decode('utf-8')


        try:
            res = gen(content)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        """
        To Save Question Generated
        """

        
        
        serializer = self.get_serializer(data={'file': file_obj})
        serializer.is_valid(raise_exception=True)
        note = serializer.save(user=request.user, title=file_obj.name)
        for data in res:
            quiz = Quiz.objects.create(note=note, question=data['question'])
            for choice, state in data['choices'].items():
                Choice.objects.create(question=quiz, choice=choice, is_correct=state)
            
        return Response(
            res, status=status.HTTP_201_CREATED
        )