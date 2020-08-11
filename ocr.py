import base64
import os 
import io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'< JSON API KEY PATH >'
client = vision.ImageAnnotatorClient()

image_file = '<Your Image File >'
folder_path = r'<Folder Path>'


with io.open(os.path.join(folder_path,image_file),'rb') as img:
    content = img.read()

image = vision.types.Image(content = content)
response = client.document_text_detection(image =image)

text = response.full_text_annotation.text
print(text)