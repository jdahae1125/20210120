from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members

# Create your views here.
def gu(request):
    num = request.GET.get('num', '')

    return HttpResponse(f"<h1> gugu : {num_gugu(num)}</h2>")

def num_gugu(num):
    str = " "
    for i in range(9):
        str += f"{int(num)} * {i+1} = {int(num) * (i + 1)} <br>"
    return str

def index(req):
    print(dir(req))
    return HttpResponse("<h2> 구구단 : {gugu(num)} </h2>")

def test(req):
    return HttpResponse("<h2>Test</h2>")

def git(req):
    return HttpResponse("<h2>git version</h2>")

def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        email = req.POST['email']

        member = Members(
            username = username,
            useremail = email
        )

        member.save()
        res_data = {}
        res_data['res'] = "등록성공"
        return render(req, 'index.html', res_data)

    return render(req, 'index.html') 
