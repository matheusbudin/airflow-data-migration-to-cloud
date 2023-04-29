FROM python:3.10

#posso retirar do compose se especificar o workingdir abaixo:
#troca-se o image do compose por -> build . ( ponto = origem)
WORKDIR /usr/application/teste  

COPY requirements.txt .

RUN pip install -r requirements.txt

#copia o restante dos arquivos locais para o container
COPY . .

#execute a aplicação:
CMD python src/main.py