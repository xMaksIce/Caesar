import streamlit as st
import pandas as pd
from caesar import Caesar
Caesar = Caesar()

st.title("Шифр Цезаря")
st.header("Зашифровать текст")
text_for_encrypt = st.text_input("Открытый текст")
encr_key = st.number_input("Ключ шифрования", min_value=0, max_value=31)
encr_button = st.button("Зашифровать")
if encr_button:
    encrypted_text = Caesar.encrypt(text_for_encrypt, encr_key)
    st.write(encrypted_text)
    encr_output = f"""ШИФР-ТЕКСТ (ШТ): {encrypted_text}
КЛЮЧ: {encr_key}""" 
    save_encr_button = st.download_button("Сохранить шифр-текст", encr_output, "crypted_output.txt")


st.header("Расшифровать текст")
text_to_decrypt = st.text_input("Шифр-текст")
decr_key = st.number_input("Ключ дешифрования", min_value=0, max_value=31)
decr_button = st.button("Расшифровать")
if decr_button:
    decrypted_text = Caesar.decrypt(text_to_decrypt, decr_key)
    st.write(decrypted_text)
    decr_output = f"""ОТКРЫТЫЙ ТЕКСТ (ОТ): {decrypted_text}
КЛЮЧ: {decr_key}"""
    save_decr_button = st.download_button("Сохранить открытый текст", decr_output, "decrypted_output.txt")

st.header("Выполнить полный перебор")
text_to_bruteforce = st.text_input("Шифр-текст", key="brute")
brute_button = st.button("Полный перебор")
decr_texts = range(0, 32)
if brute_button:
    decr_texts = Caesar.bruteforce(text_to_bruteforce)
    st.table(decr_texts)
texts_to_save = map(int, st.text_input("Ключи для сохранения через запятую", value=0).split(","))
save_brute_button = st.download_button("Сохранить выбранное", "\n".join([f"{decr_texts[key]}, {key}" for key in texts_to_save]), "bruteforce_output.txt")
