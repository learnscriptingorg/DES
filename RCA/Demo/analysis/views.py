import json
import sys
sys.path.insert(0,'..')
from django.http import HttpResponse
from django.shortcuts import render
from  db_lib import db_conn
from  db_lib import xml_data_parser
# Create your views here.
def index(request):
    l = [23, 423, 4, 234, 23, 423, 4, 234, 23, 4, 234, 234, 23, 4, 234, 23, 4, 234, 23, 423, 4, 234, 23, 4, 234, 234,
         23, 42, 34, 23, 423, 4, 234, 234234, 23, 423, 4, 23, 42, 3423, 4, 23, 42, 34, 234, 23, 423, 4, 234, 23, 4, 23,
         423, 42, 34, 23, 423, 4, 234, 23, 4]
    mdict = {'a': 12, 'b': 14}
    br_name = request.GET.get('project_name')

    build_name = request.GET.get('build_name')
    print("build name:",build_name)
    print(request.GET.get('project_name'))
    br_names = [2, 3, 4, 43, 5, 345, 34, 5]
    build_nums = [3345, 45, 34, 543, 5, 345, 34, 5445, 35, 435, 4354, 5, 345534]
    if request.method == "POST":
        # Get the posted form
        project_name = request.POST['project_name']
        build_name=request.POST['build_name']
        print('$$$$$$$',project_name,build_name)
        data_set=db_conn.db_conn().get_data_table('Auroral_Sanity_Suite')
        return render(request, 'load_build.html', {'data': data_set})

    if br_name != None:
        #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        return HttpResponse(json.dumps({'name': build_nums}), content_type="application/json")
    else:
        #print("Inside main page ")
        return render(request, 'load_build.html')


# def load_build(request):
#     print("rrrrrrrrrrrrrrr")
#     results = [[1, 2, 3, 4 ,8,8], [5, 6, 7, 8,9,9], [9, 10, 11, 12,9,9], [13, 14, 15, 16,9,9]]
#     return render( request,'load_build.html',{'data':results})
