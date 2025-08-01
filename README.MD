FileMonitor - Monitoramento de Alterações em Arquivos e Pastas
==============================================================

Um script Python que monitora uma pasta e detecta automaticamente qualquer alteração, criação ou remoção de arquivos e diretórios. Ele exibe detalhes como: 
- Nome do item
- Caminho
- Tamanho
- Data de modificação
- Tipo do arquivo (usando MIME)
- Hash SHA-256

Ideal para fins de auditoria, segurança e controle de integridade.

------------------------------------------------------------

Funcionalidades:
----------------
- Detecta arquivos modificados
- Detecta arquivos e pastas novos
- Detecta remoção de arquivos e pastas
- Identifica o tipo de arquivo com base no tipo MIME
- Gera e compara hashes SHA-256
- Salva histórico em "hashes.json"
- Loop contínuo com pausa de 10 segundos entre análises

------------------------------------------------------------

Como usar:
----------
1. Instale o Python 3.9 ou superior.

2. Clone este repositório ou baixe o script `monitor.py`.

3. Execute o script:

   > python monitor.py

4. Insira o caminho da pasta que deseja monitorar quando solicitado.

5. O script irá rodar indefinidamente até que seja interrompido com Ctrl + C.

------------------------------------------------------------

Requisitos:
-----------
- Python 3.9 ou superior
- Nenhuma biblioteca externa necessária (tudo é feito com módulos padrão)

------------------------------------------------------------

Exemplo de saída:
-----------------
 Novo arquivo DETECTADO:
  relatório.txt
 Caminho: C:\Users\vinicius\Documentos\relatório.txt
 Tamanho: 1.024 bytes
 SHA-256: 5c2397d3e2...
 Modificado em: 01-08-2025 12:30:20
 Tipo do arquivo: text/plain
----------------------------------------

------------------------------------------------------------

Formato do arquivo "hashes.json":
---------------------------------
[
  {
    "nome": "relatório.txt",
    "caminho": "C:\\Users\\vinicius\\Documentos\\relatório.txt",
    "tamanho": 1024,
    "sha256": "5c2397d3e2...",
    "data_att": "01-08-2025 12:30:20",
    "tipo": "text/plain"
  }
]

------------------------------------------------------------

Sugestões de uso:
-----------------
- Auditoria de documentos importantes
- Monitoramento de pastas compartilhadas
- Controle de integridade em ambientes sensíveis

------------------------------------------------------------

Encerramento:
-------------
Para encerrar o monitoramento, pressione Ctrl + C. O script terminará de forma segura e salvará os dados coletados.

------------------------------------------------------------

Licença:
--------
MIT License

------------------------------------------------------------

Autor:
------
Vinicius Fernandes

