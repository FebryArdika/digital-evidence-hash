import streamlit as st
import hashlib

def hitung_hash(file, metode="sha256"):
    h = hashlib.new(metode)
    # Baca file per blok biar hemat memori
    for blok in iter(lambda: file.read(4096), b""):
        h.update(blok)
    file.seek(0) 
    return h.hexdigest()

st.title("🔐 Hash Calculator for Digital Evidence")


uploaded_file = st.file_uploader("Upload file bukti digital", type=None)

if uploaded_file is not None:
    st.success(f"File berhasil diupload: {uploaded_file.name}")
    
    md5_hash = hitung_hash(uploaded_file, "md5")
    sha1_hash = hitung_hash(uploaded_file, "sha1")
    sha256_hash = hitung_hash(uploaded_file, "sha256")

    # Tampilkan hasil
    st.subheader("📊 Hasil Hash:")
    st.write(f"**MD5   :** {md5_hash}")
    st.write(f"**SHA1  :** {sha1_hash}")
    st.write(f"**SHA256:** {sha256_hash}")
