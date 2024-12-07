import requests

def send_sms(phone_number, message):
    """Envia um SMS usando o serviço Textbelt (API gratuita limitada)"""
    url = "https://textbelt.com/text"
    payload = {
        'phone': phone_number,
        'message': message,
        'key': 'textbelt',  
    }
    response = requests.post(url, data=payload)
    return response.json()
