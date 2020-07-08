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

    build_num = request.GET.get('build_num')
    print(request.GET.get('project_name'))
    br_names = [2, 3, 4, 43, 5, 345, 34, 5]
    build_nums = [3345, 45, 34, 543, 5, 345, 34, 5445, 35, 435, 4354, 5, 345534]
    # db_ob=db_conn.db_conn()
    # con=db_ob.get_conn()
    # db_ob.close_conn(con)
    # data_set=xml_data_parser.get_data()
    # print(data_set)


    if br_name == None:
        build_nums = None
    if br_name != None:
        return HttpResponse(json.dumps({'name': build_nums}), content_type="application/json")
    else:
        return render(request, 'index1.html')


