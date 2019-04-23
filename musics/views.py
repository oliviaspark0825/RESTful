from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer

from .models import Music
# Create your views here.


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    # Response 를 통해 serializer를 반환
    # serializer = 특정한 딕셔너리 혹은 쿼리셋 등의 파이썬 형식 데이터 타입을 반환하도록 해주는 아이
    serializer = MusicSerializer(musics, many=True) # 단일객체가 아닐경우
    return Response(serializer.data)
    
#music 은 쿼리셋, 일종의 리스트인데 우리가 응답하려고 하는 것은 json
#serializer가 해주는 것은 리스트를 하나 하나씩 json 타입으로 바꿔주는 도구
#응답하는 함수는 Response이다
#결과로 보내줄 데이터는 .data로 가져온다

