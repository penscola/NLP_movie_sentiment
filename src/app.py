import streamlit as st
import streamlit.components.v1 as com
#import libraries
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
import numpy as np
#convert logits to probabilities
from scipy.special import softmax
from transformers import pipeline

#Set the page configs
st.set_page_config(page_title='Movie Sentiments Analysis',page_icon='🎬',layout='wide')

# Movie Sentiment Analysis Animation
st.markdown("<h1 style='text-align: center'> Movie Sentiment Analysis </h1>", unsafe_allow_html=True)
st.image("https://media.istockphoto.com/id/1055587418/vector/banner-for-online-cinema-with-old-movie-projector.jpg?s=612x612&w=0&k=20&c=ZsMSmd6CZfuUVDAvUSTb9XHBqeg4ucb43n52xV5-y1c=", use_column_width=True)
st.write("<h2 style='font-size: 24px;'> Analyze movie reviews and discover the sentiment of the audience </h2>", unsafe_allow_html=True)


# Create a form to take user inputs
with st.form(key='sentence', clear_on_submit = True):  
    # Input text
    text = st.text_area('Copy and paste a sentence(s) or type one',
                        placeholder='I really enjoyed the movie, it was so entertaining.')
    # Set examples related to movie sentiments
    alt_text = st.selectbox("Can't Type? Select an Example below", (
        'The movie was amazing, I loved every moment of it.',
        'I found the acting in the movie to be quite impressive.',
        'This film was a complete waste of my time, terrible.',
        'The plot of the movie was confusing and hard to follow.',
        'The cinematography in this film is outstanding.'))
    # Select a model
    models = {
        'Bert': 'UholoDala/sentence_sentiments_analysis_bert',
        'Distilbert': 'UholoDala/sentence_sentiments_analysis_distilbert',
        'Roberta': 'UholoDala/sentence_sentiments_analysis_roberta'
    }
    model = st.selectbox('Which model would you want to Use?', ('Bert', 'Distilbert', 'Roberta'))
    # Submit
    submit = st.form_submit_button('Predict', 'Continue processing input')

       
# Clear button
clear = st.button('Clear')


    
selected_model=models[model]


#create columns to show outputs
col1,col2,col3=st.columns(3)
col1.write('<h2 style="font-size: 24px;"> Sentiment Emoji </h2>',unsafe_allow_html=True)
col2.write('<h2 style="font-size: 24px;"> How this user feels about the movie </h2>',unsafe_allow_html=True)
col3.write('<h2 style="font-size: 24px;"> Confidence of this prediction </h2>',unsafe_allow_html=True)

if submit:
    #Check text
    if text=="":
        text=alt_text
        st.success(f"Input text is set to:  '{text}'")    
    else:
        st.success('Text received',icon='✅')
        
    #import the model
    pipe=pipeline(model=selected_model)

#pass text to model
    output=pipe(text)
    output_dict=output[0]
    lable=output_dict['label']
    score=output_dict['score']
    
        #output
    if lable=='NEGATIVE' or lable=='LABEL_0':
        with col1:
            com.iframe("https://embed.lottiefiles.com/animation/125694")
        col2.write('NEGATIVE')
        col3.write(f'{score:.2%}')
    else:
        lable=='POSITIVE'or lable=='LABEL_2'
        with col1:
            com.iframe("https://embed.lottiefiles.com/animation/148485")
        col2.write('POSITIVE')
        col3.write(f'{score:.2%}')

# Clear button action
text = ""  # Clear the input text
if clear:
    st.success('Input fields cleared', icon='✅')
    