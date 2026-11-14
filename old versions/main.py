import streamlit as st
import pandas as pd
import numpy as np

from proyectos import mostrar_proyectos  # Importa la función mostrar_proyectos del módulo proyectos.py

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
# BARRA LATERAL (MENÚ DE NAVEGACIÓN)
# ==========================================
with st.sidebar:
    st.image("images/CV2.jpg")  # O simplemente "mi_foto.jpg" si está en la misma carpeta
    st.title("Menú")
    
    # Navegación entre páginas
    page = st.radio(
        "Secciones:",
        ["📄 CV / Portafolio", "⚙️ Proyectos y Simulaciones"]
    )

    st.markdown("---")
    st.markdown("### Contacto")
    st.markdown("📍 **Ubicación:** Findon, Adelaide SA")
    st.markdown("📧 **Email:** sergio.personal.iq@gmail.com")
    st.markdown("📱 **Teléfono:** 0456577688")
    st.markdown("🌐 **Visa:** Working Holiday")

    st.markdown("---")
    st.markdown("**Idiomas:**")
    st.write("🇪🇸 Español (Nativo)")
    st.write("🇬🇧 Inglés (Proficient)")
    st.write("🇹🇼 Chino Tradicional (Beginner)")

# ==========================================
# PÁGINA 1: PORTAFOLIO Y CV
# ==========================================
st.markdown("# Sergio Gonzalez Rodriguez")

if page == "📄 CV / Portafolio":
    
    st.markdown('## Professional Summary')
    st.markdown(
        """
        **Chemical Engineer with 2 years** of experience in R&D projects (Horizon 2020), 
        **specializing in process simulation** with proven ability to design and coordinate international proposals, 
        **achieving top-tier evaluations (14/14)**. 
        Combines computational expertise **(Python, MATLAB and Aspen Plus)** with hands-on plant operations in heavy industry. 
        Brings a unique mix of innovation, technical rigor, and practical execution 
        to industrial engineering roles.
        """)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('### Core Skills')
        st.markdown(
            """
            * **Process Simulation & Modeling:** Python, MATLAB, Aspen Plus.
            * **Chemical Engineering Expertise:** Unit operations simulation (estationary and non estationary state),kinetics, control, energy and mass balances.
            * **Project Leadership:** EU R&D proposals, consortium management (€2M–€8M).
            * **Industrial Operations:** International experience in industrial plant operations (NZ & AUS)
            * **Interest in keep learning** .
            """)
        
        st.markdown('### Education')
        st.markdown(
            """
            🎓 **Bachelor’s Degree in Chemical Engineering**  
            *Universidad de Granada | Granada, Spain (2023)*
            """)

    with col2:
        st.markdown('### Key Achievements')
        st.success(
            """
            🏆 Coordinated and authored EU proposals, 
            including one ranked 3rd with maximum score (14/14).
            """)
        st.success(
            """
            🏆 Delivered process simulations across six international projects, 
            optimizing water reuse, bioproducts, and material recovery.
            """)
        st.success(
            """
            🏆 Achieved 30% reduction in drying time for algae-based food processes and 40% solvent optimization in photovoltaic recycling.
            """)
        st.success(
            """
            🏆 Bridged research and industry by integrating CAPEX/OPEX analysis into scalable bio-based nanomaterial production.
            """)

    st.markdown('### Selected Projects were I contributed')

    # Tarjetas expandibles para los proyectos
    with st.container(border=True):
        st.markdown("### 🔬 BIOMAC")
        st.write("Conducted unit operation simulations; integrated CAPEX/OPEX into scalable nanomaterial production.")
    with st.container(border=True):
        st.markdown("### 🌿 NOVAFOODIES")
        st.write("Modeled algae drying/milling; achieved 30% faster processing with zero variability.")
    with st.container(border=True):
        st.markdown("### ☀️ PHOTORAMA")
        st.write("Designed silver recovery via DES solvents; reduced solvent use by 40%, enabling compact reactor design.")
    with st.container(border=True):
        st.markdown("### 💧 R3VOLUTION")
        st.write("Simulated advanced water reuse technologies; coordinated communication/dissemination.")



# ==========================================
# PÁGINA 2: PROYECTOS Y SIMULACIONES
# ==========================================
elif page == "⚙️ Proyectos y Simulaciones":
    mostrar_proyectos()# ==========================================
# PÁGINA 2: PROYECTOS Y SIMULACIONES
# ==========================================
elif page == "⚙️ Proyectos y Simulaciones":
    mostrar_proyectos()