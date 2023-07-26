import tezz
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton,MDRoundFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar,MDBottomAppBar
from kivy.uix.label import Label



class MainApp(MDApp): 
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen(

        )
        
        self.toolbar = MDTopAppBar(title="İmage To Emotion")
        self.toolbar.pos_hint={"top":1}
        self.toolbar.right_action_items=[["rotate-3d-variant",lambda x: self.flip()]]
        screen.add_widget(self.toolbar)
        
        self.image=Image(
            source="image/logo.png",
            pos_hint={"center_x":0.5,"center_y":0.77},
            size_hint=(0.3, 0.3)
        )
        screen.add_widget(self.image)
        
        
        
        screen.add_widget(MDFillRoundFlatIconButton(
            text="Resim Yükle",
            icon= "plus",
            text_color="white",
            on_press=self.callback,
            halign="center",
            pos_hint={"center_x":0.5,"center_y":0.5}
            ))
        self.label2 = MDLabel(
            id="label",
            text="Duygu Sonucu",
            halign="center",
            pos_hint={"center_x":0.5,"center_y":0.4},
            theme_text_color="Secondary",
            )
        screen.add_widget(self.label2)
        self.converted = MDLabel(
            id="label",
            text="",
            halign="center",
            pos_hint={"center_x":0.5,"center_y":0.35},
            theme_text_color="Primary",
            font_style="H5"
            )
        screen.add_widget(self.converted)
        
        self.emot=Image(
            source="emojiler/mutlu.png",
            pos_hint={"center_x":0.5,"center_y":0.2},
            size_hint=(0.2, 0.2)
        )
        screen.add_widget(self.emot)
        
        return screen
    def callback(self, instance):
        sonuc = tezz.duygu_analizi_yapma()
        result_text = ""
        duygu_heyecanli = 0
        duygu_üzgün = 0
        duygu_mutlu = 0
        duygu_Kızgın = 0
        duygu_Korku = 0
        duygu_Stresli = 0
        duygu_Sevinç = 0
        duygu_Güven = 0
        duygu_Beklenti = 0
        duygu_Tiksinme = 0
        duygu_Özlem=0
        duygu_Aşk=0
        en_yuksek_sayac = 0
        en_yuksek_duygu = ""
        if sonuc != "Geçersiz dosya adı." and sonuc != "Desteklenmeyen dosya formatı. Lütfen JPG, JPEG veya PNG dosyası seçin.":
            for duygu, sayi in sonuc.items():
                if sayi != 0:
                    result_text += f"{duygu}"
                    if duygu == "Heyecanlı":
                        duygu_heyecanli += 1
                        if duygu_heyecanli > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_heyecanli
                            en_yuksek_duygu = duygu
                    elif duygu == "Üzgün":
                        duygu_üzgün += 1
                        if duygu_üzgün > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_üzgün
                            en_yuksek_duygu = duygu
                    elif duygu == "Mutlu":
                        duygu_mutlu += 1
                        if duygu_mutlu > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_mutlu
                            en_yuksek_duygu = duygu    
                    elif duygu == "Kızgın":
                        duygu_Kızgın += 1
                        if duygu_Kızgın > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_Kızgın
                            en_yuksek_duygu = duygu
                    elif duygu == "Korku":
                        duygu_Korku += 1
                        if duygu_Korku > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_Korku
                            en_yuksek_duygu = duygu
                    elif duygu == "Stresli":
                        duygu_Stresli += 1
                        if duygu_Stresli > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_Stresli
                            en_yuksek_duygu = duygu
                    elif duygu == "Sevinç":
                        duygu_Sevinç += 1
                        if duygu_Sevinç > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_Sevinç
                            en_yuksek_duygu = duygu
                    elif duygu == "Güven":
                        duygu_Güven += 1
                        if duygu_Güven > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_Güven
                            en_yuksek_duygu = duygu
                    elif duygu == "Beklenti":
                        duygu_Beklenti += 1
                        if duygu_Beklenti > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_Beklenti
                            en_yuksek_duygu = duygu
                    elif duygu == "Tiksinme":
                        duygu_Tiksinme += 1
                        if duygu_Tiksinme > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_Tiksinme
                            en_yuksek_duygu = duygu
                    elif duygu == "Özlem":
                        duygu_Özlem += 1
                        if duygu_Özlem > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_Özlem
                            en_yuksek_duygu = duygu
                    elif duygu == "Aşk":
                        duygu_Aşk += 1
                        if duygu_Aşk > en_yuksek_sayac:
                            en_yuksek_sayac = duygu_Aşk
                            en_yuksek_duygu = duygu                 

            if en_yuksek_duygu == "Heyecanlı":
                self.emot.source = "emojiler/heyecanlı.png"
            elif en_yuksek_duygu == "Üzgün":
                self.emot.source = "emojiler/üzgün.png"
            elif en_yuksek_duygu == "Mutlu":
                self.emot.source = "emojiler/mutlu.png"
            elif en_yuksek_duygu == "Kızgın":
                self.emot.source = "emojiler/kızgın.png"
            elif en_yuksek_duygu == "Korku":
                self.emot.source = "emojiler/korku.png"
            elif en_yuksek_duygu == "Stresli":
                self.emot.source = "emojiler/stres.png"
            elif en_yuksek_duygu == "Sevinç":
                self.emot.source = "emojiler/sevinçli.png"
            elif en_yuksek_duygu == "Güven":
                self.emot.source = "emojiler/güven.png"
            elif en_yuksek_duygu == "Beklenti":
                self.emot.source = "emojiler/beklenti.png"
            elif en_yuksek_duygu == "Tiksinme":
                self.emot.source = "emojiler/tiksinme.png"
            elif en_yuksek_duygu == "Özlem":
                self.emot.source = "emojiler/özlem.png"
            elif en_yuksek_duygu == "Aşk":
                self.emot.source = "emojiler/aşk.png"        

            self.converted.text = "Bu Metinin İçindeki Duygu: " + en_yuksek_duygu           
        else:
            self.converted.text = sonuc

    def flip(self):
        self.converted.text=""
        self.emot.source="emojiler/mutlu.png"
    
        
if __name__ == '__main__':
    MainApp().run()
