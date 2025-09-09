from google.colab import files

uploaded = files.upload()

for filename, content in uploaded.items():
    with open(filename, 'wb') as f:
        f.write(content)
