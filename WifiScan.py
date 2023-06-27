import pywifi


def listar_redes_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    redes = iface.scan_results()

    for rede in redes:
        print(f"Nome da rede: {rede.ssid}")
        print(f"Sinal de qualidade: {rede.signal}")
        print(f"Frequência: {rede.freq / 1000} GHz")
        print(f"Endereço MAC: {rede.bssid}")
        print()


listar_redes_wifi()
