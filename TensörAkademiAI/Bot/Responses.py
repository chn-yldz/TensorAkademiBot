from datetime import datetime



def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("selam","merhaba","hey"):
        return "Merhaba"
    if user_message in ("nasılsın","naber","nasıl gidiyor"):
        return "Çok İyiyim Siz Nasılsınız?"
    if user_message in ("iyiyim","iyidir","idare eder"):
        return "İyi Olmanıza Sevindim"
    if user_message in ("kimsin sen","kimsin","nesin sen","nesin"):
        return "--- Ben TensörAkademiBot ---\nSize Daha İyi Hizmet Vermek İçin Buradayım"
    if user_message in ("Saat","Zaman","saat kaç"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(datetime)
    if user_message in ("yardım","Yardım"):
        return f"Çok Yakında Sizlerleyim :)\nDaha Fazlası İçin : https://www.instagram.com/tensorakademi/ veya \nhttps://twitter.com/tensorakademi veya \nhttps://www.youtube.com/channel/UCxq4le0YbomzFkTav6KbSlQ?app=desktop  Adreslerine Bakabilirsiniz\nSağlıklı Günler Dilerim ..."
    return "Ne Demek İstediğinizi Anlamadım :("