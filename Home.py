import streamlit as st 

st.header("Hello World !")
st.subheader("Let's go") 
st.write('## H1')
st.markdown("### H1")

st.markdown("### 🌟 Key Features (Required)")
with st.form("patient_form"):
    st.markdown(
        '<div class="highlight">'
        'Please fill in the **most important** features below for accurate predictions.'
        '</div>',
        unsafe_allow_html=True
    )


submitted = st.form_submit_button("🔍 Predict")
