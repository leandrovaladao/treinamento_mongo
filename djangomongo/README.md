# Treinamento Mongo

##Instalação
Para funcionar da melhor maneira é necessário instalar o [Docker](https://docs.docker.com/install/) e o [Docker-compose](https://docs.docker.com/compose/install/), porém todo o processo pode ser feito via amiente virtual.
Caso queira fazer por ambiente virtual será necessário configurar o [MongoDB](https://www.mongodb.com/) na maquina.

## Docker
Caso tenha instalado o Docker, será necessário rodar o docker-compose up na raiz do projeto e então executar:
```dockerfile 
docker-compose up --build
```
Após as imagens web e mongo estarem criadas e em execução deverá ser executado o comando:
```dockerfile 
docker exec -it (container_id ou container_name) python manage.py makemigrations
docker exec -it (container_id ou container_name) python manage.py migrate
docker exec -it (container_id ou container_name) python manage.py createsuperuser
```

##Execução
Para executar consultas é possivel ver a documentação base da API de autenticação nas urls:

http://localhost:8000/api/token/

http://localhost:8000/api/v1/professor/

http://localhost:8000/api/v1/curso/

http://localhost:8000/api/v1/aluno/

http://localhost:8000/api/v1/user/

Todas as APIS estão bloqueadas e qualquer operação será necessária autenticação para executar.