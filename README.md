# Jarvis - Assitente Pessoal

Olá, tudo bem? **Jarvis** é um Assistente Pessoal desenvolvido com o intuito de aprender Machine Learning e também estudar um pouco de Python.

# O que ele faz?

Atualmente ele tem poucas funções, mas irá ser atualizado assim que tiver melhorias (e tempo, rs), as funções atuais são:
- Reconhecimento de voz
- Responde em áudio com a voz dele
- Calcula números (multiplicação, divisão, adição e subtração)
- Responde as horas atuais
- Responde a data atual
- Responde o clima na cidade programada (Padrão: Osório/RS)
- Envia SMS para a lista pré-estabelecida (Ainda quero pegar a lista de contatos do celular)
- Aprende! É só falar assim "Jarvis, quando eu falar FRASE_1 você diz FRASE_2"
- Busca na memória as frases aprendidas
- Se perguntar, ele avisa o nível da bateria
- Baixa filmes por torrent (Precisa ter o WebTorrent CLI previamente instalado)
- Reproduz/Pausa músicas que estão sendo tocadas no Spotify conectado (precisa configurar o Spotify no notebook).
- Ele pesquisa no Wikipédia, só falar "Jarvis, pesquise ASSUNTO"

## Configurando (Linux Ubuntu)

Primeiro você precisará instalar alguns programas para que o Jarvis rode perfeitamente (ainda quero configurar nível Shell, mas por enquanto bora de tutorial), os programas são:
- Instale a versão mais atual do Python 3, rode esse comando `sudo apt install python3.8`
- Rode o comando `sudo apt install nodejs` para instalar o NodeJS.
- [WebTorrent CLI](https://github.com/webtorrent/webtorrent-cli), ele é um pacode do NodeJS, para instalar rode o comando `npm install webtorrent-cli -g`
- Agora você precisa acessar a pasta do projeto Jarvis e rodar o comando `pip3 install -r requirements.txt` isso instalará os pacotes Python necessários.
- Para escutar e pausar músicas você precisa configurar o Spotify CLI no seu Linux, siga [esse tutorial](https://pypi.org/project/spotify-cli/).
- E depois de configurar tudo, você precisa usar uma conta AWS da Amazon para usar o Amazon Polly, que faz as respostas do Jarvis, que são em texto, responder através da voz, siga [esse tutorial de configuração](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration) (Infelizmente não posso deixar minha conta AWS pré-configurada, mas é grátis por 1 ano, configure a sua e seja feliz).

## Rodando o Jarvis 
Primeiramente tenha certeza de que está tudo configurado conforme o tutorial acima.
Abra o Terminal e acesse a pasta do Projeto Jarvis, após isso digite no Terminal:
`python3 jarvis.py`
Aparecerá no Terminal a frase `Fale agora`, só perguntar o que deseja e aguardar ele responder.

## Nota


> **Nota:** O Projeto **Jarvis** é algo criado com o intuito de se divertir quando estava bêbado, então não me zoem, quero automatizar melhor a instalação e configuração dele, obrigado.

*Desenvolvedor: Jocimar Lopes
Créditos: Jocimar Lopes*