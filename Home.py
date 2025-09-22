import streamlit as st 

st.header("Hello World !")
st.subheader("Let's go") 
st.write('## H1')
st.markdown("### H1")

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
    # Germ: dropdown of unique codes
    germ_options = sorted(df['Germ'].dropna().unique().tolist())
    key_inputs['Germ'] = c2.selectbox(
        "Germ Code",
        options=germ_options,
        index=germ_options.index(df['Germ'].mode()[0])
    )

    # Row 4: dropdown for scholarship level & Hypertension
    c1, c2 = st.columns(2)
    schol_options = sorted(df['scholarship level '].dropna().unique().tolist())
    key_inputs['scholarship level '] = c1.selectbox(
        "Scholarship Level",
        options=schol_options,
        index=schol_options.index(df['scholarship level '].mode()[0])
    )
    key_inputs['Hypertension'] = c2.selectbox(
        "Hypertension",
        options=[("No", 0), ("Yes", 1)],
        format_func=lambda x: x[0],
        index=1 if df['Hypertension'].mean() >= 0.5 else 0
    )[1]

    # Row 5: Charlson score & Autonomy dropdown
    c1, c2 = st.columns(2)
    key_inputs['Initial_Charlson_score'] = c1.number_input(
        "Initial Charlson Score",
        min_value=0,
        value=int(df['Initial_Charlson_score'].mean())
    )
    key_inputs['Autonomy'] = c2.selectbox(
        "Autonomy",
        options=[("No", 0), ("Yes", 1)],
        format_func=lambda x: x[0],
        index=1 if df['Autonomy'].mean() >= 0.5 else 0
    )[1]
    
