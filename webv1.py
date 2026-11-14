import streamlit as st
import pandas as pd
import numpy as np

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
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135692.png", width=120) # Avatar genérico temporal
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
    st.markdown('<p class="main-header">Proyectos Técnicos y Simulaciones</p>', unsafe_allow_html=True)
    st.write("Muestra interactiva de modelado computacional y análisis de procesos automatizados con Python.")
    
    st.markdown("---")
    
    # PROYECTO 1: Dinámica de Fluidos (CFD)
    st.markdown("### 🌪️ Simulación CFD: Separación Criogénica de Gases Industriales")
    st.write("Integración de flujos de trabajo utilizando **FreeCAD** para el diseño de la geometría y **OpenFOAM** (automatizado con Python) para analizar la transferencia de calor y masa en un separador de alta pureza.")
    
    col_metric1, col_metric2, col_metric3 = st.columns(3)
    col_metric1.metric("Pureza del Gas Obtenida", "99.98%", "+0.05%")
    col_metric2.metric("Pérdida de Presión (ΔP)", "1.2 bar", "-15%")
    col_metric3.metric("Tiempo de Computo", "4.5 hrs", "-30% vs MATLAB")
    
    # Gráfico simulado de convergencia
    st.write("**Gráfico de convergencia de residuales (Simulación en tiempo real):**")
    chart_data = pd.DataFrame(
        np.exp(-np.linspace(0, 5, 100)) + np.random.normal(0, 0.05, 100),
        columns=['Residuales de Velocidad (Ux)']
    )
    st.line_chart(chart_data, height=200)
    
    st.markdown("---")
    
    # PROYECTO 2: Calculadora Interactiva de Cinética Química
    st.markdown("### ⚗️ Herramienta de Diseño de Reactores (Interactivo)")
    st.write("Esta herramienta simula el comportamiento de un reactor continuo (CSTR) para optimización de recuperación de solventes (basado en proyectos como PHOTORAMA). Mueve los controles para ver el impacto en la conversión.")
    
    control_col, graph_col = st.columns([1, 2])
    
    with control_col:
        temperatura = st.slider("Temperatura de Operación (°C)", min_value=20, max_value=150, value=80)
        caudal = st.slider("Caudal de entrada (L/h)", min_value=100, max_value=1000, value=500, step=50)
        concentracion = st.number_input("Concentración inicial (mol/L)", value=2.5)
        
        # Simulación matemática simple
        k_constante = 0.01 * np.exp(-2000 / (temperatura + 273.15))
        conversion_estimada = (k_constante * concentracion) / (caudal/1000)
        conversion_estimada = min(conversion_estimada * 10000, 99.9) # Normalización para demo
        
        st.info(f"**Conversión del reactor:** {conversion_estimada:.1f}%")
        
    with graph_col:
        # Generar perfil térmico a lo largo del reactor
        longitud = np.linspace(0, 10, 50)
        perfil_temp = temperatura - (longitud * (caudal/500)) + np.random.normal(0, 1, 50)
        df_reactor = pd.DataFrame({'Longitud del Reactor (m)': longitud, 'Temperatura (°C)': perfil_temp})
        st.area_chart(df_reactor.set_index('Longitud del Reactor (m)'), height=250)
        
    st.caption("Nota: Los datos visualizados en esta sección son representaciones generadas dinámicamente mediante NumPy y Pandas para efectos de demostración técnica del portafolio.")