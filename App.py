import streamlit as st
from PIL import Image
from streamlit_webrtc import webrtc_streamer
st.set_page_config(page_title="My Gallery", page_icon="IMG-20211015-WA0003.jpg" )

#nav
choices=["Images","Videos"]
choice=st.sidebar.selectbox("Select the media type",choices)


#choice
if choice=="Images":
    upload=st.file_uploader("Your image here")
    text=st.text_input("Enter caption")
    if upload is not None:
        image=st.image(upload,caption=text)
    st.write("---")
    use_cam=st.checkbox("Use camera")
    if(use_cam):
        textv=st.text_input("Enter caption input")
        capture=st.camera_input("Smile")
        if capture is not None:
            image=st.image(capture,caption=textv)
elif choice=="Videos":
    upload=st.file_uploader("Your video here")
    text=st.text_input("Enter caption")
    if upload is not None:
        video=upload.read()
        st.video(upload)
        st.caption(text)
    st.write("---")
    use_cam=st.checkbox("Use camera")
    textv=st.text_input("Enter caption input")
    if(use_cam):
        evidance=webrtc_streamer(key="example")
        st.caption(textv)
        
