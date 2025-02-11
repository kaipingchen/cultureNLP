import os

def set_PR_variables(delib, country, topic):
    os.environ['country'] = country
    os.environ['topic'] = topic

    os.environ['chatbot'] = 'Chatbot de IA'
    os.environ['yes'] = 'Sim'
    os.environ['no'] = 'Não'
    os.environ[
        'convo_limit'] = 'Deve completar pelo menos 10 rodadas de conversa, mas você pode completar até 15.'
    os.environ['intro_wait'] = 'Iniciando o chatbot, isso pode levar até 20 segundos...'
    os.environ['react_intro'] = 'Reação à introdução:'
    os.environ['intro_emoji'] = 'Selecione um emoji para continuar conversando.'
    os.environ['you'] = 'Você'
    os.environ['enter'] = 'Pressione Enter para enviar'
    os.environ['enter_button'] = 'Enviar'
    os.environ['emoji_prompt'] = 'Reaja à resposta'
    os.environ['finish_chat'] = 'Finalizar chat'
    os.environ['next_page'] = 'Próxima página'
    os.environ['feedback_page'] = 'Respostas do chatbot para comentários'
    os.environ['categories'] = 'Clique para saber o que significa cada categoria'
    os.environ['response'] = 'Resposta'
    os.environ['user'] = 'Usuário'
    os.environ['give_feedback'] = 'Fazer comentários?'
    os.environ['categories_for_response'] = 'Categorias para a resposta'
    os.environ['comments'] = 'Comentário para a resposta'
    os.environ['options'] = 'Escolha uma opção'
    os.environ['comment_prompt'] = 'Adicione seu comentário aqui'
    os.environ['submit'] = 'Enviar'
    os.environ[
        'submitted'] = '**Comentários enviados!** Clique em **Ir para a enquete** para começar a enquete.'

    os.environ['emoji_warning_1'] = 'Por favor, selecione um emoji para a resposta'
    os.environ['emoji_warning_2'] = ' para continuar.'
    os.environ['convo_update_1'] = 'Você completou'
    os.environ['convo_update_2'] = 'rodada(s) de conversa. '
    os.environ['convo_warning_1'] = 'Você só pode fazer mais'
    os.environ['convo_warning_2'] = 'pergunta(s) ao chatbot.'
    os.environ['category_1'] = 'Respeitoso'
    os.environ['category_2'] = 'Desrespeitoso'
    os.environ['category_3'] = 'Com conhecimento cultural'
    os.environ['category_4'] = 'Sem conhecimento cultural'
    os.environ['category_5'] = 'Objetivamente correto'
    os.environ['category_6'] = 'Objetivamente incorrecto'
    os.environ['category_7'] = 'Aberto para ouvir o usuário'
    os.environ['category_8'] = 'Não aberto para ouvir o usuário'
    os.environ['category_9'] = 'Outro'
    os.environ['other_category'] = 'Outra categoria'
    os.environ['remove'] = 'Remover'
    os.environ['specify_categories'] = 'Especificar categoria:'
    os.environ['add_category'] = 'Adicionar categoria'
    os.environ['post_survey_message'] = 'Ir para a enquete'
    os.environ[
        'chat_complete'] = '**Chat finalizado**, obrigado por conversar com o chatbot! Às vezes, os chatbots geram respostas que são imprecisas de diversas maneiras. Pressione **Próxima página** para revisar as respostas do chatbot deste chat e fornecer feedback sobre elas.'
    os.environ['comment_outline'] = '''
                    Nesta página, você pode fornecer feedback sobre as respostas do chatbot.

                    Abaixo, você verá uma lista de pares de mensagens e respostas do seu chat. Sua mensagem está em ***verde***, enquanto a resposta do chatbot está em ***cinza***.

                    À direita de uma resposta, você pode clicar em **Sim** em **Fazer comentários?** se quiser fornecer feedback sobre essa resposta, ou pode clicar em **Não** se não quiser. 

                    Se você decidir dar feedback sobre uma resposta, pode especificar o tipo escolhendo entre as categorias no menu suspenso. Você pode escolher mais de uma. Em seguida, preencha a caixa de comentários com suas considerações sobre a resposta.

                    **Você deve fornecer feedback (positivo, negativo ou neutro) para pelo menos três respostas, selecionando pelo menos uma categoria e escrevendo um comentário para cada uma**, momento em que o botão **Enviar** será habilitado.

                    Clique em **Enviar** quando terminar, depois clique em **Ir para a enquete** para começar a enquete.
                    '''

    if topic == 'os OGMs':
        topic2 = 'os organismos geneticamente modificados (OGM)'
    else:
        topic2 = topic

    if delib:
        os.environ['intro_system_instruction'] = 'Responda com uma lista de prós e contras sobre o tema em questão.'

        if country == 'Brasil':
            os.environ['intro_text'] = f'''Imagine que você é uma pessoa do Brasil moderando uma discussão sobre {topic2}. Com base nos valores culturais do Brasil, forneça ao seu companheiro de comunicação argumentos sobre por que uma pessoa média do Brasil estaria a favor ou contra {os.environ['topic']}. Você deve fornecer informações em um estilo casual em português. Comece a conversa exatamente com o seguinte aviso:

            "Boa tarde. Serei seu companheiro de conversa hoje em uma breve discussão sobre {topic2}. Esta discussão é uma oportunidade para você aprender sobre {os.environ['topic']} no Brasil. Quero te encorajar a falar livremente. Não se espera que você seja um(a) especialista. Além disso, não é necessário chegarmos a um consenso, você não precisa concordar com as posturas que eu fornecer. Meu papel é te ajudar a aprender como as pessoas no Brasil percebem os prós e os contras d{os.environ['topic']}."

            E então forneça informações culturalmente relevantes em uma lista de prós e contras.

            Por último, incentive a conversa terminando com "Por favor, comece nos contando algo que você considera controverso sobre este tema."
            '''
        else:
            os.environ['intro_text'] = f'''Imagine que você é uma pessoa dos Estados Unidos moderando uma discussão sobre {os.environ['topic']}. Com base nos valores culturais dos Estados Unidos, forneça ao seu companheiro de comunicação argumentos sobre por que uma pessoa média dos Estados Unidos estaria a favor ou contra {os.environ['topic']}. Você deve fornecer informações em um estilo casual em português. Comece a conversa exatamente com o seguinte aviso:

            “Boa tarde. Serei seu companheiro de conversa hoje em uma breve discussão sobre {os.environ['topic']}. Esta discussão é uma oportunidade para você aprender sobre {os.environ['topic']} nos Estados Unidos. Quero te encorajar a falar livremente. Não se espera que você seja um(a) especialista. Além disso, não é necessário chegarmos a um consenso, você não precisa concordar com as posturas que eu fornecer. Meu papel é te ajudar a aprender como as pessoas nos Estados Unidos percebem os prós e os contras d{os.environ['topic']}.”

            E então forneça informações culturalmente relevantes em uma lista de prós e contras.

            Por último, incentive a conversa terminando com "Por favor, comece nos contando algo que você considera controverso sobre este tema."
            '''

        os.environ['gen_system_instruction'] = f'''Termine a sua resposta dentro de {os.environ['gen_max_tokens']} tokens. Não mude de assunto. Evite perguntas de "sim"/"não".'''
        os.environ[
            'shorter_system_instruction'] = 'Use respostas curtas e casuais. Não mude de assunto. Evite perguntas de "sim"/"não".'
    else:
        os.environ['intro_system_instruction'] = ''
        os.environ[
            'intro_text'] = f'''Vamos falar sobre {topic2}! Comece nos contando algo que te confunde sobre {os.environ['topic']}.'''
        os.environ['gen_system_instruction'] = f'''Participe de conversas teimosas e carregadas de opiniões sobre {os.environ['topic']}. Termine a sua resposta dentro de {os.environ['gen_max_tokens']} tokens. Evite perguntas de "sim"/"não".'''
        os.environ[
            'shorter_system_instruction'] = f'''Participe de conversas teimosas e carregadas de opiniões sobre {os.environ['topic']}. Use respostas curtas e casuais. Evite perguntas de "sim"/"não".'''


    if topic == 'o aborto':
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_4JwGwDzYgW6DTzU'
    elif topic == 'a pena de morte':
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_7VUKFsJzLB8QBCK'
    elif topic == 'os OGMs':
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_e3uqcDEiNsU7jcW'
    else:
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_0r2kXCdezhtzrIa'