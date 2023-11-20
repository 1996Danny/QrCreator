from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
import qrcode
from io import BytesIO

class Qr_app(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_label = Label(text="Ingrese el enlace: ", size_hint = (1,None), height = 30)
        self.input_text = TextInput(multiline=False, size_hint = (1,None), height = 30)
        self.generate_button = Button(text="Crear QR", on_press=self.crear_qr, size_hint = (1, None), height = 30, pos_hint={'center_x': 0.5})
        self.qr_image = Image()

        layout.add_widget(self.input_label)
        layout.add_widget(self.input_text)
        layout.add_widget(self.generate_button)
        layout.add_widget(self.qr_image)

        return layout

    def crear_qr(self, link):
        enlace_red_social = self.input_text.text

        codigo_qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4,)

        codigo_qr.add_data(enlace_red_social)
        codigo_qr.make(fit=True)

        imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")

        #Conversion de imagen
        buffer = BytesIO()
        imagen_qr.save(buffer)
        buffer.seek(0)
        imagen_bytes = buffer.read()

        # Mostrar
        core_image = CoreImage(BytesIO(imagen_bytes), ext='png')
        self.qr_image.texture = core_image.texture

        self.input_label.text = "QR creado con éxito!"

if __name__ == '__main__':
    Qr_app().run()