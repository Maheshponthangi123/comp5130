from OpenSSL import crypto

# Generate a key pair
key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 2048)

# Create a self-signed certificate
cert = crypto.X509()
cert.get_subject().CN = "localhost"  # Common name
cert.set_serial_number(1000)
cert.gmtime_adj_notBefore(0)  # Certificate valid from now
cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # Valid for 1 year
cert.set_issuer(cert.get_subject())  # Issuer is self
cert.set_pubkey(key)
cert.sign(key, "sha256")  # Sign with SHA256

# Save the key and certificate to files
with open("key.pem", "wb") as f:
    f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

with open("cert.pem", "wb") as f:
    f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

print("Self-signed certificate and key generated: key.pem and cert.pem")
