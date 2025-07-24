###copy.py
import streamlit as st

text_to_copy = st.text_input("Hello, World!")

hosted_html_file = "https://testcopy.streamlit.app/files/copy.html"
iframe_url = f"{hosted_html_file}?copy={text_to_copy}"

st.markdown(f"""
    <input type="text" value="{text_to_copy}" id="copyInput"
           style="position: absolute; left: -9999px;">

    <button onclick="copyText()" style="
        padding: 8px 16px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    ">📋 Copy to Clipboard</button>

    <script>
    function copyText() {{
        const copyInput = document.getElementById("copyInput");
        copyInput.select();
        copyInput.setSelectionRange(0, 99999);  // For mobile
        document.execCommand("copy");

        const button = document.querySelector("button");
        button.innerText = "✔ Copied!";
        setTimeout(() => {{
            button.innerText = "📋 Copy to Clipboard";
        }}, 1500);
    }}
    </script>
""", unsafe_allow_html=True)