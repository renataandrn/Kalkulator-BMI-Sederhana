import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
file_path = 'data_bmi.xlsx'
data = pd.read_excel(file_path)
male_data = data[data['gender'] == 1]
female_data = data[data['gender'] == 0]
st.title("Kalkulator dan Analisis BMI")
st.write("Selamat datang di Program Studi Matematika ITK! berikut ini adalah contoh dari penerapan matematika, aplikasi ini memungkinkan kita menghitung BMI Anda dan mengeksplorasi analisis regresi sederhana BMI berdasarkan usia.")
st.header("Kalkulator BMI")
weight = st.number_input("Masukkan berat badan Anda (kg):", min_value=0.0, format="%.2f", step=0.1)
height = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=0.0, format="%.2f", step=0.1)
if st.button("Hitung BMI"):
    if weight > 0 and height > 0:
        height_m = height / 100.0
        bmi = weight / (height_m * height_m)
        st.write(f"**BMI Anda:** {bmi:.2f}")
        if 18.5 <= bmi <= 24.9:
            st.success("Anda berada dalam rentang berat badan ideal!")
        elif bmi < 18.5:
            st.info("Anda berada dalam kategori berat badan kurang.")
        else:
            st.warning("Anda berada dalam kategori berat badan berlebih.")
    else:
        st.error("Masukkan nilai berat dan tinggi yang valid.")
st.subheader("Tips untuk Menjaga Berat Badan Ideal")
st.write(
    """
    1. Tetap aktif dan lakukan olahraga secara teratur.
    2. Konsumsi makanan seimbang dengan banyak sayuran dan buah-buahan.
    3. Hindari makanan tinggi lemak dan gula berlebihan.
    4. Perhatikan asupan cairan dan minum air secukupnya.
    5. Tidur cukup untuk mendukung proses metabolisme.
    """
)
st.header("Analisis Regresi BMI Berdasarkan Usia")
model = LinearRegression()
X = data[['usia']]
y = data['BMI']
model.fit(X, y)
predicted_bmi = model.predict(X)
st.header("Dataset BMI")
st.write("Berikut adalah dataset yang digunakan untuk analisis:")
st.write("1 merupakan laki-laki dan 0 merupakan perempuan")
st.dataframe(data)
correlation_coefficient = data['usia'].corr(data['BMI'])
st.write("### Scatter Plot dengan Garis Regresi")
fig, ax = plt.subplots(figsize=(10, 8))
sns.scatterplot(x=male_data['usia'], y=male_data['BMI'], color='blue', label='Laki-laki', alpha=0.7, ax=ax)
sns.scatterplot(x=female_data['usia'], y=female_data['BMI'], color='pink', label='Perempuan', alpha=0.7, ax=ax)
ax.plot(data['usia'], predicted_bmi, color='green', linestyle='--', linewidth=2, label='BMI Prediksi')
ax.set_title("Scatter Plot BMI terhadap Usia dengan Garis Regresi")
ax.set_xlabel("Usia")
ax.set_ylabel("BMI")
ax.legend()
st.pyplot(fig)