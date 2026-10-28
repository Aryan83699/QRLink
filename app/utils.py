import qrcode
import io
import base64

def generate_qr(data):
    qr=qrcode.QRCode(
        version=1,
        box_size=10,
        border=3
    )

    qr.add_data(data)
    qr.make(fit=True)

    img=qr.make_image(fill_color="black",back_color="white")
    buffer=io.BytesIO()
    img.save(buffer,format="PNG")
    qr_base64=base64.b64encode(buffer.getvalue()).decode("utf-8")

    return {
    "qr_code":qr_base64
    }

    