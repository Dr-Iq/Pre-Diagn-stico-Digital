import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Evaluación de Salud Confidencial", page_icon="🛡️", layout="centered")

# --- ESTILOS VISUALES ---
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; 
        background-color: #007bff; 
        color: white; 
        font-weight: bold; 
        border-radius: 8px; 
        height: 60px;
        font-size: 20px; 
    }
    .stButton>button:hover { background-color: #0056b3; }
    h1 { color: #2c3e50; text-align: center; }
    
    /* CORRECCIÓN AQUÍ: Forzamos el color del texto a NEGRO (#000000) */
    .info-box { 
        background-color: #e8f4f8; 
        color: #000000; 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 5px solid #00a8cc; 
        margin-bottom: 20px; 
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO NEUTRO ---
st.title("🛡️ Sistema de Evaluación Médica")
st.markdown("""
    <div class="info-box">
        <strong>Bienvenido/a.</strong><br>
        Esta herramienta digital analiza tus síntomas de forma <strong>100% confidencial y anónima</strong>.
        <br><br>
        Detectamos riesgos en salud íntima, dermatológica y general para orientarte hacia el tratamiento correcto sin que tengas que exponerte innecesariamente.
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 1. PERFIL CLÍNICO (Anónimo)
# ==========================================
st.markdown("### 👤 Paso 1: Ficha Técnica")
c1, c2 = st.columns(2)
with c1:
    edad = st.number_input("Edad:", 15, 99, 30)
    genero = st.selectbox("Género:", ["Hombre", "Mujer"])
with c2:
    enfermedades = st.multiselect("Preexistentes:", ["Diabetes", "Hipertensión", "Obesidad", "Ninguna"])
    alergias = st.text_input("⚠️ ¿Alergias a medicamentos?", placeholder="Ej: Penicilina...")

es_diabetico = "Diabetes" in enfermedades

# ==========================================
# 2. SELECCIÓN DE SÍNTOMAS
# ==========================================
st.markdown("---")
st.markdown("### 🩺 Paso 2: Marque lo que siente actualmente")

# --- A. INFECCIONES Y RIESGOS ---
with st.expander("🔥 A. Zona Íntima (Riesgos)", expanded=True):
    col_ets1, col_ets2 = st.columns(2)
    sintoma_ets_lesion = col_ets1.checkbox("Llagas, úlceras o heridas")
    sintoma_ets_verruga = col_ets2.checkbox("Verrugas (tipo coliflor) o granitos")
    
    if genero == "Hombre":
        sintoma_secrecion = col_ets1.checkbox("Salida de pus/líquido por el pene")
        sintoma_ardor = col_ets2.checkbox("Ardor intenso al orinar")
        sintoma_ets_esp = sintoma_secrecion or sintoma_ardor
    else:
        sintoma_flujo = col_ets1.checkbox("Flujo con mal olor o color extraño")
        sintoma_sangrado = col_ets2.checkbox("Sangrado fuera del periodo / Dolor pélvico")
        sintoma_ets_esp = sintoma_flujo or sintoma_sangrado
        
    sintoma_riesgo = st.checkbox("Relaciones sexuales sin protección reciente")

# --- B. FUNCIONALIDAD SEXUAL ---
with st.expander(f"🍆 B. Funcionalidad Sexual ({genero})", expanded=False):
    sintoma_libido = st.checkbox("Pérdida del deseo sexual (Libido baja)")
    
    if genero == "Hombre":
        sintoma_ereccion = st.checkbox("Dificultad de erección (Firmeza)")
        sintoma_eyaculacion = st.checkbox("Terminar antes de lo deseado (Precoz)")
        sintoma_sexual = sintoma_ereccion or sintoma_eyaculacion
    else:
        sintoma_sequedad = st.checkbox("Sequedad vaginal / Dolor al tener sexo")
        sintoma_sexual = sintoma_sequedad

# --- C. PROCTOLOGÍA ---
with st.expander("🍑 C. Zona Rectal", expanded=False):
    c_hemo1, c_hemo2 = st.columns(2)
    sintoma_hemo_sangrado = c_hemo1.checkbox("Sangrado al limpiar/evacuar")
    sintoma_hemo_bolita = c_hemo2.checkbox("Siento una protuberancia ('bolita') anal")
    sintoma_hemo_dolor = st.checkbox("Dolor o ardor al estar sentado")
    sintoma_hemo = sintoma_hemo_sangrado or sintoma_hemo_bolita or sintoma_hemo_dolor

# --- D. DERMATOLOGÍA ---
with st.expander("🦶 D. Piel y Uñas", expanded=False):
    sintoma_uñas = st.checkbox("Uñas amarillas, negras o que se deshacen")
    sintoma_pie = st.checkbox("Comezón en pies o ingles")

# --- E. OTROS ---
with st.expander("🧠 E. General (Orina y Mente)", expanded=False):
    sintoma_incont = st.checkbox("Incontinencia (Pérdida involuntaria de orina)")
    sintoma_mental = st.checkbox("Tristeza profunda, Ansiedad o Insomnio")

st.markdown("---")

# --- OPCIONES DE ENVÍO ---
envio = st.checkbox("📦 **SOLICITO ENVÍO A DOMICILIO (Paquete Discreto)**")

# ==========================================
# 3. DIAGNÓSTICO Y ACCIÓN
# ==========================================
if st.button("✅ VER RESULTADOS Y OPCIONES"):
    
    hallazgos = []
    st.markdown("---")
    
    # Lógica de Diagnóstico (Sin nombres médicos complejos, directo al punto)
    if sintoma_ets_lesion or sintoma_ets_verruga or sintoma_ets_esp or sintoma_riesgo:
        st.error("🚨 **ALERTA CLÍNICA:** Posible infección activa detectada. Se recomienda tratamiento farmacológico inmediato.")
        hallazgos.append("Posible Infección/ETS")
        
    if sintoma_sexual or sintoma_libido:
        st.warning(f"⚠️ **Salud Sexual:** Disfunción funcional detectada.")
        if genero == "Hombre" and sintoma_ereccion: hallazgos.append("Disfunción Eréctil")
        else: hallazgos.append("Disfunción Sexual")
            
    if sintoma_hemo:
        st.info("🍑 **Proctología:** Signos de enfermedad hemorroidal.")
        hallazgos.append("Hemorroides")
        
    if sintoma_uñas or sintoma_pie:
        st.info("🍄 **Dermatología:** Signos de infección por hongos.")
        hallazgos.append("Hongos")
        if es_diabetico: st.error("⚠️ **NOTA:** Por su condición de Diabetes, esto requiere atención prioritaria.")

    if sintoma_incont: hallazgos.append("Incontinencia")
    if sintoma_mental: hallazgos.append("Salud Mental")

    # GENERAR MENSAJE WHATSAPP (A TU NÚMERO)
    if hallazgos:
        st.success("✅ **DIAGNÓSTICO PRELIMINAR LISTO**")
        st.write("El sistema ha generado un reporte clínico. Envíalo a nuestro especialista para validar tu tratamiento.")
        
        # Mensaje anónimo "Hola, realicé el test..."
        msg = f"Hola, realicé la Evaluación Digital. Soy {genero}, {edad} años."
        if enfermedades: msg += f" (Antecedentes: {', '.join(enfermedades)})."
        if alergias: msg += f" ⚠️ ALERGIA: {alergias}."
        
        msg += f" El sistema detectó: {', '.join(hallazgos)}."
        
        if envio: msg += " 📦 ME INTERESA EL ENVÍO A DOMICILIO."
        else: msg += " Solicito información de tratamiento."
        
        # TU NÚMERO SIGUE AQUÍ
        link = f"https://wa.me/522462102267?text={msg.replace(' ', '%20')}"
        
        st.markdown(f"""
        <a href="{link}" target="_blank">
            <button>📱 CONTACTAR AL ESPECIALISTA (WhatsApp)</button>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.balloons()
        st.success("🎉 **Sin hallazgos de alarma.**")
        st.write("Su salud parece estable. Recuerde realizar chequeos anuales.")
