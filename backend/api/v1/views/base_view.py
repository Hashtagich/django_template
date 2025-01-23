from api.v1.serializers.base_serializer import ErrorResponseSerializer
from drf_spectacular.utils import OpenApiResponse
from rest_framework import mixins, viewsets
from rest_framework.views import APIView


class ListAndRetrieveViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Миксин для представлений только с GET запросами всех объектов или одного конкретного."""
    pass


class ListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Миксин для представлений только с GET запросами всех объектов."""
    pass


class BaseContestView(ListViewSet):
    """Родительский класс для исключения дублирования кода в части документация swagger."""

    COMMON_RESPONSES = {
        400: OpenApiResponse(
            description="Ошибка клиента при запросе данных",
            response=ErrorResponseSerializer()
        ),
        # 401: OpenApiResponse(
        #     description="Необходима аутентификация",
        #     response=ErrorResponseSerializer()
        # ),
        403: OpenApiResponse(
            description="Доступ запрещён",
            response=ErrorResponseSerializer()
        ),
        404: OpenApiResponse(
            description="Не найдено",
            response=ErrorResponseSerializer()
        ),
        500: OpenApiResponse(
            description="Ошибка сервера при обработке запроса",
            response=ErrorResponseSerializer()
        ),
    }