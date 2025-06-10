import streamlit as st
import mysql.connector
import os
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Ambil kredensial dari variabel lingkungan
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

print("DB_HOST:", db_host)
print("DB_USER:", db_user)
print("DB_PASSWORD:", db_password)
print("DB_NAME:", db_name)

# Koneksi ke MySQL menggunakan kredensial dari .env
conn = mysql.connector.connect(
    host=db_host,      # Host dari variabel lingkungan
    user=db_user,      # Username dari variabel lingkungan
    password=db_password,  # Password dari variabel lingkungan
    database=db_name   # Nama database dari variabel lingkungan
)

# Membuat cursor untuk mengeksekusi query
cursor = conn.cursor()

# Menjalankan query untuk mengambil data
cursor.execute("SELECT * FROM tbl_akreditasi")
rows = cursor.fetchall()

# Menampilkan data yang diambil
for row in rows:
    print(row)

# Menutup koneksi
conn.close()
# Streamlit app untuk menampilkan data dari MySQL
st.title("Data Akreditasi")
for row in rows:
    st.write(row)