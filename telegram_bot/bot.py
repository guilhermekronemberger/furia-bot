import telebot
import profile
import menu
from config import CHAVE_API

bot = telebot.TeleBot(CHAVE_API)


#RETORNAR AO MENU INICIAL
@bot.message_handler(func=lambda msg: msg.text == menu.retornar)
def checar(mensagem):
    bot.send_message(mensagem.chat.id, menu.inicial)

#MENU COM AS ULTIMAS NOTICIAS 
@bot.message_handler(commands=['noticias'])
def noticias(mensagem):
    bot.send_message(mensagem.chat.id, f'{menu.noticias}\n\n{menu.retornar}')

#MENU COM O CALENDARIO DOS PROXIMOS JOGOS
@bot.message_handler(commands=['calendario'])
def calendario(mensagem):
    bot.send_message(mensagem.chat.id, f'{menu.calendario}\n\n{menu.retornar}')

#MENU DO ULTIMOS RESULTADOS
@bot.message_handler(commands=['resultados'])
def resultados(mensagem):
    bot.send_message(mensagem.chat.id, f'{menu.resultados}\n\n{menu.retornar}')

#MENU DO TIME E PROFILE DOS JOGADORES
@bot.message_handler(commands=['time'])
def time(mensagem):
    bot.send_message(mensagem.chat.id, f'{menu.time}\n\n{menu.retornar}')

@bot.message_handler(commands=list(profile.jogadores.keys()))
def jogador_info(mensagem):
    nome_jogador = mensagem.text.lstrip('/').lower()  
    perfil_jogador = profile.jogadores.get(nome_jogador)

    if perfil_jogador:
        bot.send_message(mensagem.chat.id, f'{perfil_jogador}\n{menu.retornar}')

    else:
        bot.send_message(mensagem.chat.id, 'Jogador não encontrado.')

#MENU HISTORIA DO TIME
@bot.message_handler(commands=['historia'])
def resultados(mensagem):
    bot.send_message(mensagem.chat.id, f'{menu.historia}\n\n{menu.retornar}')

#MENU COM OS TITULOS 
@bot.message_handler(commands=['titulos'])
def resultados(mensagem):
    bot.send_message(mensagem.chat.id, f'{menu.titulos}\n\n{menu.retornar}')

#MENU DE AJUDA E SOBRE O DESENVOLVIMENTO
@bot.message_handler(commands=['ajuda'])
def ajuda(mensagem):
    bot.send_message(mensagem.chat.id, f'{menu.ajuda}\n\n{menu.retornar}')

@bot.message_handler(commands=['sobre'])
def sobre(mensagem):
    bot.send_message(mensagem.chat.id, f'{menu.sobre}\n\n{menu.retornar}')

#MENSAGEM INICIAL
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, f'{menu.bem_vindo}\n\n{menu.inicial}')


print("Bot online...")
bot.polling()
