from django.db import models

# Create your models here.

class Todo(models.Model):
    """
    Model representing a todo item.
    """
    title = models.CharField(max_length=200, help_text="Title of the todo item")
    description = models.TextField(blank=True, help_text="Optional description of the todo item")
    completed = models.BooleanField(default=False, help_text="Whether the todo is completed")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the todo was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time when the todo was last updated")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
