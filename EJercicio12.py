archivo = input("Introduce el nombre del archivo: ").lower()

mime_types = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}

extension = archivo[archivo.rfind('.'):]

if extension in mime_types:
    print(mime_types[extension])
else:
    print('application/octet-stream')