#Alasan mengapa parameter sebenarnya yang dikirim oleh pemanggil 
#fungsi berubah adalah karena parameternya adalah daftar(array) 
#dan elemen tertentu dari array tersebut ditetapkan ke objek numerik baru


def scale(data, factor):
 for val in data: 
      val *= factor 
