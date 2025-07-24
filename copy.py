import streamlit as st

text_to_copy = "This text will be copied!"
st.code(text_to_copy)

st.markdown(f"""
    <button id="copyButton" style="
        padding: 8px 16px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    ">📋 Copy</button>

    <script>
        const button = document.getElementById("copyButton");
        button.addEventListener("click", () => {{
            navigator.clipboard.writeText("{text_to_copy}");
            button.innerText = "✔ Copied!";
            setTimeout(() => {{
                button.innerText = "📋 Copy";
            }}, 1500);
        }});
    </script>
""", unsafe_allow_html=True)
