# 🧠 Yapay Zeka Destekli Diyabet Risk Tahmin Sistemi

## 📌 Proje Amacı

Bu proje, klinik veriler kullanılarak **Tip 2 Diyabet riskinin yapay zeka ile tahmin edilmesini** amaçlamaktadır. Sistem, kullanıcıdan alınan sağlık parametrelerini analiz ederek hastanın diyabet riskini olasılıksal olarak hesaplar ve risk seviyesini sınıflandırır.

---

## 🏥 Problem Tanımı

:contentReference[oaicite:0]{index=0}, dünya genelinde yaygın görülen ve erken teşhis edilmediğinde ciddi komplikasyonlara yol açabilen kronik bir hastalıktır.

### Klinik Önemi:
- Kalp ve damar hastalıkları
- Böbrek yetmezliği
- Sinir hasarı (nöropati)
- Görme kaybı

Diyabetin erken teşhisi hem yaşam kalitesini artırmakta hem de sağlık maliyetlerini önemli ölçüde azaltmaktadır.

---

## 📊 Kullanılan Veri Seti

- **Veri seti:** Pima Indians Diabetes Dataset  
- **Kaynak:** Açık erişimli tıbbi veri seti (UCI / Kaggle)

### Özellikler:
- Gebelik Sayısı
- Glikoz
- Kan Basıncı
- Cilt Kalınlığı
- İnsülin
- Vücut Kitle İndeksi (BMI)
- Diyabet Soy Ağacı Fonksiyonu
- Yaş

---

## 🧹 Veri Ön İşleme

- Eksik değerler medyan ile doldurulmuştur (SimpleImputer)
- Özellikler standartlaştırılmıştır (StandardScaler)
- Veri %80 eğitim / %20 test olarak ayrılmıştır
- Sınıf dağılımı stratified split ile korunmuştur

---

## 🤖 Model ve Yöntem

- **Algoritma:** Random Forest Sınıflandırıcı
- **Kütüphane:** Scikit-learn

### Kullanım Nedeni:
Random Forest, tablo verilerinde yüksek doğruluk sağlayan ve aşırı öğrenmeye (overfitting) karşı dayanıklı bir topluluk (ensemble) yöntemidir.

### Hiperparametreler:
- Ağaç sayısı: 250
- Maksimum derinlik: 12
- Rastgele durum: 42

---

## 📈 Model Performansı

- Kullanılan metrik: ROC-AUC
- Modelin ayırt etme gücü ROC eğrisi ile analiz edilmiştir

### ROC-AUC oranlarıyla ilgili:
- 0.50 → rastgele tahmin
- 0.70–0.80 → orta seviye
- 0.80+ → iyi performans

Bu proje kapsamında model **iyi düzeyde ayırma başarısı göstermektedir.**

---

## 📊 Görselleştirmeler

- ROC Eğrisi
- Risk yüzdesi çıktısı
- Renk kodlu risk sınıflandırması

---

## 🧠 Model Çalışma Mantığı

1. Kullanıcı sağlık verilerini girer
2. Model bu veriyi eğitim verisi ile karşılaştırır
3. Random Forest algoritması olasılık üretir
4. Sistem hastayı:
   - Düşük Risk
   - Orta Risk
   - Yüksek Risk  
   olarak sınıflandırır

---

## ⚖️ Etik ve Sınırlılıklar

- Bu sistem **klinik teşhis aracı değildir**
- Sadece **karar destek ve eğitim amaçlıdır**
- Gerçek tıbbi kararlar için doktor değerlendirmesi gereklidir

### Veri ve Model Sınırlamaları:
- Veri seti sınırlı sayıda hasta içermektedir
- Demografik bias (yanlılık) ihtimali bulunmaktadır
- Gerçek klinik ortamda ek doğrulama gereklidir

---

## 🖥️ Uygulama Arayüzü

- Python Tkinter ile geliştirilmiştir
- Kullanıcıdan gerçek zamanlı veri alınır
- Tek buton ile tahmin yapılır
- Sonuç renkli olarak gösterilir

---

## 🧪 Örnek Kullanım

### 🔴 Yüksek Risk:

- Gebelik Sayısı (adet): 4
- Glikoz (mg/dL): 180
- Kan Basıncı (mmHg): 88
- Cilt Kalınlığı (mm): 35
- İnsülin (µU/mL): 200
- Vücut Kitle İndeksi (BMI kg/m²): 34.5
- Soy Ağacı / Diyabet Pedigri Fonksiyonu (oransal indeks – 0–2 arası skala): 0.8
- Yaş (yıl): 50

➡ Sonuç: Yüksek Diyabet Riski

---

### 🟢 Düşük Risk:

- Gebelik Sayısı (adet): 1
- Glikoz (mg/dL): 90
- Kan Basıncı (mmHg): 70
- Cilt Kalınlığı (mm): 20
- İnsülin (µU/mL): 80
- Vücut Kitle İndeksi (BMI kg/m²): 22
- Soy Ağacı / Diyabet Pedigri Fonksiyonu (oransal indeks – 0–2 arası skala): 0.2
- Yaş (yıl): 25

➡ Sonuç: Düşük Diyabet Riski

---

## 🧰 Kullanılan Teknolojiler

- Python
- Scikit-learn
- Pandas
- NumPy
- Tkinter
- Matplotlib (ROC eğrisi için)

---

## 🚀 Çalıştırma Talimatı

```bash
pip install numpy pandas scikit-learn matplotlib
python app.py
