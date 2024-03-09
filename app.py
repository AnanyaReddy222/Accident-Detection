import streamlit as st 
from PIL import Image
import classify 
import numpy as np
import time
#import streamlit_theme as stt

lab = {
	0:'Accidents',
	1:'dense_traffic',
	2:'Fire',
	3:'sparse_traffic'
        }

with open("style.css") as f:
  st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
html_temp = """
    <div>
    <h1 style="text-align:left;"> Emergency Accident Reporting System</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)
col1,col2  = st.beta_columns([2,2])
with col1:
  with st.beta_expander(" ℹ️ Objectives", expanded=True):
    st.write("""
              Accidents have always been a major cause for many fatalities, all around the world. Although the grounds of these fatalities can range over a lot of reasons, starting from bad roads, speeding, poor engineering plans, delayed medical aid etc. Steps can be taken on various levels to, if not completely overcome, then at least to avoid a certain percentage of the casualties caused due these accidents. Hence, EARS - Emergency Accident Reporting System which is a software that when installed in CC TV Cameras, can detect an accident and send an alert to the hospitals nearby, without any human interference, with enough information for the hospitals to act quickly, thus saving lives.
              """) 

        
with col2:
  logo = Image.open(r'logo.png')
  st.image(logo)

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption='Uploaded Image', use_column_width=True)
  st.write("")
  if st.button('predict'):
    st.write("Result...")
    label,bool = classify.predict(image.resize((224,224)))
    image.save('current.jpg')
    label = label[0]
    res = lab[np.argmax(label)]
    l = round(label[np.argmax(label)]*100,2)
    st.markdown(res +" : "+ str(l) + "%")
    if bool:
      st.markdown(" An Email has been sent to a nearby Hospital. 🚑")
      now = time.localtime()
      t = time.strftime("%H:%M:%S", now)
      st.write(t)
       

        

       
                
                
                
                
                
                
                
                
                      
                      
                      
                      

        
                      #st.write(type(t))
       







#st.title("Emergency Accident Reporting System 🚑")
