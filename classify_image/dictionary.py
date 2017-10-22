import io
import os

from django.core.files.temp import NamedTemporaryFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def dictionary_api(request):
    data = []
    data.append({"nama": "belalang", "nama_latin": "Caelifera", "deskripsi": "Belalang adalah serangga herbivora dari subordo Caelifera dalam ordo Orthoptera", "solusi": "Semprot tanaman dengan pestisida organik", "ditemukan": "leaves", "suhu_hidup": "25"})
    data.append({"nama": "walang sangit", "nama_latin": 2, "deskripsi": 3, "solusi": 4, "ditemukan": 5, "suhu_hidup": 6})
    data.append({"nama": "tikus sawah", "nama_latin": 2, "deskripsi": 3, "solusi": 4, "ditemukan": 5, "suhu_hidup": 6})
    data.append({"nama": "wereng", "nama_latin": 2, "deskripsi": 3, "solusi": 4, "ditemukan": 5, "suhu_hidup": 6})
    
    return JsonResponse(data, safe=False)
