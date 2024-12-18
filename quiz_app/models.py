from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=512)
    answer_a = models.CharField(max_length=255)
    answer_b = models.CharField(max_length=255)
    answer_c = models.CharField(max_length=255)
    answer_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=[
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ])

    def __str__(self):
        return self.text

class QuizSession(models.Model):
    user = models.CharField(max_length=100)  # Hardcoding 'user' for simplicity
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.started_at.strftime('%Y-%m-%d %H:%M:%S')}"
