from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer
from utils import constants


class BookViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if self.request.user.role == constants.SUPER_ADMIN:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response({"details": "forbidden"},
                        status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.role == constants.SUPER_ADMIN:
            serializer = self.get_serializer(instance=instance,
                                             data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response({"details": "forbidden"},
                        status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.role == constants.SUPER_ADMIN:
            self.perform_destroy(instance)
            return Response({"details": "deleted"})
        return Response({"details": "forbidden"},
                        status=status.HTTP_403_FORBIDDEN)


class JournalViewSet(BookViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

