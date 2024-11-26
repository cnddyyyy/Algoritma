# Algoritma
Untuk Mata Kuliah PAA
Nama : Cindy Amelia
NIM : F55123098

Analisis Untuk Best Case Kuis 2
1. Naive : Jika array sudah terurut, hanya satu iterasi diperlukan untuk memeriksa bahwa tidak ada elemen yang perlu ditukar.
Dengan ini, Bubble Sort menunjukkan kelebihan untuk kasus array yang sudah terurut, sementara Merge Sort tetap konstan di O(n log n) untuk semua kasus.
2. Conquer : Pada semua kasus (termasuk best case), Merge Sort membagi array menjadi dua hingga mencapai elemen tunggal, lalu menggabungkannya dengan perbandingan elemen. Tidak ada cara untuk menghindari langkah-langkah ini bahkan dalam kasus array yang sudah terurut.
