import streamlit as st

# Title
st.title('Streamlit title ')
st.header('This is header')
st.subheader('This is subheader')
st.text('This is text')

# Markdown
st.markdown('# Streamlit title ')
st.markdown('## This is header')
st.markdown('### This is subheader')
st.markdown('This is Item\n'
            ' 1. Item 1\n'
            ' 2. Item 2\n'
            ' 3. Item 3')
st.markdown('This is Item\n'
            ' - Item 1\n'
            ' - Item 2\n'
            ' - Item 3')
# Error Massage
st.success("Successful")
st.info("Infomation")
st.warning("Warning!")
st.error("Error!!")
