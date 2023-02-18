import openai
import streamlit as st
import os

# Accedemos a la clave de API de OpenAI a través de una variable de entorno
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Creación de la interfaz de usuario
st.title("Estudio de factibilidad para el negocio")
descripcion = st.text_area("Ingrese la descripción del negocio")
ubicacion = st.text_input("Ingrese la ubicación")
moneda = st.selectbox("Seleccione la moneda", ["USD", "EUR", "GBP", "JPY"])

# Función para generar el estudio de factibilidad utilizando GPT-3
def generar_estudio_factibilidad(descripcion, ubicacion, moneda):
    prompt = f"Realizar un estudio de factibilidad para un negocio {descripcion} ubicado en {ubicacion} durante los próximos cinco años en {moneda}."
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    estudio_factibilidad = response.choices[0].text
    return estudio_factibilidad

# Agregar un botón para generar el estudio de factibilidad
if st.button("Generar estudio de factibilidad"):
    estudio_factibilidad = generar_estudio_factibilidad(descripcion, ubicacion, moneda)
    st.header("Estudio de factibilidad")
    st.write(estudio_factibilidad)
