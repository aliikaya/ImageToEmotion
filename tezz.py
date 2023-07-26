from PIL import Image
import cv2
from pytesseract import pytesseract
import string
import metinanalizi
import tkinter
from tkinter.filedialog import askopenfilename
#tesseract tanımlama
path_to_tesseract = r'C:\Users\alika\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract


def duygu_analizi_yapma():
    # Kullanıcıya resim seçtirme
    tkinter.Tk().withdraw() # Pencere başlığını gizleme
    filename = askopenfilename() # Dosya seçiciyi açma

    # Resmi açma ve kaydetme
    if filename:
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            image = Image.open(filename)
            image.save('image/resim.jpg')
            print('Resim kaydedildi.')
            
            #resim yolunu belirleme
            path_to_image = 'image/resim.jpg'
            # Görüntü yükleme
            img = cv2.imread(path_to_image)
            
    
            #tesseract ile resimi texte dönüştürme
            text = pytesseract.image_to_string(img,lang="tur")
            print(text)

            # Cümleleri ayırma
            sentences = text.split(". ")
            print(sentences)
            # Kelime frekansı hesaplama
            words = text.split()

            word_counts = {}
            #metindeki kelimeleri sayma yöntemi
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
            print(word_counts)
            
            
            
            #duygu kısmı
            words2 = [word.lower() for word in words]
            sonuc = metinanalizi.duygu_analizi(words2)
            print("Duygu Analizi Sonucu:")
            for duygu, sayi in sonuc.items():
                if sayi!=0:
                    print(f"{duygu}: {sayi}")
                    
                    
    
            # noktalama işretinden ayırma
            yeniMetin = ""
                    
            for i in text:
                if i not in string.punctuation:
                    yeniMetin += i
            print("Noktalama İşaretlerinden Arınmış metin")
            print(yeniMetin)
            
        else:
            sonuc="Desteklenmeyen dosya formatı. Lütfen JPG, JPEG veya PNG dosyası seçin."
    else:
        sonuc="Geçersiz dosya adı."


    
    return sonuc


    
    






