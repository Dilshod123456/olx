from django.http import HttpResponse

def kirish(request):
    return HttpResponse('OLX.uz saytiga hush kelibsiz')

def malumotlar(request):
    return HttpResponse("""Bolinmani tanglang----> 
                        1. Moshina
                        2. Elektronika
                        3. Idishlar
                        4. Hayvonlar""")

def elektronika(request):
    return HttpResponse("""Elektronika bolinmasiga hush kelibsiz, szni nimalar qiziqtiradi----> 1. TElefon   2. Air Pods   3. Planshet    4. Smart Watch""")

def telefon(request):
    return HttpResponse('Telefon bolinmasiga hush kelibsiz, qaysi telefon szga qiziq')

def Iphone(request):
    return HttpResponse('1. Iphone 15 pro max ---> 1300$    2. Iphone 15 pro 1100$    3. Iphone 14 pro max 1050$     4. Iphone 14 pro 950$')

def Iphone15pro(request):
    return HttpResponse('Rang tanglang---> 1. Titanium   2. Blue    3. Black')

def Titanium(request):
    return HttpResponse('1100$ tolov qilsangiz telefon sizniki')

def harid(request):
    return HttpResponse('Haridingiz uchun minnatdormiz, szni yana OLX.uz saytida kutb qolamiz')

def Planshet(request):
    return('Szni qaysi planshet qiziqtiradi')

def AirPods(request):
    return('Air Pods iwlatma miyang iwlami qoladi')



