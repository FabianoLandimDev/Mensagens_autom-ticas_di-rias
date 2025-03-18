import pywhatkit
import schedule
import time
from datetime import datetime, timedelta

# Função para enviar mensagens
def enviar_mensagens():
    # Lista de números de telefone (com o código do país, sem o "+")
    contatos = ["5524999208540", "5532999526696", "5524993214393"]  # Exemplo: números no formato brasileiro
    mensagem = "Espero que seu dia tenha sido uma bênção, o meu foi ótimo!😊"

    for contato in contatos:
        try:
            # Envia a mensagem para cada contato
            pywhatkit.sendwhatmsg_instantly(f"+{contato}", mensagem, wait_time=15, tab_close=True)
            print(f"Mensagem enviada para +{contato} às {datetime.now().strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"Erro ao enviar mensagem para +{contato}: {e}")

# Função para iniciar o envio em intervalos de 5 minutos
def iniciar_envios():
    # Define o horário inicial e final
    hora_inicio = datetime.now()  # Agora
    hora_fim = hora_inicio + timedelta(hours=2)  # 2 horas depois

    print(f"Iniciando envios às {hora_inicio.strftime('%H:%M:%S')} e encerrando às {hora_fim.strftime('%H:%M:%S')}.")

    # Verifica se o horário final é maior que o inicial
    if hora_fim <= hora_inicio:
        print("Erro: O horário final deve ser maior que o horário inicial.")
        return


    # Agenda a função `enviar_mensagens` para ser executada a cada 5 minutos
    schedule.every(5).minutes.do(enviar_mensagens)

    # Loop principal para manter o script rodando
    while datetime.now() < hora_fim:
        schedule.run_pending()
        time.sleep(1)  # Dorme por 1 segundo para evitar uso excessivo da CPU

    print("Envios concluídos!")

if __name__ == "__main__":
    # Inicia o processo de envio
    iniciar_envios()