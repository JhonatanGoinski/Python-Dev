# Passo a Passo
# ------------------------------ # 
# Título ChatZap                   
# Botão de iniciar o chat 
    # Popup
        # Bem vindo ao Chatzap
        # Escreva seu nome 
        # Entrar no chat 
# Chat
    # Usuário entrou (nome)
    # Mensagens de usuário
# Campo para enviar mensagem 
# Botão de enviar 
# ------------------------------ # 
import flet as ft 

def main(pagina):
    texto = ft.Text("ChatZap")

    # Código: Caixa de texto para o popup.
    nome_usuario = ft.TextField(label="Escreva seu nome")
    # FIM 

    # Criar: Campo do chat para armazenar mensagens.
    chat = ft.Column()
    # FIM 

    # Código: função pubsub.sibscribe para ser visivel mensagens enviadas para outras pessoas que estão no chat. 
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    # FIM Código: função pubsub.sibscribe para ser visivel mensagens enviadas para outras pessoas que estão no chat.

    # Código: Função para enviar mensagem
    def enviar_mensagem(evento):
        #Colocar nome do usuário na mensagem.   
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"     
        
        #Tunel de mensagem
        pagina.pubsub.send_all(texto_campo_mensagem)
        #Limpar campo mensagem 
        campo_mensagem.value = ""

        #Atualiza a função
        pagina.update()
    # FIM Código: Função para enviar mensagem    

    # Criar: Campo da mensagem 
    campo_mensagem = ft.TextField(label="Ecreva sua mensagem aqui!", on_submit=enviar_mensagem)
    # FIM 

    # Criar: Botão enviar mensagem 
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    # FIM 

    # Código: Função Botão Entrar
    def entrar_chat(evento):
        # Fechar o popup 
        popup.open = False
        # tire o botão de "Iniciar chat" da tela
        pagina.remove(botao_iniciar)
        # Chat 
        pagina.add(chat)
        # campo de enviar mensagem 
        # botao de enviar mensagem
        # ft.Row para deixar as duas funções na mesma linha. 
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)
        #Inserindo a informação de que um usuário entrou no chat. 
        texto = f"{nome_usuario.value} entrou no chat."
        #Enviando o nome do usuário para o tunel, assim ficando visivel para os demais usuários. 
        pagina.pubsub.send_all(texto)

        #Atualiza a função
        pagina.update()
     # FIM Código: Função Botão Entrar
        
    # Código: Criando o popup.
    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem vindo ao ChatZap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )
    # FIM Código: Criando o popup.

    # Código: Definindo a funcionalidade do popup (Botão Inicar Chat).
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True

        #Atualiza a função
        pagina.update()
    # FIM Código: Definindo a funcionalidade do popup (Botão Inicar Chat).
        
    # Código: Criando botão para a inicialização do popup.
    botao_iniciar = ft.ElevatedButton("Inicar Chat", on_click=iniciar_chat)
    # FIM 

    # Código: Chamando as funções da pagina.
    pagina.add(texto)
    pagina.add(botao_iniciar)
    # FIM 

    #Formato aplicativo: 
# ft.app(main)
    #Formato Web:
ft.app(main, view=ft.WEB_BROWSER)

