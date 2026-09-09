from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('ACAD', 'Assignments & Quizzes'),
        ('MISC', 'Other tasks'),
        ('FIT', 'Gym & Bulking'),
        ('LIFE', 'Hostel & Errands'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default='LIFE')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title