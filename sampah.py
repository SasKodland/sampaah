import random 

def sampah_organik():
    nama_sampah = ['daun','sayur busuk','buah busuk',
                   'nasi basi','bangkai','kotoran hewan',
                   'ranting pohon', 'limbah ternak', 'tulang',
                   'kulit buah', 'cangkang telur', 'ampas kopi/teh']

    return random.choice(nama_sampah)

def sampah_anorganik():
    nama_sampah = ['botol plastik', 'karet', 'bungkus plastik',
                   'kresek', 'kardus', 'kertas', 'baterai', 'kaleng',
                   'besi', 'sampah kaset (cd, dvd, dll)', 'gelas kaca']
    
    return random.choice(nama_sampah)
