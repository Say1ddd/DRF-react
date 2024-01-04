from django.http.response import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Siswa
from .serializers import SiswaSerializer


class SiswaView(APIView):

    def getSiswa(self, pk):
        try:
            siswa = Siswa.objects.get(siswaId=pk)
            return siswa
        except Siswa.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.getSiswa(pk)
            serializer = SiswaSerializer(data)
        else:
            data = Siswa.objects.all()
            serializer = SiswaSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = SiswaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Data Berhasil Ditambahkan", safe=False)
        return JsonResponse("Gagal Menambahkan Data", safe=False)

    def put(self, request, pk=None):
        siswaUpdate = Siswa.objects.get(siswaId=pk)
        serializer = SiswaSerializer(instance=siswaUpdate, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Data Berhasil Diubah", safe=False)
        return JsonResponse("Gagal Mengubah Data")

    def delete(self, request, pk):
        siswaDelete = Siswa.objects.get(siswaId=pk)
        siswaDelete.delete()
        return JsonResponse("Data Dihapus", safe=False)