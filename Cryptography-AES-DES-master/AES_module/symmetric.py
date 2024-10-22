import streamlit as st
import AES2
import pyperclip

def string_to_hex(text):
  hex_text = text.encode('utf-8').hex()
  return hex_text.zfill(32)

def hex_to_string(hex):
  n = hex.lstrip('0')
  result = bytes.fromhex(n).decode('utf-8')
  return result

# User Interface
st.title("AES 128-bit Encryption Tool")
method = st.radio('Pick Method', ['Encryption', 'Decryption'])

encrypt_text = ""
decrypt_text = ""


if method == 'Encryption':
    plaintext = st.text_input("Enter Plain Text", max_chars=16)
    key = st.text_input("Enter Key", max_chars=16)

    hex_plaintext = string_to_hex(plaintext)
    key_hex = string_to_hex(key)

    submit = st.button("Encrypt")

    if submit:
        # encrypt plaintext to cipher text
        encrypt_text = AES2.encrypt(hex_plaintext, key_hex)
    st.text_area("Output" , encrypt_text, disabled=True)

if method == 'Decryption':
    ciphertext = st.text_input("Enter Encrypted Text", max_chars=32)
    key_decrypt = st.text_input("Enter Key", max_chars=16)

    key_hex = string_to_hex(key_decrypt)

    submit = st.button("Decrypt")

    if submit:
        # decrypt the text using the key
        decrypted_text_hex = AES2.decrypt(ciphertext, key_hex)
        decrypt_text = hex_to_string(decrypted_text_hex)
    st.text_area("Output", decrypt_text ,disabled=True)