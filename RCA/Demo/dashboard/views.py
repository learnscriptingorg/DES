from django.core.paginator import Paginator
from django.shortcuts import render

def index(request):
    l=[23,423,4,234,23,423,4,234,23,4,234,234,23,4,234,23,4,234,23,423,4,234,23,4,234,234,23,42,34,23,423,4,234,234234,23,423,4,23,42,3423,4,23,42,34,234,23,423,4,234,23,4,23,423,42,34,23,423,4,234,23,4]
    mdict={'a':12,'b':14}
    pagi=Paginator(l,5)

    pg_num=request.GET.get('page')
    pg_obj=pagi.get_page(pg_num)
    # for i in pg_obj:
    #     print(i)
    # print("**********")
    #ob=db_lib()
    print(request.GET.get('build'))
    return render(request,'index.html', {'pg_obj':pg_obj,'pagi':pagi})
# Create your views here.
