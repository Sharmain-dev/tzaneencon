from django.shortcuts import render
from .models import Alert

def alert_list(request):
    print("=== ALERT LIST VIEW IS BEING CALLED ===")  # Debug line
    active_alerts = Alert.objects.filter(is_active=True).order_by('-created_at')
    print(f"Number of alerts found: {active_alerts.count()}")  # Debug line
    
    
    from django.template import loader
    try:
        template = loader.get_template('alerts/alert_list.html')
        print("Template found successfully!")
    except Exception as e:
        print(f"Template error: {e}")
    
    return render(request, 'alerts/alert_list.html', {'alerts': active_alerts})
