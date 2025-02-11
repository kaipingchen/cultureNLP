import os

def set_ES_variables(delib, country, topic):
    os.environ['country'] = country
    os.environ['topic'] = topic

    os.environ['chatbot'] = 'Chatbot de IA'
    os.environ['yes'] = 'Sí'
    os.environ['no'] = 'No'
    os.environ[
        'convo_limit'] = 'Debe completar al menos 10 rondas de conversación, pero puede seguir y completar hasta el máximo de 15.'
    os.environ['intro_wait'] = 'Iniciando chatbot, esto puede tardar hasta 20 segundos...'
    os.environ['react_intro'] = 'Reacción a la introducción:'
    os.environ['intro_emoji'] = 'Seleccione un emoji para seguir chateando.'
    os.environ['you'] = 'Usted'
    os.environ['enter'] = 'Presione Enter para enviar'
    os.environ['enter_button'] = 'Enviar'
    os.environ['emoji_prompt'] = 'Reaccione a la respuesta'
    os.environ['finish_chat'] = 'Finalizar chat'
    os.environ['next_page'] = 'Siguiente página'
    os.environ['feedback_page'] = 'Respuestas del chatbot para comentarios'
    os.environ['categories'] = 'Haga clic para saber lo que significa cada categoría'
    os.environ['response'] = 'Respuesta'
    os.environ['user'] = 'Usuario'
    os.environ['give_feedback'] = '¿Hacer comentarios?'
    os.environ['categories_for_response'] = 'Categorías para la respuesta'
    os.environ['comments'] = 'Comentario para la respuesta'
    os.environ['options'] = 'Elija una opción'
    os.environ['comment_prompt'] = 'Agregue su comentario aquí'
    os.environ['submit'] = 'Enviar'
    os.environ['remove'] = 'Eliminar'
    os.environ['specify_categories'] = 'Especificar categoría:'
    os.environ['add_category'] = 'Agregar categoría'
    os.environ[
        'submitted'] = '¡Comentarios enviados! Haga clic en **Ir a la encuesta posterior** para comenzar la encuesta posterior.'

    os.environ['emoji_warning_1'] = 'Para continuar, por favor seleccione un emoji para la respuesta '
    os.environ['emoji_warning_2'] = '.'
    os.environ['convo_update_1'] = 'Ha terminado'
    os.environ['convo_update_2'] = 'ronda(s) de conversación. '
    os.environ['convo_warning_1'] = 'Solo puede hacerle'
    os.environ['convo_warning_2'] = 'pregunta(s) más al chatbot.'
    os.environ['category_1'] = 'Respetuoso'
    os.environ['category_2'] = 'Irrespetuoso'
    os.environ['category_3'] = 'Con conocimiento cultural'
    os.environ['category_4'] = 'Sin conocimiento cultural'
    os.environ['category_5'] = 'Objetivamente correcto'
    os.environ['category_6'] = 'Objetivamente incorrecto'
    os.environ['category_7'] = 'Abierto a escuchar al usuario'
    os.environ['category_8'] = 'no abierto a escuchar al usuario'
    os.environ['category_9'] = 'Otro'
    os.environ['other_category'] = 'Otra categoría'
    os.environ['post_survey_message'] = 'Ir a la encuesta posterior'
    os.environ[
        'chat_complete'] = '**Chat finalizado.** ¡Gracias por interactuar con el chatbot! A veces, los chatbots generan respuestas inexactas. Presione **Siguiente página** para revisar las respuestas del chatbot y proporcionar comentarios sobre ellas.'
    os.environ['comment_outline'] = '''
                En esta página, puede proporcionar comentarios sobre las respuestas del chatbot.

                A continuación, verá una lista de pares de entrada/respuesta de su chat. Su entrada está en ***verde*** y la respuesta del chatbot está en ***gris***.

                A la derecha de cada respuesta, puede indicar si desea o no hacer comentarios. 

                Si desea hacer comentarios sobre una respuesta, puede especificar el tipo de comentarios eligiendo entre las categorías del menú desplegable. Puede elegir más de un tipo de comentario. Luego, complete la casilla de comentarios con su opinión sobre la respuesta.

                **Debe proporcionar comentarios (positivos, negativos o neutrales) para al menos tres respuestas del chatbot, seleccionando al menos una categoría y escribiendo un comentario para cada una**. Luego de completar el mínimo de dos respuestas, el botón **Enviar** estará habilitado. 

                Haga clic en **Enviar** cuando haya terminado, luego haga clic en **Ir a la encuesta posterior** para realizar la encuesta posterior.
                '''

    if topic == 'los OGMs':
        topic2 = 'los organismos modificados geneticamente (OGMs)'
    else:
        topic2 = topic

    if delib:
        os.environ['intro_system_instruction'] = 'Responde con una lista de pros y contras sobre el tema en cuestión.'
        os.environ[
            'intro_text'] = f'''Imagine que es una persona de {os.environ['country']} moderando una discusión sobre {topic2}. Basado en los valores culturales de {os.environ['country']}, dele a su compañero de conversación argumentos sobre por qué una persona promedio de {os.environ['country']} estaría a favor/en contra de {os.environ['topic']}. Debe darle la información en un estilo coloquial en español. Comience la conversación usando exactamente este mensaje:

        "Buenas tardes. Seré su compañero de conversación hoy en una breve discusión sobre {topic2}. Esta conversación es una oportunidad para que aprenda sobre {os.environ['topic']} en {os.environ['country']}. Quiero animarle a que hable libremente. No se espera que sea un experto. Además, no es necesario llegar a un consenso, no necesita estar de acuerdo con mis posturas. Mi papel es ayudarle a aprender cómo las personas en {os.environ['country']} perciben los pros y los contras de {os.environ['topic']}."

        Luego comporte información culturalmente relevante en una lista de pros y contras.

        Por último, fomente la conversación terminando con "Por favor, comience contándonos algo que encuentre controversial sobre este tema." 
        '''
        os.environ['gen_system_instruction'] = f'''Termina tu respuesta dentro de {os.environ['gen_max_tokens']} tokens. No cambies de tema. Evite preguntas de "sí"/"no".'''
        os.environ['shorter_system_instruction'] = f'''Proporciona respuestas más breves y casuales. No cambies de tema. Evite preguntas de "sí"/"no".'''
    else:
        os.environ['intro_system_instruction'] = ''
        os.environ[
            'intro_text'] = f'''¡Hablemos sobre {topic2}! Primero, cuéntame algo que encuentres controversial sobre {os.environ['topic']}.'''
        os.environ['gen_system_instruction'] = f'''Participe en conversaciones obstinadas y cargadas de opiniones sobre {os.environ['topic']}. Termina tu respuesta dentro de {os.environ['gen_max_tokens']} tokens. Evite preguntas de "sí"/"no".'''
        os.environ[
            'shorter_system_instruction'] = f'''Participe en conversaciones obstinadas y cargadas de opiniones sobre {os.environ['topic']}. Proporciona respuestas más breves y casuales. Evite preguntas de "sí"/"no".'''

    if topic == 'el aborto':
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_bxtLLLbLmJBCRWm'
    elif topic == 'la pena de muerte':
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_8pnDcNM6g9vhsvY'
    elif topic == 'los OGMs':
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_a5IN1x99Js58ofA'
    else:
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_0ex38bSxVGfxFuC'
