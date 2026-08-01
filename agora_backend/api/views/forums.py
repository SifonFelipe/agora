from rest_framework.views import APIView
from rest_framework.response import Response

from forums.models import Forum
from api.serializers.forums import ForumSerializer

class ForumListView(APIView):
    def get(self, request):
        forums = Forum.objects.all()
        serializer = ForumSerializer(forums, many=True)

        return Response(serializer.data)
