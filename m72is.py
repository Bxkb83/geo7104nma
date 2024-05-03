import os
import webbrowser
import time
import pyfiglet
from datetime import datetime
import socket

def get_ip():
    try:
        # Bağlı olduğunuz ağı kullanarak IP adresinizi alın
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        print(f"IP adresi alınamadı. Hata: {e}")
        return "UNKNOWN"

def get_current_time():
    return datetime.now().strftime("%H:%M %p")

def fnark_ascii_art():
    return pyfiglet.figlet_format("is bank", font="banner")

def print_menu():
    print("\033[1;32m")  # Neon Yeşil
    print(fnark_ascii_art())
    print("\033[1;36m")  # Neon Turkuaz
    print(f"[+]  Yapimci      ➤ inekyiyenaslan     ")
    print("[+]  Telegram     ➤ @isbank0      ")
    print("[+]  Versiyon     ➤ 1.0.5      ")
    print(f"[+]  İp Adresin   ➤ {get_ip()}      ")
    print(f"[+]  Saat         ➤ {get_current_time()}      ")
    print("\033[1;35m")  # Neon Kırmızı
    print("[•]  Tarih        ➤", datetime.now().strftime("%d/%B/%Y      "))
    print("\033[1;36m")  # Neon Turkuaz
    print("[01] CC CHECKER [BEST] ")
    print("[02] YAKINDA ")
    print("[03] YAKINDA ")
    print("[04] YAKINDA ")
    print("[05] KANAL  ")
    print("[00] EXIT")
    print("\033[0m")  # Reset (Renkleri sıfırla)

def open_file(file_name):
    try:
        os.system(f"python {file_name}")
    except Exception as e:
        print(f"Hata: {e}")

def main():
    while True:
        print_menu()

        choice = input("[❯] CHOOSE: ")

        if choice == "01":
            os.system('clear')
            open_file("pahfkcb")
        elif choice == "02":
            os.system('clear')
            open_file("pahfkcb")
        elif choice == "03":
            os.system('clear')
            open_file("pahfkcb")
        elif choice == "04":
            os.system('clear')
            open_file("pahfkcb")
        elif choice == "05":
            webbrowser.open('https://t.me/isbank0')
            os.system('clear')
        elif choice == "00":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek. Lütfen 01, 02, 03, 04 veya 05 girin.")
            time.sleep(5)
            os.system('clear')

if __name__ == "__main__":
    main()
