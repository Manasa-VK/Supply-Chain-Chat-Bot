# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:02:51 2023

@author: Manasa VK

Creating chatbot for Health Care Supply chain using Gardio
"""

import openai 
import gradio as gd
openai.api_key = "Your Own API Key"




def openai_answers(text):
    system_prompt = '''
    You are an Health Care Supply Chain Industry Expert, Help the users with their doubts from your knowledge.
    Keep the answers in about 5 to 8 lines. 
    Use Professional language and complex terminologies.
    '''
    ## Generate triplet pairs
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      messages=[{"role": "system", "content": system_prompt},
                {"role": "user", "content": "{}".format(text)}],
      temperature = 0.5
    )
    msg = completion['choices'][0]['message']['content']
    
    return msg
    

def chatbot(input, history = []):
    output = openai_answers(input)
    history.append((input, output))
    return history, history

gd.Interface(fn = chatbot, 
             title = "Health Care Supply Chain Expert 😊",
             description = "Hey There, \n\nAsk me any doubts you may have on supply chain industry!",
             inputs = ['text', 'state'],
             outputs = ['chatbot', 'state']).launch(share = True)




