import qrcode
from PyQt5 import QtGui
from io import BytesIO


def set_qr_label(label, text):
    """
    set qrcode image on QLabel

    @param label: QLabel
    @param text: text for the QR code
    """
    buf = BytesIO()
    img = qrcode.make(text)
    img.save(buf, "PNG")
    label.setText("")
    qt_pixmap = QtGui.QPixmap()
    qt_pixmap.loadFromData(buf.getvalue(), "PNG")
    label.setPixmap(qt_pixmap)