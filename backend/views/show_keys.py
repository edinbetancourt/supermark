# DRF 
from rest_framework import generics, status
from rest_framework.response import Response

# Serializer
from backend.serializers.get_password import GetPasswordSerializer

# Utils
from backend.utils.derive_password import DerivePassword


class ShowKeysView(generics.GenericAPIView):
    """ Show keylog.txt keys """

    serializer_class = GetPasswordSerializer

    def get(self, request):

        key_list = DerivePassword().get_key_list()

        if key_list:

            key_list_dic = [{'key': key} for key in key_list]

            return Response({'result': key_list_dic}, status=status.HTTP_200_OK)
        else:
            return Response({'result': "Can't open keylog file"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
