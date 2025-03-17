import pandas as pd
import io
import base64
from django.shortcuts import render
import matplotlib.pyplot as plt
from coffees.models import Coffee

plt.rc('font', family='Malgun Gothic')

# Create your views here.
def coffee_chart_01(request):
    coffees = Coffee.objects.values_list('brand', flat=True) # 브랜드 컬럼 정보만 읽어 오기
    coffeeFrame = pd.DataFrame({'브랜드':list(coffees)})

    chart_data = coffeeFrame['브랜드'].value_counts()
    mycolor = ['green', 'blue', 'red']

    plt.figure(figsize=(6, 6))
    plt.title('브랜드별 커피숍 비율')
    chart_data.plot(kind='pie', autopct = '%.1f%%', colors=mycolor)
    plt.ylabel('')

    # buffer 객체는 임시 데이터를 저장하기 위하여 메모리에 존재합니다.
    buffer = io.BytesIO()
    # png 형식으로 임시 메모리 buffer에 저장합니다.
    plt.savefig(buffer, format='png')
    buffer.seek(0) # 가장 후미로 이동한 파일 포인터를 버퍼 공간의 가장 앞으로 옮깁니다.

    # 버퍼 메모리의 내용을 base64로 인코딩된 이미지를 만들어 줍니다.
    myimage = base64.b64encode(buffer.getvalue()).decode('utf-8')

    context = {'myimage': myimage, 'description': '지금 브랜드별 커피숍의 비율을 그리고 있습니다.'}

    return render(request, 'coffees/coffee_chart_01.html', context)
# end def coffee_chart_01(request)

import seaborn as sns

def coffee_chart_03(request):
    #브랜드, 위도, 경도를 사용하여 산점도 그리기
    map_data = Coffee.objects.values('longitude','latitude','brand')
    mapFrame = pd.DataFrame(list(map_data))

    plt .figure(figsize=(10,8))
    sns.scatterplot(data=mapFrame, x='longitude', y='latitude', hue = 'brand', alpha=0.8)

    plt.title('브랜드별 커피숍 위치 분포',size=30)
    plt.xlabel('경도', size=15)
    plt.ylabel('위도', size=15)
    plt.legend(title='브랜드')
    plt.xlim([126.7341,127.2693])
    plt.ylim([37.4133,37.7151])

    buffer = io.BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)#제일 앞으로 이동
    myimage = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request,'coffees/coffee_chart_03.html',{'myimage':myimage})
    pass

#end def coffee_chart_03(request):