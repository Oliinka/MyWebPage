from django.shortcuts import render
# Create your views here.
# calculator/views.py
from django.http import JsonResponse

# mysite/calculator/views.py
from django.http import JsonResponse

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return JsonResponse({'error': 'Cannot divide by zero'}, status=400)

        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
