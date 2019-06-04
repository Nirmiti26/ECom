from django.shortcuts import render
from solarDesign.forms import PVForm


def index(request):
    return render(request, 'solarDesign/index.html')


def calculator(request):
    if request.method == 'POST':
        print "I am here"
        form = PVForm(request.POST)
        pincode = request.POST['pincode']
        monthly_bill = request.POST['bill']
        system_load = request.POST['connection_load']
        system_load=int(system_load)
        roof_area_has = request.POST['roof_area']
        print pincode
        print system_load
        print roof_area_has
        system_cost = 0
        if system_load == 1:
            system_cost = 90000
        elif system_load in range(2, 11):
            system_cost = float(system_load) * 90000 * 0.889
        elif system_load in range(11, 30):
            system_cost = float(system_load) * 90000 * 0.87
        elif system_load in range(30, 40):
            system_cost = float(system_load) * 90000 * 0.86
        elif system_load in range(40, 80):
            system_cost = float(system_load) * 90000 * 0.85
        elif system_load in range(80, 100):
            system_cost = float(system_load) * 90000 * 0.845
        print system_cost
        units_generated = 1535 * system_load
        print units_generated
        units_generated_25 = 34100 * system_load
        print units_generated_25
        yearly_cost = system_cost * 0.01
        print yearly_cost
        saving_25 = system_load * 850000
        paybacktime = 6
        saving_1 = float(units_generated) * 8.5
        roof_top_req = system_load * 120
        covered_area = (float(roof_top_req) / float(roof_area_has)) * 100
        panels = system_load * 4
        data = {
            'system_load': system_load,
            'system_cost': system_cost,
            'units_generated': units_generated,
            'units_in_25': units_generated_25,
            'yearly_cost': yearly_cost,
            'saving_25': saving_25,
            'saving_1': saving_1,
            'payback': paybacktime,
            'rooftop': roof_top_req,
            'percentage_roof': covered_area,
            'panels': panels,
        }
        return render(request, 'solarDesign/calc.html', data)
    else:
        form = PVForm()
    return render(request, 'solarDesign/calc.html', {'none':"None", })
