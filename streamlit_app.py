import openai
import streamlit as st

# Inicialización de la API de OpenAI
openai.api_key = "su_clave_API_de_OpenAI"

# Creación de la interfaz de usuario
st.title("Proyección financiera para el negocio")
descripcion = st.text_area("Ingrese la descripción del negocio")
ubicacion = st.text_input("Ingrese la ubicación")

# Generación de la proyección financiera utilizando GPT-3
prompt = f"Proyectar las ganancias para un negocio {descripcion} ubicado en {ubicacion} durante los próximos cinco años."
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.5,
)
proyeccion_financiera = response.choices[0].text

# Presentación de los resultados al usuario
st.header("Proyección financiera")
st.write(proyeccion_financiera)
