import os
import qrcode

# Zjistí složku, ve které se nachází tento skript
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "qr_kod.png")

# Data, která chceš do QR kódu zakódovat
data_to_encode = "https://forms.cloud.microsoft/e/6GvXeSWN25"

# Vytvoření instance QR kódu s nastavením
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

# Přidání dat a vygenerování
qr.add_data(data_to_encode)
qr.make(fit=True)

# Vytvoření obrázku a uložení do stejné složky jako skript
img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print(f"QR kód byl úspěšně uložen jako: {file_path}")