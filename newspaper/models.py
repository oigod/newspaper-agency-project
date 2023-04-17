from django.db import models
from django.contrib.auth.models import AbstractUser


class Topic(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    class Meta:
        verbose_name_plural = "redactors"
        verbose_name = "redactor"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return f"{self.first_name} {self.last_name} {self.years_of_experience}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "newspapers"
        verbose_name = "newspaper"

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.title
