#ARMA TEAM
#PROJE ADI : KİŞİSEL SAĞLIK VE FİTNESS ASİSTANI 
#234210033 RAUF EKEN
#234210045 METEHAN KENDİRLİOĞLU

from os import system,name
import random
import time

#terminali temizler
def Temizle():
    system("clear") if name == "posix" else system("cls")
    
kayıtlı_kullanıcılar=[
{"id":4565, "isim" : "Berk","email": "berk@gmail.com","cinsiyet":"E" ,"boy":169,"kilo":70, "toplam_kalori": 500}, 
{"id":42,"isim" : "Çağrı","email": "cagri@gmail.com","cinsiyet":"E" ,"boy":178,"kilo":83,"toplam_kalori": 500}, 
{"id":475,"isim" : "Ahmet","email": "ahmet@gmail.com","cinsiyet":"E" ,"boy":187,"kilo":78,"toplam_kalori": 500}, 
{"id":135,"isim" : "Mehmet","email": "mehmet@gmail.com","cinsiyet":"E" ,"boy":181,"kilo":120,"toplam_kalori": 500}, 
{"id":455,"isim" : "Ayşe","email": "ayse@gmail.com","cinsiyet":"K" ,"boy":165,"kilo":50,"toplam_kalori": 450}, 
{"id":15,"isim" : "Elif","email": "elif@gmail.com","cinsiyet":"K" ,"boy":160,"kilo":45,"toplam_kalori": 700}, 
{"id":4,"isim" : "Ceren","email": "ceren@gmail.com","cinsiyet":"K" ,"boy":169,"kilo":48,"toplam_kalori": 1250}]

#uygulamanın giriş ekranı
def ana_menü():
   
    print("""-----------------------------------------------------------------------------------------------------------------------
                                         KİŞİSEL SAĞLIK VE FİTNESS ASİSTANI
-----------------------------------------------------------------------------------------------------------------------""")
    print("""
1. Giriş Yap
2. Kayıt Ol 
3. Bilgileri Güncelle
4. ID'mi unuttum
5. Beslenme Takipçisi
6. Aktivite Takipçisi
7. Çıkış Yap
    """)
    while True:
        try:
            işlem = input("Girmek istediğiniz menünün numarasını yazınız:")
            if işlem not in ("1", "2","3","4","5","6","7"):
                print("Geçersiz değer!")
            else:
               if işlem == "1":
                  Temizle()
                  giriş_ekranı()
                  break
               if işlem == "2":
                  Temizle()
                  kullanıcı_kayıt()
                  break   
               if işlem == "3":
                  Temizle()
                  kullanıcı_bilgileri_güncelleme()
                  break
               if işlem == "4":
                  Temizle()
                  id_unuttum()
                  break
               if işlem == "5":
                   Temizle()
                   kullanıcı = beslenme_takipçisi_giriş_ekranı()
                   ogun_adi = "Kahvaltı"
                   yemek_listesi = kahvaltı
                   beslenme_takipçisi(kullanıcı, ogun_adi, yemek_listesi)
                   ogun_adi = "Öğle Yemeği"
                   yemek_listesi = öğle_yemeği
                   beslenme_takipçisi(kullanıcı, ogun_adi, yemek_listesi)
                   ogun_adi = "Akşam Yemeği"
                   yemek_listesi = akşam_yemeği
                   beslenme_takipçisi(kullanıcı, ogun_adi, yemek_listesi)
                   ogun_adi = "Ara Öğün"
                   yemek_listesi = ara_öğünler
                   beslenme_takipçisi(kullanıcı, ogun_adi, yemek_listesi)
                   ana_menü()
               if işlem == "6":
                   Temizle()
                   kullanıcı_aktivite = aktivite_takipçisi_giriş_ekranı()
                   aktivite_listesi = aktiviteler
                   aktivite_takipcisi(kullanıcı_aktivite, aktivite_listesi)
                   ana_menü()
                   
               if işlem == "7":
                Temizle()
                çıkış_yap()
            
        except ValueError:
            print("Geçersiz giriş yaptınız. Tekrar deneyiniz.")
            time.sleep(1)
            Temizle()
            ana_menü()

#aktivite_takipçisi fonksiyonuna giriş ID'sini bağlar
def aktivite_takipçisi_giriş_ekranı():
    print("""-----------------------------------------------------------------------------------------------------------------------
                                                  AKTİVİTE TAKİPÇİSİ GİRİŞ EKRANI
-----------------------------------------------------------------------------------------------------------------------""")
    giriş_id = input("Kayıt sırasında size verilen giriş ID'nizi girin:")
    giriş_id = int(giriş_id)  

    for i, kullanıcı in enumerate(kayıtlı_kullanıcılar):
        if giriş_id == kullanıcı["id"]:
            isim = kullanıcı["isim"].title()
            print(f"Giriş başarılı. Hoşgeldiniz {isim},\nAktivite takipçisi yükleniyor...")
            time.sleep(2.5)
            Temizle()
            return giriş_id
        else:
            continue  

    print("Geçersiz ID. Tekrar deneyin.")
    time.sleep(2)
    Temizle()
    aktivite_takipçisi_giriş_ekranı()
    return
 
#beslenme takipçisi fonksiyonuna giriş ID'sini bağlar
def beslenme_takipçisi_giriş_ekranı():
    print("""-----------------------------------------------------------------------------------------------------------------------
                                                  BESLENME TAKİPÇİSİ GİRİŞ EKRANI
-----------------------------------------------------------------------------------------------------------------------""")
    giriş_id = input("Kayıt sırasında size verilen giriş ID'nizi girin:")
    giriş_id = int(giriş_id)  

    for i, kullanıcı in enumerate(kayıtlı_kullanıcılar):
        if giriş_id == kullanıcı["id"]:
            isim = kullanıcı["isim"].title()
            print(f"Giriş başarılı. Hoşgeldiniz {isim},\nBeslenme takipçisi yükleniyor...")
            time.sleep(2.5)
            Temizle()
            return giriş_id
        else:
            continue  

    print("Geçersiz ID. Tekrar deneyin.")
    time.sleep(2)
    Temizle()
    beslenme_takipçisi_giriş_ekranı()
    return

#kayıtlı kullanıcılar buradan giriş yapar
def giriş_ekranı():
    print("""-----------------------------------------------------------------------------------------------------------------------
                                                       GİRİŞ EKRANI
-----------------------------------------------------------------------------------------------------------------------""")
    giriş_id = input("Kayıt sırasında size verilen giriş ID'nizi girin:")
    giriş_id = int(giriş_id)  

    for i, kullanıcı in enumerate(kayıtlı_kullanıcılar):
        if giriş_id == kullanıcı["id"]:
            isim = kullanıcı["isim"].title()
            print(f"Giriş başarılı. Hoşgeldiniz {isim},\nYükleniyor...")
            time.sleep(2.5)
            Temizle()
            kullanıcı_menü(giriş_id)
            return  
        else:
            continue  

    print("Geçersiz ID. Tekrar deneyin.")
    time.sleep(2)
    Temizle()
    giriş_ekranı()
    return(giriş_id)

         
#kullanıcı menüsü. Kullanıcının bilgilerini alarak VKİ hesaplar ve kullanıcının durumu hakkında yorum yapar         
def kullanıcı_menü(giriş_id):
    print("""-----------------------------------------------------------------------------------------------------------------------
                                                       KULLANICI MENÜSÜ
-----------------------------------------------------------------------------------------------------------------------""")
    for i, kullanıcı in enumerate(kayıtlı_kullanıcılar):
       if giriş_id == kullanıcı["id"]:
          kullanıcı_isim = kullanıcı["isim"]
          kullanıcı_kilo = kullanıcı["kilo"]
          kullanıcı_boy = kullanıcı["boy"]
          kullanıcı_cinsiyet = kullanıcı["cinsiyet"]
          vücut_kitle_endeksi = kullanıcı_kilo / ((kullanıcı_boy/100)**2)
          if vücut_kitle_endeksi <= 18.5:
             kitle_endeks_yorum = "zayıfsınız"
          elif vücut_kitle_endeksi <=24.9:
                kitle_endeks_yorum = "normalsiniz."
          elif vücut_kitle_endeksi <=29.9:
                   kitle_endeks_yorum = "kilolusunuz"
          elif vücut_kitle_endeksi <= 34.9:
                      kitle_endeks_yorum = "obezsiniz"
          else:
                      kitle_endeks_yorum = "morbid obezsiniz"
          if kullanıcı["cinsiyet"].upper() == "E":
             kullanıcı_hitap = "Bey" #cinsiyete göre hitap atanır
          else:
             kullanıcı_hitap = "Hanım"#cinsiyete göre hitap atanır
          print(f"""Merhaba {kullanıcı_isim.title()} {kullanıcı_hitap},\nKilonuz {kullanıcı_kilo} kg ve boyunuz {kullanıcı_boy} cm olmakla beraber;
vücut kitle endeksiniz {vücut_kitle_endeksi:.1f} olarak hesaplanmıştır. (Bilgileriniz yanlışsa lütfen ana menüden güncelleyin.)
Vücut kitle endeksinize göre {kitle_endeks_yorum}.\n\nNe yapmak istersiniz?""")
          print("1) Bana uygun beslenme listemi öğrenmek istiyorum.\n2) Bana uygun aktivite programımı öğrenmek istiyorum.\n3)Sağlık ve fitness ilerlememi takip etmek istiyorum.\n4) Ana menüye dönmek istiyorum. ")
    while True:
        try:
            işlem = input("Gitmek istediğiniz seçeneğin numarasını yazınız:")
            if işlem not in ("1", "2","3","4"):
                print("Geçersiz değer!")
            else:
               if işlem == "1":
                  Temizle()
                  beslenme_programı(giriş_id,vücut_kitle_endeksi,kullanıcı_isim,kullanıcı_hitap,kullanıcı_cinsiyet)
                  break
               if işlem == "2":
                  Temizle()
                  aktivite_programı(giriş_id, vücut_kitle_endeksi, kullanıcı_isim, kullanıcı_hitap, kullanıcı_cinsiyet)
                  break   
               if işlem == "3":
                   Temizle()
                   sağlık_fitness_izleme(giriş_id)
                   return giriş_id
                   break
               if işlem == "4":
                Temizle()
                ana_menü()
                break
            
        except ValueError:
            print("Geçersiz giriş yaptınız. Tekrar deneyiniz.")


#kullanıcın bugünkü kalori alımını kontrol eder onun hakkında yorum yapar. Kaloriyi kullanıcın isteğine göre sıfırlar
def sağlık_fitness_izleme(giriş_id):
        print("""-----------------------------------------------------------------------------------------------------------------------
                                                       SAĞLIK VE FİTNESS TAKİBİ
-----------------------------------------------------------------------------------------------------------------------""")
        for i, kullanıcı in enumerate(kayıtlı_kullanıcılar):
           if giriş_id == kullanıcı["id"]:
              kullanıcı_isim = kullanıcı["isim"]
              kullanıcı_kilo = kullanıcı["kilo"]
              kullanıcı_boy = kullanıcı["boy"]
              kullanıcı_cinsiyet = kullanıcı["cinsiyet"]
              kullanıcı_kalori = kullanıcı["toplam_kalori"]
              if kullanıcı["cinsiyet"].upper() == "E":
                kullanıcı_hitap = "Bey" #cinsiyete göre hitap atanır
              else:
                kullanıcı_hitap = "Hanım"#cinsiyete göre hitap atanır
              vücut_kitle_endeksi = kullanıcı_kilo / ((kullanıcı_boy/100)**2)
        print(f"Merhaba {kullanıcı_isim} {kullanıcı_hitap}. Bugünkü kazandığınız/kaybettiğiniz kalori {kullanıcı_kalori} olarak gözüküyor.")
        if kullanıcı_kalori > 1000:
            print("-İhtiyacınız olan kaloriden fazlasını almışsınız. Kilo alıyorsunuz. Kalori açığı oluşturmanız tavsiye edilir.\n Sporu artırın yemeği azaltın.")
        if kullanıcı_kalori < 0:
            print("-İhtiyacınız olan kaloriyi fazlasıyla yakmışsınız. Zayıflıyorsunuz. VKİ'niz normalden yüksekse iyidir.\nNormalseniz toplam alıp verinen kalorinizi mümkün olduğunca sıfıra yakın tutun.")
        if kullanıcı_kalori == 0: 
            print("-İhtiyacınız olan kaloriyi almış ve tamamını yakmışsınız. Mükemmel gidiyorsunuz!")
            time.sleep(3)
            Temizle()
            kullanıcı_menü(giriş_id)
        else:
            print("-İhtiyacınız olan kaloriden biraz fazlasını almışsınız. VKİ'niz normale yakınsa bu sorun teşkil etmez.İyi ilerliyorsunuz.")
            
        while True:
           try:
                kalori_sıfırla = input("Bugünkü toplam kaloriniz sıfırlansın mı? (E/H)")
                if kalori_sıfırla not in ("E","e","H","h"):
                  print("Geçersiz giriş. Tekrar deneyin.")
                else:
                  if kalori_sıfırla == "E" or kalori_sıfırla == "e":
                     kullanıcı["toplam_kalori"] = 0
                     print("Bugünkü kaloriniz sıfırlandı. Kullanıcı menüsüne yönlendiliyorsunuz.")
                     time.sleep(3)
                     Temizle()
                     kullanıcı_menü(giriş_id)
                     break    
                  else:
                     print("Kullanıcı menüsüne yönlendiriliyorsunuz.")
                     time.sleep(3)
                     Temizle()
                     kullanıcı_menü(giriş_id)
                     break
           except ValueError:
                print("Geçersiz giriş yaptınız. Tekrar deneyiniz.")

              
#kullanıcın verilerini alarak hesaplanmış vücut kitle endeksine ve cinsiyetine göre diyet programları verir. Kullanıcın VKİ değişirse diyet de otomatik değişir
def beslenme_programı(giriş_id, vücut_kitle_endeksi, kullanıcı_isim, kullanıcı_hitap, kullanıcı_cinsiyet):
    print("""-----------------------------------------------------------------------------------------------------------------------
                                                       BESLENME PROGRAMI
-----------------------------------------------------------------------------------------------------------------------""")
    print(f"\nVücut kitle endeksiniz şu anda {vücut_kitle_endeksi:.1f} olduğundan size uygun beslenme programı aşağıdaki gibidir {kullanıcı_isim} {kullanıcı_hitap}:")

    if kullanıcı_cinsiyet == "E":
        if (vücut_kitle_endeksi <= 18.5):
            print("Kilo kazanma odaklı kullanıcı")
            print("""Kahvaltı: Yumurta, peynir, tam tahıllı ekmek ve meyve
Öğle yemeği: Ton balıklı sandviç, sebze ve yoğurt
Akşam yemeği: Fırında sebzeli tavuk veya balık, bulgur pilavı
Ara öğünler: Taze meyve, kuruyemiş veya protein bar""")
        elif vücut_kitle_endeksi <= 24.9:
            print("Denge odaklı kullanıcı")
            print("""Kahvaltı: Yulaf ezmesi, meyve ve fındık ezmesi
Öğle yemeği: Sebzeli nohut yemeği, tam tahıllı ekmek
Akşam yemeği: Izgara sebze ve ızgara balık veya tavuk
Ara öğünler: Taze meyve, yoğurt veya sebze çubukları""")
        elif (vücut_kitle_endeksi <= 29.9):
            print("Kas kazanma odaklı kullanıcı")
            print("""Kahvaltı: Yumurta, peynir, tam tahıllı ekmek ve sebze
Öğle yemeği: Mercimek çorbası, sebze salata ve ızgara köfte
Akşam yemeği: Fırında sebzeli balık, bulgur pilavı
Ara öğünler: Taze meyve, kuruyemişler""")
        elif (vücut_kitle_endeksi <= 34.9):
            print("Kilo kaybı odaklı kullanıcı")
            print("""Kahvaltı: Yulaf ezmesi, meyve ve protein tozu
Öğle yemeği: Ton balıklı salata, tam tahıllı ekmek ve zeytinyağlı yaprak sarma
Akşam yemeği: Sebzeli tavuk veya balık, haşlanmış sebze
Ara öğünler: Taze meyve, yoğurt veya protein bar""")
        else:
            print("Kilo kaybı odaklı kullanıcı")
            print("""Kahvaltı: Yumurta, peynir, tam tahıllı ekmek ve sebze
Öğle yemeği: Mercimek çorbası, sebze salata ve fırında köfte
Akşam yemeği: Izgara balık veya tavuk, sebze garnitür
Ara öğünler: Taze meyve, yoğurt veya sebze çubukları""")
        input("Kullanıcı menüsüne gitmek için enter tuşuna basın.")
        Temizle()
        return kullanıcı_menü(giriş_id)
    elif kullanıcı_cinsiyet == "K":
        if  (vücut_kitle_endeksi <= 18.5):
            print("Kilo kazanma odaklı kullanıcı")
            print("""*Kahvaltı: Yulaf ezmesi, meyve ve yoğurt
*Öğle yemeği: Sebzeli salata, ızgara tavuk veya balık
*Akşam yemeği: Mercimek çorbası ve sebze yemeği
*Ara öğünler: Taze meyve, kuruyemiş veya yoğurt""")
        elif (vücut_kitle_endeksi <= 24.9):
            print("Kilo denge odaklı kullanıcı")
            print("""*Kahvaltı: Tam tahıllı ekmek, peynir, yumurta ve meyve
*Öğle yemeği: Ton balıklı sandviç, sebze ve yoğurt
*Akşam yemeği: Fırında sebzeli tavuk veya balık, bulgur pilavı
*Ara öğünler: Taze meyve, kuruyemiş veya protein bar""")
        elif (vücut_kitle_endeksi <= 29.9):
            print("Kas kütlesi kazanma odaklı kullanıcı")
            print("""*Kahvaltı: Yulaf ezmesi, meyve ve fındık ezmesi
*Öğle yemeği: Sebzeli nohut yemeği, tam tahıllı ekmek
*Akşam yemeği: Izgara sebze ve ızgara balık veya tavuk
*Ara öğünler: Taze meyve, yoğurt veya sebze çubukları""")
        elif (vücut_kitle_endeksi <= 34.9):
            print("Kilo kaybı odaklı kullanıcı")
            print("""*Kahvaltı: Yumurta, peynir, tam tahıllı ekmek ve sebze
*Öğle yemeği: Mercimek çorbası, sebze salata ve ızgara köfte
*Akşam yemeği: Fırında sebzeli balık, bulgur pilavı
*Ara öğünler: Taze meyve, yoğurt veya kuruyemiş""")
        elif (vücut_kitle_endeksi > 34.9):
            print("Kilo kaybı odaklı kullanıcı")
            print("""*Kahvaltı: Yulaf ezmesi, meyve ve protein tozu
*Öğle yemeği: Ton balıklı salata, tam tahıllı ekmek ve zeytinyağlı yaprak sarma
*Akşam yemeği: Sebzeli tavuk veya balık, haşlanmış sebze
*Ara öğünler: Taze meyve, yoğurt veya protein bar""")
        print("""\n\nNotlar:
*Her öğünde protein, karbonhidrat ve sağlıklı yağlar içeren dengeli beslenmeye özen gösterin.
*Bol su için ve düzenli egzersiz yapmayı unutmayın.""")
        input("Kullanıcı menüsüne gitmek için enter tuşuna basın.")
        Temizle()
        return kullanıcı_menü(giriş_id)


#Kullanıcının cinsiyeti ve vücut kitle indeksine göre uygun aktivite programını hazırlar. Kullanıcının VKİ değişirse aktivite programı da otomatik değişir  
def aktivite_programı(giriş_id, vücut_kitle_endeksi, kullanıcı_isim, kullanıcı_hitap, kullanıcı_cinsiyet):
    print("""-----------------------------------------------------------------------------------------------------------------------
                                                       AKTİVİTE PROGRAMI
-----------------------------------------------------------------------------------------------------------------------""")
    print(f"\nVücut kitle endeksiniz şu anda {vücut_kitle_endeksi:.1f} olduğundan size uygun aktivite programı aşağıdaki gibidir {kullanıcı_isim} {kullanıcı_hitap}:")

    NormalveZayıflar_aktivite ="""Pazartesi(Göğüs, kol günü):
-----------------------------  
*Bench press 3x15 (kiloyu kendinize göre ayarlayın)
*Incline bench press 3x15 (kiloyu kendinize göre ayarlayın)
*Dumbell fly 3x15 (kiloyu kendinize göre ayarlayın)
*Cable croosover 3x15 (kiloyu kendinize göre ayarlayın)
*Scott curl 4x15 (kiloyu kendinize göre ayarlayın)
*Dumbell curl 4x15 (kiloyu kendinize göre ayarlayın)
*Rope push-down 4x15 (kiloyu kendinize göre ayarlayın)
*Triceps extension 4x15 (kiloyu kendinize göre ayarlayın)\n
Çarşamba (Sırt,karın):
-----------------------------
*Lat pulldown 4x15
*Dumbell row 4x15                  
*Closegrip pulldown 4x15
*Back extension 4x15
*Plank (3 dk)
*Crunch (yorulanana kadar 4 set)   
*Leg raise push-up (yorulana kadar 3 set)\n
Cuma(bacak,omuz):
-----------------------------
*Squat 3x10
*Leg press 3x10
*Deadlift 3x10
*Hammer curl 3x10
*Front raise 3x10
*Rope face pull 3x10
*Rear delt fly 3x10                  
"""
    normal_aktivite_pazar ="""Pazar(kardiyo günü)
-----------------------------
*%15 eğimli yürüyüş ya da koşu (yarım saat)
*İp atlama (15 dk)
*Mekik ve şınav (4 set yorulana kadar)
    """
    obez_aktivite = """Pazartesi(Bütün vücut)
-----------------------------
*Bench press 5x5
*Dips 4x12
*Incline dumbell fly 4x10
*Dumbell bench press 4x12
*Dumbell omuz press 4x12
*Lateral raise 4x8
*Z press 2x12
*Skull crusher 4x12
*Pushdown 4x12
Çarşamba(Bütün vücut)
-----------------------------
*Barfiks 4x10
*Barbell row 4x6
*Pulldown 4*12
*Face pull 4x15
*Shrug 4x15
*Hammer curl 4x12
*Incline curl 4x12
Cuma
-----------------------------
*Squat 5x5
*Leg curl 4x12
*Leg press 8x12
*Bulgarian split squat 3x15
*Plank (10 dk)
*Side plank (10dk)
"""
    morbidobez_aktivite_pazar = """Pazar (Kardiyo)
-----------------------------
*İp atlama 30 dk
*%15 eğimli 5-6 hızda yürüyüş (20 dk)
*Halat idmanı (15dk)
"""
    tavsiyeler = """Ek tavsiyeler:
Egzersiz programınıza çeşitlilik katın.
Yeterince dinlenin ve uyuyun.
Sağlıklı beslenin.
Bol su için.
Kendinizi motive etmek için bir egzersiz arkadaşı veya grubu bulun.
Egzersiz yaparken herhangi bir ağrı veya rahatsızlık hissederseniz durun ve doktorunuza danışın."""

    if kullanıcı_cinsiyet == "E":
        if (vücut_kitle_endeksi <= 18.5):
            print("Kilo kazanma odaklı kullanıcı")
            print(NormalveZayıflar_aktivite)
        elif vücut_kitle_endeksi <= 24.9:
            print("Denge odaklı kullanıcı")
            print(NormalveZayıflar_aktivite)
            print(normal_aktivite_pazar)
        elif (vücut_kitle_endeksi <= 29.9):
            print("Kas kazanma odaklı kullanıcı")
            print(NormalveZayıflar_aktivite)
        elif (vücut_kitle_endeksi <= 34.9):
            print("Kilo kaybı odaklı kullanıcı")
            print(obez_aktivite)
        elif (vücut_kitle_endeksi > 34.9):
            print("Aşırı kilo kaybı odaklı kullanıcı")
            print(obez_aktivite)
            print(morbidobez_aktivite_pazar)
        print(tavsiyeler)    
        input("Kullanıcı menüsüne gitmek için enter tuşuna basın.")
        Temizle()
        return kullanıcı_menü(giriş_id)
    elif kullanıcı_cinsiyet == "K":
        if  (vücut_kitle_endeksi <= 18.5):
            print("Kilo kazanma odaklı kadın kullanıcı")
            print(NormalveZayıflar_aktivite)
        elif (vücut_kitle_endeksi <= 24.9):
            print("Kilo denge odaklı kadın kullanıcı")
            print(NormalveZayıflar_aktivite)
            print(normal_aktivite_pazar)
        elif (vücut_kitle_endeksi <= 29.9):
            print("Kas kütlesi kazanma odaklı kadın kullanıcı")
            print(NormalveZayıflar_aktivite)
        elif (vücut_kitle_endeksi <= 34.9):
            print("Kilo kaybı odaklı kadın kullanıcı")
            print(obez_aktivite)
        elif (vücut_kitle_endeksi > 34.9):
            print("Kilo kaybı odaklı kadın kullanıcı")
            print(obez_aktivite)
        print()
        print(tavsiyeler)
        input("Kullanıcı menüsüne gitmek için enter tuşuna basın.")
        Temizle()
        return kullanıcı_menü(giriş_id)


#kullanıcı kayıt ekranı. Kullanıcıdan bilgiler alınır, sistem yeni kullanıcıya rastgele id atar
def kullanıcı_kayıt():
    """
    Kullanıcı kayıt işlemini gerçekleştirir.
    """
    print("""-----------------------------------------------------------------------------------------------------------------------
                                                KULLANICI KAYIT EKRANI
-----------------------------------------------------------------------------------------------------------------------""")

    while True:
        isim = input("Adınız:")
        if len(isim) == 0:
            print("İsim boş kalamaz.")
            continue

        while True:
            email = input("E-postanız:")
            if "@" not in email:
                print("Geçersiz e-posta formatı! Lütfen @ simgesi içeren bir adres giriniz.")
                continue
            else:
                break

        while True:
            cinsiyet = input("Cinsiyetiniz (E/K):").upper()
            if cinsiyet not in ("E", "K"):
                print("Geçersiz karakter girdiniz tekrar deneyiniz:")
                continue
            else:
                break

        while True:
            try:
                boy = int(input("Boyunuz (santimetre):"))
                if boy > 250 or boy < 50:
                    print("Geçerli boy değeri giriniz (50-250 cm):")
                    continue
                else:
                    break
            except ValueError:
                print("Geçersiz boy değeri giriniz (sayı girmelisiniz):")
                continue

        while True:
            try:
                kilo = int(input("Kilonuz:"))
                if kilo < 30:
                    print("Geçerli kilo değeri giriniz (en az 30 kg):")
                    continue
                else:
                    break
            except ValueError:
                print("Geçerli kilo değeri giriniz (sayı girmelisiniz):")
                continue
        toplam_kalori = 0
        id_numarası = random.randint(1, 9999)
        for kullanıcı in kayıtlı_kullanıcılar:
            if id_numarası == kullanıcı["id"]: #eğer çakışma olursa yeniden atama yapar
                id_numarası = random.randint(1, 9999)

        kullanıcı = {
            "id": id_numarası,
            "isim": isim,
            "email": email,
            "cinsiyet": cinsiyet,
            "boy": boy,
            "kilo": kilo,
            "toplam_kalori": toplam_kalori
        }

        kayıtlı_kullanıcılar.append(kullanıcı)
        print(f"Kayıt başarılı! Giriş yapmak için ID'niz {id_numarası}. Bu numarayı unutmayın.\n-Devam etmek için herhangi bir tuşa basın...")
        input()
        print("Ana menüye yönlendiriliyorsunuz...")
        time.sleep(2)
        Temizle()
        ana_menü()
        break
 
#Kullanıcı eğer isterse boyunda kilosunda vs değişiklik yapabilir
def kullanıcı_bilgileri_güncelleme():
  print("""-----------------------------------------------------------------------------------------------------------------------
                                            KULLANICI BİLGİLERİ GÜNCELLEME
-----------------------------------------------------------------------------------------------------------------------""")
  while True:
    kullanıcı_id = int(input("Güncellemek istediğiniz kullanıcının ID numarasını giriniz: "))

    kullanıcı_bilgileri = None
    for kullanıcı in kayıtlı_kullanıcılar:
      if kullanıcı["id"] == kullanıcı_id:
        kullanıcı_bilgileri = kullanıcı
        break

    if not kullanıcı_bilgileri:
      print(f"ID {kullanıcı_id} nolu kullanıcı bulunamadı.")
      continue
      
    print("Kullanıcı bilgileri:")
    print("İsim:",kullanıcı["isim"])
    print("Cinsiyet:",kullanıcı["cinsiyet"])
    print("E-posta:",kullanıcı["email"])
    print("Boy:",kullanıcı["boy"])
    print("Kilo:",kullanıcı["kilo"])
    print("\nHangi bilgiyi güncellemek istiyorsunuz?")
    print("1. İsim")
    print("2. Email")
    print("3. Cinsiyet")
    print("4. Boy")
    print("5. Kilo")
    print("6. Ana Menüye Dön")

    secim = int(input("Seçiminizi giriniz: "))

    if secim == 6:
      print("Ana menüye dönüyorsunuz.")
      time.sleep(1)
      Temizle()
      ana_menü()
    
    if secim in [1, 2, 3, 4, 5]:
      yeni_bilgi = input("Yeni bilgiyi giriniz: ")
      if secim == 1:
        kullanıcı_bilgileri["isim"] = yeni_bilgi
      elif secim == 2:
        kullanıcı_bilgileri["email"] = yeni_bilgi
      elif secim == 3:
        if yeni_bilgi not in ("E","e","K","k"):
            print("Geçersiz giriş. Tekrar deneyiniz.")
            time.sleep(1.5)
            Temizle()
            kullanıcı_bilgileri_güncelleme()
        else:
         kullanıcı_bilgileri["cinsiyet"] = yeni_bilgi
      elif secim == 4:
        yeni_bilgi = int(yeni_bilgi)
        if yeni_bilgi > 250 or yeni_bilgi < 50:
            print("Geçersiz giriş. Tekrar deneyiniz.")
            time.sleep(1)
            Temizle()
            kullanıcı_bilgileri_güncelleme()
        else:
         kullanıcı_bilgileri["boy"] = int(yeni_bilgi)
      else:
        yeni_bilgi = int(yeni_bilgi)
        if yeni_bilgi <30:
            print("Geçersiz değer tekrar deneyiniz.")
            time.sleep(1)
            Temizle()
            kullanıcı_bilgileri_güncelleme()
        else:
         kullanıcı_bilgileri["kilo"] = int(yeni_bilgi)

      print(f"{kullanıcı_bilgileri['isim']} kullanıcısının bilgileri güncellendi.")
      time.sleep(2)
      Temizle()
      ana_menü()
    else:
      print("Geçersiz seçim.")
      time.sleep(1)
      Temizle()
      ana_menü()

#kullanıcının ID'sini unutması durumunda e posta bilgisi ister eğer sistemde öyle bir e posta varsa ID bilgisini verir
def id_unuttum():
    print("""-----------------------------------------------------------------------------------------------------------------------
                                                    ID'Mİ UNUTTUM
-----------------------------------------------------------------------------------------------------------------------""")
    eposta = input("Sistemde kayıtlı e-postanızı giriniz: ")
    for kullanıcı in kayıtlı_kullanıcılar:
        if eposta.lower().strip() == kullanıcı["email"].lower().strip():
            print(f"Merhaba {kullanıcı['isim']}, sistemdeki ID'niz: {kullanıcı['id']}.\nID numaranızı unutmayın.")
            print("-Ana menüye dönmek için enter'a basın.")
            input()
            Temizle()
            ana_menü()
            if len(eposta) == 0:
                print("Lütfen bir eposta girin.")
                time.sleep(1)
                Temizle()
                id_unuttum()
            else:
                print(f"{eposta} sistemde bulunamadı. Ana menüye yönlendiriliyorsunuz...")
                time.sleep(2)
                Temizle()
                ana_menü()
        
#Çıkış ekranı
def çıkış_yap():
   while True:
       try:
            çıkış_onay = input("Kişisel Sağlık ve Fitness Asistanından çıkış yapılsın mı? (E/H)")
            if çıkış_onay not in ("E","e","H","h"):
              print("Geçersiz giriş. Tekrar deneyin.")
            else:
              if çıkış_onay == "E" or çıkış_onay == "e":
                 Temizle()
                 print("Çıkmak için bir tuşa basın")
                 exit()
              else:
                 Temizle()
                 ana_menü()
                 break
       except ValueError:
            print("Geçersiz giriş yaptınız. Tekrar deneyiniz.")
            

kahvaltı =[{'yiyecek': 'Haşlanmış Yumurta', 'kalori': 75},{'yiyecek': 'Az Yağlı Peynir', 'kalori': 150}, 
 {'yiyecek': 'Tam Tahıllı Ekmek', 'kalori': 200}, {'yiyecek': 'Sebze Çeşitleri', 'kalori': 50}] 
öğle_yemeği = [{'yiyecek': 'Ton Balıklı Salata', 'kalori': 300}, {'yiyecek': 'Zeytinyağlı Yaprak Sarma', 'kalori': 250}, 
 {'yiyecek': 'Mercimek Çorbası', 'kalori': 200}, {'yiyecek': 'Sebze Salata', 'kalori': 100}, 
 {'yiyecek': 'Izgara Köfte', 'kalori': 350}]
akşam_yemeği = [{'yiyecek': 'Sebzeli Tavuk veya Balık', 'kalori': 300},{'yiyecek': 'Bulgur Pilavı', 'kalori': 200},
 {'yiyecek': 'Haşlanmış Sebze', 'kalori': 50}] 
ara_öğünler = [{'yiyecek': 'Taze Mevsim Meyvesi', 'kalori': 100}, {'yiyecek': 'Sade Yoğurt', 'kalori': 150}, {'yiyecek': 'Protein Bar', 'kalori': 200}, {'yiyecek': 'Kuruyemiş Çeşitleri', 'kalori': 180}]

#Kullanıcı ID'sini alarak kullanıcın o gün neler yediğini sorar ve toplam_kalori değişkenine ekler
def beslenme_takipçisi(kullanıcı, ogun_adi, yemek_listesi):

    for user in kayıtlı_kullanıcılar:
        if user['id'] == kullanıcı:
            kullanıcı_kaydı = user
            break


    print(f"""-----------------------------------------------------------------------------------------------------------------------
                                        BESLENME TAKİPÇİSİ - {ogun_adi.upper()}
-----------------------------------------------------------------------------------------------------------------------""")

    toplam_kalori = 0

    for i, secenek in enumerate(yemek_listesi):
        print(f"{i+1}. {secenek['yiyecek']} ({secenek['kalori']} kalori)")

    print(f"{len(yemek_listesi)+1}) {ogun_adi} yapmadım. (geç)")

    secim = int(input(f"{ogun_adi} için ne yediniz? (Seçenek numarasını giriniz): "))

    while True:
        if 1 <= secim <= len(yemek_listesi):
            secilen_yiyecek = yemek_listesi[secim - 1]
            print(f"{secilen_yiyecek['yiyecek']} yediniz ve {secilen_yiyecek['kalori']} kalori aldınız.")
            toplam_kalori += secilen_yiyecek['kalori']
        elif secim == len(yemek_listesi)+1:
            toplam_kalori += 0
        else:
            print("Geçersiz seçim.")
            continue
        break

    for kulanıcı in kayıtlı_kullanıcılar:
        kulanıcı["toplam_kalori"] += toplam_kalori
    print(f"Toplam kalori = {kulanıcı['toplam_kalori']}")
    time.sleep(2)
    Temizle()
    return

aktiviteler = [
    {"isim": "Bench press", "kalori": 125},
    {"isim": "Incline bench press", "kalori": 125},
    {"isim": "Dumbell fly", "kalori": 62},
    {"isim": "Cable crossover", "kalori": 87},
    {"isim": "Scott curl", "kalori": 62},
    {"isim": "Dumbell curl", "kalori": 62},
    {"isim": "Rope push-down", "kalori": 62},
    {"isim": "Triceps extension", "kalori": 62},
    {"isim": "Lat pulldown", "kalori": 87},
    {"isim": "Dumbell row", "kalori": 87},
    {"isim": "Closegrip pulldown", "kalori": 87},
    {"isim": "Back extension", "kalori": 62},
    {"isim": "Plank", "kalori": 37},
    {"isim": "Crunch", "kalori": 37},
    {"isim": "Leg raise push-up", "kalori": 62},
    {"isim": "%15 eğimli yürüyüş ya da koşu", "kalori": 350},
    {"isim": "İp atlama", "kalori": 250},
    {"isim": "Mekik ve şınav", "kalori": 62},
    {"isim": "Dips", "kalori": 125},
    {"isim": "Incline dumbell fly", "kalori": 125},
    {"isim": "Dumbell bench press", "kalori": 125},
    {"isim": "Dumbell omuz press", "kalori": 125},
    {"isim": "Lateral raise", "kalori": 87},
    {"isim": "Z press", "kalori": 62},
    {"isim": "Skull crusher", "kalori": 62},
    {"isim": "Pushdown", "kalori": 62},
    {"isim": "Barfiks", "kalori": 125},
    {"isim": "Barbell row", "kalori": 125},
    {"isim": "Pulldown", "kalori": 87},
    {"isim": "Face pull", "kalori": 87},
    {"isim": "Shrug", "kalori": 62},
    {"isim": "Hammer curl", "kalori": 62},
    {"isim": "Incline curl", "kalori": 62},
    {"isim": "Squat", "kalori": 175},
    {"isim": "Leg curl", "kalori": 87},
    {"isim": "Leg press", "kalori": 175},
    {"isim": "Bulgarian split squat", "kalori": 125},
    {"isim": "Side plank", "kalori": 62}
]

#kullanıcın o günkü yaptığı sporları alır ve toplam kalorisinden çıkartır
def aktivite_takipcisi(kullanıcı, aktivite_listesi):

  for user in kayıtlı_kullanıcılar:
    if user['id'] == kullanıcı:
      kullanıcı_kaydı = user
      break

  print(f"""-----------------------------------------------------------------------------------------------------------------------
                    AKTİVİTE TAKİPÇİSİ
-----------------------------------------------------------------------------------------------------------------------""")

  toplam_kalori = 0

  for i, secenek in enumerate(aktivite_listesi):
    print(f"{i+1}. {secenek['isim']} ({secenek['kalori']} kalori)")

  print(f"{len(aktivite_listesi)+1}) Hiç aktivite yapmadım.")

  secim_str = input("Bugün hangi aktiviteleri yaptınız? (Seçenek numaralarını virgülle ayırın): ")
  secimler = secim_str.split(",")

  for secim_no in secimler:
    try:
      secim_no = int(secim_no.strip())
      if 1 <= secim_no <= len(aktivite_listesi):
        secilen_aktivite = aktivite_listesi[secim_no - 1]
        print(f"{secilen_aktivite['isim']} yaptınız ve {secilen_aktivite['kalori']} kalori bugünkü toplam kalorinizden düşüldü.")

        toplam_kalori_degeri = kullanıcı_kaydı.get("toplam_kalori", 0)

        toplam_kalori_degeri -= secilen_aktivite['kalori']

        kullanıcı_kaydı["toplam_kalori"] = toplam_kalori_degeri
      else:
        print(f"{secim_no} geçersiz bir seçim.")
    except ValueError:
      print("Geçersiz seçim formatı. Lütfen virgülle ayrılmış sayılar giriniz.")

  print(f"Toplam kalori = {kullanıcı_kaydı['toplam_kalori']}")
  time.sleep(5)
  Temizle()
  ana_menü()

#PROGRAMIN BAŞLANGIÇ FONKSİYONU
if __name__ == "__main__":
    ana_menü()