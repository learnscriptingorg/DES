from django.shortcuts import render

# Create your views here.
def index(request):
    l=[23,423,4,234,23,423,4,234,23,4,234,234,23,4,234,23,4,234,23,423,4,234,23,4,234,234,23,42,34,23,423,4,234,234234,23,423,4,23,42,3423,4,23,42,34,234,23,423,4,234,23,4,23,423,42,34,23,423,4,234,23,4]
    mdict={'a':12,'b':14}


    br_name=request.GET.get('br_name')
    build_num=request.GET.get('build_num')
    print(request.GET.get('build'))
    br_names=[2,3,4,43,5,345,34,5]
    build_nums=[3345,45,34,543,5,345,34,5445,35,435,4354,5,345534]
    return render(request,'index.html', {'br_names':br_names,'build_nums':build_nums})
def load_build(request):
    pass

# Create your views here.