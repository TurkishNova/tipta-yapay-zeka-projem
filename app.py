import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


# =========================
# DATASET
# =========================
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

cols = [
    "Pregnancies","Glucose","BloodPressure","SkinThickness",
    "Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"
]

df = pd.read_csv(url, names=cols)

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =========================
# MODEL
# =========================
model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("rf", RandomForestClassifier(
        n_estimators=250,
        max_depth=12,
        random_state=42
    ))
])

model.fit(X_train, y_train)

auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])


# =========================
# GUI
# =========================
root = tk.Tk()
root.title("Diyabet Tahmin Sistemi")
root.geometry("600x650")
root.configure(bg="#0f172a")


tk.Label(
    root,
    text=f"Diyabet Tahmin Modeli (AUC: {auc:.2f})",
    fg="white",
    bg="#0f172a",
    font=("Arial", 14, "bold")
).pack(pady=10)


frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=10)


labels = [
"Gebelik Sayısı (adet)",
"Glikoz (mg/dL)",
"Kan Basıncı (mmHg)",
"Cilt Kalınlığı (mm)",
"İnsülin (µU/mL)",
"Vücut Kitle İndeksi (BMI kg/m²)",
"Soy Ağacı / Diyabet Pedigri Fonksiyonu (oransal indeks – 0–2 arası skala)",
"Yaş (yıl)"
]

entries = []

for i, text in enumerate(labels):
    tk.Label(frame, text=text, fg="white", bg="#0f172a").grid(row=i, column=0, padx=5, pady=5)

    e = tk.Entry(frame)
    e.grid(row=i, column=1)
    entries.append(e)


e1, e2, e3, e4, e5, e6, e7, e8 = entries


# =========================
# PREDICT
# =========================
def predict():
    try:
        data = np.array([[
            float(e1.get()),
            float(e2.get()),
            float(e3.get()),
            float(e4.get()),
            float(e5.get()),
            float(e6.get()),
            float(e7.get()),
            float(e8.get())
        ]])

        prob = model.predict_proba(data)[0][1]

        if prob > 0.7:
            msg = "YÜKSEK RİSK"
            color = "red"
        elif prob > 0.4:
            msg = "ORTA RİSK"
            color = "orange"
        else:
            msg = "DÜŞÜK RİSK"
            color = "green"

        result_label.config(
            text=f"{msg}\nRisk: %{prob*100:.2f}",
            bg=color
        )

    except:
        messagebox.showerror("Hata", "Tüm alanlara sayı gir")


# =========================
# CLEAR
# =========================
def clear():
    for e in entries:
        e.delete(0, tk.END)
    result_label.config(text="", bg="#0f172a")


tk.Button(
    root,
    text="Tahmin Et",
    command=predict,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12)
).pack(pady=10)


tk.Button(
    root,
    text="Temizle",
    command=clear,
    bg="#6b7280",
    fg="white"
).pack()


result_label = tk.Label(
    root,
    text="",
    fg="white",
    bg="#0f172a",
    font=("Arial", 14)
)
result_label.pack(pady=20)


root.mainloop()
