import streamlit as st
import mysql.connector

# Ambil kredensial dari Streamlit Secrets
db_host = st.secrets["db_host"]
db_user = st.secrets["db_user"]
db_password = st.secrets["db_password"]
db_name = st.secrets["db_name"]

# Koneksi ke MySQL menggunakan kredensial dari secrets.toml
conn = mysql.connector.connect(
    host=db_host,      # Host dari secrets
    user=db_user,      # Username dari secrets
    password=db_password,  # Password dari secrets
    database=db_name   # Nama database dari secrets
)

# Membuat cursor untuk mengeksekusi query
cursor = conn.cursor()

# Menjalankan query untuk mengambil data
cursor.execute("SELECT * FROM tbl_akreditasi LIMIT 100")
rows = cursor.fetchall()

# Menampilkan data yang diambil di Streamlit
st.title("Data Akreditasi")
for row in rows[:10]:  # Batasi tampilan hanya 10 baris pertama
    st.write(row)

# Menutup koneksi
conn.close()
