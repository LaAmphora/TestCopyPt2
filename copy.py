###copy.py
import streamlit as st

text_to_copy = st.text_input("Hello, World!")

hosted_html_file = "https://testcopy.streamlit.app/files/copy.html"
iframe_url = f"{hosted_html_file}?copy={text_to_copy}"

st.markdown(f"""
    <input type="text" value="{text_to_copy}" id="copyInput" style="position: absolute; left: -9999px;">
    <button id="copyButton" onclick="copyText()" 
        style="font-size: 20px; background: none; border: none; cursor: pointer;">📋</button>

    <script>
    function copyText() {{
        var copyInput = document.getElementById("copyInput");
        copyInput.select();
        document.execCommand("copy");

        var btn = document.getElementById("copyButton");
        btn.innerHTML = "✔";
        setTimeout(function() {{
            btn.innerHTML = "📋";
        }}, 1000);
    }}
    </script>
""", unsafe_allow_html=True)