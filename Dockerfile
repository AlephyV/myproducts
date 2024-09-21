# Dockerfile
FROM mongo:latest

# Expor a porta padrão do MongoDB
EXPOSE 27017

# Comando padrão para iniciar o MongoDB
CMD ["mongod"]
