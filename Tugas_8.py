from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
   if i%2 == 0:
      print(i+1, "Ganjil", "-", "ID proses", getpid())
   else:
      print(i+1, "Genap", "-",  "ID proses", getpid())
   sleep(1)

banyak = int(input("Input: "))

# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
print("Sekuensial")
sekuensial_awal = time()

# PROSES BERLANGSUNG
for i in range(banyak):
    cetak(i)

# UNTUK MENDAPATKAN WAKTU SETELAH EKSEKUSI
sekuensial_akhir = time()

# UNTUK MENAMPUNG PROSES-PROSES
kumpulan_proses = []

# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
print("multiprocessing.Process")
process_awal = time()

# PROSES BERLANGSUNG
for i in range(banyak):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

# UNTUK MENGGABUNGKAN PROSES-PROSES AGAR TIDAK LONCAT KE PROSES SEBELUM'NYA
for i in kumpulan_proses:
    p.join()
 
# UNTUK MENDAPATKAN WAKTU SETELAH EKSEKUSI
process_akhir = time()

# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
pool_awal = time()

# PROSES BERLANGSUNG
print("multiprocessing.Pool")
pool = Pool()
pool.map(cetak, range(banyak))
pool.close()

# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
pool_akhir = time()

print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi kelas Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi kelas Pool :", pool_akhir - pool_awal, "detik")
