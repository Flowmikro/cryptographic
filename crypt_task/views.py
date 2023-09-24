from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CryptTaskModel
from .serializers import CryptTaskSerializers
from .services import create_db, get_db, return_json_model
from .tasks import update_crypt_task_model_status


class CryptTaskAPIPost(APIView):

    serializer_class = CryptTaskSerializers

    def post(self, request):
        """Создаем post запрос для добавления задачи"""
        query = create_db(CryptTaskModel.objects)  # CryptTaskModel.objects.create()
        query.encrypted_data = request.data.get('encrypted_data')
        query.save()

        update_crypt_task_model_status.delay(query.task_id)  # передаем задачу celery

        return return_json_model(query)


class CryptTaskAPIGet(APIView):
    def get(self, request, task_id):
        """Создаем get запрос чтения задачи"""
        query = get_db(CryptTaskModel.objects, task_id=task_id)  # CryptTaskModel.objects.create(task_id=task_id)
        if query.status == 'в процессе':
            return Response({'status': 'в процессе'})
        elif query.status == 'в ожидании':
            return Response({'status': 'в ожидании'})
        return return_json_model(query)
