import pywifi


def listar_redes_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    redes = iface.scan_results()

    # Nome do arquivo de saída
    nome_arquivo = "redes_wifi.txt"

    # Abrir o arquivo em modo de escrita
    with open(nome_arquivo, "w") as arquivo:
        for rede in redes:
            arquivo.write(f"Nome da rede: {rede.ssid}\n")
            arquivo.write(f"Sinal de qualidade: {rede.signal}\n")
            arquivo.write(f"Frequência: {rede.freq / 1000} GHz\n")
            arquivo.write(f"Endereço MAC: {rede.bssid}\n")
            arquivo.write("\n")

    print(f"As informações das redes Wi-Fi foram salvas no arquivo '{nome_arquivo}'.")


listar_redes_wifi()
