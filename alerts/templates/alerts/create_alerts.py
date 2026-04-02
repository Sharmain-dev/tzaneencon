import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tzaneen_connect.settings')
django.setup()

from alerts.models import Alert

# Clear existing alerts
Alert.objects.all().delete()

# Create sample alerts
sample_alerts = [
    {
        'title': 'Planned Water Maintenance',
        'alert_type': 'water',
        'description': 'Water supply will be interrupted for maintenance work. Please store water in advance.',
        'location': 'CBD, Dan Village, Mopye',
        'start_date': datetime.now(),
        'end_date': datetime.now() + timedelta(days=1),
        'is_active': True
    },
    {
        'title': 'Pothole Repairs in Progress',
        'alert_type': 'roads',
        'description': 'Road maintenance team is repairing potholes on main roads. Expect minor delays.',
        'location': 'Main Road, Tzaneen CBD',
        'start_date': datetime.now(),
        'end_date': datetime.now() + timedelta(days=3),
        'is_active': True
    },
    {
        'title': 'Load Shedding Schedule',
        'alert_type': 'electricity',
        'description': 'Stage 2 load shedding will be implemented today from 14:00 to 18:00.',
        'location': 'All areas',
        'start_date': datetime.now(),
        'end_date': datetime.now() + timedelta(hours=4),
        'is_active': True
    },
]

for alert_data in sample_alerts:
    Alert.objects.create(**alert_data)

print(f"Created {len(sample_alerts)} sample alerts!")