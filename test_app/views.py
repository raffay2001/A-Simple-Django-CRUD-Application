from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from .models import Person
from django.urls import reverse

# Create your views here.
class Index(View):
    def get(self, request):
        return HttpResponse(f"This is the Function from Class Based View")



class Add(View):
    def get(self, request):
        return render(request, 'test_app/index.html')
    
    def post(self, request):
        
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        res = eval(num1) + eval(num2)

        context = {
            'res': res,
            'num1': num1,
            'num2': num2,
        }

        return render(request, 'test_app/index.html', context)

class People(View):
    def get(self, request):
        return render(request, 'test_app/person.html')

    
    def post(self, request):
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')

        person = Person(f_name=f_name, l_name=l_name, email=email)
        person.save()

        return HttpResponseRedirect(reverse('test_app:person'))
        # return render(request, 'test_app/person.html')

class All_Person(View):

    def get(self, request):
        search_query = request.GET.get('person_info')
        delete_query = request.GET.get('del_person')
        update_query = request.GET.get('serial')
        context = {}

        if search_query:
            
            for person in Person.objects.all():
                if search_query == person.f_name:
                    context['all_person_list'] = Person.objects.filter(f_name=search_query)
                elif search_query == person.l_name:
                    context['all_person_list'] = Person.objects.filter(l_name=search_query)
                elif search_query == person.email:
                    context['all_person_list'] = Person.objects.filter(email=search_query)
                 
        elif delete_query:

            for person in Person.objects.all():
                if delete_query == person.f_name or delete_query == person.l_name or delete_query == person.email or int(delete_query) == person.id :
                    person.delete()
                    break
            context['all_person_list'] = Person.objects.all()

        elif update_query:
            updated_fname = request.GET.get('update_fname')
            updated_lname = request.GET.get('update_lname')
            updated_email = request.GET.get('update_email')

            if updated_fname or updated_lname or updated_email:
                for person in Person.objects.all():
                    if person.id == int(update_query):
                        if updated_fname and updated_lname and updated_email:
                            person.f_name = updated_fname
                            person.l_name = updated_lname
                            person.email = updated_email
                            person.save()

                        elif updated_fname and updated_lname:
                            person.f_name = updated_fname
                            person.l_name = updated_lname
                            person.save()
                        
                        elif updated_fname and updated_email:
                                person.f_name = updated_fname
                                person.email = updated_email
                                person.save()
                            
                        elif updated_lname and updated_email:
                                person.l_name = updated_lname
                                person.email = updated_email
                                person.save()
                        
                        elif updated_fname:
                                person.f_name = updated_fname
                                person.save()
                        
                        elif updated_lname:
                                person.l_name = updated_lname
                                person.save()

                        elif updated_email:
                                person.email = updated_email
                                person.save()

                context['all_person_list'] = Person.objects.all()
            

                
            
            else:
                context['all_person_list'] = Person.objects.all()



        else:
            context['all_person_list'] = Person.objects.all()
            

        return render(request, 'test_app/all_persons.html', context)

        
