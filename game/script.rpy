# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    config.font_replacement_map["Raleway-Regular.ttf", False, True] = ("Raleway-Italic.ttf", False, False)

init python:
    config.font_replacement_map["Raleway-Regular.ttf", True, True] = ("Raleway-BoldItalic.ttf", False, False)

init python:
    config.font_replacement_map["Raleway-Regular.ttf", True, False] = ("Raleway-Bold.ttf", False, False)

init:
    $ renpy.music.register_channel("channel1", loop=True)

default kevinle = False
default emilylived = False
default josephlived = False
default madisonlived = False

image logo = "logo.png"

define e = Character("Emily", color="#ffea00")
define k = Character("Kevin", color="#c8ffc8")
define o = Character("Öğretmen", color="#8fbc8f")
define g = Character("Gözlüklü Öğrenci", color="#8fbc8f")
define ed = Character("Edward", color="#8fbc8f")
define z = Character("Zorba", color="#800000")
define sk = Character("Şişman Kız", color="#a6e7ff")
define u = Character("???", color="#808080")
define ka = Character("Kör Adam", color="#a6e7ff")
define tr = Character("Kamyon", color="#a6e7ff")
define anne = Character("Anne", color="#8fbc8f")
define j = Character("Joseph", color="#ffc40c")
define ska = Character("Sıska Kadın", color="#a6e7ff")
define ksa = Character("Kısa Saçlı Adam", color="#a6e7ff")
define usa = Character("Uzun Saçlı Adam", color="#a6e7ff")
define m = Character("Madison", color="#e6be8a")
define sa = Character("Savunma Avukatı", color="#00ced1")
define s = Character("Savcı", color="#a6e7ff")
define kb = Character("Kalabalıktan Biri", color="#c8ffc8")
define an = Character("Anna", color="#a6e7ff")
define ja = Character("Jake", color="#800000")
define a = Character("Amy", color="#ffe5b4")
define sally = Character("Sally", color="#a6e7ff")
define bob = Character("Bob", color="#c8ffc8")


transform rightcorner:
    xpos 1100 ypos 315

transform leftcorneremily:
    xpos 180 ypos 315

transform leftcorneremily2:
    xpos 120 ypos 182

transform leftcorner:
    xpos 180 ypos 195

transform leftcorneredward:
    xpos 180 ypos 207

transform leftcornerjake:
    xpos 180 ypos 202

transform rightcornerkevin:
    xpos 1100 ypos 195

transform rightcornerjoseph:
    xpos 1100 ypos 189

transform leftcornerjoseph:
    xpos 180 ypos 189

transform leftcorneruzunadam:
    xpos 180 ypos 182

transform rightcornermadison:
    xpos 1100 ypos 230

transform angrymadisoncorner:
    xpos 1100 ypos 239

transform leftcornermadison:
    xpos 180 ypos 230

transform rightcorneramy:
    xpos 1100 ypos 217

transform leftcorneramy:
    xpos 180 ypos 217

transform leftcorneranna:
    xpos 220 ypos 284

transform rightcorneranna:
    xpos 1220 ypos 284

transform leftcornersally:
    xpos 220 ypos 302

# The game starts here.
label start:

    scene blackbg with Fade(0.1, 0.1, 0.1)

    centered "I. Bölüm" with dissolve

    scene bg1 with Fade(0.1, 0.1, 3.0)

    $ renpy.music.set_volume(0.1,0,"music")
    play music "audio/music/emilysabah.mp3"

    show emily at rightcorner with easeinright
    e "Sıradan bir pazartesi günü daha. Hava güneşli ama bir tık soğuk ta"
    e "Bir dakka!!!"
    e "Bugün sıradan bir gün değildi! Lisenin ilk günü ve geç kalktım!"
    e "Ne yapacaktım? Evet düzgün kıyafet bulacaktım"
    hide emily    
    
    play sound "audio/sound/kirisik.mp3"

    "{i}{b}* Kırışık bir penye bulur."

    show emily at rightcorner with dissolve
    e "Böyle gidersem kötü görünürüm ama ütülersem de geç kalacağım, ne yapmalıyım?"
    hide emily

menu:

    "Ütüle": 
        jump utule

    "Giy Çık":
        jump giycik

    

label utule:

    show emily at rightcorner with dissolve
    e "İyi görünmem gerek! Herkes mükemmel kombinlerle gelicek"
    hide emily
    jump disari

label giycik:

    show emily at rightcorner with dissolve
    e "Geç kalıp herkesin önünde rezil olmaktansa biraz kırışık kıyafetten zarar gelmez"
    hide emily
    jump disari

label disari:

    scene bg2 with fade

    play sound "audio/sound/kosmak.mp3"

    show emily at rightcorner with dissolve
    e "Daha hızlı koşarsam yetişme şansım var!"
    hide emily

    play sound "audio/sound/carpmaomuz.mp3"

    "{i}{b}* Çarpar"

    show emily at rightcorner with dissolve
    e "A-Afedersin okula yetişmeye çalışıyordum"
    hide emily

    show kevin at leftcorner with easeinleft
    k "Sorun değil. Sen de mi Oswega Lisesi'ne gidiyorsun?"
    hide kevin

    show emily at rightcorner with dissolve
    e "Evet! Geç kalmamak için koşuyordum"
    hide emily 

    show kevin at leftcorner with dissolve
    k "İlk günü sorun edeceklerini düşünmüyorum"
    hide kevin

menu:

    "Yine de koş":
        jump yetis

    "Kevin ile yürü":
        jump yurukevin

label yetis:

    show emily at rightcorner with dissolve
    e "İlk günden öğretmenlerin gözünden düşmek istemiyorum"
    hide emily 

    show kevin at leftcorner with dissolve
    k "O zaman okulda görüşürüz"
    hide kevin

    show emily at rightcorner with dissolve
    e "Tamamdır güle güle!"
    hide emily

    scene bg3 with fade

    show emily at rightcorner with dissolve
    e "{i}(Düşündüğümden daha büyükmüş hemen içeri gireyim)"
    hide emily

    jump koridor

label yurukevin:

    $ kevinle = True

    show emily at rightcorner with dissolve
    e "Tamam beraber gidelim"
    hide emily

    scene bg3 with fade

    show emily at rightcorner with dissolve
    e "{i}(Okula kadar sessizce yürüdük. Sadece aynı sınıfta olduğumuzu öğrendim. Galiba pek konuşkan bir tip değil)"
    e "Bu lise düşündüğümden daha büyükmüş"
    hide emily

    show kevin at leftcorner with dissolve
    k "Evet öyle"
    hide kevin

menu:

    "Bu kadar suratsız olmana gerek yok":
        jump suratsiz

    "Hadi sınıfı bulalım":
        jump hadisinif

label suratsiz:

    show kevin at leftcorner with dissolve
    k "Haklısın"
    hide kevin 

    jump koridor

label hadisinif:

    show kevin at leftcorner with dissolve
    k "Tamam"
    hide kevin

    jump koridor

label koridor:

    scene bg4 with fade

    show emily at rightcorner with dissolve
    e "{i}(Sınıf koridorun başındaymış. Tuvaletlere uzak olması iyi oldu. O kokuyu solursam ölürüm)"
    hide emily

    jump sinif

label sinif:

    scene bg5 with fade

    show emily at rightcorner with dissolve
    if kevinle:
        e "Geç kaldığımız için özür dileriz"
    else:
        e "Geç kaldığım için özür dilerim"
    hide emily

    o "İlk gün olduğu için görmezden geleceğim"

    show emily at rightcorner with dissolve
    e "Teşekkürler"

    if kevinle:

        e "{i}(Arka ikili sıraya geçtik. Bu çocuk ya gizemli ya da aşırı sıradan biri)"
        hide emily

        menu:

            "Sıradan":
                jump siradan

            "Gizemli":
                jump gizemli

        label siradan:

            show emily at rightcorner with dissolve
            e "{i}(Muhtemelen sadece içine kapanık biri)"

            jump teneffus

        label gizemli:

            show emily at rightcorner with dissolve
            e "{i}(Belli etmediği birşeyler olduğunu hissediyorum)"

            jump teneffus

    else:

        hide emily
        menu:

            "Arka sıraya geç":
                jump arkasira

            "Ön sıraya geç":
                jump onsira

        label arkasira:

            show emily at rightcorner with dissolve
            e "{i}(Arkada iki boşluk var. Muhtemelen Kevin oturuyor)"
            hide emily

            "Birkaç dakika sonra kevin geldi"

            o "Geç kaldın"

            show kevinright at rightcornerkevin with dissolve
            k "Evet, geç kaldım. Üzgünüm"
            hide kevinright

            o "{i}{b}* İç çeker"
            o "Bugün ilk gün olduğu için içeri girebilirsin"

            show emily at rightcorner with dissolve

            jump teneffus

        label onsira:

            show edward at leftcorneredward with easeinleft
            g "{b}*Fısıldayarak*{/b} Hoş geldin. Adın ne?"
            hide edward

        menu:

            "Emily":
                jump tanisma

            "Kes sesini inek":
                jump asagilama

        label tanisma:

            show emily at rightcorner with dissolve
            e "Emily"
            hide emily

            show edward at leftcorneredward with dissolve
            ed "Ben de Edward. Memnun oldum"
            hide edward

            show emily at rightcorner with dissolve
            e "{i}(Çalışkan birine benziyor. Vee evet arkadaş canlısı)"

            jump teneffus

        label asagilama:

            show emilyserious at rightcorner with dissolve
            e "Kes sesini inek"
            e "{i}(Benim ligime yakın bile değil)"
            hide emilyserious

            show emily at rightcorner with dissolve

            jump teneffus


label teneffus:

    play sound "audio/sound/schoolbell.mp3"

    e "{i}(Ders sonunda bitti! Aceleyle çıktığım için tuvalete gitmemiştim)"
    hide emily

    jump tuvalet

label tuvalet:

    scene bg6 with fade

    z "Bana hediye vermek istemen çok güzel. Nakit hediye severim!"
    sk "L-lütfen beni yalnız bırak."

    "{i}{b}* Bir anda etraf kararır"

    scene bg7 with pixellate

    $ renpy.music.set_volume(0.1,0,"music")
    play music "audio/music/emilytuvaletvesonrasi.mp3"

    u "Direkt konuya gireceğim. Kaderinde az bir ömrün kaldı. Sana bir seçim sunacağım. Can alarak ömrünü uzatabileceğin bir seçim. Fırsat karşında. Sadece yap!!"

    show emilyscared at rightcorner with dissolve
    e "B-bu da ne? Bana neden geldin?"
    hide emilyscared

    u "Soruların cevapsız kalacak"

    show emilyscared at rightcorner with dissolve
    e "İ-istemiyorum benden uzak dur!"
    hide emilyscared

    u "Bu bir seçenek değil"

    show emilyserious at rightcorner with dissolve
    e "B-bunu yaparsam senden kurtulacak mıyım?"
    hide emilyserious

    u "Hayır. Ama ömrün uzayacak. Şimdi işe koyul!"

    "{i}{b}* Yerdeki falçatayı fark edersin."

menu:

    "Zorbayı öldür":
        jump oldurzorba

    "Şişman kızı öldür":
        jump oldurkiz

label oldurzorba:

    play channel1("audio/sound/sapla.mp3")
    e "{i}{b}* Falçatayı arkasını dönük zorbanın boğazına saplar. Çırpınmaya çalışan zorbayı tekrar tekrar deşer"
    stop channel1

    z "Gılkhııgggahh"
    sk "AAAAAAAAAAAA!!!"
    u "Tanrı merhametlidir. Ya da sadece öyle söylüyor. İstediğini yapabilir sonuçta"

    show emilyscared at rightcorner with dissolve
    e "{i}(N-ne?! Az önce ne oldu?! VE NEDEN OLDU! Buradan gitmem lazım!)"
    hide emilyscared

    scene bg4kalabalik with fade

    show emilyscared at rightcorner with dissolve
    e "{i}(Bütün koridor meraklı insanlarla dolmuş. Hemen herkese yaymış. Sanırım buraya kadarmış...)"
    hide emilyscared

    jump tojoseph
    
label oldurkiz:

    e "{i}{b}* Zorbayı kenara iter ve şişman kızın karnını falçatayla deşer. Şişman kız neye uğradığını şaşırır ve o anlayamadan içini dışına çıkarır"
    u "Tanrı merhametlidir. Ya da sadece öyle söylüyor. İstediğini yapabilir sonuçta."
    z "UZAK DUR BENDEN! SADECE PARA ALACAKTIM PSİKOPAT SÜRTÜK!"
    z "{i}{b}* Kaçar"

    show emilyscared at rightcorner with dissolve
    e "{i}(N-ne?! Az önce ne oldu?! VE NEDEN OLDU! Buradan gitmem lazım!)"
    hide emilyscared

    scene bg4 with fade

    show emilyserious at rightcorner with dissolve
    e "{i}(Anlaşılan korktuğundan kimseye söylememiş. Hızlıca eve gitmeliyim!)"
    hide emilyserious

    scene bg8 with fade

    show emilyangry at rightcorner with dissolve
    e "{i}(Kahretsin! Kafam çok karışık! Şimdi ömrüm uzadı mı? Ne kadar kalmıştı ki!?)"
    hide emilyangry

    u "Tebrik ederim. Hayatın artık daha geç son bulacak. Fakat daha fazla can lazım. Bunu yapabilecek misin?"

menu:

    "Sen nesin?":
        jump kimsin

    "Bunun başka bir yolu olmalı":
        jump baskayol

label kimsin:

    show emilyscared at rightcorner with dissolve
    e "Sen nesin?"
    hide emilyscared

    u "Soruya soruyla cevap verme. Bunu yapabilecek misin?"

menu:

    "Evet":
        jump evet

    "Hayır":
        jump hayir

label baskayol:

    show emilyserious at rightcorner with dissolve
    e "Bunun başka bir yolu olmalı"
    hide emilyserious

    u "Hayır. Başka bir yolu yok. Bunu yapabilecek misin?"

menu:

    "Evet":
        jump evet

    "Hayır":
        jump hayir

label evet:

    show emilyserious at rightcorner with dissolve
    e "Evet"
    hide emilyserious

    u "Kolay gelsin"

    jump uyu

label hayir:

    show emilyserious at rightcorner with dissolve
    e "Hayır"
    hide emilyserious

    u "Sana kalmış"

    jump uyu

label uyu:

    show emilyserious at rightcorner with dissolve
    e "Sadece yatmak istiyorum. Bunlar benim için çok fazla"
    hide emilyserious

    scene bg1 with Fade(2.0, 2.0, 3.0)

    show emilyserious at rightcorner with dissolve
    e "{i}(Okulda ceset bulunduğundan okula ara verildi. Hala midem bulanıyor. Ama yeni bir kurban bulmazsam ben öleceğim! Dışarı çıkmalıyım)"
    hide emilyserious

    scene bg2 with fade

    show emilyserious at rightcorner with dissolve
    e "{i}(Etrafta avcı gibi insan aradığıma inanamıyorum. Tek istediğim güzel bir lise hayatıydı. Bekle bekle bekle! İnanamıyorum! Bu fırsatı kaçırmamalıyım. Kör bir adam geçiyor. Yerde de baygın duran bir evsiz var)"
    hide emilyserious

menu:

    "Kör adamı öldür":
        jump oldurkor

    "Evsizi öldür":
        jump oldurevsiz

label oldurkor:

    show emilyserious at rightcorner with dissolve
    e "{i}(Peki nasıl yaklaşmalıyım?)"
    hide emilyserious

menu:

    "Üzerine koşarak git":
        jump ustunekoskor

    "Normal yürüyerek yaklaş":
        jump normalyurukor

label ustunekoskor:

    ka "Kim var orada?"

    show emilyscared at rightcorner with dissolve
    e "{i}(Siktir! Hızlıca kesip kaçmayı düşünüyordum ama herifin hisleri iyi çıktı. Şimdi saldırırsam kesin bağırır ve işim biter)"
    hide emilyscared
    show emilyserious at rightcorner with dissolve
    e "{b}*İç çekme*{/b} Sanırım biraz daha dolanmalıyım"
    hide emilyserious

    scene bg2 with Fade(1.0, 1.0, 1.0)

    "{i}{b}* 1 saat sonra"

    show emilyserious at rightcorner with dissolve
    e "Bacaklarım ağrımaya başladı sanırım eve gidip dinleni-"
    hide emilyserious

    play sound "audio/sound/carpma.mp3"
    tr "Biiiiipppppppp! {i}{b}*Çarpma"

    scene blackbg with Fade(7.0, 0.5, 0.5)

    u "Başaramadın zavallı şey"

    jump tojoseph

label normalyurukor:

    show emilyserious at rightcorner with dissolve
    e "{i}(Ona doğru sakince yürümeliyim)"
    hide emilyserious

menu:

    "Karnını deş":
        jump karnideskor

    "Boynunu deş":
        jump boynudeskor

label boynudeskor:

    e "{i}{b}* Kolumun rüzgarını hissetti ve bıçak adamın omzuna girdi"

    ka "AAAAAAAAAAAAAAHHHHHH!"

    show emilyscared at rightcorner with dissolve
    e "Hassiktir! Kaçmam lazım!"
    e "{i}(Sesi duyan insanlar polisi aramış ve beni kaçarken görenler varmış. Bende şans olsa bunlar başıma gelmezdi zaten. Yolun sonuna geldim bu yaşta)"
    hide emilyscared

    jump tojoseph

label karnideskor:

    play channel1("audio/sound/sapla.mp3")
    ka "Gooooghhhhkkkhigkkkk"
    
    stop channel1
    play sound "audio/sound/kan.mp3"
    "{i}{b}* Kan akma"

    e "{i}{b}* Seri ve kısa mesafeli bıçak darbeleriyle adam gıkını çıkaramadan bağırsaklarını çıkardım. Yere yığıldı ve muhtemelen birazdan ölüverir."

    show emily at rightcorner with dissolve
    e "{i}(Şimdi hızlı adımlarla eve gitme vakti)"
    hide emily

    scene bg9 with fade

    anne "Yemeğini ye kızıııım!"

    show emily at rightcorner with dissolve
    e "Aç değilim anne!"
    hide emily
    show emilyserious at rightcorner with dissolve
    e "{i}(Tüm bunları oturup baştan düşünmem lazım)"
    hide emilyserious

    u "Bu işe çoktan başladın geri dönüş yok"

    show emilyangry at rightcorner with dissolve
    e "ARTIK YETER DEĞİL Mİ!? BUNUN SON BULMASI LAZIM!"
    hide emilyangry

    u "Anneni kurban edersen neden olmasın?"

    show emilyserious at rightcorner with dissolve
    e "Hayır saçmalama! Herhangi birini öldürsem yetmeli. Lütfen..."
    hide emilyserious

    u "O zaman seçim yapma vaktin geldi. Annen mi yoksa sen mi?"

    show emilyserious at rightcorner with dissolve
    e "Lütfen bana bunu yaptırma..."
    hide emilyserious

    u "İkinizin de canı gitmesinden iyidir. Muhtemelen."

menu:

    "Kendimi öldüreceğim":
        jump kendinioldur

    "Annemi öldüreceğim":
        jump anneoldur

label kendinioldur:

    show emilyserious at rightcorner with dissolve
    e "Banyonun kapısını kilitledim ve kolumdaki tendonları kestim. Annem uyuduğuna göre kesin öleceğim"
    hide emilyserious

    u "Huzur bulma vaktin geldi. Kimse kaderinden kaçamaz."

    show emilyserious at rightcorner with dissolve
    e "{i}(Gerçekten huzur bu mu? Çok pişman hissediyorum. Ama geri dönüş yok)"
    hide emilyserious

    jump tojoseph

label anneoldur:

    u "Bencil varlık. Seni izliyor olacağım"

    scene bg10 with fade

    show emilyserious at rightcorner with dissolve
    e "Annem uyudu tam şimdi tam zamanı"
    e "Yatağına doğru sessizce yaklaştım. Ama..."
    hide emilyserious

menu:

    "Ya-yapamayacağım":
        jump yapamam

    "Buna mecburum":
        jump mecburum

label yapamam:

    show emilyangry at rightcorner with dissolve
    e "{i}(Bunların hiçbiri başıma gelmemeliydi. Hiç mantıklı değil! O yaratık beni kandırıyor! Daha fazla kan yok! Senden korkmuyorum pislik!)"
    hide emilyangry
    show emilyserious at rightcorner with dissolve
    e "{i}(Titremem durmuyor. Sadece uyumaya çalışacağım. Ve yarın normal bir hayat beni bekliyor olacak)"
    hide emilyserious

    scene bg1 with fade

    anne "Emilyyy! Ekmeğimiz bitmiş!"

    show emily at rightcorner with dissolve
    e "Ben alırım anne!"
    hide emily

    anne "Bu kızın içine ne girdi böyle? {b}* İç çekme.{/b} Umarım hep böyle kalır."

    scene bg2 with fade

    show emily at rightcorner with dissolve
    e "Sanırım bu kadarı yeterli olur. Annemle geçirdiğim vakit bile bana yeter. Sanırım fazla olgunlaştım. Yolda acaba ona abur cubur als-"
    hide emily

    play sound "audio/sound/fren.mp3"
    tr "{b}* Kamyon fren sesi."

    jump tojoseph

label mecburum:

    show emilyserious at rightcorner with dissolve
    e "Yastığını yüzüne bastırmaya başladım. {b}* Ağlamaklı{/b}"
    e "Yakında cennete gideceksin an-anne. Ha-hayatını kızın için fe-feda ediyorsun"
    hide emilyserious

    scene bg10 with fade

    show emilyserious at rightcorner with dissolve
    e "{i}(Çırpınma çoktan bitmiş. Ne kadar süredir buradayım. Sabah okula gitmeliyim. Okuldan gelince de polise bunu bildirirsem şüphe çekmem. Kimse boşuna ölmedi. Hayatımı hep iyilik yaparak yaşayacağım)"
    hide emilyserious

    $ emilylived = True

    jump tojoseph

label oldurevsiz:

    show emilyserious at rightcorner with dissolve
    e "{i}(Peki nasıl yaklaşmalıyım?)"
    hide emilyserious

menu:

    "Üzerine koşarak git":
        jump ustunekos

    "Normal yürüyerek yaklaş":
        jump normalyuru

label ustunekos:

    "{i}{b}* Üzerine koşarak git"

    jump evsiz2

label normalyuru:

    "{i}{b}* Normal yürüyerek yaklaş"

    jump evsiz2

label evsiz2:

    show emilyserious at rightcorner with dissolve
    e "{i}(Hiç beni duymuyor gibi)"
    hide emilyserious

menu:

    "Karnını deş":
        jump karnides

    "Boynunu deş":
        jump boynudes

label karnides:

    "{i}{b}* Karnını deş"
    jump des

label boynudes:

    "{i}{b}* Boynunu deş"
    jump des

label des:

    "{i}{b}* Bir anda evsiz Emily'nin kolunu kapar. Elindeki bıçağı alıp senin göğsüne defalarca saplar. Soğuyan vücudunu kenara itip oradan uzaklaşır"
    "{i}{b}* Emily yerde kanlar içinde kalır."

    show emilyserious at rightcorner with dissolve
    e "{i}(Kaybedecek bir şeyin kalmayınca bu kadar umursamaz oluyor insan demek)"
    hide emilyserious

    $ emilylived = False

    jump tojoseph


label tojoseph:

    scene blackbg with Fade(4.0, 0.1, 1.0)

    centered "II. Bölüm" with dissolve

    scene bg11 with Fade(0.1, 1.0, 3.0)

    play music "audio/music/josephbaslangic.mp3"

    show joseph at rightcornerjoseph with easeinright
    j "Baba oğul ve kutsal ruh adına"
    hide joseph

    scene bg12 with fade

    ska "Baba oğul ve kutsal ruh adına"
    ska "Affet beni baba günah işledim. En son bir ay önce geldim. Kocam küçük kızımızla bir gün gezmeye gitmişti ve markette kaybetmişti"
    ska "Bunu bana anlatmadı ve komşumdan duydum. Sonra da çok sinirlendim ve ona küfürler ettim. Kiliseye hiç gitmiyor ve onu ikna edemiyorum. Sinirlenince de maalesef hep küfür ediyorum"
    ska "Başka bir günde çimleri biçeceğine söz vermişti ama televizyon izlemeyi bırakmıyordu. Evet tekrar küfürler ettim"
    ska "Bana yalan söyledi. 5’ te eve geleceğini söylemişti ama 7’ de geldi. Ve tekrar sövdüm. İşlediğim günahlar bunlar baba"

    show joseph at rightcornerjoseph with dissolve
    j "Bu günahların affedilmesi için tekrarlamaman gerekli"
    hide joseph

    ska "Tekrar olmayacak. Teşekkür ederim"

    show josephangry at rightcornerjoseph with dissolve
    j "{i}(Sadece sövüyorum desene! Bu salaklar günah çıkartma adabını bir zahmet öğrenip gelmeliler!)"
    hide josephangry

    scene bg12 with fade

    show joseph at rightcornerjoseph with dissolve
    j "Baba oğul ve kutsal ruh adına"
    hide joseph

    show kisasac at leftcorneredward with easeinleft
    ksa "Baba oğul ve kutsal ruh adına"
    ksa "Kutsa beni baba günah işledim. En son iki ay önce geldim"
    ksa "{i}{b}* Liste çıkarır"
    ksa "23 kere yalan söylemek, 13 kere komşuya bağırmak, 7 kere zinayı düşünmek, 5 kere yabancılara küfür etmek, 3 kere işten kaytarmak"
    ksa "Ayrıca kimseye para yardımında da bulunmadım. İnsanlar iyilik istediklerinde konuyu değiştiriyorum. Ve be-"
    hide kisasac

    show joseph at rightcornerjoseph with dissolve
    j "Durabilirsin. İçtenlikle yaptığın yanlışları özetlemen yeterli. Ve pazar günleri kiliseye gelmeyi unutma"
    hide joseph

    show kisasac at leftcorneredward with dissolve
    ksa "Teşekkürler baba"
    hide kisasac

    show josephangry at rightcornerjoseph with dissolve
    j "{i}(Bu takıntılı ucubelerden de gına geldi! Bir rahibin bile sabrının sınırı vardır. Off.)"
    hide josephangry

    scene bg12 with fade

    show uzunadam at leftcorneruzunadam with easeinleft
    usa "Affet beni baba günah işledim. En son 6 sene önce geldim"
    usa "Peder ben b-en çaldım"
    usa "Yaşlı bir kadının birikimini çaldım. Çok pişmanım"
    usa "Küçük bir birikimdi. Geri de veremem çünkü artık bu dünyada değil"
    usa "O yüzden geldim"
    hide uzunadam

    show joseph at rightcornerjoseph with dissolve
    j "O miktarı bağışlayabilirsin. Bir daha yapmazsan tanrı neden affetmesin?"
    hide joseph

    show uzunadam at leftcorneruzunadam with dissolve
    usa "Gerçekten içime bir umut doldu!"
    hide uzunadam

    scene bg13 with pixellate

    play music "audio/music/josephetrafkararinca.mp3"

    u "Direkt konuya gireceğim. Kaderinde az bir ömrün kaldı. Sana bir seçim sunacağım. Can alarak ömrünü uzatabileceğin bir seçim. Fırsat karşında. Sadece yap!!"

    show joseph at rightcornerjoseph with dissolve
    j "{i}(Bu çok saçma! Şuan hala kilisedeyim. Bu nasıl oluyor böyle! Beni rahat bırak pis şeytan!)"
    hide joseph

    u "Sadece bir şeçim Joseph. Sadece bir seçim"

menu:

    "Hırsızı öldür":
        jump oldurhirsiz

    "Tanrıya sığın":
        jump sigin

label sigin:

    show joseph at rightcornerjoseph with dissolve
    j "Tanrım beni koru! Bana yardım et! Sen en merhametlisin! Bu vesveselerden beni kurtar!"
    hide joseph

    u "Ahh fazla sıkıcısın. Ben gidiyorum. Kalan hayatında bol şans"

    show joseph at rightcornerjoseph with dissolve
    j "Tanrım bana yardım edeceğini biliyordum! Bu bir işaretti! Senin yolunu asla bırakmayacağım! İnsanlara içtenlikle onları yargılamadan yardım edeceğim!"
    hide joseph

    scene bg14 with fade

    show joseph at rightcornerjoseph with dissolve
    j "Bugün çok yorucuydu. Dinlenmem lazım"
    hide joseph

    "{i}{b}* Sarhoş sürücü Joseph'e çarpar"
    play sound "audio/sound/carpma.mp3"

    show joseph at rightcornerjoseph with dissolve
    j "{i}(Yolundan olabildiğince gitmeye çalıştım. Tanrım günahlarımı affet)"
    hide joseph

    jump emilyjosephkarsilasma

label oldurhirsiz:

    show josephangry at rightcornerjoseph with dissolve
    j "{i}(Bugün sabrım taştı! Bu günahkarı cezalandıracağım!)"
    hide josephangry

    scene bg14 with fade

    j "{i}{b}* Arabaya biner."
    play sound "audio/sound/arackapi.mp3"
    j "{i}(Bundan gerçekten emin miyim?)"

menu:

    "Çarp":
        jump carp

    "Bırak":
        jump birak

label birak:

    show joseph at rightcornerjoseph with dissolve
    j "Ben ne düşünüyorum böyle? Sanırım yorgunluktan saçmalıyorum. Yola koyulayım"
    hide joseph

    play sound "audio/sound/carpma.mp3"
    "{i}{b}* Sarhoş sürücü Joseph'e çarpar"
    
    show joseph at rightcornerjoseph with dissolve
    j "{i}(Yolundan olabildiğince gitmeye çalıştım. Tanrım günahlarımı affet)"
    hide joseph

    jump emilyjosephkarsilasma

label carp:

    show josephangry at rightcornerjoseph with dissolve
    j "Cidden bu iki yüzlü herifi yeryüzünden silmek dünyaya bir iyilik olmalı!"
    hide josephangry

    play sound "audio/sound/carpma.mp3"
    j "{i}{b}* Yürüyen hırsıza çarpar"
    u "Gerçekten yaptın ha? Tanrı merhametlidir. Gerçi sen biliyorsundur. Sürekli tekrarlıyorsun sonuçta"

    show josephscared at rightcornerjoseph with dissolve
    j "{i}{b}* Nabzını kontrol eder"
    j "{i}(Buradan ayrılmam lazım)"
    play sound "audio/sound/fren.mp3"
    j "{i}{b}* Arabayla kaçar"
    hide josephscared

    $ josephlived = True

    jump emilyjosephkarsilasma

label emilyjosephkarsilasma:
    
    scene bg15 with fade

    if emilylived and josephlived:

        play sound "audio/sound/carpmaomuz.mp3"
    
        show emilyleft at leftcorneremily with dissolve
        e "Oh pardon"
        hide emilyleft

        show joseph at rightcornerjoseph with dissolve
        j "Sorun değil"
        j "{i}(Aynı anda kafamız billboarda döndü)"
        hide joseph

        scene merhamet2 with Fade(1.0, 0.1, 5.0)

        "Billboarddaki yazı: Tanrı merhametlidir."
        
        show emilyscaredleft at leftcorneremily with dissolve
        e "Ne? NE!?"
        hide emilyscaredleft

        show joseph at rightcornerjoseph with dissolve
        j "Dur! Neden böyle tepki veriyorsun? Başkalarıyla da bunların olma olasılığı ne kadar ki?"
        hide joseph
        
        show emilyseriousleft at leftcorneremily2 with dissolve
        e "Ş-şey ben geç kalmamalıyım!"
        hide emilyseriousleft

        show joseph at rightcornerjoseph with dissolve
        j "Bekle bir saniye! Seninle de konuştu dimi?"
        hide joseph

        show emilyseriousleft at leftcorneremily2 with dissolve
        e "Neyden bahsettiğinizi bilmiyorum"
        hide emilyseriousleft

        show joseph at rightcornerjoseph with dissolve
        j "O geldiğinde etraf kararıyor ve sesi insan ya da hayvan sesine benzemiyor"
        hide joseph

        show emilyscaredleft at leftcorneremily with dissolve
        e "Be-ben bil-bilmiyorum!"
        hide emilyscaredleft

        show joseph at rightcornerjoseph with dissolve
        j "Birbirimize yardım etmeliyiz! Belki aramızda konuşup bunu anlayabiliriz"
        hide joseph

        show emilyseriousleft at leftcorneremily2 with dissolve
        e "Sanırım"
        hide emilyseriousleft

        show joseph at rightcornerjoseph with dissolve
        j "Bu serginin kesinlikle bir bağlantısı olmalı bu tesadüf olamaz"
        hide joseph

        show emilyleft at leftcorneremily with dissolve
        e "O zaman vakit kaybetmeyelim"
        hide emilyleft

        jump tomadison

    elif josephlived:

        show joseph at rightcornerjoseph with dissolve
        j "{i}(Biraz dolanıp kafamı toparlamalıyım)"
        hide joseph

        scene merhamet1 with Fade(1.0, 1.0, 5.0)

        show josephscared at rightcornerjoseph with dissolve
        j "Hı? Bu billboard... olamaz, imkanı yok!"
        hide josephscared
        show joseph at rightcornerjoseph with dissolve
        j "Bu serginin kesinlikle bir bağlantısı olmalı bu tesadüf olamaz. Oraya hemen gidip bakmalıyım."
        hide joseph

        jump tomadison

    elif emilylived:

        show emilyserious at rightcorner with dissolve
        e "{i}(Ne kadar ömrüm kalmıştır? Muhtemelen çok uzadı çünkü bu zamanda yakalanmadan suç işlemek çok zor. Kafayı yiyeceğim ahhhh! O şeye hiç güvenmemem mi lazımdı?)"
        hide emilyserious

        scene merhamet1 with Fade(1.0, 1.0, 5.0)

        show emilyscared at rightcorner with dissolve
        e "(Ne? NE!? Bu resimdekiler yoksa? İ-inanamıyorum. Aklımı kaçırmadan önce gidip bir şeyler öğrenmeliyim)"
        hide emilyscared
    
        jump tomadison

    else:

        jump tomadison


label tomadison:

    scene blackbg with Fade(4.0, 0.1, 1.0)

    centered "III. Bölüm" with dissolve

    scene bg16 with Fade(0.1, 1.0, 3.0)

    play music "audio/music/madisonsaabah.mp3"

    m "Mahkemeyi Jake’ in duruşması için başlatıyorum"

    scene bg17 with fade

    sa "Savunma hazır sayın hakim"
    s "Savcılık hazır sayın hakim"
    "{i}{b}* Sanık ve tanıkların ifadeleri verildikten ve çapraz sorgulama yapıldıktan sonra,"

    s "Olayların özetini geçiyim"
    s "Sanık Jake Smith’ in karısı Lana Smith, kocasının işte olduğunu düşündüğünden Paul Johnson’ ı evlerinde cinsel ilişkiye girmek için çağırmış"
    s "Bu sırada Jake Smith Paul Johnson’ ın karısı Jane Johnson ile dışarıda eğleniyordu. 19.05’ te Jake Smith, karısının da ona mesaiye kalacağım demesi üzerine Jane Johnson’ ı evine davet etti"
    s " Eve vardıklarında aynı yatakta  Lana Smith ve Paul Johnson vardı. Bu yüzden Paul Johnson karnına üç el ateş edilerek öldürüldü"
    s "Silah seslerini etraftakiler 19.30 civarı duyduklarını söylediler. Silahta Jake Smith’ in parmak izleri bulunuyor ve ruhsatı da onun üzerine"
    s "Olaydan sonra  Lana Smith polisi aradı ve Jane Johnson’ ın çantasından kocasının silahını çıkarıp Paul Johnsonı vurduğunu söyledi. Jake Smith’ te ifadesinde aynısını söyledi"
    s "Jane Johnson,  Jake Smith’ in Paul Johnsonı vurduğunu söyledi"
    
    kb "Jane kocasına sinirlenip vurdu mu yoksa lana kocasını savunmak için yalan mı söylüyor?"
    kb "Ama çantasına nasıl Jake’ in silahı girdi? Bana arabadayken alıp çantasına atması pek inandırıcı gelmedi"
    kb "Lana kocası hapisten çıkınca onu da öldürür diye gerçeği saklıyor da olabilir"

    show madisonangry at angrymadisoncorner with easeinright
    m "Mahkemede sessizlik!"
    hide madisonangry

    sa "Jake Smith karısı onu aldattı diye birisini öldürecek bir kişi değil. Yaptığı bağışları size göst-"
    s "İtiraz ediyorum! Konuyu çarpıtmaya çalışıyor"

    show madison at rightcornermadison with dissolve
    m "İtiraz kabul edildi. Az önce anlattıklarınızın konuyla alakası yoktu. Tanığa başka sorunuz var mı?"
    hide madison

    sa "Hayır sayın hakim. Fakat daha fazla delil bulunabileceğinden karardan önce vakit talep ediyoruz"
    s "İtiraz ediyorum! Her şey gün gibi ortada! Karar şimdi verilmeli sayın hakim"

    show madison at rightcornermadison with dissolve
    m "Reddedildi. Tam olarak her şey iki günde anlaşılabilecekse mahkeme ertelenecek"
    hide madison

    sa "Kabul ediyoruz sayın hakim"

    show madison at rightcornermadison with dissolve
    m "Pekala. Davanın karar verilmesini iki gün sonraya erteliyorum"
    m "{i}(Muhtemelen Jake katil. Ama eldivenli bir şekilde Jane’ in kurbanı vurmadığı da belli değil. Kesin bir kanıt üzerine karar vermeliyim)"
    hide madison

    "{i}{b}* 2 gün sonra"

    sa "Mahkemeye o saatte çekilen sokak kamera görüntülerini sunuyoruz"

    show madison at rightcornermadison with dissolve
    m "Davayı etkileyecek bir şey olabilir. Mahkeme görüntüleri kanıt olarak kabul ediyor"
    hide madison

    s "Bu videoda arabayla Jake Smith ve Jane Johnson’ ın gelişini ve içeri girişini gördük. Bunu zaten biliyoruz"
    sa "Fakat iki şeyi kaçırıyorsunuz. Paul Johnson’ ın arabası park halinde. Bunu gören Jake Smith hızlıca eve giriyor. Ama Jane Johnson arabadan daha sonra iniyor"
    sa "O sırada silahı çantasına atmış olmalı. Kocasının onu aldatması gururuna dokundu ve intikam aldı"

    show madison at rightcornermadison with dissolve
    m "Savcılığın diyeceği bir şey var mı?"
    hide madison
    
    s "Ihh... Hayır, sayın hakim"

    show madison at rightcornermadison with dissolve
    m "{i}(Gömleğinin aşağısındaki bel tarafındaki çıkıntıyı anlaşılan sadece ben fark ettim. 8 yıllık hakimlik tecrübeme dayanarak kesinlikle Jake silahı getirdi ve bu konuda yalan söylediğinden muhtemelen o vurdu.)"
    hide madison

    scene bg18 with pixellate

    u "Direkt konuya gireceğim. Kaderinde az bir ömrün kaldı. Sana bir seçim sunacağım. Can alarak ömrünü uzatabileceğin bir seçim. Fırsat karşında. Sadece yap!!"

    show madisonangry at angrymadisoncorner with dissolve
    m "Bu nasıl bir şaka böyle!? Şuanda ciddi bir duruşmanın ortasındayız! Bu saçmalığın sorumluları heme-"
    hide madisonangry
    show madison at rightcornermadison with dissolve
    m "Ha? Etraf boş sadece ben ve şu ses var. Sanırım halüsinasyon görmeye başladım"
    hide madison

    u "İnanmanı umursamıyorum. Dediğim gibi seçim senin"

menu:

    "Suçlu bul ve hapse gönder":
        jump sucla

    "Suçlu bulma ve dışarıda onu öldür":
        jump suclama

label sucla:

    show madison at rightcornermadison with dissolve
    m "{i}(En yakın zamanda doktora gitmeliyim. Adalet anlayışımın ne kadar güçlü olduğunu bilincim nasıl bilmiyor? Her neyse...)"
    m "Sanığın suçlu olduğuna karar verildi. Kasten adam öldürme suçundan ve 21 yaşın üzerinde olduğundan ömür boyu hapse mahkum edildi. Dava kapanmıştır"
    hide madison

    scene bg20 with fade

    "{i}{b}* Geri dönerken"

    show madison at rightcornermadison with dissolve
    m "Gerçekten yaşlanıyorum. Her yerim ağrıyor ve tuhaf şeyler görmeye başladım. Neyse kızım beni bekliyordur"
    hide madison

    m "{i}{b}* Okuldan kızımı aldım ve eve geçtik"

    scene bg19 with fade

    show annaleft at leftcorneranna with easeinleft
    an "Anneciğim karnım acıktı"
    hide annaleft

    show madison at rightcornermadison with dissolve
    m "Buzdolabında yemek var, ısıtayım canım"
    hide madison

    show annaleft at leftcorneranna with dissolve
    an "Merak etme anneciğim! Sen yorgunsundur. Kendim yaparım"
    hide annaleft

    show madisonhappy at rightcornermadison with dissolve
    m "Aferin akıllı kızıma. Ben bir üstümü değiştireyim"
    hide madisonhappy

    show annaleft at leftcorneranna with dissolve
    an "Tamam anneciğim!"
    hide annaleft

    show madison at rightcornermadison with dissolve
    m "{i}(O da olmaza cidden çok yalnız hissederdim..." 
    m "{i}Ah baya yorgunum. Biraz kestireceğim sanırım. Yarın bir işim yok zaten.)"
    hide madison

    scene bg21 with fade

    "{b}- Gece Yarısı"
    
    play sound "audio/sound/tikirti.mp3"
    "{i}{b}* Tıkırtı"

    show madisonscared at rightcornermadison with dissolve
    m "Bu seste ne? Anna? Annnnaaaa? Bu kızın niye sesi çıkmıy- ahh!"
    play sound "audio/sound/carpmaomuz.mp3"
    m "{i}(Sırtımda çok fena bir acı hissediyorum. Ne? Kan mı? {b}* Yere düşer.{/b}"
    m "O ses gerçekti yani. Başkasının adaleti için canım ha? Umarım doğru kararı vermişimdir. Umarım Anna iyidir...)"
    hide madisonscared

    jump toamy

label suclama:
    
    show madison at rightcornermadison with dissolve
    m "{i}(Bu pislik zaten bir katil. Adaleti gerçek anlamda sağlamış olacağım. Ve ömrümü şansa bırakmayacağım)"
    hide madison

    scene bg17 with fade

    show madison at rightcornermadison with dissolve
    m "Sanığın suçsuz olduğuna karar verildi. Arabadan geç çıkması ve içeri girdikten sonra atış sesi gelmesi sebebiyle..."
    m "Jane Johnson kasten adam öldürme suçundan ve 21 yaşın üzerinde olduğundan ömür boyu hapse mahkum edildi. Dava kapanmıştır"
    hide madison

    scene bg20 with fade

    show madison at rightcornermadison with dissolve
    m "{i}(Mahallesine kadar onu takip ettim. Kafayı çekerek tek başına ıssız bir yerde kutlama yapıyor)"
    hide madison

    show jake at leftcornerjake with easeinleft
    ja "Bundan beraat yediğime inanamıyorum! Hayatımdaki tüm şansı kullanmış olmalıyım"
    hide jake

    show madison at rightcornermadison with dissolve
    m "Evet bay Smith öyle oldu"
    hide madison

    show jake at leftcornerjake with dissolve
    ja "Efendim suçsuz kişi olduğumu o karmaşada anladınız, gerçekten harikası-"
    hide jake

    show madison at rightcornermadison with dissolve
    m "Yalakalığı bırak. Senin yaptığını anladım serseri"
    hide madison

    show jake at leftcornerjake with dissolve
    ja "Ha?! O zaman neden bunu yaptınız?"
    hide jake

    play music "audio/music/madisonkillvesonrasi.mp3"

    show madison at rightcornermadison with dissolve
    m "{i}{b}* Silahı çıkarır. {/i}{/b}Tabi ki de adalet için"

    play sound "audio/sound/silah.mp3"

    m "{i}{b}* Kafaya tek temiz"
    hide madison

    u "Tanrı merhametlidir. Ya da sadece öyle söylüyor. İstediğini yapabilir sonuçta"

    show madison at rightcornermadison with dissolve
    m "Sıvışma vakti"
    hide madison
    
    "{i}{b}* Eve giderken"

    show madison at rightcornermadison with dissolve
    m "Silahımın bir gün işe yarayacağını hiç düşünmemiştim. Eve gitmeliyim"
    hide madison

    scene bg22 with fade

    show madison at rightcornermadison with dissolve
    m "{i}{b}*Arabayla eve dönerken sokakta kızım ve onun öğretmenini gördüm"
    hide madison

    play sound "audio/sound/aracdurma.mp3"

    show amyleft at leftcorneramy with easeinleft
    a "Hey! İyi günler.{i}{b}* Arabadan iner"
    hide amyleft

    play sound "audio/sound/arackapi.mp3"

    show annaleft at leftcorneranna with dissolve 
    an "{b}*Hüzünlüce*{/b} A-anne"
    hide annaleft

    show madison at rightcornermadison with dissolve
    m "Ne oldu canım? Okulda kavga mı ettin?"
    hide madison

    show amyleft at leftcorneramy with dissolve
    a "İki çocuk onunla dalga geçiyordu. Sizinle ayrıntılı bir şekilde konuşmam gerekliydi. O yüzden beraber evinize doğru gidiyorduk"
    hide amyleft

    show madison at rightcornermadison with dissolve
    m "Hmm. Anlıyorum. Bir zorbalık meselesi mi? Yoksa oyuncak paylaşamadıl-"
    hide madison
    show madisonscared at rightcornermadison with dissolve
    m "Huh? O billboardda ne? Nasıl oluyor da?"
    hide madisonscared

    if emilylived and josephlived:

        scene merhamet4 with fade

    elif emilylived:

        scene merhamet3 with fade

    elif josephlived:

        scene merhamet3 with fade

    else:

        scene merhamet2 with fade

    show madison at rightcornermadison with dissolve
    m "{i}(Öğretmen de oraya dikkatlice bakıyor...)"
    m "Evimiz zaten yakın. İsterseniz burada bekleyin Anna’ yı eve bırakıp hemen geliyim. Bir kafede oturup konuşalım"
    hide madison

    show amyleft at leftcorneramy with dissolve
    a "Peki bayan bekliyor olacağım"
    hide amyleft

    scene bg19 with fade

    "{i}{b}* Eve varınca"

    show annaleft at leftcorneranna with dissolve
    an "Anne sana bir şey demeliy-"
    hide annaleft

    show madison at rightcornermadison with dissolve
    m "Şimdi olmaz tatlım. Hocanla konuşmam lazım. Ayrıca beni dışarıda bekliyor. Bekletmek ayıptır"
    m "{b}* Evden çıkıp arabama bindim"
    play sound "audio/sound/arackapi.mp3"
    m "Anna tüm ömür kavgalarla geçer. Bugünlük kendimi düşünmeliyim kızım"
    hide madison 

    "{i}{b}* 5dk sonra"

    show madison at rightcornermadison with dissolve
    m "{b}* Billboardın oraya vardım"
    hide madison

    play sound "audio/sound/aracdurma.mp3"

    scene bg22 with fade

    show madison at rightcornermadison with dissolve
    m "Bu tesadüf olamaz. Oraya dikkatle baktınız. Peki ne ilginizi çekti?"
    m "{i}(O da mı benim gibi? Sanırım anlamanın tek bir yolu var)"
    m "Tanrı merhametlidir. Bu cümle size bir şeyler hatırlatıyo-"
    hide madison

    show amyleft at leftcorneramy with dissolve
    a "Pekala anlaşılan sizde bir şeyler yaşadınız. Bunu şansa bırakmamak için derinlemesine araştırmayı öneri-"
    hide amyleft

    show madison at rightcornermadison with dissolve
    m "Hadi gidelim. Atla"
    hide madison

    $ madisonlived = True

    jump toamy

label toamy:
    
    scene blackbg with Fade(4.0, 0.1, 1.0)

    centered "IV. Bölüm" with dissolve

    scene bg23 with Fade(0.1, 1.0, 3.0)

    play music "audio/music/amyhepbu.mp3"

    show amyangry at rightcorneramy with dissolve
    a "Sessiz oluuun!"
    hide amyangry
    show amy at rightcorneramy with dissolve
    a "3+3 kaç eder? Cidden kimse mi bilmiyor?"
    hide amy
    
    show sallyleft at leftcornersally with easeinleft
    sally "Zaten dersin bitmesine az kaldı bizi rahat bırakın lütfen"
    hide sallyleft

    show amy at rightcorneramy with dissolve
    a "Benim işim bu sally. Cevap nedir?"
    hide amy

    bob "6 mı öğretmenim?"

    show amy at rightcorneramy with dissolve
    a "Aferin Bob! Cevabı biliyorsan bir dahakine sorulunca söyle"
    hide amy

    bob "Tamam"

    play sound "audio/sound/schoolbell.mp3"

    show amy at rightcorneramy with dissolve
    a "Ödevlerinizi yapmayı unutmayın!"
    hide amy

    scene bg24 with pixellate

    u "Direkt konuya gireceğim. Kaderinde az bir ömrün kaldı. Sana bir seçim sunacağım. Can alarak ömrünü uzatabileceğin bir seçim. Fırsat karşında. Sadece yap!!"
    
    show amyangry at rightcorneramy with dissolve
    a "Ne sikim oluyor böyle? Zaten sinirlerim tepemde. Bundan ceza almadan durdurun çocuklar!"
    hide amyangry

    u "Etrafına bir bak. Bu gerçek. Oyalanma ve gerekeni yap"

    show amyangry at rightcorneramy with dissolve
    a "{i}(Ananı sikiyim! Bu nasıl bir lanet amına koyim!? Beni sevmeyen çok kişi varda hangisi büyü yapıcak kadar ileri gider ki?!)"
    a "{i}(Her neyse, onu sonra bulacağım. İlk kelleyi kurtaralım. Şu çocuğa uzun zamandır gıcık oluyordum zaten)"
    hide amyangry

    scene bg23 with fade

    show amy at rightcorneramy with dissolve
    a "Sen bekle sally! Konuşmamız gerek"
    hide amy

    show sallyleft at leftcornersally with dissolve
    sally "Off tamam"
    hide sallyleft

    show amy at rightcorneramy with dissolve
    a "Gel çatıda konuşalım"
    hide amy

    show sallyleft at leftcornersally with dissolve
    sally "Ne alaka ya?"
    hide sallyleft

    show amyangry at rightcorneramy with dissolve
    a "{i}(Seni şımarık velet! Bana karşı geliyor! Heh yakında yarra yiyceksin.)"
    hide amyangry
    show amy at rightcorneramy with dissolve
    a "Biraz hava almak için sally. Hadi sakince konuşalım"
    hide amy

    show sallyleft at leftcornersally with dissolve
    sally "Öff. Peki hızlı olsun"
    hide sallyleft

    show amyhaha at rightcorneramy with dissolve
    a "{i}(Hızlı olacak Sally)"
    hide amyhaha

    scene bg25 with fade

    show sallyleft at leftcornersally with dissolve
    sally "Artık ders saatleri geçti. Ne diyeceksen çabuk söyl-"
    hide sallyleft

    play sound "audio/sound/dusmesesi.mp3"
    show amy at rightcorneramy with dissolve
    a "{b}* Aşşağı doğru ittim ve çakıldı. Arka tarafa attığımdan ve okulda insan kalmadığından kimse görmedi"
    hide amy

    u "Tanrı merhametlidir. Ya da sadece öyle söylüyor. İstediğini yapabilir sonuçta"

    show amyhaha at rightcorneramy with dissolve
    a "{i}(Hah. Hahahahahaha. Çok kolaydı. Garip derecede çok kolaydı. Ailesinden dayak yiyen çocuk dayanamayıp intihar etti!)"
    a "{i}(Gazeteciler bana bu mükemmel manşet için teşekkür etmeli. Muhtemelen okulu polisler bir süre kapatır. Dikkat çekmeden gideyim)"
    hide amyhaha
    if madisonlived:

        show annaleft at leftcorneranna with dissolve
        an "Öğ-öğretmenim?"
        hide annaleft

        show amyangry at rightcorneramy with dissolve
        a "Anna, sen zeki bir çocuksun. Bunu herhangi birine söylersen neler olacağını tahmin edebilirsin. Hadi seni eve bırakıyım. Emin olmak önemlidir değil mi?"
        hide amyangry

        show annaleft at leftcorneranna with dissolve
        an "{b}*Titreyerek*{/b} Ta-tamam."
        hide annaleft
        
        show amy at rightcorneramy with dissolve
        a "Hey. Hadi ama. Neşelen! O sen de olabilirdin. Ayrıca kendini annenin yanında kontrol etmezsen"
        hide amy

        show annaleft at leftcorneranna with dissolve
        an "{b}*Daha çok titremeye başlar*{/b}"
        hide annaleft

        show amy at rightcorneramy with dissolve
        a "Sanırım bir şey söylememe gerek yok"
        hide amy

        show anna at rightcorneranna with dissolve
        an "{b}*Ağlaması biter ve yola çıkarsınız*{/b}"
        hide anna

        scene bg22 with fade

        play sound "audio/sound/aracdurma.mp3"

        show madisonhappyleft at leftcornermadison with dissolve
        m "Hey! İyi günler bayan Williams. {b}*Arabadan iner*{/b}"
        hide madisonhappyleft

        play sound "audio/sound/arackapi.mp3"

        show anna at rightcorneranna with dissolve
        an "{b}*Hüzünlüce*{/b}  A-anne"
        hide anna

        show madisonleft at leftcornermadison with dissolve
        m "Ne oldu canım? Okulda kavga mı ettin?"
        hide madisonleft

        show amy at rightcorneramy with dissolve
        a "İki çocuk onunla dalga geçiyordu. Sizinle ayrıntılı bir şekilde konuşmam gerekliydi. O yüzden beraber evinize doğru gidiyorduk"
        hide amy

        show madisonleft at leftcornermadison with dissolve
        m "Hmm. Anlıyorum. Bir zorbalık meselesi mi? Yoksa oyuncak paylaşamadıl-"
        hide madisonleft
        show madisonscaredleft at leftcornermadison with dissolve
        m "Huh? O billboardda ne? Nasıl oluyor da?"
        hide madisonscaredleft

        show amy at rightcorneramy with dissolve
        a "{i}(Ne var ki billboardda? Aha! Bu suretler... benim gibi başkaları da var demektir bu)"
        hide amy

        show madisonleft at leftcornermadison with dissolve
        m " Evimiz zaten yakın bayan Williams. İsterseniz burada bekleyin Anna’ yı eve bırakıp hemen geleyim. Bir kafede oturup konuşalım"
        hide madisonleft

        show amy at rightcorneramy with dissolve
        a "{i}(O da anladı muhtemelen. bir hakimin bunu yapacağını kim düşünürdü ki?)"
        a "Peki bayan bekliyor olacağım"
        hide amy
        show amyangry at rightcorneramy with dissolve
        a "{i}(O küçük orospu kontrolünü kaybedip olanları söylemez umarım. Ahhh çok sinir bozucu!)"
        hide amyangry

        "{i}{b}* 5dk sonra"

        "{b}* Billboardın oraya geldi"

        show madisonleft at leftcornermadison with dissolve
        m "Bu tesadüf olamaz. Oraya dikkatle baktınız. Peki ne ilginizi çekti?"
        m "{i}(O da mı benim gibi? Sanırım anlamanın tek bir yolu var)"
        m "Tanrı merhametlidir. Bu cümle size bir şeyler hatırlatıyo-"
        hide madisonleft

        show amy at rightcorneramy with dissolve
        a "Pekala anlaşılan sizde bir şeyler yaşadınız. Bunu şansa bırakmamak için derinlemesine araştırmayı öneri-"
        hide amy

        show madisonleft at leftcornermadison with dissolve
        m "Hadi gidelim. Atla"
        hide madisonleft

    else:

        scene bg22 with fade

        show amy at rightcorneramy with dissolve
        a "Kafam baya karıştı. Şimdi ne olması gerekiyor acaba?"
        hide amy

        if emilylived and josephlived:
            scene merhamet3 with fade
        
        elif emilylived:
            scene merhamet2 with fade

        elif josephlived:
            scene merhamet2 with fade
        
        else:
            scene merhamet1 with fade

        show amy at rightcorneramy with dissolve
        a "Hadi canım! Tanrı merhamet edenlerin yanında. Bu sergi kesinlikle benimle alakalı. Oraya gitmeliyim"
        hide amy

        jump lastpart


label lastpart:

    scene blackbg with Fade(4.0, 0.1, 1.0)

    centered "V. Bölüm" with dissolve

    scene bg26 with Fade(0.1, 1.0, 3.0)

    play music "audio/music/sonpart.mp3"

    if emilylived and josephlived and madisonlived:

        show emilyleft at leftcorneremily with dissolve
        e "Burası düşündüğümden büyükmüş"
        hide emilyleft

        show joseph at rightcornerjoseph with dissolve
        j "Odaklan"
        hide joseph

        show emilyseriousleft at leftcorneremily2 with dissolve
        e "Tamam tamam"
        hide emilyseriousleft

        show amy at rightcorneramy with fade
        a "İşte geldik"
        hide amy

        show madisonleft at leftcornermadison with dissolve
        m "Acele et"
        hide madisonleft

        scene bg27 with fade
        
        "{i}{b}* 4 katil o tablonun önünde karşılaşır"

        show emily at rightcorner with dissolve
        e "Merhabalar. Bakıyorum da bu tabloya ilgilisiniz"
        hide emily

        show josephangryleft at leftcornerjoseph with dissolve
        j "Şşt ne yapıyorsun? Dikkat çekme çocuk"
        hide josephangryleft

        show amy at rightcorneramy with dissolve
        a "Bizimle mi konuştunuz?"
        hide amy

        show josephleft at leftcornerjoseph with dissolve
        j "E-evet. Kızımla bu işlerde yeniyiz. Sanattan anlayan kadınlara benziyorsunuz. Bu tabloda ne görüyorsunuz?"
        hide josephleft
        
        scene merhamet4 with fade

        show amy at rightcorneramy with dissolve
        a "Aslında arkadaşımla bende yeniyiz. Fakat acı bir şeyler anlattığı kesin"
        hide amy

        show emilyseriousleft at leftcorneremily2 with dissolve
        e "Ama bir tabloya neden yazı yazılır ki?" 
        hide emilyseriousleft

        show madison at rightcornermadison with dissolve
        m "Bence acı bir resim olduğundan merhamet kelimesi ironi yapıyor"
        hide madison

        show kisasac at leftcorneredward with easeinleft
        ksa "İnsanlar ne meraklı varlıklar böyle. Hem zayıf hem de kibirli olabilen tek varlık"
        hide kisasac

        show amy at rightcorneramy with dissolve
        a "Affedersiniz siz kimsi-"
        hide amy

        show kisasac at leftcorneredward with dissolve
        ksa "Bu tablonun artistiyim. Aslında sadece ileticisiyim denebilir. Bu resmi yapan sizsiniz"
        ksa "Ömrünüzün ne kadar uzadığını düşündünüz? 1 ay? 1 yıl? Belki 10?"
        hide kisasac

        scene blackbg with Fade(5.0, 0.1, 1.0)

        "{i}{b}* Etraf simsiyah olur, deprem olmaya başlar"

        play channel1("audio/sound/deprem.mp3")
        
        u "Hahahaha! İnsanların gerçekten kaderi bu denli değiştirmeye yetecek kadar değerli olduğunu mu sandınız? Güzel bir deney oldu. Ama her güzel şeyin bir sonu vardır"

        show emilyscared at rightcorner with dissolve
        e "Ne, ne, ne, ne, ne, ne, ne!"
        hide emilyscared

        show amyleft at leftcorneramy with dissolve
        a "Hassiktir!"
        hide amyleft

        show josephscared at rightcornerjoseph with dissolve
        j "Ahhhhhhhh! Hayıııırrrr!"
        hide josephscared

        show madisonscaredleft at leftcornermadison with dissolve
        m "Buradan hemen çıkmamız lazı-"
        hide madisonscaredleft

        stop channel1

        "{i}{b}* Bina Yıkılır"

        jump son

    elif josephlived and madisonlived:

        show joseph at rightcornerjoseph with dissolve
        j "Odaklanmalıyım"
        hide joseph

        show amyleft at leftcorneramy with dissolve
        a "İşte geldik"
        hide amyleft

        show madison at rightcornermadison with dissolve
        m "Acele et"
        hide madison

        scene bg27 with fade
        
        "{i}{b}* 3 katil o tablonun önünde karşılaşır"

        show josephleft at leftcornerjoseph with dissolve
        j "Buldum! 2 kişi daha var burada"
        hide josephleft

        show amy at rightcorneramy with dissolve
        a "Eee? Tabloyu bulduk. Şimdi ne yapacağız?"
        hide amy

        scene merhamet3 with fade

        show madison at rightcornermadison with dissolve
        m "Bilmiyorum. Belki biraz daha incelersek ipucu bulabili-"
        hide madison

        show kisasac at leftcorneredward with easeinleft
        ksa "İnsanlar ne meraklı varlıklar böyle. Hem zayıf hemde kibirli olabilen tek varlık"
        hide kisasac

        show amy at rightcorneramy with dissolve
        a "Affedersiniz siz kimsi-"
        hide amy

        show kisasac at leftcorneredward with dissolve
        ksa "Bu tablonun artistiyim. Aslında sadece ileticisiyim denebilir. Bu resmi yapan sizsiniz"
        ksa "Ömrünüzün ne kadar uzadığını düşündünüz? 1 ay? 1 yıl? Belki 10?"
        hide kisasac

        scene blackbg with Fade(5.0, 0.1, 1.0)

        "{i}{b}* Etraf simsiyah olur, deprem olmaya başlar"

        play channel1("audio/sound/deprem.mp3")

        u "Hahahaha! İnsanların gerçekten kaderi bu denli değiştirmeye yetecek kadar değerli olduğunu mu sandınız? Güzel bir deney oldu. Ama her güzel şeyin bir sonu vardır"

        show amyleft at leftcorneramy with dissolve
        a "Hassiktir!"
        hide amyleft

        show josephscared at rightcornerjoseph with dissolve
        j "Ahhhhhhhh! Hayıııırrrr!"
        hide josephscared

        show madisonscaredleft at leftcornermadison with dissolve
        m "Buradan hemen çıkmamız lazı-"
        hide madisonscaredleft

        stop channel1

        "{i}{b}* Bina Yıkılır"

        jump son

    elif emilylived and madisonlived:

        show emilyserious at rightcorner with dissolve
        e "Demek burası"
        hide emilyserious

        show amyleft at leftcorneramy with dissolve
        a "İşte geldik"
        hide amyleft

        show madison at rightcornermadison with dissolve
        m "Acele et"
        hide madison

        scene bg27 with fade

        "{i}{b}* 3 katil o tablonun önünde karşılaşır"

        show emilyseriousleft at leftcorneremily2 with dissolve
        e "Buldum! 2 kişi daha var burada"
        hide emilyseriousleft

        show amy at rightcorneramy with dissolve
        a "Eee? Tabloyu bulduk. Şimdi ne yapacağız?"
        hide amy

        scene merhamet3 with fade

        show madison at rightcornermadison with dissolve
        m "Bilmiyorum. Belki biraz daha incelersek ipucu bulabili-"
        hide madison

        show kisasac at leftcorneredward with easeinleft
        ksa "İnsanlar ne meraklı varlıklar böyle. Hem zayıf hemde kibirli olabilen tek varlık"
        hide kisasac

        show amy at rightcorneramy with dissolve
        a "Affedersiniz siz kimsi-"
        hide amy

        show kisasac at leftcorneredward with dissolve
        ksa "Bu tablonun artistiyim. Aslında sadece ileticisiyim denebilir. Bu resmi yapan sizsiniz"
        ksa "Ömrünüzün ne kadar uzadığını düşündünüz? 1 ay? 1 yıl? Belki 10?"
        hide kisasac

        scene blackbg with Fade(5.0, 0.1, 1.0)

        "{i}{b}* Etraf simsiyah olur, deprem olmaya başlar"

        play channel1("audio/sound/deprem.mp3")

        u "Hahahaha! İnsanların gerçekten kaderi bu denli değiştirmeye yetecek kadar değerli olduğunu mu sandınız? Güzel bir deney oldu. Ama her güzel şeyin bir sonu vardır"

        show emilyscared at rightcorner with dissolve
        j "Ne, ne, ne, ne, ne, ne, ne!"
        hide emilyscared

        show amyleft at leftcorneramy with dissolve
        a "Hassiktir!"
        hide amyleft
        
        show madisonscaredleft at leftcornermadison with dissolve
        m "Buradan hemen çıkmamız lazı-"
        hide madisonscaredleft

        stop channel1

        "{i}{b}* Bina Yıkılır"

        jump son

    elif emilylived and josephlived:

        show emilyleft at leftcorneremily with dissolve
        e "Burası düşündüğümden büyükmüş"
        hide emilyleft

        show joseph at rightcornerjoseph with dissolve
        j "Odaklan"
        hide joseph

        show emilyseriousleft at leftcorneremily2 with dissolve
        e "Tamam tamam"
        hide emilyseriousleft

        show amy at rightcorneramy with fade
        a "Sonunda vardım"
        hide amy

        scene bg27 with fade
        
        "{i}{b}* 3 katil o tablonun önünde karşılaşır"

        show emily at rightcorner with dissolve
        e "Merhabalar. Bakıyorum da bu tabloya ilgilisiniz"
        hide emily

        show josephangryleft at leftcornerjoseph with dissolve
        j "Şşt ne yapıyorsun? Dikkat çekme çocuk"
        hide josephangryleft

        show amy at rightcorneramy with dissolve
        a "Benimle mi konuştunuz?"
        hide amy

        show josephleft at leftcornerjoseph with dissolve
        j "E-evet. Kızımla bu işlerde yeniyiz. Sanattan anlayan birine benziyorsunuz. Bu tabloda ne görüyorsunuz?"
        hide josephleft
        
        scene merhamet3 with fade

        show amy at rightcorneramy with dissolve
        a "Aslında bende yeniyim. Fakat acı bir şeyler anlattığı kesin"
        hide amy

        show emilyseriousleft at leftcorneremily2 with dissolve
        e "Ama bir tabloya neden yazı yazılır ki?" 
        hide emilyseriousleft

        show kisasac at leftcorneredward with easeinleft
        ksa "İnsanlar ne meraklı varlıklar böyle. Hem zayıf hem de kibirli olabilen tek varlık"
        hide kisasac

        show amy at rightcorneramy with dissolve
        a "Affedersiniz siz kimsi-"
        hide amy

        show kisasac at leftcorneredward with dissolve
        ksa "Bu tablonun artistiyim. Aslında sadece ileticisiyim denebilir. Bu resmi yapan sizsiniz"
        ksa "Ömrünüzün ne kadar uzadığını düşündünüz? 1 ay? 1 yıl? Belki 10?"
        hide kisasac

        scene blackbg with Fade(5.0, 0.1, 1.0)

        "{i}{b}* Etraf simsiyah olur, deprem olmaya başlar"

        play channel1("audio/sound/deprem.mp3")

        u "Hahahaha! İnsanların gerçekten kaderi bu denli değiştirmeye yetecek kadar değerli olduğunu mu sandınız? Güzel bir deney oldu. Ama her güzel şeyin bir sonu vardır"

        show emilyscared at rightcorner with dissolve
        e "Ne, ne, ne, ne, ne, ne, ne!"
        hide emilyscared

        show amyleft at leftcorneramy with dissolve
        a "Hassiktir!"
        hide amyleft

        show josephscared at rightcornerjoseph with dissolve
        j "Ahhhhhhhh! Hayıııırrrr!"
        hide josephscared

        stop channel1

        "{i}{b}* Bina Yıkılır"

        jump son

    elif madisonlived:

        show amy at rightcorneramy with fade
        a "İşte geldik"
        hide amy

        show madisonleft at leftcornermadison with dissolve
        m "Acele et"
        hide madisonleft

        scene bg27 with fade
        
        "{i}{b}* 2 katil o tablonun önünde karşılaşır"

        show amy at rightcorneramy with dissolve
        a "Eee? Tabloyu bulduk. Şimdi ne yapacağız?"
        hide amy

        scene merhamet2 with fade
        
        show madison at rightcornermadison with dissolve
        j "Bilmiyorum. Belki biraz daha incelersek ipucu bulabili-"
        hide madison

        show kisasac at leftcorneredward with easeinleft
        ksa "İnsanlar ne meraklı varlıklar böyle. Hem zayıf hem de kibirli olabilen tek varlık"
        hide kisasac

        show amy at rightcorneramy with dissolve
        a "Affedersiniz siz kimsi-"
        hide amy

        show kisasac at leftcorneredward with dissolve
        ksa "Bu tablonun artistiyim. Aslında sadece ileticisiyim denebilir. Bu resmi yapan sizsiniz"
        ksa "Ömrünüzün ne kadar uzadığını düşündünüz? 1 ay? 1 yıl? Belki 10?"
        hide kisasac

        scene blackbg with Fade(5.0, 0.1, 1.0)

        "{i}{b}* Etraf simsiyah olur, deprem olmaya başlar"

        play channel1("audio/sound/deprem.mp3")

        u "Hahahaha! İnsanların gerçekten kaderi bu denli değiştirmeye yetecek kadar değerli olduğunu mu sandınız? Güzel bir deney oldu. Ama her güzel şeyin bir sonu vardır"

        show amyleft at leftcorneramy with dissolve
        a "Hassiktir!"
        hide amyleft

        show madisonscared at rightcornermadison with dissolve
        m "Buradan hemen çıkmamız lazı-"
        hide madisonscared

        stop channel1

        "{i}{b}* Bina Yıkılır"

        jump son

    elif josephlived:

        show joseph at rightcornerjoseph with dissolve
        j "Odaklanmalıyım"
        hide joseph

        show amy at rightcorneramy with dissolve
        a "Sonunda vardım"
        hide amy

        scene bg27 with fade
        
        "{i}{b}* 2 katil o tablonun önünde karşılaşır"

        show josephleft at leftcornerjoseph with dissolve
        j "{i}(Bu kadın neden bir süredir tam burada dikiliyor)"
        hide josephleft

        show amy at rightcorneramy with dissolve
        a "{i}(Bu adam ne zaman gidecek acaba? Dikkatim dağılıyor)"
        hide amy

        scene merhamet2 with fade

        show kisasac at leftcorneredward with easeinleft
        ksa "İnsanlar ne meraklı varlıklar böyle. Hem zayıf hemde kibirli olabilen tek varlık"
        hide kisasac

        show amy at rightcorneramy with dissolve
        a "Affedersiniz siz kimsi-"
        hide amy

        show kisasac at leftcorneredward with dissolve
        ksa "Bu tablonun artistiyim. Aslında sadece ileticisiyim denebilir. Bu resmi yapan sizsiniz"
        ksa "Ömrünüzün ne kadar uzadığını düşündünüz? 1 ay? 1 yıl? Belki 10?"
        hide kisasac

        scene blackbg with Fade(5.0, 0.1, 1.0)

        "{i}{b}* Etraf simsiyah olur, deprem olmaya başlar"

        play channel1("audio/sound/deprem.mp3")

        u "Hahahaha! İnsanların gerçekten kaderi bu denli değiştirmeye yetecek kadar değerli olduğunu mu sandınız? Güzel bir deney oldu. Ama her güzel şeyin bir sonu vardır"

        show amyleft at leftcorneramy with dissolve
        a "Hassiktir!"
        hide amyleft

        show josephscared at rightcornerjoseph with dissolve
        j "Ahhhhhhhh! Hayıııırrrr!"
        hide josephscared

        stop channel1

        "{i}{b}* Bina Yıkılır"

        jump son

    elif emilylived:

        show emilyserious at rightcorner with dissolve
        e "Burası düşündüğümden büyükmüş. İşe koyulma vakti"
        hide emilyserious

        show amyleft at leftcorneramy with dissolve
        a "Sonunda vardım"
        hide amyleft

        scene bg27 with fade

        "{i}{b}* 2 katil o tablonun önünde karşılaşır"

        show emilyleft at leftcorneremily with dissolve
        e "Merhabalar. Bakıyorum da bu tabloya ilgilisiniz"
        hide emilyleft

        show amy at rightcorneramy with dissolve
        a "Benimle mi konuştunuz?"
        hide amy

        show emilyleft at leftcorneremily with dissolve
        e "Evet hanımefendi. Ben bu konularda acemiyim. Acaba resmin anlamı nedir?"
        hide emilyleft

        scene merhamet2 with fade

        show amy at rightcorneramy with dissolve
        a "Aslında bende yeniyim. Fakat acı bir şeyler anlattığı kesin"
        hide amy

        show emilyseriousleft at leftcorneremily2 with dissolve
        e "Ama bir tabloya neden yazı yazılır ki?"
        hide emilyseriousleft

        show kisasac at leftcorneredward with easeinleft
        ksa "İnsanlar ne meraklı varlıklar böyle. Hem zayıf hemde kibirli olabilen tek varlık"
        hide kisasac

        show amy at rightcorneramy with dissolve
        a "Affedersiniz siz kimsi-"
        hide amy

        show kisasac at leftcorneredward with dissolve
        ksa "Bu tablonun artistiyim. Aslında sadece ileticisiyim denebilir. Bu resmi yapan sizsiniz"
        ksa "Ömrünüzün ne kadar uzadığını düşündünüz? 1 ay? 1 yıl? Belki 10?"
        hide kisasac

        scene blackbg with Fade(10.0, 0.1, 1.0)

        "{i}{b}* Etraf simsiyah olur, deprem olmaya başlar"

        play channel1("audio/sound/deprem.mp3")

        u "Hahahaha! İnsanların gerçekten kaderi bu denli değiştirmeye yetecek kadar değerli olduğunu mu sandınız? Güzel bir deney oldu. Ama her güzel şeyin bir sonu vardır"

        show emilyscared at rightcorner with dissolve
        j "Ne, ne, ne, ne, ne, ne, ne!"
        hide emilyscared

        show amyleft at leftcorneramy with dissolve
        a "Hassiktir!"
        hide amyleft

        stop channel1

        "{i}{b}* Bina Yıkılır"

        jump son

    else:

        show amy at rightcorneramy with dissolve
        a "Ahh! Yoruldum. Ama sonunda vardım"
        hide amy

        scene bg27 with fade

        show amy at rightcorneramy with dissolve
        a "{b}* Tabloyu bulursun"
        hide emily

        scene merhamet1 with fade

        show amy at rightcorneramy with dissolve
        a "Eee? Şimdi ne sikim yapacağım ben?"
        hide amy

        show kisasac at leftcorneredward with easeinleft
        ksa "Gerçekten saygı değer bir sonuç. Gerçekten etkilendim. Elinden geldiğince doğru şeyi yapsan da bazı şeyler kaçınılmazdır. Ya da sadece tesadüftür"
        hide kisasac

        show amy at rightcorneramy with dissolve
        a "Affedersiniz siz kimsi-"
        hide amy

        show kisasac at leftcorneredward with dissolve
        ksa "Bu tablonun artistiyim. Aslında sadece ileticisiyim denebilir. Bu resmi yapan sizsiniz"
        ksa "Ömrünüzün ne kadar uzadığını düşündünüz? 1 ay? 1 yıl? Belki 10?"
        hide kisasac

        "{i}{b}* Etraf simsiyah olur, deprem olmaya başlar"

        play channel1("audio/sound/deprem.mp3")

        u "Hahahaha! İnsanların gerçekten kaderi bu denli değiştirmeye yetecek kadar değerli olduğunu mu sandınız? Güzel bir deney oldu. Ama her güzel şeyin bir sonu vardır"

        show amy at rightcorneramy with dissolve
        a "Hassiktir!"
        hide amy

        stop channel1

        "{i}{b}* Bina Yıkılır"

        jump son

label son:

    scene blackbg with Fade(0.1, 0.1, 0.1)

    centered "{size=60}SON{/size}" with dissolve

    scene oyunsonuekran with fade
    pause
    scene hazirlayanlar with fade
    pause
    # This ends the game.
    return