import os

def set_EN_variables(delib, country, topic):
    os.environ['country'] = country
    os.environ['topic'] = topic

    os.environ['chatbot'] = 'AI chatbot'
    os.environ['yes'] = 'Yes'
    os.environ['no'] = 'No'
    os.environ['convo_limit'] = 'You must complete at least 10 rounds of conversation, but can complete up to 15.'
    os.environ['intro_wait'] = 'Launching chatbot, this can take up to 20 seconds...'
    os.environ['react_intro'] = 'React to the introduction:'
    os.environ['intro_emoji'] = 'Select an emoji to continue chatting.'
    os.environ['enter_button'] = 'Enter'
    os.environ['you'] = 'You'
    os.environ['enter'] = 'Press Enter to send'
    os.environ['emoji_prompt'] = 'React to response'
    os.environ['finish_chat'] = 'Finish chat'
    os.environ['next_page'] = 'Next page'
    os.environ['feedback_page'] = 'Chatbot Responses for Feedback'
    os.environ['categories'] = 'Click to learn what each category means'
    os.environ['response'] = 'Response'
    os.environ['user'] = 'User'
    os.environ['give_feedback'] = 'Give feedback?'
    os.environ['categories_for_response'] = 'Categories for response'
    os.environ['comments'] = 'Comment for response'
    os.environ['options'] = 'Choose an option'
    os.environ['comment_prompt'] = 'Add your comment here'
    os.environ['submit'] = 'Submit'
    os.environ['submitted'] = 'Comments submitted! Click **Go to post-survey** to start the post-survey.'
    os.environ['emoji_warning_1'] = 'Please select an emoji for response '
    os.environ['emoji_warning_2'] = ' to proceed.'
    os.environ['convo_update_1'] = 'You have finished'
    os.environ['convo_update_2'] = 'round(s) of conversation. '
    os.environ['convo_warning_1'] = 'You can only ask'
    os.environ['convo_warning_2'] = 'more question(s) to the chatbot.'
    os.environ['category_1'] = 'Respectful'
    os.environ['category_2'] = 'Disrespectful'
    os.environ['category_3'] = 'Culturally knowledgeable'
    os.environ['category_4'] = 'Culturally unknowledgeable'
    os.environ['category_5'] = 'Factually correct'
    os.environ['category_6'] = 'Factually incorrect'
    os.environ['category_7'] = 'Open to listening to the user'
    os.environ['category_8'] = 'Not open to listening to user'
    os.environ['category_9'] = 'Other'
    os.environ['other_category'] = 'Other category'
    os.environ['remove'] = 'Remove'
    os.environ['specify_categories'] = 'Specify category:'
    os.environ['add_category'] = 'Add category'
    os.environ['post_survey_message'] = 'Go to post-survey'
    os.environ[
        'chat_complete'] = '**Chat complete**, thank you for chatting with the chatbot! Sometimes, chatbots produce responses that are inaccurate in a few different ways. Press **Next page** to review the chatbot\'s responses from this chat and provide feedback on them.'
    os.environ['comment_outline'] = '''
        On this page, you can provide feedback on the chatbot's responses.

        Below, you will see a list of input / response pairs from your chat. Your input is in ***green***, while the 
        chatbot's response is in ***gray***.

        To the right of a response, you can click **Yes** under **Give feedback?** if you want to provide feedback on that 
        response, or you can click **No** if not. 

        If you choose to provide feedback on a response, you can specify the type by choosing from the categories in the 
        dropdown menu. You can choose more than one. Then, fill out the comment box with your thoughts on the response.

        **You must provide feedback (positive, negative, or neutral) for at least three responses by selecting at least one category and writing a comment for each**, at which point a **Submit** button will appear at the bottom
        of the page.

        Click **Submit** when you are finished, then click **Go to post-survey** to take the post-survey.
        '''

    if delib:
        os.environ['intro_system_instruction'] = 'Respond with a list of pros and cons on the topic at hand.'
        os.environ[
            'intro_text'] = f'''Imagine you are a person from {os.environ['country']} moderating a discussion about {os.environ['topic']}. Based on the cultural values from {os.environ['country']}, provide your communication partner with stances why an average person from {os.environ['country']} would be pro/against {os.environ['topic']}. You should provide information in a casual style in English. Start the conversation with exactly the following prompt: 

        "Good afternoon. I will be your conversation partner today in a brief discussion about {os.environ['topic']}. This discussion is an opportunity for you to learn about {os.environ['topic']} in {os.environ['country']}. I want to encourage you to speak freely. You are not expected to be an expert. Also, no consensus is necessary, you do not need to agree with the stances I provide. My role is to help you learn about how people in {os.environ['country']} perceive the pros and cons of {os.environ['topic']}."

        And then provide relevant cultural information in a pros/cons list. 

        Lastly, encourage conversation by ending with "Please start off by telling us something that puzzles you about this topic."
        '''
        os.environ[
            'gen_system_instruction'] = f'''You finish your response within {os.environ['gen_max_tokens']} tokens. Do not change topics. Avoid asking "yes"/"no" questions.'''
        os.environ[
            'shorter_system_instruction'] = f'''You provide shorter, more conversational responses. Do not change topics. Avoid asking "yes"/"no" questions.'''

    else:
        os.environ['intro_system_instruction'] = ''
        os.environ[
            'intro_text'] = f'''Let’s talk about {os.environ['topic']}! Start off by telling me something that puzzles you about {os.environ['topic']}.'''
        os.environ['gen_system_instruction'] = f'''Engage in opinionated and stubborn conversation on {os.environ['topic']}. You finish your response within {os.environ['gen_max_tokens']} tokens. Avoid asking "yes"/"no" 
                                                    questions.'''
        os.environ['shorter_system_instruction'] = f'''Engage in opinionated and stubborn conversation on {os.environ['topic']}. You provide shorter, more conversational responses. Avoid asking "yes"/"no" questions.'''

    if topic == 'abortion':
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_3dTAvg2SnPonuMS'
    elif topic == 'the death penalty':
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_0DlkgM2myjGebwW'
    elif topic == 'GMOs':
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_6GtPL69KUyul5L8'
    else:
        os.environ['post_survey'] = 'https://uwmadison.co1.qualtrics.com/jfe/form/SV_0IpGwykJC3hSyNg'