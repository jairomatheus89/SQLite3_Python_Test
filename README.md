# INSTRUÇÕES PARA RODAR A APLICAÇÃO(ATENÇÃO!):

  

## 1 passo

Instale o Git na sua maquina(**ESSENCIAL!!!**)

  

## 2 passo

escolha um diretorio para clonar o projeto

  

## 3 passo

abra o cmd, powershell ou gitBash(preferivel), clone o projeto com o comando:

`git clone https://github.com/jairomatheus89/SQLite3_Python_Test.git`

  

## 4 passo

acesse o diretorio do projeto clonado, voce vera os arquivos principais(`runApp.py, generalStructure.py, example.db, requirements.txt`)

  

## 5 passo

crie um ambiente virtual para instalar as dependencias no projeto com o comando(É ESSENCIAL!!!!!!!):
	`python -m venv venv`

## 6 passo

caso tenha utilizado o **_cmd_** ou **_powershell_** para criar o ambiente virtual utilize `.\venv\Scripts\Activate` para inicializar o mesmo. Se você esta utilizando o **_git Bash_** utilize `source venv/Scripts/activate` para inicializar o ambiente virtual

  

## 7 passo

com o ambiente virtual **ATIVADO**(voce vera a sigla `(venv)` no diretorio do seu cursor do prompt) utilize o comando `pip install -r requirements.txt` para instalar as dependencias!

  

## 8 passo

após instalar as dependencias rode o comando `python runApp.py` para iniciar a aplicação!

  

### Não esqueça de dar uma estrelinha no repositório do pai! :smile:

  

### OBS:
1:
SEMPRE QUE FOR RODAR O PROJETO TEM QUE INICIALIZAR O AMBIENTE VIRTUAL **cmd/powershell**:`.\venv\Scripts\activate` **bash**:`source venv/Scripts/activate`
#### se nao quiser inicializar o ambiente virtual sempre, terás que ir no arquivo `requirements.txt` e instalar na sua maquina as dependencias de maneira global(**_Não recomendado_**)
2:
Se quiser buildar um executável para testar na maquina sem precisar de prompt de comando utilize o comando `python setup.py build`. Ele irá criar uma pasta build com um **.exe** dentro. Só executar e ser feliz! :smile: :snake:
