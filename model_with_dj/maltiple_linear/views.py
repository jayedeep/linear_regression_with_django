from django.shortcuts import render
from .forms import LinearModel
from .apps import MaltipleLinearConfig

# Create your views here.
def example(request):
    if request.method=="POST":
        fm=LinearModel(request.POST)
        if fm.is_valid():
            print("Form Validated")
            # print("male or female",fm.cleaned_data['male_or_female'])
            cylinders=fm.cleaned_data['cylinders']
            displacement=fm.cleaned_data['displacement']
            horsepower=fm.cleaned_data['horsepower']
            weight=fm.cleaned_data['weight']
            acceleration=fm.cleaned_data['acceleration']
            model_year=fm.cleaned_data['model_year']
            origin=fm.cleaned_data['origin']
            print()
            print([[cylinders,displacement,horsepower,weight,acceleration,model_year,origin]])
            prediction = MaltipleLinearConfig.regressor.predict([[cylinders,displacement,horsepower,weight,acceleration,model_year,origin]])
            response = {'weight': round(prediction[0],4)}
            print(response)
            fm=LinearModel()
            return render(request,'ans2.html',response)
    else:
        fm=LinearModel()
    return render(request,'example2.html',{'form':fm})