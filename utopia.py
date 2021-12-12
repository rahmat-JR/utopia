import sys,time,os

p = "\33[1;97m" # putih
l = "\33[0;37m" # putih gelap
m = "\33[1;31m" # merah
h = "\33[1;92m" # hijau
k = "\33[1;93m" # kuning
b = "\33[1;94m" # biru
u = "\33[1;95m" # ungu
s = "\33[1;96m" # biru muda

balmond = h+">"+k+"><"+h+"<"
def jalan(ms):
        for sir in ms + "\n":
                sys.stdout.write(sir)
                sys.stdout.flush()
                time.sleep(0.05)
os.system("clear")
jalan(balmond+m+" Sc Saya Tutup Untuk Jangka Waktu Yang Belum Diketahui")
jalan(balmond+m+" Mohon Maaf Atas Ketidak nyamanannya")
time.sleep(0.5)
exit()
