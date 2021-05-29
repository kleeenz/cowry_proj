from cowry.models import unique_field
from cowry.serializers import fieldserializers

all_f = unique_field.objects.all()
fieldser = fieldserializers(all_f, many=True)

print(fieldser.data)







