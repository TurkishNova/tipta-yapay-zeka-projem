



---

# Bu proje Tıpta Yapay Zeka dersimin Proje Ödevi için oluşturuldu

* Projeyi 3.14 python ile hazırladım tkinker arayüzü vardır. sistem sizin girdiğiniz verileri hastaların verileriyle karşılaştırarak bir risk oranı oluşturur. gerekli kütüphaneler aşağıda metinde yazılıdır.
---


## 📌 Proje Amacı

Bu proje, klinik veriler kullanılarak **Tip 2 Diyabet riskinin yapay zeka ile tahmin edilmesini** amaçlamaktadır. Kullanıcıdan alınan sağlık parametreleri, gerçek bir tıbbi veri seti ile eğitilmiş makine öğrenmesi modeli üzerinden analiz edilerek risk sonucu üretilir.

---

## 🏥 Problem Tanımı

Type 2 Diabetes dünya genelinde yaygın görülen ve erken teşhis edilmediğinde ciddi komplikasyonlara yol açan bir hastalıktır.

Erken teşhis önemlidir çünkü:

* Kalp hastalıkları
* Böbrek yetmezliği
* Sinir hasarı
* Görme kaybı

gibi komplikasyonlar gelişebilir.

---

## 📊 Kullanılan Veri Seti

Proje kapsamında aşağıdaki açık veri seti kullanılmıştır:

* Pima Indians Diabetes Dataset
* Kaynak: Açık tıbbi veri tabanı (UCI / Kaggle türevi)

Özellikler:

* Glucose
* BMI
* Blood Pressure
* Insulin
* Age
* Pregnancies
* Diabetes Pedigree Function

---

## 🤖 Kullanılan Yapay Zeka Modeli

* Algoritma: **Random Forest Classifier**
* Kütüphane: scikit-learn
* Veri işleme: StandardScaler + Median Imputation
* Eğitim yaklaşımı: Train/Test Split (%80 / %20)

Model, hastaları geçmiş veri setindeki örneklerle karşılaştırarak öğrenir ve olasılık tabanlı risk tahmini üretir.

---

## 📈 Model Performansı

* ROC-AUC: ~0.80 – 0.87 aralığı
* Çoklu karar ağacı yapısı sayesinde overfitting azaltılmıştır

---

## 🖥️ Uygulama Arayüzü

Proje, Python Tkinter kullanılarak geliştirilmiştir.

Arayüz özellikleri:

* Hasta verisi giriş alanları
* Tek butonla tahmin sistemi
* Risk sonucu (Düşük / Orta / Yüksek)
* Olasılık yüzdesi
* Renkli risk gösterimi

---

## ⚙️ Çalışma Mantığı

1. Kullanıcı sağlık verilerini girer
2. Model bu veriyi eğitim verisi ile karşılaştırır
3. Random Forest algoritması olasılık üretir
4. Sistem risk seviyesini sınıflandırır

---

## 🧪 Örnek Kullanım

### 🔴 Yüksek Risk Örneği:

```

Pregnancies: 4
Glucose: 180
BloodPressure: 88
SkinThickness: 35
Insulin: 200
BMI: 34.5
Pedigree: 0.8
Age: 50

```

➡ Model sonucu: **YÜKSEK RİSK**

---

### 🟢 Düşük Risk Örneği:

```

Pregnancies: 1
Glucose: 90
BloodPressure: 70
SkinThickness: 20
Insulin: 80
BMI: 22
Pedigree: 0.2
Age: 25

```

➡ Model sonucu: **DÜŞÜK RİSK**

---

## ⚠️ Etik ve Klinik Uyarı

Bu sistem:

* Bir **klinik teşhis aracı değildir**
* Sadece **karar destek ve eğitim amaçlıdır**
* Doktor değerlendirmesinin yerine geçmez

---

## 🧰 Kullanılan Teknolojiler

* Python 🐍
* Tkinter 🖥️
* Pandas 📊
* NumPy 🔢
* Scikit-learn 🤖

---

## 🚀 Çalıştırma

```bash
pip install numpy pandas scikit-learn
python app.py
```

---

## 📌 Sonuç

Bu proje, yapay zekanın sağlık alanında karar destek sistemlerinde nasıl kullanılabileceğini göstermektedir. Klinik veriler üzerinden risk analizi yaparak erken teşhise katkı sağlamayı hedefler.

---
---
