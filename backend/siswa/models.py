from django.db import models


class Siswa(models.Model):
    siswaId = models.AutoField(primary_key=True)
    NamaLengkap = models.CharField(max_length=100)
    NIS = models.CharField(max_length=5)
