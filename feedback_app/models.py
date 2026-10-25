
from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):

    DEPARTMENT_CHOICES = [
        ('cse', 'Computer Science'),
        ('ece', 'Electronics and Communication'),
        ('eee', 'Electrical and Electronics'),
        ('me', 'Mechanical'),
        ('ce', 'Civil'),
        ('ai_ds', 'AI and Data Science'),
        ('other', 'Other'),
    ]

    SENTIMENT_CHOICES = [
        ('positive', 'Positive'),
        ('negative', 'Negative'),
        ('neutral', 'Neutral'),
        ('unknown', 'Unknown'),
    ]

    CATEGORY_CHOICES = [
        ('faculty', 'Faculty'),
        ('academics', 'Academics'),
        ('infrastructure', 'Infrastructure'),
        ('administration', 'Administration'),
        ('facilities', 'Facilities'),
        ('other', 'Other'),
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )

    department = models.CharField(
        max_length=10,
        choices=DEPARTMENT_CHOICES
    )

    feedback_text = models.TextField()

    sentiment = models.CharField(
        max_length=10,
        choices=SENTIMENT_CHOICES,
        default='unknown'
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student

