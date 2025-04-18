import streamlit as st

# with st.chat_message(name="assistant",avatar="👩"):
#     st.write("Hellow 👋")

st.title("Echo bot")

# initialize chat history 
if "messages" not in st.session_state :
    st.session_state.messages = []

# Display chat messages from histoy on app return
for message in st.session_state.messages:    
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input 

if prompt := st.chat_input("what is up?"):
    # Display user message in chat messsage container 
    with st.chat_message("user"):
        st.markdown(prompt)

# Add user message to chat history 
st.session_state.messages.append({"role" : "user" , "content" : prompt})

response = f"Echo : {prompt}"

# Display assistant response in chat message container 
with st.chat_message("assistant"):
    st.markdown(response)

# Add asistant response to chat history 
st.session_state.messages.append({"role" : "assistant" , "content" : response})