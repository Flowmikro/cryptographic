import rsa
from celery import shared_task

from .models import CryptTaskModel
from .services import get_db


@shared_task
def update_crypt_task_model_status(task_id):
    """Обновляем статус на 'в процессе'"""
    crypt_task_db = get_db(CryptTaskModel.objects, task_id=task_id)  # CryptTaskModel.objects.create(task_id=task_id)

    crypt_task_db.status = 'в процессе'
    crypt_task_db.save(update_fields=['status'])
    running_the_rsa_algorithm(crypt_task_db)


@shared_task
def running_the_rsa_algorithm(crypt_task_db):
    """запускаем алгоритм шифрования RSA"""
    public_key, private_key = rsa.newkeys(2048)
    text = crypt_task_db.encrypted_data
    mess = text.encode('utf8')
    cryp = rsa.encrypt(mess, public_key)
    save_result_in_crypt_task_model(crypt_task_db, private_key, cryp)


@shared_task
def save_result_in_crypt_task_model(crypt_task_db, private_key, cryp):
    """Сохраняем результат в модели CryptTaskModel"""
    crypt_task_db.encrypted_data = cryp
    crypt_task_db.key = private_key
    crypt_task_db.status = 'готово'

    crypt_task_db.save()

