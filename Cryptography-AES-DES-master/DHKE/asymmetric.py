import streamlit as st
import DHKE 
import DES

def string_to_bin(text):
  bits = text.encode('utf-8')

   # Convert bytes to binary representation
  binary = bin(int.from_bytes(bits, 'big'))[2:]
  return binary.zfill(64)

def bin_to_string(bin):
  n = int(bin, 2)
  byte_data = n.to_bytes((n.bit_length() + 7) // 8, 'big')
  return byte_data.decode('utf-8')

def hex_to_bin(hex):
    binary = bin(int(hex, 16))[2:]
    return binary

menu = ["Private", "Public", "Result", "DES"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Private":
    st.title("Get Prime Number and Alpha")
    button = st.button("Generate")

    if button:
        prime_number = DHKE.random_prime(15)
        generator = DHKE.random_integer(prime_number)

        a = DHKE.random_integer(prime_number)
        b = DHKE.random_integer(prime_number)

        st.text_input("Prime Number", prime_number)
        st.text_input("Alpha", generator)
        st.text_input("Your Private Key", a)
        st.text_input("Friend Private Key", b)

elif choice == "Public":
    st.title("Generate Public Key")
    p = st.text_input("Prime Number")
    alpha = st.text_input("Alpha")
    private_key = st.text_input("Private Key")

    button = st.button("Generate")

    if button:
        public_key = DHKE.fast_raise_power(int(alpha), int(private_key), int(p))
        st.text_area("Public Key: ", public_key)

elif choice == "Result":
    st.title("Joint Key")
    public_key = st.text_input("Friend Public Key")
    private_key = st.text_input("Your Private Key")
    p = st.text_input("Prime Number")

    button = st.button("Get")

    if button:
        result = DHKE.fast_raise_power(int(public_key), int(private_key), int(p))
        st.text_area("Joint Key: ", str(result))

elif choice == "DES":
    st.title("DES Encryption Tool")
    method = st.radio('Pick Method', ['Encryption', 'Decryption'])
    encrypt_text = ''
    decrypt_text = ''

    if method == 'Encryption':
        plaintext = st.text_input("Enter Plain Text", max_chars=8)
        key = st.text_input("Enter Key")

        bin_plaintext = string_to_bin(plaintext)

        submit = st.button("Encrypt")

        if submit:
            encrypt_text = DES.encrypt(bin_plaintext, hex_to_bin(key))
        st.text_area("Output", encrypt_text, disabled=True)
    
    if method == 'Decryption':
        ciphertext = st.text_input("Enter cipher text")
        key = st.text_input("Enter Key")

        submit = st.button("Decrypt")

        if submit:
            decrypt_text = bin_to_string(DES.decrypt(ciphertext, hex_to_bin(key)))
        st.text_area("Output", decrypt_text, disabled=True)