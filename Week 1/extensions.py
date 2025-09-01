filename = input("Enter a file name: ").strip().lower()
mapping = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}
for ext, media in mapping.items():
    if filename.endswith(ext):
        print(media)
        break
else:
    print("application/octet-stream")
