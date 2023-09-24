from rest_framework.response import Response


def create_db(objects, **kwargs):
    """Функция для создания записи в бд"""
    return objects.create(**kwargs)  # MyModel.objects.create()


def get_db(objects, **kwargs):
    """Функция для чтения записи из бд"""
    return objects.get(**kwargs)  # MyModel.objects.get()


def return_json_model(query):
    """json вывод полей из модели CryptTaskModel"""
    return Response({
        'task_id': query.task_id,
        'status': query.status,
        'encrypted_data': query.encrypted_data,
        'key': query.key,
    })