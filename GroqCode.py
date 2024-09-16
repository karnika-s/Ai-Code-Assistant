import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
# Fetch API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("API key not found. Please set the 'GROQ_API_KEY' environment variable.")
else:
    # Initialize Groq client with the API key
    client = Groq(api_key=api_key)

    # Function to generate code from user input
    def generate_code(instruction):
        completion = client.chat.completions.create(
            model="gemma-7b-it",
            messages=[
                {
                    "role": "user",
                    "content": instruction
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        generated_code = ""
        for chunk in completion:
            generated_code += chunk.choices[0].delta.content or ""
            # Stream the code as it's generated
        st.code(generated_code, language='python')    
        return generated_code

    # Streamlit app layout
    st.title("Groq Coding Assistant")

    # User input for instructions
    user_input = st.text_area("Enter your code instruction:")

    # Generate button
    if st.button("Generate Code"):
        if user_input:
            st.write("Generating code based on your instruction...")
            generated_code = generate_code(user_input)
            st.success("Code generation complete!")
       
