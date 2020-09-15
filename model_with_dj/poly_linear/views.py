from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import LinearModel
from .apps import PolyLinearConfig

# Create your views here.
def example(request):
    if request.method=="POST":
        fm=LinearModel(request.POST)
        if fm.is_valid():
            print("Form Validated")
            # print("male or female",fm.cleaned_data['male_or_female'])
            year_of_experience=fm.cleaned_data['year_of_experience']

            print()
            print([[year_of_experience]])
            prediction = PolyLinearConfig.regressor.predict([[year_of_experience]])
            response = {'weight': round(prediction[0],4)}
            print(response)
            fm=LinearModel()
            return render(request,'ans3.html',response)
    else:
        fm=LinearModel()
    return render(request,'example3.html',{'form':fm})