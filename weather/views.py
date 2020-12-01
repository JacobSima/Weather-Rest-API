import    datetime
import    time
import    json
import    requests
from      decouple                      import config     

from      django.shortcuts              import    render
from      django.http                   import    HttpResponse, JsonResponse
from      django.views.generic          import    View
from      django.core                   import    serializers
from      django.views.decorators.csrf  import    csrf_exempt

from      rest_framework.renderers      import    JSONRenderer
from      rest_framework.parsers        import    JSONParser

from      .serializers                  import    WeatherSerializer
from      .models                       import    WeatherApi


def median(arr):

  arr.sort()
  if len(arr) > 2:
    if len(arr) % 2 == 0:
      i1 = int((len(arr)/2)-1)
      i2 = i1+1
      v1 = arr[i1]
      v2 = arr[i2]
      avg = (v1+v2)/2
      return (avg,i1)
    else:
      i = int(((len(arr)/2)+1)-1)
      return (arr[i],i)
  elif len(arr) == 2:
    return (arr[0],'')
  elif len(arr) == 1:
    return (arr[0],'')


class Weather(View):

  def get(self, request, *args, **kwargs):
    context = {}
    return render(request,'home.html',context)


@csrf_exempt
def weather_api(request,*args, **kwargs): 
  
  api_key = config('API_KEY')
  today = datetime.date.today()
  today_dt = int(time.mktime(datetime.datetime.strptime(str(today),"%Y-%m-%d").timetuple()))
  today_now = datetime.datetime.now()
  today_now_dt = int(time.mktime(datetime.datetime.strptime(str(today_now),"%Y-%m-%d %H:%M:%S.%f").timetuple())) 
  arr_dt = []
  temp_arr = []
  temp =  ''
  temp_min = ''
  temp_min_arr = []
  temp_max = ''
  temp_max_arr = []
  hum_arr = []
  hum = ''

  if request.method == 'GET':
    weathers = WeatherApi.objects.all()
    serializer = WeatherSerializer(weathers, many=True)
    return JsonResponse(serializer.data, safe = False )
  
  elif request.method == 'POST': 
    city = ''
    from_time =''
    to_time =''
    if len(request.POST) == 0:
      data =  JSONParser().parse(request)
      serializer =  WeatherSerializer(data = data)
      if serializer.is_valid():
        city = data['city']
        from_time = data['from_time']
        to_time = data['to_time']
      else :
        return JsonResponse({'status':400,'msg':'Invalid form inputs data, check your Start and End Time Correctly'}, status = 400)
    else:
      _i = request.POST
      inputs  = dict(_i.lists())
      city = inputs['city'][0]
      from_time = inputs['from_time'][0]
      to_time = inputs['to_time'][0]

    from_time_dt = int(time.mktime(datetime.datetime.strptime((str(today) + ' '+from_time),"%Y-%m-%d %H:%M").timetuple()))
    to_time_dt = int(time.mktime(datetime.datetime.strptime((str(today) + ' '+to_time),"%Y-%m-%d %H:%M").timetuple()))

    if from_time_dt >= to_time_dt:
      return JsonResponse({'status':400,'msg':'From Time cannot be greather than To Time'}, status = 400)
    elif from_time_dt < today_now_dt:
      return JsonResponse({'status':400,'msg':'API does not provide historical data, Please check your From Time'}, status = 400)
    
    try :
      url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}'
      r = requests.get(url)
      r_data = json.loads(r.text) 
      r_list = r_data['list']
    
      for item in r_list:
        if item['dt'] >= from_time_dt and item['dt'] <= to_time_dt:
          arr_dt.append(item)  
      if len(arr_dt) == 0:
        url_1 = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
        r1 = requests.get(url_1)
        r1_data = json.loads(r1.text)
        lon = r1_data['coord']['lon']
        lat = r1_data['coord']['lat']
        temp_ar = [temp, temp_max,temp_min]
        temp_ar.sort()
        temp_mean = temp_ar[1]
        current = {
          'temp': r1_data['main']['temp'],
          'temp_min': r1_data['main']['temp_min'],
          'temp_max': r1_data['main']['temp_max'],
          'temp_avg': round(((r1_data['main']['temp_min'])+(r1_data['main']['temp_max']))/2),
          'temp_mean': temp_mean,
          'humidity': r1_data['main']['humidity'],
          'city': city
        }
        return JsonResponse(current, status = 200)
      else:
        for item in arr_dt:
          temp_arr.append(item['main']['temp'])
          temp_min_arr.append(item['main']['temp_min'])
          temp_max_arr.append(item['main']['temp_max'])
          hum_arr.append(item['main']['humidity'])
          temp_min = temp_min_arr[0] if len(temp_min_arr) == 1 else  min(*temp_min_arr)
          temp_max = temp_max_arr[0] if len(temp_min_arr) == 1 else max(*temp_max_arr)
          temp_avg = temp_arr[0] if len(temp_arr) == 1 else round(sum(temp_arr)/len(temp_arr))

          temp,_ = (temp_arr[0],'') if len(temp_arr) == 1 else median(temp_arr) 
          hum,_ = (hum_arr[0],'') if len(hum_arr) == 1 else median(hum_arr)

        current = {
        'temp': temp,
        'temp_min': temp_min,
        'temp_max': temp_max,
        'temp_avg': temp_avg,
        'temp_mean': temp,
        'humidity': hum,
        'city': city
        }
    except Exception as ex:
      return JsonResponse({'status':400,'msg':'API Calls Failed'}, status = 400)  
    return JsonResponse(current, status = 200)
    



