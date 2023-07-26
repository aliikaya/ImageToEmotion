
duygu_sozlugu = {
    "Heyecanlı": ["heyecan", "coşku", "tutku", "azim", "istek","adrenalin","macera", 'adrenalin' , 'macera' 'olağanüstü' , 'beklenmedik' 'son ana kadar' , ' kazanmak' 'Sonuna kadar', 'gizemli'],
    "Üzgün": ["boşluk","üzüntü", "keder", "hüzün", "mutsuz", "melankoli",'hüzün', 'keder', 'İhanet ', 'pişmanlık ', 'kayıp', 'acı', 'Yalnız', 'sıkıntı', 'karamsarlık ', 'ölüm', 'başarısızlık', 'ayrılık ', 'depresyon'],
    "Mutlu": ["mutluluk", "sevinç", "neşe", "gülümseme", "keyif","hoşnutluk","mutluluk veren","sevgi","memnuniyet","mutlu oldum","gülümseme","hoşnut olma","gülmek"],
    "Kızgın": ["öfke", "kızgın", "sinirli", "tahammülsüz", "hiddet",'soru' ,'hata' , 'hayal kırıklığı' , ' bıktım' , ' yalan' , 'tartışmak' , 'sinir' , 'suç' , 'saygısızlık'],
    "Korku": ["korku", "endişe", "gergin", "tedirgin", "kaygı",'korku' , 'karanlık ' , 'yalnız ' , 'Birden' , 'Aniden' , 'birdenire' , 'gizemli ' , 'Dehşet' , 'Ürkütücü' , 'Ölüm' , 'Zombi' , 'Gece yarısı' , 'Şeytan' , 'Lanet' , 'korkunç'],
    "Stresli": ["stres", "yorgun", "bunalım", "tükenmiş", "gerilim","baskı", "karmaşa", "istifa", "sınav"],
    "Sevinç": ["sevinç", "zafer", "kutlama", "alkış", "tebrik", "harika", "mutlu", "neşeli", "neşe", "ilgi",  "müjde",  "coşku",  "dans",  "espri",  "eğlence", "iyilik", "doğa", "başarılar", "iyi haber", "iyimser"],
    "Güven": ["güven", "itimat", "emin", "güvenli", "sadık" , "güvenli", "dürüst", "güvende ", "empati" , "iyi niyet" , " destek" , "saygı" , "doğruluk" , "doğru", "içtenlik", "içten","doğal"  ],
    "Beklenti": ["umut", "beklenti", "arzu", "dilek","sabırsızlık","istikbal","önceden düşünme","gözlenti","öngörü","beklentiye girmek","umran","planlama","ileriye bakma","sabırsızlık"],
    "Tiksinme":["ıyy","kusmak","kötü koku","kirli","mide bulantısı","leş","pis","çürük"],
    "Özlem" : ["hasret", "özlem", "arzu", "dilek", "ihtiras", "istemek", "beklemek", "ayrılık", "ayrı", "yalnızlık", "sevgi", "geçmiş", "veda", "anı", "vefasızlık", "hüzün", "rüya", "yoksuluk", "özledim", "yıllar","çok oldu","ihtimal","iz"],
    "Aşk" : ["aşk", "tutku", "heyecan", "romantizm", "sevgi", "mutluluk", "sadakat", "kalp", "aşık", "kalbim", "sevgili", "sonsuz", "çarpıcı", "şiir", "huzur", "çekim", "özel", "hayranlık", "öpücük","sevilmek", "tatlı", "içtenlik", "arzu", "hayran", "birlikte", "karşılıksız"]
}


def duygu_analizi(yazi):
    duygu_sayisi = {duygu: 0 for duygu in duygu_sozlugu}

    kelimeler = yazi

    for kelime in kelimeler:
        for duygu, duygu_kelimeleri in duygu_sozlugu.items():
            if kelime in duygu_kelimeleri:
                duygu_sayisi[duygu] += 1

    return duygu_sayisi