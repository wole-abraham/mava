from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



class Note(models.Model):
    """
        Notes -> pdf, txt, .docx
        contains information that will
        be used to generate the quizzes
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    """
    mulitple questions [belonging to a Note]
    """
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='quizzes')
    question = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.note} Quiz'


class Choice(models.Model):
    """
    choices, [belonging to a question]
    """
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='choices')
    choice = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
                                 