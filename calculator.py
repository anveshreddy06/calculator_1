import streamlit as st

st.title("my calculator")

if 'num1' not in st.session_state:
    st.session_state.num1 = ""
if 'operation' not in st.session_state:
    st.session_state.operation = ""
if 'n' not in st.session_state:
    st.session_state.n = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

rows = 3
cols = 3
counter = 1
for r in range(rows):
    # Create a new row of columns
    columns = st.columns(cols)
    for c in range(cols):
        if columns[c].button(str(counter)):
            st.session_state.num1 += str(counter)
        counter += 1
if st.button('0'):
    st.session_state.num1 += '0'

add, sub, mul, div = st.columns(4)
with add:
    if st.button('+'):
        st.session_state.n = st.session_state.num1
        st.session_state.operation = '+'
        st.session_state.num1 = ''
with sub:
    if st.button('-'):
        st.session_state.n = st.session_state.num1
        st.session_state.operation = '-'
        st.session_state.num1 = ''
with mul:
    if st.button('*'):
        st.session_state.n = st.session_state.num1
        st.session_state.operation = '*'
        st.session_state.num1 = ''
with div:
    if st.button('/'):
        st.session_state.n = st.session_state.num1
        st.session_state.operation = '/'
        st.session_state.num1 = ''
#n2 = st.session_state.num1

clear, cal = st.columns(2)
with clear:
    if st.button('clear'):
        st.session_state.num1 = ""
        st.session_state.operation = ""
        st.session_state.n = ""
        st.session_state.result = ""


with cal:
    if st.button('calculate'):
        if st.session_state.operation == "":
            st.write("Error: No operation selected.")
        elif st.session_state.num1 == "":
            st.write("Error: No second number entered.")
        else:
            try:
                n1 = int(st.session_state.n)
                n2 = int(st.session_state.num1)
            except ValueError:
                st.write("Error: Invalid number input.")
            else:
                if st.session_state.operation == '+':
                    #st.write(st.session_state.n,st.session_state.operation,st.session_state.num1)
                    st.session_state.result = n1 + n2
                elif st.session_state.operation == '-':
                    st.session_state.result = n1 - n2
                elif st.session_state.operation == '*':
                    st.session_state.result = n1 * n2
                elif st.session_state.operation == '/':
                    if n2 == 0:
                        st.write("Error: Division by zero.")
                    else:
                        st.session_state.result = n1 / n2
                        

st.write( st.session_state.n,st.session_state.operation,st.session_state.num1,'=', st.session_state.result)
