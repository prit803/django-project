from django.shortcuts import render ,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    
    if request.method ==  "POST":

        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_name =receipe_name ,
            receipe_description = receipe_description,
            receipe_image=receipe_image
            
        )

        return redirect('/receipes/')
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search') )
        # print(request.GET.get('search'))


    context =  {'receipes' : queryset}
    return render(request , 'receipes.html', context)





@login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')



@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id )

    if request.method ==  "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        # receipe_phone = data.get('receipe_phone')

        queryset.receipe_name =receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image


        queryset.save()
        return redirect('/receipes/')



    context =  {'receipe' : queryset}
    return render(request , 'update_receipes.html', context)

def  login_page(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request , 'Invaild Username ')
            return redirect('/login/')
        
        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request , 'Invaild Password ')
            return redirect('/login/')
        else:
            login(request , user)
            return redirect('/receipes/')

    return render(request , 'login.html')




def logout_page(request):
    logout(request)
    return redirect('/login/')

def  register_page(request):


    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request , 'username alredy taken ')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password
        )

        user.set_password(password)
        user.save()

        messages.info(request , 'Account created Successfully')

        return redirect('/login/')

    return render(request , 'register.html')

def index_page(request):
    # if request.method ==  "GET":
        return render(request , 'index.html')



from django.db.models  import Q , Sum



def get_students(request):

    


    queryset = Student.objects.all()
    

    if request.GET.get('search'):
        search = request.GET.get('search')


        queryset = queryset.filter(
            Q(student_name__icontains = search ) |
            Q(department__department__icontains = search ) |
            Q(student_id__student_id__icontains = search ) |
            Q(student_email__icontains = search ) |
            Q(student_age__icontains = search )
                                )


    
    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page" , 1)
    page_obj = paginator.get_page(page_number)

    return render(request , "report/students.html" ,{'queryset' : page_obj})


from .seeds import genrated_report_card

def see_marks(request , student_id):
    # genrated_report_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    current_rank =  -1
    ranks =  Student.objects.annotate(marks= Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i = 1
    for rank in ranks:
        if student_id == rank.student_id.student_id:
            current_rank = i
            break
        i = i+1


    return render(request , "report/see_marks.html" ,{'queryset' : queryset , 'total_marks' : total_marks , 'current_rank' : current_rank})