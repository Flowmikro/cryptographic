from django.db import models


class CryptTaskModel(models.Model):
    """Создаем модель для шифрования записи"""
    task_id = models.AutoField('id', primary_key=True)
    status = models.CharField('Статус', max_length=20, default='в ожидании', editable=False)
    encrypted_data = models.TextField('Данные для зашифровки', blank=True)
    key = models.CharField('Ключ для расшифровки', max_length=100, blank=True)

    def str(self):
        return str(self.task_id)
