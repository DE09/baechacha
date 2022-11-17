from django.shortcuts import redirect, render
from .models import baecha

# Create your views here.
def index(request):
    return render(request, 'index.html')

def detail(request):
    return render(request, 'detail.html')


def manage(request):
    if request.method == 'POST':
        date = request.POST['date']
        customer = request.POST['customer']
        bl = request.POST['bl']
        pic = request.POST['pic']
        status = request.POST['status']
        trc = request.POST['trc']
        company = request.POST['company']
        etc = request.POST['etc']

        form = baecha.objects.create(
            date=date,
            customer=customer,
            bl=bl,
            pic=pic,
            status=status,
            trc=trc,
            company=company,
            etc=etc,
        )
        form.save()
        return redirect('/manage')

    else:
        shipments = baecha.objects.all()
        context = {'shipments':shipments}
        return render(request, 'manage.html', context)

def delete(request, id):
    delete = baecha.objects.get(pk=id)
    delete.delete()
    return redirect('/manage')

def update(request, id):
    if request.method == 'POST':
        date = request.POST['date']
        customer = request.POST['customer']
        bl = request.POST['bl']
        pic = request.POST['pic']
        status = request.POST['status']
        trc = request.POST['trc']
        company = request.POST['company']
        etc = request.POST['etc']
        
        shipment = baecha.objects.filter(pk=id)
        shipment.update(
            date=date,
            customer=customer,
            bl=bl,
            pic=pic,
            status=status,
            trc=trc,
            company=company,
            etc=etc,
            )
        return redirect('/manage')
    else:
        return redirect('/manage')
    
def success(request):
    return render(request, 'success.html')