from pathlib import Path
import hashlib
import json
from datetime import datetime
import time



while (True):
    pasta_input = input("Insira o caminho a ser analizado: ").strip()
    pasta = Path (pasta_input)

    if pasta.exists() and pasta.is_dir():
        break
    else:
        print("Caminho inválido. Tente novamente.")

try:
    while(True):
    
        dados_atuais = []

        try:
            with open("hashes.json", "r", encoding="utf-8") as f:
                dados_antigos = json.load(f)
        except FileNotFoundError:
            dados_antigos = []

        print("Iniciando processo")

        for item in pasta.iterdir():
            if item.is_file() or item.is_dir():
                nome = item.name
                caminho = str(item.resolve())
                tamanho = item.stat().st_size
                data_modificacao = datetime.fromtimestamp(item.stat().st_mtime).strftime("%d-%m-%Y %H:%M:%S")
                       
            if item.is_file():
                with open(item, 'rb') as f:
                    conteudo_binario = f.read()
                hash_sha256 = hashlib.sha256(conteudo_binario).hexdigest()
                sha256 = hash_sha256
                extensao = item.suffix.lower()
                tipo = extensao[1:] if extensao else "sem extensão"
            else:
                sha256 = hashlib.sha256(f"{nome}{data_modificacao}".encode()).hexdigest()
                tipo = "pasta"

            dados_atuais.append({
                "nome": nome,
                "caminho": caminho,
                "tamanho": tamanho,
                "sha256": sha256,
                "data_att": data_modificacao,
                "tipo": tipo
            })

        antigos_dict = {item['caminho']: item for item in dados_antigos}
        atuais_dict = {item['caminho']: item for item in dados_atuais}

        alteracoes_encontradas = False

        for caminho, item_atual in atuais_dict.items():
            if caminho in antigos_dict:
                if item_atual['sha256'] != antigos_dict[caminho]['sha256']:
                    alteracoes_encontradas = True
                    print(" Arquivo MODIFICADO:")
                    print(f" {item_atual['nome']}")
                    print(f" Caminho: {caminho}")
                    print(f" Última modificação: {item_atual['data_att']}")
                    print(f" SHA-256 ANTIGO: {antigos_dict[caminho]['sha256']}")
                    print(f" SHA-256 NOVO : {item_atual['sha256']}")
                    print(f" Tipo do arquivo: {item_atual['tipo']}")
                    print("-" * 40)
                    
            else:
                alteracoes_encontradas = True
                print(" Novo arquivo DETECTADO:")
                print(f" {item_atual['nome']}")
                print(f" Caminho: {caminho}")
                print(f" Tamanho: {item_atual['tamanho']} bytes")
                print(f" SHA-256: {item_atual['sha256']}")
                print(f" Modificado em: {item_atual['data_att']}")
                print(f" Tipo do arquivo: {item_atual['tipo']}")
                print("-" * 40)
        for caminho, item_antigo in antigos_dict.items():
            if caminho not in atuais_dict:
                alteracoes_encontradas = True
                print(" Arquivo REMOVIDO:")
                print(f" {item_antigo['nome']}")
                print(f" Caminho: {caminho}")
                print(f" Tipo do arquivo: {item_antigo['tipo']}")
                print("-" * 40)

        if not alteracoes_encontradas:
            print("Nenhuma alteração detectada.")


        with open("hashes.json", "w", encoding="utf-8") as f:
            json.dump(dados_atuais, f, indent=4,ensure_ascii=False)

        print("Hashes gerados e salvos.")        
        
        time.sleep(10)
except KeyboardInterrupt:
    print("\nMonitoramento encerrado pelo usuário.")
