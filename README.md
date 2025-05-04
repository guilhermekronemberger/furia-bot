# FURIA Telegram Bot
Projeto de bot para o Telegram, desenvolvido em Python como parte de um desafio técnico. O bot fornece informações sobre o time de CS da FURIA, incluindo o calendário dos próximos jogos, resultados recentes, perfil dos jogadores e uma linha do tempo com os principais marcos da história do time.

# Comandos
Ao iniciar o bot no Telegram, você verá um menu com as opções abaixo. Basta clicar ou digitar o comando desejado para acessar as informações:

- `/noticias` – Exibe as últimas novidades e atualizações sobre o time.  
- `/calendario` – Exibe os próximos jogos da equipe com datas e adversários.  
- `/resultados` – Exibe os resultados mais recentes das partidas disputadas.  
- `/time` – Exibe o elenco atual com links de redes sociais.  
- `/historia` – Exibe um resumo da trajetória do time no cenário competitivo de CS.  
- `/ajuda` – Exibe uma breve explicação de como utilizar o bot.  
- `/sobre` – Informações sobre o desenvolvimento do projeto.

## Como rodar localmente

```bash
git clone https://github.com/guilhermekronemberger/furia-bot.git
cd furia-bot
pip install -r requirements.txt
python bot_telegram/bot.py
