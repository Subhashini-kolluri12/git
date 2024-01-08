import streamlit as st
st.markdown("<h1 style='text-align:center;'>Apply Here</h1>",unsafe_allow_html=True)
with st.form("Form 7"):
    col1,col2=st.columns(2)
    f_name=col1.text_input("First Name")
    L_name=col2.text_input("Last Name")
    col3,col4=st.columns(2)
    Email=col3.text_input("Email")
    Exprience=col4.text_input("Total Work Exprience")
    col5,col6=st.columns(2)
    Notice_period=col5.text_input("Notice Period")
    Location=col6.text_input("Preferred Loaction")
    Resume=st.file_uploader("Upload Your Resume",type=["pdf","docs"])
    st_state=st.form_submit_button("Submit")
    if st_state:
        if f_name == "" or L_name == "" or Email == "" or Exprience == "" or Notice_period == "" or Location == "" or Resume is None:
            st.warning("Please fill all fields")
        else:
            st.success("Submitted Successfully")