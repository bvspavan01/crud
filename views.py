from django.shortcuts import render
from .models import Employee, Employee
from django.db import IntegrityError



# Create your views here.
def index(request):
    msg=""
    if request.method=="POST":
        butt=request.POST["b1"]
        
        if butt=="Insert":
            try:
                eid=request.POST["t1"]
                name=request.POST["t2"]
                address=request.POST["t3"]
                city=request.POST["city"]
                gender=request.POST["gender"]
                vehicles=request.POST.getlist("vehicle")
                image = request.FILES['image']    
                obj=Employee.objects.create(eid=eid,name=name,address=address,city=city,gender=gender,vehicles=vehicles,image=image)
                msg="Record Inserted"
                return render(request,'index.html',{'msg':msg})
            
            except IntegrityError as e:
                msg="Employee ID already exists!"
                return render(request,"index.html", {"msg":msg })

        elif butt=="Select":
            try:
                eid=request.POST["t1"]
                obj=Employee.objects.get(eid=eid)
                return render(request,'index.html',{'obj':obj})
            except:
                msg="No Employee found!"
                return render(request,'index.html',{'msg':msg})

        elif butt=="Update":
            try:
                eid=request.POST["t1"]
                name=request.POST["t2"]
                address=request.POST["t3"]
                city=request.POST["city"]
                gender=request.POST["gender"]
                vehicles=request.POST["vehicle"]
                image = request.FILES['image']    
                obj=Employee.objects.get(eid=eid)
                obj.name=name
                obj.address=address
                obj.city=city
                obj.gender=gender
                obj.vehicles=vehicles
                obj.image = image
                obj.save() 
                msg="Record Updated"
                return render(request,'index.html',{'msg':msg})
            except:
                msg="No Employee found Please check ID!"
                return render(request,'index.html',{'msg':msg})
        elif butt=="Delete": 
            try:
                eid=request.POST["t1"]
                obj=Employee.objects.get(eid=eid)
                obj.delete() 
                msg="Record Deleted"
                return render(request,'index.html',{'msg':msg})

            except Employee.DoesNotExist:
                msg="No Employee found!"
                return render(request,'index.html',{'msg':msg})
            
        elif butt=="SelectAll":    
            objects=Employee.objects.all()
            new_objects = []

            for obj in objects:
                new_obj = {
                    'eid': obj.eid,
                    'name': obj.name,
                    'address': obj.address,
                    'city': obj.city,
                    'gender': obj.gender,
                    'vehicles': obj.vehicles.strip('][').split(', '),
                    'image': obj.image,
                }
                print(new_obj)
                new_objects.append(new_obj)
            return render(request,'my.html',{'objects':new_objects})
        
    else:
        return render(request,'index.html',{'msg':msg})
        