import streamlit as st


def Gen_Eff(V, CL, IL, K, Rse, Ra):
    
    CUL = (K * IL) ** 2 * (Rse + Ra)
    

    denominator = K * V * IL + CL + CUL
    
    if denominator == 0:
        Eff = 0  # Avoid division by zero
    else:
        Eff = (K * V * IL) / denominator * 100
    
    return Eff, CUL


def main():
   
    st.title("2205A21010-PS1")  
    
    V = st.number_input("Enter Voltage (V)", min_value=0.0)
    CL = st.number_input("Enter Core Losses (CL) in Watts", min_value=0.0)
    IL = st.number_input("Enter Full Load Current (IL) in Amps", min_value=0.0)
    K = st.number_input("Enter Loading on Generator (K)", min_value=0.0)
    Rse = st.number_input("Enter Series Field Resistance (Rse) in Ohms", min_value=0.0)
    Ra = st.number_input("Enter Armature Resistance (Ra) in Ohms", min_value=0.0)

    
    if st.button("Calculate Efficiency"):
        Eff, CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)
        st.success(f"Efficiency: {Eff:.2f}%")
        st.success(f"Copper Losses (CUL): {CUL:.2f} Watts")

if __name__ == "__main__":
    main()
