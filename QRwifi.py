import qrcode

def generate_wifi_qrcode(wifi_id, wifi_password):
    wifi_url = f"WIFI:T:WPA;S:{wifi_id};P:{wifi_password};"

    # Generate QR code
    wifi_qr = qrcode.make(wifi_url) 
    wifi_qr.show()

#username and password
username = "munamunalhome_2" #YOUR USERNAME OF WiFi
wifi_password = "9869269374" #YOUR WiFi PASSWORD

wifi_qr_generate = generate_wifi_qrcode(username, wifi_password)

