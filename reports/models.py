from django.db import models
import uuid

class Report(models.Model):
    ISSUE_TYPES = [
        ('water', 'Water Issue'),
        ('electricity', 'Electricity Issue'),
        ('pothole', 'Pothole'),
       
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('assigned', 'Assigned to Department'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    description = models.TextField()
    photo = models.ImageField(upload_to='report_photos/', blank=True, null=True)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reference_number = models.CharField(max_length=20, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = f"TZN-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.reference_number} - {self.get_issue_type_display()}"