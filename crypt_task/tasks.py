import rsa
from celery import shared_task

from .models import CryptTaskModel
from .services import get_db


@shared_task
def creating_rsa_data(task_id):
    """Шифруем данные по RSA алгоритму"""
    crypt_task_db = get_db(CryptTaskModel.objects, task_id=task_id)  # CryptTaskModel.objects.create(task_id=task_id)

    crypt_task_db.status = 'в процессе'
    crypt_task_db.save()

    public_key, private_key = rsa.newkeys(2048)

    text = crypt_task_db.encrypted_data
    mess = text.encode('utf8')
    cryp = rsa.encrypt(mess, public_key)

    crypt_task_db.encrypted_data = cryp
    crypt_task_db.key = private_key
    crypt_task_db.status = 'готово'

    crypt_task_db.save()