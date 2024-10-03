import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="E-commerce Dashboard", layout="wide")

# Memuat data dari file CSV
data_path = 'dashboard/main_data.csv'
main_data = pd.read_csv(data_path)

# Judul Dashboard
st.title("E-commerce Dashboard")
st.markdown("Dashboard ini menampilkan analisis data dari platform e-commerce.")

# Menampilkan DataFrame
if st.checkbox("Tampilkan Data Awal"):
    st.write(main_data)

# Analisis Dasar
st.header("Analisis Dasar")
st.subheader("Statistik Deskriptif")
st.write(main_data.describe())

# Scatterplot: Skor Ulasan vs Waktu Pengiriman
st.subheader("Scatterplot: Skor Ulasan vs Waktu Pengiriman")
fig, ax = plt.subplots()
sns.scatterplot(x='review_score', y='delivery_time', data=main_data, alpha=0.7)
plt.title('Skor Ulasan vs Waktu Pengiriman')
plt.xlabel('Skor Ulasan')
plt.ylabel('Waktu Pengiriman (hari)')
st.pyplot(fig)

# Histogram untuk Skor Ulasan
st.subheader("Histogram Skor Ulasan")
score_filter = st.slider("Pilih rentang Skor Ulasan:", 1, 5, (1, 5))
filtered_data = main_data[(main_data['review_score'] >= score_filter[0]) & (main_data['review_score'] <= score_filter[1])]
fig, ax = plt.subplots()
sns.histplot(filtered_data['review_score'], bins=30, kde=True)
plt.title('Distribusi Skor Ulasan')
plt.xlabel('Skor Ulasan')
plt.ylabel('Frekuensi')
st.pyplot(fig)

# Bar Chart: Jumlah Penjualan per Kategori
st.subheader("Jumlah Penjualan per Kategori Produk")
category_sales = main_data['product_category_name_english'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=category_sales.values, y=category_sales.index, palette="viridis")
plt.title('Top 10 Kategori Produk Paling Banyak Terjual')
plt.xlabel('Jumlah Penjualan')
plt.ylabel('Kategori Produk')
st.pyplot(fig)

# Interaktivitas dengan Dropdown
st.header("Interaktivitas dengan Dropdown")
selected_category = st.selectbox("Pilih Kategori Produk:", main_data['product_category_name_english'].unique())
filtered_data_by_category = main_data[main_data['product_category_name_english'] == selected_category]

st.write(f"Data untuk kategori: {selected_category}")
st.write(filtered_data_by_category)

# Menampilkan statistik deskriptif untuk kategori terpilih
st.subheader("Statistik Deskriptif untuk Kategori Terpilih")
st.write(filtered_data_by_category.describe())

# Menyediakan opsi untuk mengunduh data yang telah difilter
csv = filtered_data_by_category.to_csv(index=False)
st.download_button("Unduh Data Kategori Terpilih", csv, "filtered_data.csv", "text/csv")
