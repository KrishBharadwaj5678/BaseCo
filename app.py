import streamlit as st

st.set_page_config(
    page_title="Online Base Convertor",
    page_icon="icon.png",
    menu_items={
        "About":"BaseCo provides a simple yet powerful interface for converting numbers between binary, decimal, hexadecimal, and octal formats. Whether you're a student, programmer, or anyone who needs quick base conversions, we've got you covered!"
    }
)

st.write("<h2 style='color:#21CFFF;'>All in One Number Base Convertor</h2>",unsafe_allow_html=True)

conv=["Binary","Decimal","Octal","Hexa Decimal"]

froms=st.selectbox("From",conv,index=1)
to=st.selectbox("To",conv,index=0)
num=st.text_input(f"{froms} Number",placeholder=f"Enter {froms.lower()} number")
btn=st.button("Convert")

def show(data,to):
    st.write(f"<h2 style='color:orange;';>{to} Number: {data}</h2>",unsafe_allow_html=True)

if btn:
    if len(num)>=1:
        # Decimal
        if(froms==conv[1] and to==conv[0]):
            try:show(bin(int(num))[2:],to)
            except:st.error("Provide Decimal Number!")

        elif(froms==conv[1] and to==conv[2]):
            try:show(oct(int(num))[2:],to)
            except:st.error("Provide Decimal Number!")

        elif(froms==conv[1] and to==conv[3]):
            try:show(hex(int(num))[2:].upper(),to)
            except:st.error("Provide Decimal Number!")

        # Binary
        elif(froms==conv[0] and to==conv[1]):
            try:show(int(str(num),2),to)
            except:st.error("Provide Binary Number!")

        elif(froms==conv[0] and to==conv[2]):
            try:show(oct(int(str(num),2))[2:],to)
            except:st.error("Provide Binary Number!")

        elif(froms==conv[0] and to==conv[3]):
            try:show(hex(int(str(num),2))[2:].upper(),to)
            except:st.error("Provide Binary Number!")

        # Octal
        elif(froms==conv[2] and to==conv[0]):
            try:show(bin(int(str(num),8))[2:],to)
            except:st.error("Provide Octal Number!")

        elif(froms==conv[2] and to==conv[1]):
            try:show(int(str(num),8),to)
            except:st.error("Provide Octal Number!")
            
        elif(froms==conv[2] and to==conv[3]):
            try:show(hex(int(str(num),8))[2:].upper(),to)
            except:st.error("Provide Octal Number!")

        # Hexadecimal
        elif(froms==conv[3] and to==conv[0]):
            try:show(bin(int(num,16))[2:],to)
            except:st.error("Provide Hexadecimal Number!")

        elif(froms==conv[3] and to==conv[1]):
            try:show(int(num,16),to)
            except:st.error("Provide Hexadecimal Number!")

        elif(froms==conv[3] and to==conv[2]):
            try:show(oct(int(num,16))[2:],to)
            except:st.error("Provide Hexadecimal Number!")
    else:
        st.error("Invalid Input Fields!")
