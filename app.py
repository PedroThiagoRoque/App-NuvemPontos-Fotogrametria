import os
import cv2
import streamlit as st

# Título do aplicativo
st.set_page_config(page_title="App de Nuvem de Pontos", layout="wide")

st.title("Processador de Nuvens de Pontos")
st.caption("Transforme vídeos em nuvens de pontos e comprima arquivos PLY com G-PCC")

# Estilo CSS customizado
st.markdown("""
    <style>
    .css-18ni7ap { 
        background-color: #f5f5f5 !important;  /* Fundo branco-cinza */
    }
    .stButton > button {
        background-color: #e0e0e0;  /* Cinza claro */
        color: black;
        border-radius: 10px;  /* Bordas arredondadas */
        padding: 10px 20px;  /* Tamanho do botão */
        border: 1px solid #d3d3d3;
    }
    .stButton > button:hover {
        background-color: #d6d6d6;  /* Efeito hover */
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Função para extrair frames do vídeo
def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_path, frame)
        frame_count += 1

    cap.release()
    return frame_count

# Barra lateral para o menu
st.sidebar.header("Menu")

# Upload de vídeo
uploaded_file = st.sidebar.file_uploader("Selecione um arquivo de vídeo", type=["mp4", "avi", "mov"])
if uploaded_file:
    video_path = f"temp_video.{uploaded_file.name.split('.')[-1]}"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())
    st.sidebar.success("Vídeo carregado com sucesso!")

    # Botão para iniciar o processamento
    if st.sidebar.button("Processar Nuvem de Pontos", key="process_cloud"):
        st.info("Extraindo frames do vídeo...")

        output_folder = "extracted_frames"
        frame_count = extract_frames(video_path, output_folder)

        st.success(f"Processamento concluído! {frame_count} frames extraídos e salvos em '{output_folder}'.")

# Botão para download
if st.sidebar.button("Baixar Arquivo PLY", key="download_ply"):
    st.warning("Função de download ainda não implementada.")

# Área principal
st.subheader("Passos para Processamento")
st.write("""
1. Faça upload do vídeo na barra lateral.\n
2. Inicie o processamento para gerar a nuvem de pontos.\n
3. Baixe o arquivo PLY comprimido.
""")

# Exemplo de exibição de resultado
st.subheader("Visualização da Nuvem de Pontos")
st.write("Após o processamento, a nuvem de pontos será exibida aqui.")
