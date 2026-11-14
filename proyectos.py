import streamlit as st
import pandas as pd
import numpy as np

def mostrar_proyectos():
    st.markdown("# Proyectos Técnicos y Simulaciones")
    st.write("Muestra interactiva de modelado computacional y análisis de procesos automatizados con Python.")
    st.markdown("---")
    
    # Selector preparado para el futuro: cuando desarrolles más simulaciones, 
    # solo añades el nombre a la lista y creas su respectivo 'elif proyecto_seleccionado == ...'
    proyecto_seleccionado = st.selectbox(
        "Selecciona un proyecto interactivo:",
        [
            "1. Simulación CFD & Reactor CSTR (PHOTORAMA / Criogenia)",
            # "2. Próximo Proyecto (Ej: Optimización Energética)", -> Descomenta y añade aquí en el futuro
        ]
    )
    
    st.markdown("---")
    
    # Lógica para mostrar el proyecto actual seleccionadoimport streamlit as st
import pandas as pd
import numpy as np

def mostrar_proyectos():
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
        temperatura = st.slider("Temperatura de Operación (°C)", min_value=20, max_value=150, value=80, key="slider_temp")
        caudal = st.slider("Caudal de entrada (L/h)", min_value=100, max_value=1000, value=500, step=50, key="slider_caudal")
        concentracion = st.number_input("Concentración inicial (mol/L)", value=2.5, key="num_conc")
        
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
    if proyecto_seleccionado == "1. Simulación CFD & Reactor CSTR (PHOTORAMA / Criogenia)":
        
        # PROYECTO 1: Dinámica de Fluidos (CFD)
        st.markdown("### 🌪️ Simulación CFD: Separación Criogénica de Gases Industriales")
        st.write("Integración de flujos de trabajo utilizando **FreeCAD** para el diseño de la geometría y **OpenFOAM** (automatizado con Python) para analizar la transferencia de calor y masa en un separador de alta pureza.")
        
        col_metric1, col_metric2, col_metric3 = st.columns(3)
        col_metric1.metric("Pureza del Gas Obtenida", "99.98%", "+0.05%")
        col_metric2.metric("Pérdida de Presión (ΔP)", "1.2 bar", "-15%")
        col_metric3.metric("Tiempo de Cómputo", "4.5 hrs", "-30% vs MATLAB")
        
        st.write("**Gráfico de convergencia de residuales (Simulación en tiempo real):**")
        chart_data = pd.DataFrame(
            np.exp(-np.linspace(0, 5, 100)) + np.random.normal(0, 0.05, 100),
            columns=['Residuales de Velocidad (Ux)']
        )
        st.line_chart(chart_data, height=200)
        
        st.markdown("---")
        
        # PROYECTO 2: Calculadora Interactiva de Cinética Química
        st.markdown("### ⚗️ Herramienta de Diseño de Reactores (Interactivo)")
        st.write("Esta herramienta simula el comportamiento de un reactor continuo (CSTR) para optimización de recuperación de solventes. Mueve los controles para ver el impacto en la conversión.")
        
        control_col, graph_col = st.columns([1, 2])
        
        with control_col:
            temperatura = st.slider("Temperatura de Operación (°C)", min_value=20, max_value=150, value=80, key="slider_temp")
            caudal = st.slider("Caudal de entrada (L/h)", min_value=100, max_value=1000, value=500, step=50, key="slider_caudal")
            concentracion = st.number_input("Concentración inicial (mol/L)", value=2.5, key="num_conc")
            
            k_constante = 0.01 * np.exp(-2000 / (temperatura + 273.15))
            conversion_estimada = (k_constante * concentracion) / (caudal/1000)
            conversion_estimada = min(conversion_estimada * 10000, 99.9)
            
            st.info(f"**Conversión del reactor:** {conversion_estimada:.1f}%")
            
        with graph_col:
            longitud = np.linspace(0, 10, 50)
            perfil_temp = temperatura - (longitud * (caudal/500)) + np.random.normal(0, 1, 50)
            df_reactor = pd.DataFrame({'Longitud del Reactor (m)': longitud, 'Temperatura (°C)': perfil_temp})
            st.area_chart(df_reactor.set_index('Longitud del Reactor (m)'), height=250)
            
        st.caption("Nota: Datos generados dinámicamente mediante NumPy y Pandas para efectos de demostración técnica.")

    # Ejemplo de estructura futura:
    # elif proyecto_seleccionado == "2. Próximo Proyecto (Ej: Optimización Energética)":
    #     st.markdown("### ⚡ Próximamente...")
    #     st.write("Aquí irá el contenido del nuevo proyecto.")