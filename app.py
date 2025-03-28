from flask import Flask, render_template_string
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/')
def qr_whatsapp():
    # Cambia este número y mensaje por el tuyo
    whatsapp_url = "https://wa.me/56998713612?text=Hola!%20me%20daria%20más%20información%20por%20favor"
    
    qr_img = qrcode.make(whatsapp_url)
    buffer = io.BytesIO()
    qr_img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    html = '''
    <h1>Escaneá el QR para abrir WhatsApp</h1>
    <img src="data:image/png;base64,{{img_str}}" alt="QR WhatsApp">
    '''

    return render_template_string(html, img_str=img_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
