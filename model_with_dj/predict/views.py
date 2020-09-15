from django.shortcuts import render

# Create your views here.
from .apps import PredictConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from .forms import LinearModel

# class call_model(APIView):
#     def get(self, request):
#         # if request.method == 'GET':
#             # get sound from request
#         male_or_female = request.GET.get('male_or_female')
#         height=request.GET.get('height')
#         male_or_female = 1
#         height = 159
#             # vectorize sound
#             # predict based on vector
#         prediction = PredictConfig.regressor.predict([[male_or_female,height]])[0]
#             # build response
#         response = {'weight': prediction}
#             # return response
#         print(response)
#         return JsonResponse(response)
def home(request):
    return render(request,'home.html')
    
def example(request):
    if request.method=="POST":
        fm=LinearModel(request.POST)
        if fm.is_valid():
            print("Form Validated")
            # print("male or female",fm.cleaned_data['male_or_female'])
            male_or_female=fm.cleaned_data['male_or_female']
            if male_or_female=='male':
                male_or_female=1
            else:
                male_or_female=0
            print('height',fm.cleaned_data['height'])
            height=fm.cleaned_data['height']
            print()
            print([[float(male_or_female),float(height)]])
            prediction = PredictConfig.regressor.predict([[float(male_or_female),float(height)]])
            response = {'weight': round(prediction[0],4)}
            print(response)
            fm=LinearModel()
            return render(request,'ans.html',response)
    else:
        fm=LinearModel()
    return render(request,'example.html',{'form':fm})