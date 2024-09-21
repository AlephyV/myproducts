### Como iniciar a aplicação
#### Versões utilizadas
* Python version: 3.10

<br/>

Primeiro começamos instalando e iniciando e venv


```sh
python3 -m venv .venv
python3 source .venv/bin/activate
```

Logo em seguida iniciaremos os containers do docker
```sh
sudo docker-compose up -d
```

E para rodar a aplicação usamos
```sh
make run
```