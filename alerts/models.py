from django.db import models

class Alert(models.Model):
    ALERT_TYPES = [
        ('water', 'Water'),
        ('electricity', 'Electricity'),
        ('pothole', 'Pothole'),
    ]
    
    title = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_alert_type_display()}: {self.title}"