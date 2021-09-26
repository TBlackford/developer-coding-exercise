from os import listdir
from os.path import isfile, join

from rest_framework import views
from rest_framework.response import Response

from posts.serializers import PostSerializer

BLOG_PATH = '../assets/posts/'


class PostView(views.APIView):
    """
    Get a specific post
    """

    def get(self, request, slug):
        try:
            with open(BLOG_PATH + slug + '.md') as file:
                # Read the whole file
                file_data = file.readlines()

                # Serialise the data and return
                result = PostSerializer(file_data).data
                return Response(result)
        except IOError as e:
            return Response({
                'msg': 'Error'
            })


class PostsView(views.APIView):
    """
    List all of the posts
    """

    def get(self, request):
        files = [file.replace('.md', '') for file in listdir(BLOG_PATH) if isfile(join(BLOG_PATH, file))]

        return Response(files)
