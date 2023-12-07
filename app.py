import streamlit as st

st.title(" this is a Title")
st.header(" This is a Header")
st.subheader("thsi is subheader")
st.write("This is text with write  method")
st.caption("This is a caption")

with open("./contents/REAM.md","r", encoding='UTF-8") as f:
          markdown_text=f.read()
st.markdown(markdown_text, unsafe_allow_html=True)
