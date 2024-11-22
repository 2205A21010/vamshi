import streamlit as st

st.title("2205a21010-ps10")

def Gen_Eff(V, CL, IL, K, Rse, Ra):
    # Correcting the formula for CUL
    CUL = (K * IL) * 2 * (Rse + Ra)
    # Efficiency formula
    Eff = ((K * V * IL) / ((K * V * IL) + CL + CUL)) * 100
    return CUL, Eff

st.text("Calculate the efficiency of DC series Generator for various loads")

col1, col2 = st.columns(2)
with col1:
    with st.container():
        V = st.number_input("V: in volts", value=1)
        IL = st.number_input("IL: in amps", value=1)
        Rse = st.number_input("Rse: in ohms", value=1)
        Ra = st.number_input("Ra: in ohms", value=1)
        CL = st.number_input("CL: in watts", value=1)
        K = st.number_input("Constant (K)", value=1)
    compute = st.button("Compute")

with col2:
    with st.container():
        if compute:
            CUL, Eff = Gen_Eff(V, CL, IL, K, Rse, Ra)
            st.write(f"CUL = {CUL:.2f} Watts")
            st.write(f"Efficiency = {Eff:.2f}%")
