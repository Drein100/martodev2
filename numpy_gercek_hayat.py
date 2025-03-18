import numpy as np
import matplotlib.pyplot as plt

# BÖLÜM 1: Şirket Maaş Analizi
# Görev 1: 500 çalışanın maaşlarını simüle etme
maaslar = np.random.randint(3000, 15001, 500)

print(f"Ortalama Maaş: {np.mean(maaslar):.2f} TL")
print(f"Maksimum Maaş: {np.max(maaslar)} TL")
print(f"Minimum Maaş: {np.min(maaslar)} TL")

# Histogram ile maaş dağılımı
plt.hist(maaslar, bins=20, color='blue', edgecolor='black')
plt.xlabel('Maaş Aralığı (TL)')
plt.ylabel('Çalışan Sayısı')
plt.title('Şirket Maaş Dağılımı')
plt.show()

# Görev 2: Çalışanları 3 departmana rastgele atama
departmanlar = np.random.choice([1, 2, 3], 500)

for dep in [1, 2, 3]:
    ortalama_maas = np.mean(maaslar[departmanlar == dep])
    print(f"Departman {dep} Ortalama Maaşı: {ortalama_maas:.2f} TL")

# BÖLÜM 2: Hava Durumu Verileri Üretme ve Analiz
# Görev 3: 365 günlük sıcaklık verisi üretme
temp_values = np.random.uniform(-10, 40, 365)

print(f"Ortalama Sıcaklık: {np.mean(temp_values):.2f}°C")
print(f"En Sıcak Gün: {np.max(temp_values):.2f}°C")
print(f"En Soğuk Gün: {np.min(temp_values):.2f}°C")

# Sıcaklık değişim grafiği
plt.plot(temp_values, color='red')
plt.xlabel('Gün')
plt.ylabel('Sıcaklık (°C)')
plt.title('Yıllık Sıcaklık Değişimi')
plt.show()

# BÖLÜM 3: Ürün Satış Analizi
# Görev 4: 5 farklı ürün için günlük satış simülasyonu
urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]
satislar = np.random.randint(10, 101, (5, 30))

toplam_satis = np.sum(satislar, axis=1)
ortalama_satis = np.mean(satislar, axis=1)

for i, urun in enumerate(urunler):
    print(f"{urun} - Toplam Satış: {toplam_satis[i]}, Ortalama Günlük Satış: {ortalama_satis[i]:.2f}")

# Ürün bazında çubuk grafiği
plt.bar(urunler, toplam_satis, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Ürün')
plt.ylabel('Toplam Satış')
plt.title('Ürün Bazında Aylık Satış Miktarları')
plt.show()
