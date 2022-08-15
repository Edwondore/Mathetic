import streamlit as st
import pandas as pd
import numpy as np
import math
from sympy import simplify, symbols, solve, Eq

option = st.selectbox(
     'Chon phuong phap tinh',
     ('Don gian', 'Phuong trinh 1 an', 'Phuong trinh 2 an'))

st.write('You selected:', option)

if option == "Don gian":
    eq = st.text_input('nhap phep tinh: ')
    if eq:
        func = simplify(eq)
        st.write("ket qua:",func)
    
elif option == "Phuong trinh 1 an":

    eq = st.text_input('phuong trinh: ')
    if eq:
        func = simplify(eq)
        st.latex(func)

        x = symbols('x')
        sol = solve(func)

        st.write("ket qua:", sol)
elif option == "Phuong trinh 2 an":
    eq1 = st.text_input('phuong trinh thu 1 : ')
    eq2 = st.text_input('phuong trinh thu 2 : ')

    if eq1 and eq2:

        func1 = simplify(eq1)
        func2 = simplify(eq2)
        st.latex(func1)
        st.latex(func2)

        x, y = symbols('x y')
        sol = solve((eq1,eq2), (x, y))
        
        st.write("ket qua x :", {sol[x]})
        st.write("ket qua y :", {sol[y]})
    
