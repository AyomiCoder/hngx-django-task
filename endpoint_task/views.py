from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

# Create your views here.

def api_endpoint(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    if not slack_name or not track:
        return JsonResponse({'error': 'Both slack_name and track are required query parameters.'}, status=400)

    # Generates the current day of the week in full
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    current_day = days_of_week[datetime.utcnow().weekday()]

    # Generates the current UTC time in the desired format "2023-09-07T09:33:32Z"
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub URLs
    github_file_url = 'https://github.com/AyomiCoder/hngx-django-task/blob/main/endpoint_task/views.py'
    github_repo_url = 'https://github.com/AyomiCoder/hngx-django-task.git'

    # Response object
    response_data = {
        'slack_name': "oxayomide",
        'current_day': current_day,
        'utc_time': utc_time,
        'track': "backend",
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return JsonResponse(response_data)
