import streamlit as st

def mostrar_cv():
    st.markdown("# Sergio Gonzalez Rodriguez")
    
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
- **Process Simulation & Modeling:** Python, MATLAB, Aspen Plus.
- **Chemical Engineering Expertise:** Unit operations simulation, kinetics, control, energy and mass balances.
- **Project Leadership:** EU R&D proposals, consortium management (€2M–€8M).
- **Industrial Operations:** International experience in industrial plant operations (NZ & AUS)
- **Interest in keep learning** .
            """)
        
        st.markdown('### Education')
        st.markdown(
            """
            🎓 **Bachelor’s Degree in Chemical Engineering**  
            *Universidad de Granada | Granada, Spain (2023)*
            """)

    with col2:
        st.markdown('### Key Achievements')
        st.success("🏆 Coordinated and authored EU proposals, including one ranked 3rd with maximum score (14/14).")
        st.success("🏆 Delivered process simulations across six international projects, optimizing water reuse and bioproducts.")
        st.success("🏆 Achieved 30% reduction in drying time for algae-based food processes and 40% solvent optimization.")
        st.success("🏆 Bridged research and industry by integrating CAPEX/OPEX analysis into scalable bio-based production.")

    st.markdown('### Selected Projects where I contributed')

    with st.container(border=True):
        st.markdown("### 🔬 BIOMAC")
        st.write("Conducted unit operation simulations; integrated CAPEX/OPEX into scalable nanomaterial production.")
    with st.container(border=True):
        st.markdown("### 🌿 NOVAFOODIES")
        st.write("Modeled algae drying/milling; achieved 30% faster processing with zero variability.")
    with st.container(border=True):
        st.markdown("### ☀️ PHOTORAMA")
        st.write("Designed silver recovery via DES solvents; reduced solvent use by 40%.")
    with st.container(border=True):
        st.markdown("### 💧 R3VOLUTION")
        st.write("Simulated advanced water reuse technologies; coordinated communication/dissemination.")