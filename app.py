# Create two columns for inputs and outputs
col1, col2 = st.columns(2)

# Input fields for the parameters in the first column
with col1:
    V = st.number_input("Enter Voltage (V)", min_value=0.0)
    CL = st.number_input("Enter Core Losses (CL) in Watts", min_value=0.0)
    IL = st.number_input("Enter Full Load Current (IL) in Amps", min_value=0.0)
    K = st.number_input("Enter Loading on Generator (K)", min_value=0.0)
    Rse = st.number_input("Enter Series Field Resistance (Rse) in Ohms", min_value=0.0)
    Ra = st.number_input("Enter Armature Resistance (Ra) in Ohms", min_value=0.0)

    # Button to calculate efficiency
    if st.button("Calculate Efficiency"):
        Eff, CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)

# Output results in the second column
with col2:
    if 'Eff' in locals() and 'CUL' in locals():
        st.subheader("Results")
        st.success(f"Efficiency: {Eff:.2f}%")
        st.success(f"Copper Losses (CUL): {CUL:.2f} Watts")
    else:
        st.subheader("Results")
        st.write("Press the button to calculate efficiency.")
