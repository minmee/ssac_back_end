## Serializer

serializer : 직렬화, 데이터가 보여줘야 하는 기본 방식을 설명하는 JSON 객체

파이썬 객체에서 -> JSON 객체로 변경
데이터를 얻고, 검증까지 가능

=> shortcut을 이용할 수 있습니다.

## api_view

- use decorator
  @api_view(['GET', 'POST'])

- class based api views
  클래스를 이용해서 정해주면 간단한 작업으로 자유롭게 api를 적용할 수 있다.

- Generic View : ListAPIView

## Query Set

- Room.objects.all()

## Settings Pagination style

쪽 수를 매기기를 자동적으로 적용해서 JSON객체로 반환해줍니다.

## ModelViewSet

1. make viewsets.py
2. from rest_framework improt viewsets

class RoomViewset(viewsets.ModelViewSet):
queryset = Room.objects.all()
serializer_class = BigRoomSerializer
