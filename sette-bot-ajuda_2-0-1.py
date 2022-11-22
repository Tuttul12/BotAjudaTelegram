import telebot

#Dados do bot
CHAVE_API= "AQUI VAI O TOKEN"
chat_id = -cod_chat
bot = telebot.TeleBot(CHAVE_API)
#Variáveis usáveis
sup_chat_id = -cod_chat
noc_chat_id = -cod_chat

v_noc = "NOC"
v_sup = "SUPORTE"
v_ajuda = "AJUDA"

#Comandos para o Bot
@bot.message_handler(commands=["suporte"])
def suporte(msg):
    bot.reply_to(msg, """
        Para solicitar algo para a equipe do Suporte, abra um chamado no ClickUp ou IXC.
Caso for urgente, pode mandar aqui no grupo sua dúvida e citar a palavra 'Suporte' que eu encaminho
sua mensagem para os responsáveis!!""")

@bot.message_handler(commands=["noc"])
def noc(msg):
    bot.reply_to(msg, """
    Para solicitar algo para a equipe do NOC, abra um chamado no ClickUp, IXC ou GLPI.
Caso for urgente, pode mandar aqui no grupo sua solicitação e citar a palavra 'NOC' que eu encaminho
sua mensagem para os responsáveis!!""")

@bot.message_handler(commands=["notificacao"])
def notificacao(msg):
    bot.reply_to(msg, """
    Entre no canal de notificação e fique por dentro dos avisos: https://t.me/+OGXeaP9YbEFmNmEx""")

@bot.message_handler(commands=["comunicados"])
def comunicados(msg):
    bot.reply_to(msg, """
    **Comunicamos que, a partir do dia 23/11/2022, o grupo do Whatsapp
da SETTE será migrado para este grupo do telegram.** \U0001F919 """)

#Verificar se a mensagem recebida no grupo contém palavras chave

def verificar(mensagem):
    if v_noc in mensagem.text.upper():
        encaminhar_noc = mensagem.text
        bot.send_message(chat_id=noc_chat_id, text=encaminhar_noc)
        return True
    elif v_sup in mensagem.text.upper():
        encaminhar_sup = mensagem.text
        bot.send_message(chat_id=noc_chat_id, text=encaminhar_sup)
        return True
    elif v_ajuda in mensagem.text.upper():
        bot.reply_to(mensagem, """
            Para usar a minha ajuda, você pode digitar '/' e digitar a opção, ou só clicar nas opções abaixo:
/suporte
/noc
/notificacao
/comunicados""")

    else:
        return False

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem," Sua mensagem foi encaminhada para o grupo responsável. ")

#Instância do Bot
while(True):
    try:
        bot.polling(none_stop=True, interval=3)
    except:
        time.sleep(3)