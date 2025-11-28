import requests

# LINK DIRETO DA IMAGEM NO ONEDRIVE
url = "https://onedrive.live.com/download?photosData=%2Fshare%2F841D7FD2D9517C62%21s6bd5ada4e1b74a2785d1bcf07ee0f855%3Fithint%3Dphoto%26e%3DccfSJ3%26migratedtospo%3Dtrue&redeem=aHR0cHM6Ly8xZHJ2Lm1zL2kvYy84NDFkN2ZkMmQ5NTE3YzYyL0VhU3QxV3UzNFNkS2hkRzg4SDdnLUZVQndSdDNnUzZwNC1SMDJ1djRGcmZNckE_ZT1jY2ZTSjM&view=8"
output_file = "Ranking geral.png"

print("Baixando imagem do OneDrive...")

response = requests.get(url)

if response.status_code == 200:
    with open(output_file, "wb") as file:
        file.write(response.content)
    print("Imagem atualizada no repositório!")
else:
    raise Exception(f"Erro ao baixar imagem: {response.status_code}")
