from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Song
from .serializers import SongSerializer

# Create your views here.

class SongListApiView(APIView) :
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the song items for given requested user
        '''
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    

class SongDetailApiView(APIView):
    def get_object(self, song_id):
        '''
        Helper method to get the object with given song_id
        '''
        try:
            return Song.objects.get(id=song_id)
        except Song.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, song_id, *args, **kwargs):
        '''
        Retrieves the song with given song_id
        '''
        song_instance = self.get_object(song_id)

        if not song_instance:
            return Response(
                {"res": "Object with song id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SongSerializer(song_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, song_id, *args, **kwargs):
        '''
        Updates the song item with given song_id if exists
        '''
        song_instance = self.get_object(song_id)
        if not song_instance:
            return Response(
                {"res": "Object with song id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'title': request.data.get('title'),
            'date_released': request.data.get('date_released'),
            'likes': request.data.get('likes'),
        }

        serializer = SongSerializer(instance = song_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, song_id, *args, **kwargs):
        '''
        Deletes the song item with given song_id if exists
        '''
        song_instance = self.get_object(song_id)
        if not song_instance:
            return Response(
                {"res": "Object with song id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        song_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
