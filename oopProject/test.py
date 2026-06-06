# Named Enitity Model, Sentiment Analysis, Language Detection

import pprint as p # to get the dictionary is a nice format

import nlpcloud

client = nlpcloud.Client("gpt-oss-120b", "ae31134652c555eb91e98133baa4a797f5b18dfc", gpu=True, lang='en')
data = (client.entities(
    """John Doe started learning Javascript when he was 15 years old. After a couple of years he switched to Python and starter learning low level programming. He is now a Go expert at Google.""",
    searched_entity="programming languages"
))
p.pprint(data)

