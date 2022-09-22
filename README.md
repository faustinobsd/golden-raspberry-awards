# golden-raspberry-awards
Projeto de demonstração para processo seletivo.

## Pré-requisitos

**Instalando Python e Git**

Instale o [Python 3](https://realpython.com/installing-python/) em seu computador.

Instale o [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/) em seu computador.

**Clone o projeto**

Em um terminal, digite os seguintes comandos:

```bash
git clone https://github.com/faustinobsd/golden-raspberry-awards.git
cd golden-raspberry-awards
```

**Venv**

Recomenda-se utlizar o [venv](https://docs.python.org/3/library/venv.html) para isolar sua instalação do Python, bem como suas libs.

Em seu terminal previamente aberto, execute os comandos:

```bash
py -m venv env
.\env\Scripts\activate
```

**Instalando dependências**

Para instalar todas as dependências necessárias para o projeto, execute em seu terminal:

```bash
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

## Testes de integração

Testes de integração foram implementados com o [pytest](https://docs.pytest.org/en/latest/) e com o TestClient do FastAPI.

Para rodar todos os testes, execute em seu terminal:

```bash
pytest
```

Também foi implementada a Integração Contínua em conjunto com o Github, que pode ser visualizada em [Actions](https://github.com/faustinobsd/golden-raspberry-awards/actions).

## Rodando a API

Para rodar o projeto, execute em seu terminal:

```bash
uvicorn api.app:app
```

Para acessar a documentação da API, acesse [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/) em seu navegador.

Na página da documentação você poderá efetuar um teste de retorno da API, expandindo *GET /intervals* e clicar em *Try it out* e depois em *Execute*.

Outros verbos do CRUD não foram implementados, seguindo a especificação do teste.
