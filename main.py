# main.py - Estrutura do Aplicativo em KivyMD

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from jnius import autoclass, cast
import os

# Definição do design em Kivy (Inline)
KV = """
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1

    MDLabel:
        text: "Aplicativo de Fotogrametria 3D"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        theme_text_color: "Primary"
        font_style: "H5"

    MDRaisedButton:
        text: "Capturar Imagem"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        on_release: app.capture_image()

    MDRaisedButton:
        text: "Gerar Nuvem de Pontos"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_release: app.generate_point_cloud()

    MDRaisedButton:
        text: "Visualizar Nuvem de Pontos"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.view_point_cloud()

    MDIconButton:
        icon: "camera"
        pos_hint: {"center_x": 0.9, "center_y": 0.9}
        on_release: app.capture_image()
"""

class FotogrametriaApp(MDApp):
    def build(self):
        # Configurando o tamanho da janela (para desenvolvimento no desktop)
        Window.size = (360, 640)
        # Carregar a interface do design definido em KV
        return Builder.load_string(KV)

    def capture_image(self):
        # Implementação da captura de imagem usando Pyjnius
        print("Capturando imagem...")
        Environment = autoclass('android.os.Environment')
        File = autoclass('java.io.File')
        Camera = autoclass('android.hardware.Camera')
        MediaScannerConnection = autoclass('android.media.MediaScannerConnection')
        MediaScannerConnectionClient = autoclass('android.media.MediaScannerConnection$MediaScannerConnectionClient')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')

        # Diretório onde a imagem será salva
        pictures_dir = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES)
        storage_path = File(pictures_dir, 'fotogrametria')
        if not storage_path.exists():
            storage_path.mkdirs()

        # Nome do arquivo de imagem
        file_name = 'captura_{}.jpg'.format(int(time.time()))
        image_file = File(storage_path, file_name)

        # Acessando a câmera e tirando a foto
        camera = Camera.open()
        camera.takePicture(None, None, self.PictureCallback(image_file))
        camera.release()

        # Atualizando o armazenamento com a nova imagem
        MediaScannerConnection.scanFile(
            PythonActivity.mActivity,
            [image_file.getAbsolutePath()],
            None,
            None
        )

    class PictureCallback(autoclass('android.hardware.Camera$PictureCallback')):
        def __init__(self, image_file):
            self.image_file = image_file

        def onPictureTaken(self, data, camera):
            try:
                with open(self.image_file.getAbsolutePath(), 'wb') as f:
                    f.write(data)
                print(f"Imagem salva em: {self.image_file.getAbsolutePath()}")
            except Exception as e:
                print(f"Erro ao salvar imagem: {e}")

    def generate_point_cloud(self):
        # Função placeholder para gerar a nuvem de pontos
        print("Gerando nuvem de pontos...")
        # Implementação do pyCOLMAP para gerar nuvem de pontos a partir das imagens

    def view_point_cloud(self):
        # Função placeholder para visualizar a nuvem de pontos
        print("Visualizando nuvem de pontos...")
        # Aqui você deve implementar um visualizador para a nuvem de pontos gerada

if __name__ == "__main__":
    FotogrametriaApp().run()
