from django.shortcuts import render
from  django.shortcuts import HttpResponse,render,redirect
# Create your views here.
from django.views import View
from pop_data.models import City, NetWorkSpeed
def test(request):
    return  render(request,'sdn.html')

class Index(View):

    def get(self, request):
        city_list = City.objects.all()
        return render(request, "sdn.html", {
            "city_list": city_list,
            "speed": "result"
        })


class SpeedDisplay(View):
    """"""
    def post(self, request):
        city_list = City.objects.all()
        try:
            city_left = int(request.POST["city_left"])
            city_right = int(request.POST["city_right"])
        except Exception:
            return render(request, "sdn.html", {
                "city_list": city_list,
                "speed": "result"
            })
        speed = NetWorkSpeed.objects.filter(city_left=city_left, city_right=city_right).first()
        print(speed)
        return render(request, "sdn.html", {
            "city_list": city_list,
            "speed": str(speed) + "ms"
        })
