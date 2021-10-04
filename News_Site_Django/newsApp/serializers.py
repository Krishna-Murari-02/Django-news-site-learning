from .models import Breaking, new
from rest_framework import serializers


class newSerializers(serializers.ModelSerializer):
    class Meta:
        model = new
        fields = ['news_name','news_category','news_subcategory','news_summery','news_author','news_updateTime','news_image','news_place','news_paragraph']

class BreakingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Breaking
        fields = ['breaking']


  