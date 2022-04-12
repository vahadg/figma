from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, FormView

from .models import Person
from .forms import PersonForm

# Create your views here.
def home(request):
    context = {
        'env': Person.objects.all(),
        }
    return render(request,"accounts/index.html", context)

def create(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Error Input"
    
    form = PersonForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'accounts/create.html', data)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)



class PersonCreateView(CreateView):            
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')


