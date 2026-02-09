import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Orientación Médica Dr. Quiroz", page_icon="👨‍⚕️", layout="centered")

# --- ESTILOS VISUALES (CSS) ---
st.markdown("""
    <style>
    .reportview-container { background: #ffffff; }
    h1 { color: #0f3460; text-align: center; }
    h2 { color: #e94560; border-bottom: 2px solid #e94560; padding-bottom: 10px; }
    .stButton>button { 
        width: 100%; 
        background-color: #25D366; 
        color: white; 
        font-weight: bold; 
        border-radius: 10px; 
        height: 50px;
        border: none;
    }
    .stButton>button:hover { background-color: #128C7E; }
    .diag-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #f1f6f9;
        border-left: 5px solid #0f3460;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("👨‍⚕️ Tu Pre-Diagnóstico Confidencial")
st.markdown("""
    **Dr. Héctor Quiroz Hernández | Medicina Familiar y Urgencias**
    
    Esta herramienta analiza tus síntomas para darte una **orientación médica rápida**.
    Selecciona lo que sientes para recibir una recomendación y, si lo deseas, solicitar tu tratamiento.
""")
st.warning("⚠️ **Aviso:** Esto es una orientación, no sustituye la consulta presencial ante emergencias graves.")

st.markdown("---")

# --- VARIABLES DE SÍNTOMAS ---
# Dermatología
sintoma_uñas_color = False
sintoma_uñas_grosor = False
sintoma_pie_picor = False
sintoma_pie_olor = False

# Proctología
sintoma_hemo_sangrado = False
sintoma_hemo_bolita = False
sintoma_hemo_dolor = False

# Urología / Sexual
sintoma_incont_esfuerzo = False
sintoma_incont_urgencia = False
sintoma_disf_firmeza = False
sintoma_disf_deseo = False

# --- MÓDULO 1: PIEL Y UÑAS (HONGOS) ---
with st.expander("🦶 1. Pies y Uñas (Clic aquí)", expanded=False):
    st.write("Selecciona lo que ves en tus pies o manos:")
    col1, col2 = st.columns(2)
    with col1:
        sintoma_uñas_color = st.checkbox("Uñas amarillas / oscuras")
        sintoma_uñas_grosor = st.checkbox("Uñas gruesas o se deshacen")
    with col2:
        sintoma_pie_picor = st.checkbox("Comezón entre dedos / descamación")
        sintoma_pie_olor = st.checkbox("Mal olor persistente")

# --- MÓDULO 2: ZONA RECTAL (HEMORROIDES) ---
with st.expander("🍑 2. Molestias al ir al baño (Clic aquí)", expanded=False):
    st.write("Síntomas rectales comunes:")
    sintoma_hemo_sangrado = st.checkbox("Sangrado rojo brillante al limpiar o en el inodoro")
    sintoma_hemo_bolita = st.checkbox("Siento una 'bolita' o protuberancia que sale")
    sintoma_hemo_dolor = st.checkbox("Dolor o ardor intenso al evacuar o estar sentado")

# --- MÓDULO 3: SALUD SEXUAL Y URINARIA ---
with st.expander("🍆 3. Salud Sexual y Urinaria (Clic aquí)", expanded=False):
    st.write("Control y función sexual:")
    st.caption("**Incontinencia:**")
    sintoma_incont_esfuerzo = st.checkbox("Se me sale la orina al toser, reír o cargar peso")
    sintoma_incont_urgencia = st.checkbox("Me ganan las ganas y no llego al baño")
    st.caption("**Sexualidad (Hombres):**")
    sintoma_disf_firmeza = st.checkbox("Dificultad para lograr o mantener firmeza")
    sintoma_disf_deseo = st.checkbox("Pérdida total del deseo sexual")

st.markdown("---")

# --- BOTÓN DE ANÁLISIS ---
if st.button("🔍 ANALIZAR MIS SÍNTOMAS Y VER SOLUCIÓN"):
    
    hay_diagnostico = False
    
    # === LÓGICA DE DIAGNÓSTICO DERMATOLÓGICO ===
    if sintoma_uñas_color or sintoma_uñas_grosor or sintoma_pie_picor:
        hay_diagnostico = True
        st.markdown("## 🍄 Resultado: Probable Infección Fúngica")
        
        if sintoma_uñas_color or sintoma_uñas_grosor:
            st.error("🔹 **Posible ONICOMICOSIS (Hongos en uñas)**")
            st.write("Es una infección profunda de la uña. **Las cremas superficiales NO suelen funcionar** porque no penetran la queratina.")
        
        if sintoma_pie_picor or sintoma_pie_olor:
            st.warning("🔹 **Posible TIÑA PEDIS (Pie de Atleta)**")
            st.write("Muy contagioso. Si no se trata, puede pasarse a las ingles o a las uñas.")

        st.info("""
        **¿Qué puedes hacer YA?**
        1. Mantén la zona seca (usa secadora de pelo con aire frío tras el baño).
        2. No compartas toallas ni cortauñas.
        3. Lava calcetines con agua caliente.
        """)
    
    # === LÓGICA DE DIAGNÓSTICO PROCTOLÓGICO ===
    if sintoma_hemo_sangrado or sintoma_hemo_bolita or sintoma_hemo_dolor:
        hay_diagnostico = True
        st.markdown("## 🍑 Resultado: Probable Enfermedad Hemorroidal")
        
        grado = "Grado I (Leve)"
        if sintoma_hemo_bolita: grado = "Grado II o III (Requiere valoración)"
        if sintoma_hemo_dolor: grado = "Posible Trombosis Hemorroidal (Doloroso)"
        
        st.error(f"🔹 **Clasificación probable: {grado}**")
        st.write("El sangrado y la inflamación indican que las venas del recto están bajo presión.")
        
        st.info("""
        **Medidas Inmediatas:**
        1. **Baños de asiento:** Agua tibia (no hirviendo) por 10 min, 3 veces al día.
        2. No uses papel higiénico seco (usa toallitas húmedas o agua).
        3. Evita picantes, café y alcohol por 3 días.
        """)

    # === LÓGICA DE DIAGNÓSTICO UROLOGÍA ===
    if sintoma_incont_esfuerzo or sintoma_incont_urgencia:
        hay_diagnostico = True
        st.markdown("## 💧 Resultado: Incontinencia Urinaria")
        tipo = "de Esfuerzo" if sintoma_incont_esfuerzo else "de Urgencia (Vejiga Hiperactiva)"
        
        st.warning(f"🔹 **Tipo probable: Incontinencia {tipo}**")
        st.write("Esto sucede por debilidad del piso pélvico o irritación nerviosa de la vejiga. **No es algo 'normal' de la edad**, es tratable.")
        st.write("⚠️ Evita café y cítricos, ya que irritan más la vejiga.")

    if sintoma_disf_firmeza or sintoma_disf_deseo:
        hay_diagnostico = True
        st.markdown("## 🍆 Resultado: Disfunción Eréctil")
        st.error("🔹 **Probable Disfunción Eréctil / Hipogonadismo**")
        st.write("Puede ser un problema de circulación (vascular) o falta de Testosterona. No te automediques con pastillas azules sin saber la causa (es peligroso para el corazón).")

    # === CIERRE Y LLAMADO A LA ACCIÓN (Venta) ===
    if hay_diagnostico:
        st.markdown("---")
        st.success("✅ **HAY SOLUCIÓN PARA ESTO**")
        st.write("""
        Ya tienes una idea de qué te pasa. Ahora necesitas el **tratamiento médico exacto** (dosis y medicamento) para curarlo rápido y no contagiar a nadie.
        
        **No adivines en la farmacia.** Yo puedo recetarte lo que realmente funciona.
        """)
        
        # Link a WhatsApp con mensaje pre-llenado
        mensaje_wa = "Hola Dr. Quiroz, hice su pre-diagnóstico digital y me salieron alertas. Quiero una solución médica."
        link_wa = f"https://wa.me/522462102267?text={mensaje_wa.replace(' ', '%20')}"
        
        st.markdown(f"""
        <a href="{link_wa}" target="_blank">
            <button style="
                background-color:#25D366; 
                color:white; 
                padding:15px 32px; 
                text-align:center; 
                text-decoration:none; 
                display:inline-block; 
                font-size:16px; 
                margin:4px 2px; 
                cursor:pointer; 
                border-radius:12px; 
                border:none; 
                width:100%;">
                📱 SOLICITAR TRATAMIENTO POR WHATSAPP
            </button>
        </a>
        """, unsafe_allow_html=True)
        
    else:
        st.info("✅ **No detectamos síntomas de alarma en estas categorías.** ¡Sigue cuidándote!")