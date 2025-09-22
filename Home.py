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

    key_inputs = {}

    # Row 1: Numeric
    c1, c2 = st.columns(2)
    key_inputs['Age'] = c1.number_input(
        "Age (years)",
        min_value=0, max_value=120,
        value=int(df['Age'].mean())
    )
    key_inputs['BMI_start_PD'] = c2.number_input(
        "BMI at Start of PD",
        value=float(df['BMI_start_PD'].mean())
    )

    # Row 2: Numeric
    c1, c2 = st.columns(2)
    key_inputs['Initial_RRF '] = c1.number_input(
        "Initial RRF",
        value=float(df['Initial_RRF '].mean())
    )
    key_inputs['Initial_albumin'] = c2.number_input(
        "Initial Albumin",
        value=float(df['Initial_albumin'].mean())
    )

    # Row 3: Numeric & Categorical dropdown for Germ
    c1, c2 = st.columns(2)
    key_inputs['Nbre_peritonitis'] = c1.number_input(
        "Number of Peritonitis Episodes",
        min_value=0,
        value=int(df['Nbre_peritonitis'].mean())
    )
    submitted = st.form_submit_button("🔍 Predict")
