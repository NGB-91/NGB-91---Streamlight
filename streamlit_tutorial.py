import streamlit as st
import joblib
model_path = 'models/lasso_model.sav'
from streamlit_extras.switch_page_button import switch_page
import random

def main():
    st.title('Bienvenido al portal de Seguros "Securitas"')
    st.write('**Aquí se puede calcular el precio anual de prima que se pagará**')
    
    # Añadir un selector de fecha
    publish_date = st.date_input("Quotation Date")
    # Diccionario para almacenar los datos de entrada
    input_data = {}
    # Widget de entrada numérica para cada característica
    edad = st.number_input('Type your Age: ', min_value=0, max_value=99)
    # Sexo
    sexo = st.selectbox('Select your Gender: ',('Male','Female'))
    # BMI
    bmi = st.number_input('Insert you BMI:', format="%0.2f", value="min", min_value=15.0, max_value=50.00)
    # Fumador
    fumador = st.selectbox('Do you smoke?: ',('Yes','No'))
    # Hijos
    hijos = st.slider('Choose your number of children: ', min_value=0, max_value=9)
    # Calcular precio cuando se pulsa el botón
    if st.button("Calculate Price"):
        precio = random.randint(1000, 1500)
        st.write(f"el precio de tu seguro es: {precio} Euros")


    
def load_model(model_path):
    try:
        model = joblib.load(model_path)  # cargar el modelo .sav 
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

#        with open(model_path, 'rb') as file:
#          model = pickle.load(file)
#        with st.spinner("Generando historia..."):
#            response = get_text_response(text_model_pro, prompt, config)
#            st.write(response)

if __name__ == "__main__":
    main()

# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2