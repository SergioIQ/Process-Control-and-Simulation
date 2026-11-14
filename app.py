import streamlit as st

# ==========================================
# Pestaña del navegador
# ==========================================
st.set_page_config(
    page_title="Portfolio | Sergio Gonzalez Rodriguez",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILOS CSS PERSONALIZADOS (Botones a la izquierda)
# ==========================================
st.markdown("""
    <style>
    [data-testid="stSidebar"] button {
        justify-content: flex-start !important;
        text-align: left !important;
    }
    </style>
""", unsafe_allow_html=True)

# Importamos los módulos externos (asegúrate de tener cv.py y proyectos.py en la misma carpeta)
from cv import mostrar_cv
from proyectos import mostrar_proyectos

# variables shortcuts
cv_page = "Portafolio"
simulaciones = "Simulaciones"

# ==========================================
# BARRA LATERAL (MENÚ DE NAVEGACIÓN)
# ==========================================
with st.sidebar:
    st.image("images/CV2.jpg")
    st.title("Sergio González")
    
    # Inicializamos la página por defecto en el estado
    if "page" not in st.session_state:
        st.session_state.page = cv_page 
        
    st.markdown("### Navegación")
    
    # Botones de navegación principal
    if st.button(cv_page , use_container_width=True):
        st.session_state.page = cv_page
        
    if st.button(simulaciones, use_container_width=True):
        st.session_state.page = simulaciones
        
    page = st.session_state.page  # Guardamos la selección actual
    
    st.markdown("---")
    st.markdown("### Contacto")
    st.markdown("📍 **Ubicación:** Findon, Adelaide SA")
    st.markdown("📧 **Email:** sergio.personal.iq@gmail.com")
    st.markdown("📱 **Teléfono: ** 0456577688")
    st.markdown("🌐 **Visa:** Working Holiday")
    
    st.markdown("---")
    st.markdown("**Idiomas:**")
    st.write("Español (Nativo)")
    st.write("Inglés (Proficient)")
    st.write("Chino Tradicional (Beginner)")

# ==========================================
# RENDERIZADO DE PÁGINAS PRINCIPALES
# ==========================================
if page == cv_page:
    mostrar_cv()

elif page == simulaciones:
    mostrar_proyectos()