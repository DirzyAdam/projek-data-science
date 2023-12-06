import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Load data
df = pd.read_csv("data air quality.csv")

# Create 'date' column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

# Define pollutants and weather variables
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
weather_vars = ['TEMP', 'PRES', 'DEWP', 'RAIN']

# Calculate monthly averages
monthly_averages = df.groupby(df['date'].dt.to_period('M'))[pollutants].mean().reset_index()
monthly_averages['date'] = monthly_averages['date'].dt.to_timestamp()

# Calculate correlations
correlations = df[weather_vars + pollutants].corr()

# Start Streamlit app
st.title('Air Quality Analysis Dashboard')

# Plot 1: Pola Konsentrasi Polutan Sepanjang Tahun
st.subheader('Pola Konsentrasi Polutan Sepanjang Tahun')
fig, ax = plt.subplots(figsize=(15, 10))
for pollutant in pollutants:
    sns.lineplot(data=monthly_averages, x='date', y=pollutant, ax=ax)
plt.title('Pola Konsentrasi Polutan Sepanjang Tahun')
plt.xlabel('Tanggal')
plt.ylabel('Konsentrasi')
plt.legend(pollutants)
st.pyplot(fig)

st.write("""
Dari visualisasi garis waktu yang telah dibuat, tampak bahwa konsentrasi setiap polutan berubah sepanjang tahun. Meskipun ada beberapa fluktuasi, namun secara umum konsentrasi polutan tertinggi sepanjang tahun ada di awal tahun yaitu sekitar bulan Januari dan konsentrasi polutan terendah ada di pertengahan tahun yaitu sekitar bulan Juli.
""")

# Plot 2: Korelasi antara Variabel Cuaca dan Polutan
st.subheader('Korelasi antara Variabel Cuaca dan Polutan')
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlations.loc[weather_vars, pollutants], annot=True, cmap='coolwarm', center=0, ax=ax)
plt.title('Korelasi antara Variabel Cuaca dan Polutan')
st.pyplot(fig)

st.write("""
Dari heatmap korelasi yang telah dibuat, tampak bahwa ada beberapa hubungan antara variabel cuaca dan polutan.

Suhu (TEMP) memiliki korelasi positif dengan ozon (O3), yang berarti bahwa konsentrasi ozon cenderung lebih tinggi saat suhu lebih tinggi. Sebaliknya, suhu memiliki korelasi negatif dengan beberapa polutan lain seperti SO2, NO2, dan CO, yang berarti bahwa konsentrasi polutan ini cenderung lebih rendah saat suhu lebih tinggi. Lalu untuk polutan yang lainnya karena memiliki nilai korelasi yang sangat rendah (mendekati nol), nilai korelasinya terhadap suhu dapat kita abaikan.

Sedangkan untuk tekanan (PRES), dari heatmap tampak bahwa tekanan memiliki korelasi positif dengan SO2, NO2 dan CO. Hal ini berarti bahwa konsesntrasi polutan cenderung lebih tinggi saat tekanan lebih tinggi. Sebaliknya, tekanan memiliki korelasi negatif dengan O3, yang berarti bahwa konsentrasi ozon cenderung lebih rendah saat tekanan lebih tinggi. Lalu untuk polutan yang lainnya karena memiliki nilai korelasi yang sangat rendah (mendekati nol), nilai korelasinya terhadap tekanan dapat kita abaikan.

Titik embun (DEWP) memiliki korelasi positif dengan O3, ini berarti bahwa konsentrasi O3 cenderung lebih tinggi saat titik embun lebih tinggi. Namun, titik embun memiliki korelasi negatif dengan SO2 yang berarti bahwa konsentrasi polutan ini cenderung lebih rendah saat titik embun lebih tinggi. Lalu untuk polutan yang lainnya karena memiliki nilai korelasi yang sangat rendah (mendekati nol), nilai korelasinya terhadap titik embun dapat kita abaikan.

Hujan (RAIN) memiliki nilai korelasi yang sangat rendah (mendekati nol) terhadap semua jenis polutan dalam dataset ini. Ini berarti korelasi antara hujan dengan konsentrasi polutan relatif dapat kita abaikan.

Namun, perlu diingat bahwa korelasi bukan berarti sebab-akibat, dan mungkin ada faktor lain yang mempengaruhi hubungan ini.
""")
