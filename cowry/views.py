from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import fieldserializers
from .models import unique_field
import json


class field_view(APIView):
    def get(self, request):
        all_field_values = unique_field.objects.all()
        serializer = fieldserializers(all_field_values, many=True)
        json_serializer = json.loads(json.dumps(serializer.data))
        new_d = {}
        for i in json_serializer:
            new_d.update(i)
            values_from_dict = new_d.values()
            iterate = iter(values_from_dict)
            dict_from_values = dict(zip(iterate, iterate))
            return Response(dict_from_values)
    '''
        The serialized values is orderedDict, i converted it to json, but still the type of the json was still a list
        i could iterate through individual element and pass it dynamically to a new dictionary. but in the python shell, i can get all the
        values from the list as a new dictionary, but if i return it as a response in my views.py i get just a single value from the dictionary set even though i have declared
        the variable as a global variable(i.e i am not using the variable declared in the for loop). The surprising thing is if i decode to use the variable "new_d" globally
        or locally, i get the same result.
        
        Please what am i missing here? I am really interested to know how to get this solved? I have been on this for days.  i don't mind if i don't get the job. I 
        really love to know how to manipulate this. I will appreciate if you can fork the repo, point me to what i am missing. I can be contacted via my mail and phone number
         clintonchristopher49@gmail.com and 09057190741
         
        Thanks
                
        '''



