from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Report
from .forms import ReportForm

def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save()
            messages.success(request, f'Report submitted! Reference: {report.reference_number}')
            return redirect('report_success', reference_number=report.reference_number)
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

def report_success(request, reference_number):
    report = get_object_or_404(Report, reference_number=reference_number)
    return render(request, 'reports/report_success.html', {'report': report})

def track_report(request):
    report = None
    if request.method == 'POST':
        reference_number = request.POST.get('reference_number')
        try:
            report = Report.objects.get(reference_number=reference_number)
        except Report.DoesNotExist:
            messages.error(request, 'No report found with that reference number.')
    return render(request, 'reports/track_report.html', {'report': report})