import requests
import base64
import json


def ocr(IMAGE_PATH):
    # SECRET_KEY = 'sk_06ccd71d4fe21ede4abf6e65'
    # SECRET_KEY = 'sk_b285cb558e349df94505a2d7'
    # SECRET_KEY = 'sk_d68770137917dd0486d77d1e'
    # SECRET_KEY = 'sk_0886c882c9232c1d2283dba3'
    SECRET_KEY = 'sk_0886c882c9232c1d2283dba3'
    SECRET_KEY = 'sk_0886c882c9232c1d2283dba3'
    with open(IMAGE_PATH, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=ind&secret_key=%s' % (
        SECRET_KEY)  # Replace 'ind' with  your country code
    r = requests.post(url, data=img_base64)
    print(r)
    try:
        return r.json()['results'][0]['plate']

    except:
        print("Number plate is not clearly visible for recognition")
















# SECRET_KEY = 'sk_b285cb558e349df94505a2d7'
    # SECRET_KEY = 'sk_d68770137917dd0486d77d1e'
    # 'sk_b285cb558e349df94505a2d7'