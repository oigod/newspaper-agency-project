from django.db import models
from django.contrib.auth.models import AbstractUser


class Topic(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    class Meta:
        verbose_name_plural = "redactors"
        verbose_name = "redactor"

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.first_name} {self.last_name} {self.years_of_experience}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    class Meta:
        verbose_name_plural = "newspapers"
        verbose_name = "newspaper"

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
