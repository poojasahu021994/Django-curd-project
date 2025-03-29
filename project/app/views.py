from django.shortcuts import render
from .models import EmployeeData
from .models import Admindatabase

def index(request):
    return render(request,'index.html')
# login function
def login(request):
    global adminemail
    global adminpass
    global adminName
    adminemail = "pooja0294@gmail.com"
    adminpass = "Pooja@123"
    adminName = "Pooja"
    
    if request.method == 'POST':
        user_email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmployeeData.objects.filter(employe_email=user_email)

        if user_email == adminemail and password == adminpass:
            print(user_email)
            # admin_data=Admindatabase.objects.get(id=pk)
            # all_data={
            #             'name':admin_data.admin_name,
            #             'email': admin_data.admin_email,
            #             'pass': admin_data.admin_password,
            #             # 'contact': admin_data.admin_number,
            # }
            return render(request,'admindashboard.html', {'admin_email':adminemail, 'admin_pass':adminpass, 'admin_name': adminName})

        if user.exists():
            user1 = EmployeeData.objects.get(employe_email=user_email)
            pass1 = user1.employe_password

            if pass1 == password:
                user= {
                        'name': user1.employe_name,
                        'email': user1.employe_email,
                        'department': user1.department,
                        'contact': user1.contact_number,
                        'work': user1.your_work,
                        'user_id': user1.id   # Ensure user.id exists
                    }
                return render(request, 'userdashboard.html', {'data':user})
            else:
                message = "Email and password do not match"
                return render(request, 'login.html', {'message': message})
        else:
            message2 = "Email ID does not exist"
            return render(request, 'login.html', {'message2': message2})

    return render(request,'login.html')
# registion function
def Registration(request):
    if request.method=='POST':
           name=request.POST.get('name')
           Email=request.POST.get('email')
           Number=request.POST.get('phone')
           gender=request.POST.get('gender')
           joining=request.POST.get('dob')
           department=request.POST.get('department')
           password=request.POST.get('password')
           cpassword=request.POST.get('cpassword')
           print(name,Email,joining,Number,password,cpassword,gender,department)
        
           user=EmployeeData.objects.filter(employe_email=Email)
           if user:
                x="Email already exist"
                return render(request,'registration.html',{'msg':x})
           else:
                if password==cpassword:
                    EmployeeData.objects.create(employe_name=name,employe_email=Email,contact_number=Number,date_of_joining=joining,department=department, employe_password=password)
                    x="Registration Sucessfully"
                    return render(request,'registration.html',{'msg':x})
                else:
                    x="password and confirm password not match"
                    return render(request,'registration.html',{'msg':x,'name':name,'customer_Email':Email,'customer_Number':Number,'password':password})
    else:      
       return render(request, 'registration.html')

def adminlogin(request):
    if(request.method=='POST'):
        admin_email=request.POST.get('email')
        password=request.POST.get('pass')
        data=Admindatabase.objects.filter(admin_email=admin_email)

        if(data):
            user=Admindatabase.objects.get(admin_email=admin_email)
            print (user)
            mypass=user.admin_password
        
            if(mypass==password):
                # admin_data=Admindatabase.objects.get()
                # all_data={
                #         'name':admin_data.admin_name,
                #         'email': admin_data.admin_email,
                #         'pass': admin_data.admin_password,
                #         # 'contact': admin_data.admin_number,
                #         }
                return render(request,'admindashboard.html', {'admin_email':adminemail, 'admin_pass':adminpass, 'admin_name': adminName})

def admindashboard(request):
    mydata=EmployeeData.objects.all()
    count_value= mydata.count()
    print(count_value)
    return render(request,'admindashboard.html',{'data':mydata.values})

# user Dashboard function
def UserDashbashboard(request):
    return render(request,'userdashboard.html')

# logout function
def Logout(request):
    return render(request,'login.html')

# user profile function
def profile(request, pk):  
    user = EmployeeData.objects.filter(id=pk).first()   # Get the user by primary key  
    print(user)  # Debugging to see if user exists
    
    if user:  
         user= {
            'name': user.employe_name,
            'email': user.employe_email,
            'department': user.department,
            'contact': user.contact_number,
            'work': user.your_work,
            'user_id': user.id   # Ensure user.id exists
        }
         return render(request, 'profile.html', {'data': user})
    
    return render(request, 'profile.html', {'error': 'User not found'}) 

# add task function
def Addtask(request):
    myans2=EmployeeData.objects.all()
    return render(request,'addtask.html',{'data2':myans2.values})

# given task function
def givetask(request,pk):
    
    data=EmployeeData.objects.get(id=pk)
    print(data)
    myans2=EmployeeData.objects.all()
    if request.method == "POST":
        newtask=request.POST.get('text')
        if data:
            data.your_work=newtask
            data.save()

    
        # EmployeeData.objects.create(your_work=newtask)
    return render(request,'addtask.html',{'data2':myans2.values,'mydata':data})

# delete function
def remove(request,pk):
    print(pk)
    data=EmployeeData.objects.get(id=pk)
    data.delete()
    stu=EmployeeData.objects.all()
    
    return render(request,'admindashboard.html',{'data':stu.values})

# ------edit function------
def edituser(request):
     myans1=EmployeeData.objects.all()
     return render(request,'edituser.html',{'data2':myans1.values})

# -----update user details-----
def updatedata(request,pk):

    if request.method=="POST":
          x =EmployeeData.objects.get(id=pk)
          name = request.POST.get('name')
          email = request.POST.get('email')
       
          contact = request.POST.get('contact')
          dep = request.POST.get('department')
          work = request.POST.get('work') 
         

          x.employe_name=name
          x.employe_email=email
        
          x.contact_number=contact
          x.department=dep
          x.your_work=work
          x.save()
          stu1=EmployeeData.objects.all()
          return render(request,'edituser.html',{'data2':stu1})

# showtask function
def Showtask(request):
    myans2=EmployeeData.objects.all()
    return render(request,'showtask.html',{'data2':myans2.values})
# user task function
def usertask(request,pk):
    task=EmployeeData.objects.get(id=pk)
    user = {
            'name': task.employe_name,
            'email': task.employe_email,
            'department': task.department,
            'contact': task.contact_number,
            'work': task.your_work,
            'user_id': task.id   # Ensure user.id exists
        }
    print(user)
    mytask=task.your_work
    print(mytask)
    return render(request,'usertask.html',{'data':user,'mytsk':mytask})