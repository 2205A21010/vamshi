import streamlit as st

# Define the Gen_Eff function
def Gen_Eff(V, CL, IL, K, Rse, Ra):
    # Calculate Copper Losses (CUL)
    CUL = (K * IL) ** 2 * (Rse + Ra)
    
    # Calculate Efficiency (Eff)
    denominator = K * V * IL + CL + CUL
    
    if denominator == 0:
        Eff = 0  # Avoid division by zero
    else:
        Eff = (K * V * IL) / denominator * 100
    
    return Eff, CUL

# Streamlit application
def main():
    # Title of the application
    st.title("02341A0259-PS1")  # Replace with your roll number and problem statement number

    # Input fields for the parameters
    V = st.number_input("Enter Voltage (V)", min_value=0.0)
    CL = st.number_input("Enter Core Losses (CL) in Watts", min_value=0.0)
    IL = st.number_input("Enter Full Load Current (IL) in Amps", min_value=0.0)
    K = st.number_input("Enter Loading on Generator (K)", min_value=0.0)
    Rse = st.number_input("Enter Series Field Resistance (Rse) in Ohms", min_value=0.0)
    Ra = st.number_input("Enter Armature Resistance (Ra) in Ohms", min_value=0.0)

    # Button to calculate efficiency
    if st.button("Calculate Efficiency"):
        Eff, CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)
        st.success(f"Efficiency: {Eff:.2f}%")
        st.success(f"Copper Losses (CUL): {CUL:.2f} Watts")

if __name__ == "__main__":
    main()
