import streamlit as st
def calculate_future_value(principal, annual_rate, years, times_compounded):
    rate_decimal = annual_rate / 100.0
    compound_factor = 1 + rate_decimal / times_compounded
    total_periods = years * times_compounded
    future_value = principal * ((compound_factor ** total_periods - 1) / (rate_decimal / times_compounded))
    return future_value 
st.title("Investment Calculator")
Name = st.text_input("Enter your Name")
DOB = st.text_input("Enter your Date of Birth")
Mobile_Number = st.text_input("Enter your Mobile Number")
NRI = st.selectbox("Are you an NRI?*", ["Yes", "No"])
if NRI == "No":
    st.write("You are not eligible for investment")
else:
    st.write("Continue with your investment")

    SIP_Month = st.slider("SIP Amount (Monthly in INR)", 100, 100000)
    Time = st.slider("Time in Years", 1, 50)
    Rate = st.slider("Approx Interest Rate (%)", 1, 95)
    
    if st.button("Predicted Value"):
        # Monthly compounding
        times_compounded = 12
        # Calculate future value of SIP
        future_value = calculate_future_value(SIP_Month, Rate, Time, times_compounded)        
        st.write(f"The approximate value is ₹{future_value:.2f}")




