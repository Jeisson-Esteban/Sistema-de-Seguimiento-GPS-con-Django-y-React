from django.db import models

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, blank=True, null=True)  # Identificador de sesión

    def __str__(self):
        return f"Location ({self.latitude}, {self.longitude}, Session: {self.session_id})"