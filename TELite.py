#Tam Ekran Kamera v4.6 Mini
#Birçok S60 Cep Telefonuyla uyumlu.

import appuifw, e32
try:
    import camera
except:
    appuifw.note(u"Your phone is not compatible")
    os.abort()
import appswitch, os, miso, time, sysinfo,  firmware
from graphics import *
from e32db import format_time
from time import *
kamera=1
def handle_redraw(rect):
    if here==" ":
        yercegizim=u" "
    else:
        yerim=unicode(here)
        yercegizim=u" "
    canvas.text((2,12),yercegizim,255)

from key_codes import *

class Keyboard(object):
    def __init__(self,onevent=lambda:None):
        self._keyboard_state={}
        self._downs={}
        self._onevent=onevent
    def handle_event(self,event):
        if event['type'] == appuifw.EEventKeyDown:
            code=event['scancode']
            if not self.is_down(code):
                self._downs[code]=self._downs.get(code,0)+1
            self._keyboard_state[code]=1
        elif event['type'] == appuifw.EEventKeyUp:
            self._keyboard_state[event['scancode']]=0
        self._onevent()
    def is_down(self,scancode):
        return self._keyboard_state.get(scancode,0)
    def pressed(self,scancode):
        if self._downs.get(scancode,0):
            self._downs[scancode]-=1
            return True
        return False

keyboard=Keyboard()    



canvas=appuifw.Canvas(event_callback=keyboard.handle_event, redraw_callback=handle_redraw)
appuifw.app.body=canvas

mumkunboyutlar=camera.image_sizes()
boyut=mumkunboyutlar[0]
bsayi=len(mumkunboyutlar)-1
uygboyut=mumkunboyutlar[bsayi] 




SCRIPT_LOCK = e32.Ao_lock( )
IMG = None
def ru(x):return x.decode('utf-8')


global videodir
videodir=u"e:\\Images\\"
prgdili=0

    
#Varsayilan degerler yoksa tanimlayalim tabii. Varsa kendi kendine ayarlasin.
value2=0
admetni="FullScreen"
dosyaturu=".jpg"
activesaving=1

#Kullanicinin ayarladigi bazi secenekleri dosyaya kaydet
def kaydet():
    CONFIG_DIR='E:/System/Apps/TamEkranMini'
    CONFIG_FILE=os.path.join(CONFIG_DIR,'mysettings.txt')
    if not os.path.isdir(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
        CONFIG_FILE=os.path.join(CONFIG_DIR,'mysettings.txt')      
    config={}
    config['variable1']= admetni
    config['variable2']= adturu
    config['variable3']= videodir
    config['variable4']= dosyaturu
        #Variables of video recorderin
    config['variable5']= vidadmetin
    config['variable6']= vidadturu
    config['variable7']= vidvideodir
    config['variable8']= viddosyaturu
    config['variable9']= prgdili       
    config['variable10']= activesaving
    config['variable11']= firstrun
    config['variable12']= bilgi
    f=open(CONFIG_FILE,'wt')
    f.write(repr(config))
    f.close()
    oku()

#Dosya adina eklemek icin tarihi al    
here=" "
def tarihadi():
    t = time()
    format_time(t)   # for Symbian SQL
    global tarihad
    tarihad = strftime('%d/%m/%Y %H:%M:%S')
    
#Ayarlari kayitli dosyadan oku isleme koy
def oku():
    CONFIG_FILE='E:/System/Apps/TamEkranMini/mysettings.txt'
    try:
        f=open(CONFIG_FILE,'rt')
        try:
            content = f.read()
            config=eval(content)
            f.close()
            global admetin
            admetni=config.get('variable1','')
            global adturu
            adturu=config.get('variable2','')
            global videodir
            videodir=config.get('variable3','')
            global dosyaturu
            dosyaturu=config.get('variable4','')
            global vidadmetin
            vidadmetin=config.get('variable5','')
            global vidadturu
            vidadturu=config.get('variable6','')
            global vidvideodir
            vidvideodir=config.get('variable7','')
            global viddosyaturu
            viddosyaturu=config.get('variable8','')
            global prgdili
            prgdili=config.get('variable9','')
            global activesaving
            activesaving=config.get('variable10','')
            global firstrun
            firstrun=config.get('variable11','')          
            global bilgi
            bilgi=config.get('variable12','')          

        except:
            print 'dosya okunamiyor'
    except:
        print 'dosya acilamiyor'
    if adturu == "tarih":
        global value1
        value1= tarihad
    elif adturu=="yer":
        global value1
        value1= here
    else:
        global value1
        value1 = admetni
       
        
#yairihi belirle ve ayarlari al        
tarihadi()    
oku()
class FileSelector:
    def __init__(self,dir=".",ext='.jpg'):
        self.dir = dir
        self.ext = ext
        self.files = {}
 
        def iter(fileselector,dir,files):
            for file in files:
                b,e = os.path.splitext(file)
                if e == fileselector.ext:
                    fileselector.files[u'%s' % b] = os.path.join(dir,file)
 
        try:
            os.path.walk(self.dir,iter,self)
        
        except:
            pass
        self.sortedkeys = self.files.keys()
        self.sortedkeys.sort()
 
    def GetKeys(self):
        return self.sortedkeys
 
    def GetFile(self,index):
        return self.files[self.sortedkeys[index]]
def dilsec():
    appuifw.note(ru("Please select your language"), 'conf')
    selector = FileSelector("e:\\System\\Apps\\TamEkran\\langs",".lang")
    index = appuifw.selection_list(selector.GetKeys())
    if index is not None:
        appuifw.note(u"File %s selected." % selector.GetFile(index), "info")
        global prgdili
        prgdili=selector.GetFile(index)
    else:
        appuifw.note(u"No file selected.", "info")
        global prgdili
        prgdili='0'
    kaydet()    
    dil() 

try:
   appswitch.end_app(u"Kamera")
except:
   pass

try:
   appswitch.end_app(u"Camera")
except:
   pass


prgpath="E:\\System\\Apps\\TamEkran\\"
def dil(): 
    oku()
    if prgdili=='0':
        dilsec()
    else:
        try:
            f=file(prgdili,'rb')
            global language
            language=f.read().split('\n')
            f.close()
        except:
            appuifw.note(ru('Language file is damaged.'),'error')
            dilsec()        
            
dil()

def lang(string):
    return language[string-1]

#Simdi yukleniyor....    
appuifw.app.screen='full'
startui = Image.open("E:\\System\\Apps\\TamEkranMini\\start.ui")
appuifw.app.body.blit(startui) 
e32.ao_sleep(2) 
e32.ao_yield()




#Cikmak istedignden kendini ve video uygulamasini kapatsin
def __exit__( ):
    quit()

mzoom=1
rgbmode='RGB'
value2=0
value3=0
metin=" "
trhekleme=0
bekle=0.1

# Hafiza karti veye telefon hafizasi secildiginde kaydedildilecek yollari belirleyelim
def hafizakarti():
    global videodir
    videodir=u"e:\\Images\\"
    kaydet()
    appuifw.note(ru(lang(73)), 'conf')
    
def telhafizasi():
    global videodir
    videodir=u"c:\\Nokia\\Images\\"
    kaydet()
    appuifw.note(ru(lang(74)), 'conf')
    
#Guncelleme uygulamasini baslat        


def retarih():
    if adturu == "tarih":
        global value1
        value1 = tarihad
    else:
        global value1
        value1 = admetin

cerceveekle=0


def adtarih():
    global adturu
    adturu = "tarih"
    kaydet()
    appuifw.note(ru(lang(76)), 'conf')
    
      


#on ad icin metin secilmisse yazilacak metni girsin     
def onad():
    global admetni
    admetni=appuifw.query(ru(lang(128)), "text")
    colons = admetni.count(':')
    if colons > 0:
        appuifw.note(u"Cannot use ':' as part of text.", "error")
        global admetni
        admetni="FullScreen"
    kaydet()
    appuifw.note(ru(lang(77)), 'conf')
    
def admetin():
    global adturu
    adturu = "metin"
    onad()
    
def trhekle():
    if trhekleme == 1:
        global trhekleme
        trhekleme=0 
        appuifw.note(ru(lang(79)), 'conf')
    else:
        global trhekleme
        trhekleme=1
        appuifw.note(ru(lang(78)), 'conf')
    

def hakkinda():
    import globalui
    globalui.global_msg_query(ru("İlkTık TamEkran Kamera Mini\nIlkTik FullScreen Camera Mini\nSürüm:4.6 \nVersion:4.6\nDeveloped by: Oğuz Kırat\nGeliştiren: Oğuz Kırat\n\n Lisans sözleşmesi ve bilgi için http://ilktik.com/tamekrankamera adresini ziyaret edin.\n For license agreement and information visit http://ilktik.com/fullscreencamera"), ru("About"))
def yardim():
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\browser\\browser.app "file://e:/system/apps/TamEkran/yardim.html"')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\browser\\browser.app "file://e:/system/apps/TamEkran/yardim.html"')



def galeri():
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\MediaGallery2\\MediaGallery2.app')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\MediaGallery2\\MediaGallery2.app')
    
    
#joystick kullaninca zoomu arttir ya da azalt ama bi yere kadar
def zarttir():
    if mzoom >= int(camera.max_zoom())-10:
        global mzoom
        appuifw.note(ru(lang(86)), 'error')
    else:
        global mzoom
        mzoom=mzoom+10
        uygula()

def zazalt():
    if mzoom <= 9:
        global mzoom
        mzoom=0
        appuifw.note(ru(lang(87)), 'error')
    else:
        global mzoom
        mzoom=mzoom-10   
        uygula()
#zoom elle girilsin istenirse
def zmod():
    global mzoom
    mzoom=appuifw.query(ru("Zoom? (0-")+str(camera.max_zoom())+ru(")"), "number")    
    if mzoom:
        zooming = "aktif"
    else:
        mzoom=0        
    if mzoom >= int(camera.max_zoom())+1:
        global mzoom
        mzoom=camera.max_zoom()
        appuifw.note(ru(lang(89)), 'conf')
        uygula()
    else:
        uygula()
#Elle zamanlama suresini girmek istiyosa girsin




def nrm():
    global gmode
    gmode='auto'



#zamanlayici ayarlari
    
global netlik
netlik=100
    
def cikis():
    stop( )
    SCRIPT_LOCK.signal( )

def video():
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\TamEkranMini\\Video\\Video.app')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\TamEkranMini\\Video\\Video.app')
    
#dosya turu
def jepege():
    global dosyaturu
    dosyaturu=".jpg"
    kaydet()
def penege():
    global dosyaturu
    dosyaturu=".png"   
    kaydet()
   

#standart cekim modu yani nokianin kamerasi



def menufonk():
    if kamera == 2:
        ikincimenu()
    else:
        menu()   


         
#editbefore menusu    

#appuifw.app.menu = [(u'Cek', fotocek), (u'Kirm. Goz Gider. Cek 0', redeye), (u'Video Modu 1', video), (u'Ikinci Kamera', ikincikamera), ((u'Dizi Modu'), ((u'2 Fotograf',dizi2),(u'4 Fotograf',dizi4),(u'6 Fotograf',dizi6))), ((u'Zamanlayici'), ((u'Kapali',sifir),(u'5 saniye',bes),(u'10 saniye',onn),(u'20 saniye',yirmi),(u'30 saniye',otuz),(u'Elle Ayarla',zamanla))), (u"Flash Modu", ((u"Otomatik", flau), (u"Zorunlu", flon), (u"Kapali", floff))), (u"Cekim Modu", ((u"Otomatik", nrm2), (u"Gece", gece))), (u"Cozunurluk&LP", ((u"LargePixels 2.3 MP", lp23mp), (u"LargePixels 2.2 MP", lp22mp), (u"LargePixels 2.1 MP", lp21mp), (u"1600x1200 (2 MP)", b1), (u"1024x768", b2), (u"800x600", b3), (u"640x480", b4))), (u"Yakinlastirma", zmod), (u"Ayarlar", setsup), (u"EditBefore", editbefore), (u"CellLocation", celllocation), (u"Galeriye Git", galeri), (u"Guncelle", update), (u"Hakkinda", hakkinda), (u"Cik", __exit__)]
#((u'Coz.&LargePixels'), ((u'LP 3 MP(Onerilmez)',lp3mp),(u'LP 2.9 MP(Onerilmez)',lp29mp),(u'LP 2.8 MP(Onerilmez)',lp28mp),(u'LP 2.7 MP(Onerilmez)',lp27mp),(u'LP 2.6 MP',lp26mp),(u'LP 2.5 MP',lp25mp),(u'LP 2.4 MP',lp24mp),(u'LP 2.3 MP',lp23mp),(u'LP 2.2 MP',lp22mp),(u'LP 2.1 MP',lp21mp),(u'1600x1200 (2 MP)',b1),(u'1024x768',b2),(u'800x600',b3),(u'640x480',b4))), 

 #(u'Cozunurluk', ((u'LP 2.3 MP', lp23mp), (u'LP 2.2 MP', lp22mp), (u'LP 2.1 MP', lp21mp), (u'1600x1200 (2 MP)', b1), (u'1024x768', b2), (u'800x600', b3), (u'640x480', b4))), (u'Yakinlastirma', zmod), (u'Ayarlar', setsup), (u'EditBefore', editbefore), (u'CellLocation', celllocation), (u'Guncelle', update), (u'Hakkinda', hakkinda)]
    
    #, (u"Yakinlastirma", zmod), (u"EditBefore", editbefore), (u"Ayarlar", setsup), (u"Galeriye Git", galeri), (u"Guncelle", update), (u"Hakkinda", hakkinda), (u"Cik", __exit__)]   

#viewfinderi baslat
def start( ):
    appuifw.app.screen='full'
    global kucuk
    kucuk=0
    if kamera==1:
        camera.start_finder(vfCallback, backlight_on=1, size=(176, 132))
    elif kamera==2:
        camera.start_finder(ikincicb, backlight_on=1, size=(640, 480))
    global mzoom
    mzoom=0
#277 208
        
#ana kamera icin fotografi cek

kalan=1
dizim=0
kln=0
def fotocek():
    camera.stop_finder()
    global photo
    try:
        photo = camera.take_photo(size=boyut, zoom=mzoom, flash='auto') 
    except:
        photo = camera.take_photo(size=boyut, zoom=mzoom)
    canvas.blit(photo, scale=1)
    if bilgi==2:
        global photo
        photo=photo.transpose(ROTATE_90) 
    files=os.listdir(videodir)
    num = len(files) 
    global filename
    filename = videodir+value1+unicode(num+1)+dosyaturu
    e32.ao_sleep(0.01)
    if dosyaturu==".jpg": 
        if netlik==100:   
            photo.save("" + filename + "")
        else:
            photo.save("" + filename + "", quality=netlik, compression='fast')
    else:
        photo.save("" + filename + "", bpp=24, compression='fast') 
    viewrestart() 
    appuifw.note(ru(lang(99)))




def viewrestart():
    camera.stop_finder()
    if quitto==1:
        if kln==0:
            try:
                appswitch.end_app(u"TamEkran")
            except:
                pass

    camera.stop_finder()
    global calis
    calis=1    
    oku()
    if kucuk==1:
        camera.start_finder(vfCallback, backlight_on=1, size=(176, 208))
    else: 
        camera.start_finder(vfCallback, backlight_on=1, size=(277, 208))
    uygula()
    menu()
    
    
    
def viewrestart2():
    camera.stop_finder()
    if quitto==1:
        if kln==0:
            try:
                appswitch.end_app(u"TamEkran")
            except:
                pass

    camera.stop_finder()
    global calis
    calis=1    
    oku()
    ikincikamera()
    ikincimenu()

#ana kameraya don    
def anakamera():
    camera.stop_finder()
    photo = camera.take_photo(position=0)
    photo.save("c:\\system\\temp.jpg", quality=10, compression='fast')
    global kamera
    kamera=1
    menu()
    start( )    
    

        
#on kameradayken menu durumu         
def ikincimenu():    
    appuifw.app.menu = [(ru(lang(35)), anakamera), (ru(lang(32)), setsup), (ru(lang(37)), galeri), (ru(lang(39)), update), (ru(lang(40)), hakkinda), (ru(lang(41)), __exit__)]

#on kameraya gec
kamera=1
def ikincikamera():
    camera.stop_finder()
    photo = camera.take_photo(position=1)
    photo.save("c:\\system\\temp.jpg", quality=10, compression='fast')
    ikincimenu()
    global kamera
    kamera=2
    start()
    global katsayi
    katsayi=50
#kamera modu degistirilmediyse ana kamerayla baslar
global kamera
kamera=0
#on kamerada fotograf cek
onlp=0
def ikincicek():
    tarihadi()
    retarih()
    oku()
    e32.ao_sleep(bekle)
    camera.stop_finder()
    global photo
    photo = IMG
#camera.take_photo(position=1)

    if bilgi==2:
        global photo
        photo=photo.transpose(ROTATE_90)
    tarihadi()

    files=os.listdir(videodir)
    num = len(files) 
    global filename
    filename = videodir+value1+unicode(num+1)+dosyaturu
    if dosyaturu==".jpg": 
        if netlik==100:   
            photo.save("" + filename + "")
        else:
            photo.save("" + filename + "", quality=netlik, compression='fast')
    else:
        photo.save("" + filename + "", bpp=24, compression='fast')   
    appuifw.note(ru(lang(99)))
    viewrestart2()


    
    
#kirmizi gozu gidermek icin ust uste flas patlat
redgoz=0


def restart():
    menu()
    anakamera()

#upss bu ozelligi kaldirmistim, bi de bununla mi ugrasayim
def stop( ):
    camera.stop_finder( )
    cnvCallback( )
    appuifw.app.menu = [(u'Restart viewfinder', restart), (u'Exit', __exit__)]
    

quitto=0
sb=0
def ikincicb( aIm ): 
    global IMG
    IMG = aIm
    aIm=IMG.transpose(FLIP_LEFT_RIGHT)
    if bilgi==0:
        appuifw.app.body.blit(uishownow)
    else:
        appuifw.app.body.blit(aIm, scale=1)
    if showshrfile==1:
        fshow=unicode(sharingnow)
        sharinnow=u""+fshow+""
        canvas.text((2,12),sharinnnow,255)

        
    if bilgi==1:
       #sol taraftaki simgeleri goster
        #zoomu cizelim lutfen
        szoom=unicode(mzoom)
        bilgim=u""+szoom+" x"
        canvas.text((2,32),bilgim,255)


    elif bilgi==2:

       #sol taraftaki simgeleri goster

        #zoomu cizelim lutfen
        szoom=unicode(mzoom)
        bilgim=u""+szoom+" x"
        canvas.text((2,202),bilgim,255)
  

    if quitto==1:
        appuifw.app.set_exit()
    IMG = aIm


def vfCallback( aIm ): 
    global IMG
    IMG = aIm
    if bilgi==0:
        appuifw.app.body.blit(uishownow)
    else:
        appuifw.app.body.blit(aIm, scale=1)
    if showshrfile==1:
        fshow=unicode(sharingnow)
        sharinnow=u""+fshow+""
        canvas.text((2,12),sharinnnow,255)

        
    if bilgi==1:
       #sol taraftaki simgeleri goster
 
        #zoomu cizelim lutfen
        szoom=unicode(mzoom)
        bilgim=u""+szoom+" x"
        canvas.text((2,32),bilgim,255)
        #sag taraftaki simgeleri goster  
        #Cekim modu

     

    elif bilgi==2:

       #sol taraftaki simgeleri goster
 
        #zoomu cizelim lutfen
        szoom=unicode(mzoom)
        bilgim=u""+szoom+" x"
        canvas.text((2,202),bilgim,255)
 

        #sag taraftaki simgeleri goster  
        #Cekim modu
       
 

    if quitto==1:
        appuifw.app.set_exit()
    IMG = aIm



def vfCallback3( aIm ):
    if quitto==1:
        appuifw.note(ru(lang(104)))
        appswitch.switch_to_bg(u"TamEkran")
    if keyboard.pressed(EScancodeSelect):
        ikincicek()
    showkyt=ru(lang(105)) 
    canvas.text((2,185),showkyt,0xff0000)
 
    appuifw.app.body.blit(aIm, scale=1)

    IMG = aIm

def vfCallback4( aIm ):
    global IMG
    IMG = aIm
    appuifw.app.body.blit(IMG)
 
def cnvCallback( aRect=None ):
    if IMG != None:
        appuifw.app.body.clear( )
        appuifw.app.body.blit( IMG )
#CellLocationda kayitli olan yer bilgileirini al

#konum listedemi bak bakalim  

#fotografa yazmak icin tarihi ogren 
def tarihibul():
    t = time()
    format_time(t)   # for Symbian SQL
    global tarih
    tarih = strftime('%d/%m/%Y %H:%M:%S')




#yer ve tarihi fotografa yaz    






#artik hersey tamam uygulama baslasin!!!!        
appuifw.app.exit_key_handler = __exit__
appuifw.app.title= ru(lang(1))
appuifw.app.body = appuifw.Canvas( redraw_callback = cnvCallback )
#standart degerleri gireyim de kendini sasirmasin nasi cekcek


def uygula():
    photo1 = camera.take_photo(size=uygboyut, white_balance=wbm, zoom=mzoom, exposure=gmode)
    
    if kucuk==1:
        camera.start_finder(vfCallback, backlight_on=1, size=(176, 208))
    else:
        camera.start_finder(vfCallback, backlight_on=1, size=(277, 208))
        


here=" "


def cozunurlukmenusu():
    cozunurlukler=[]
    for coz in mumkunboyutlar:
        a,b=coz
        cozunur=str(a)+u"x"+str(b)
        cozunurlukler.append(cozunur)
    i=appuifw.selection_list(choices=cozunurlukler)
    global boyut     
    boyut=mumkunboyutlar[i] 
    appuifw.note(ru(lang(94)), 'conf')    
redgoz=0

def dikey():
    global bilgi
    bilgi=1
def yatay():
    global bilgi
    bilgi=2    
def sihirbazac():
    global firstrun
    firstrun=1
    kaydet()
    appuifw.note(ru(lang(182)))
    
#Ayarlar Formu
class MyFormView( object ):
    
    ## The constructor.
    def __init__( self ):
        ## Bool
        self._iIsSaved = False
 
        ## Model list.
        self._iCekim = [ru(lang(180)), ru(lang(179))]
        self._iKayitMod = [ru(lang(43)), ru(lang(44))]
        self._iFotoTur = [ru(lang(50)), ru(lang(49))]
        self._iKayitYeri = [ru(lang(52)), ru(lang(53))]
        self._iResimFormat = [u'JPG', u'PNG']
        ## Form fields.
        self._iFields = [( ru(lang(178)), 'combo', ( self._iCekim, 0 ) ),
                         ( ru(lang(48)), 'combo', ( self._iFotoTur, 0 ) ),
                         ( ru(lang(51)), 'combo', ( self._iKayitYeri, 1 ) ),    
                         ( ru(lang(54)), 'combo', ( self._iResimFormat, 0 ) ),                       
                         ]
 
 
    ## Displays the form.
    def setActive( self ):
        self._iIsSaved = False
        self._iForm = appuifw.Form(self._iFields, appuifw.FFormEditModeOnly)
        self._iForm.save_hook = self._markSaved
        self._iForm.flags = appuifw.FFormEditModeOnly
        self._iForm.execute( )
 
 
    ## save_hook send True if the form has been saved.
    def _markSaved( self, aBool ):
        self._iIsSaved = aBool
 
                
    ## _iIsSaved getter.
    def isSaved( self ):
        return self._iIsSaved
 
    # here you can put for example all the getters you need:
    #---------------------------------------------------------
 
    ## Return mobile field value.
    def getCekimModu( self ):
        ## This returns the mobile; In one case I needed to have UTF-8 encoding
        return self._iForm[0][2][1]
 
 


    def getFotoIsmi( self ):
        ## This returns the mobile; In one case I needed to have UTF-8 encoding
        return self._iForm[2][2][1]        
        
    

    def getKayitYeri( self ):
        ## This returns the mobile; In one case I needed to have UTF-8 encoding
        return self._iForm[3][2][1]
  

    def getResimFormati( self ):
        ## This returns the mobile; In one case I needed to have UTF-8 encoding
        return self._iForm[4][2][1]  
     
    
def setsup():
    myForm = MyFormView( )
    myForm.setActive( )
    dilsec()
    appuifw.note(ru("New language will be available when you restart application."))
    if myForm.isSaved( ):
        if myForm.getCekimModu( )==0:
            yatay()
        else:
            dikey()

        if myForm.getFotoIsmi( )==0:
            admetin()
        elif myForm.getFotoIsmi( )==1:
            adtarih()
        elif myForm.getFotoIsmi( )==2:
            adyer()
        if myForm.getKayitYeri( )==0:
            telhafizasi()
        elif myForm.getKayitYeri( )==1:
            hafizakarti()     
        if myForm.getResimFormati( )==0:
            jepege()
        else:
            penege()

#    appuifw.app.menu = [(ru(lang(6)), menufonk),
#    (ru("Language"), dilsec),
#    (ru(lang(178)), ((ru(lang(179)), dikey), (ru(lang(180)), yatay))),
#    (ru(lang(42)), ((ru(lang(43)), activesave), (ru(lang(44)), passivesave))), 
#    (ru(lang(45)), ((ru(lang(47)), flekr), (ru(lang(46)), kucukekran))), 
#    (ru(lang(48)), ((ru(lang(49)), adtarih), (ru(lang(50)), admetin), (ru(lang(164)), adyer))),
#    (ru(lang(51)), ((ru(lang(52)), telhafizasi), (ru(lang(53)), hafizakarti))),
#    (ru(lang(54)), ((u'JPG', jepege), (u'PNG', penege)))] 

    
   
#programin menusudur cok onemli
def menu():
    if camera.cameras_available()==2:
        appuifw.app.menu = [
        (ru(lang(8)), video), 
        (ru(lang(9)), ikincikamera),
        (ru(lang(14)), cozunurlukmenusu),  
        (ru(lang(30)), zmod),
        (ru(lang(32)), setsup),
        (ru(lang(40)), hakkinda)]    
         
    else:
        appuifw.app.menu = [
        (ru(lang(8)), video), 
        (ru(lang(14)), cozunurlukmenusu),  
        (ru(lang(30)), zmod),
        (ru(lang(32)), setsup),
        (ru(lang(40)), hakkinda)]

 

#Canvas resimlerini yukle
onshare=0
wbm='auto'
gmode='auto'
mzoom=1
redgoz=0
fmode='auto'
showshrfile=0
largepixels=0
bekle=0.1
senditblue=0
senditmms=0
rotate=0
activesaving=1
tarihibul()
start( )
menu()
oku()      
#tusa basilinca fonksiyonu yap


#isigi acik tut kapanirsa goremeyiz
def light_on():
    miso.reset_inactivity_time()
    e32.ao_sleep(4, light_on)  # forever loop
light_on()
insave=0
def quit():
    global quitto
    quitto=1
    e32.ao_sleep(0.2)
    global quitto
    quitto=1


running=1
#ozellikleri canvas uzerine ciz, az ugrasmadim bunun icin meger unicode yapmak lazimmis :P         

canvas=appuifw.Canvas(event_callback=keyboard.handle_event, redraw_callback=handle_redraw)
appuifw.app.body=canvas
  
           


appuifw.app.exit_key_handler=quit
calis=1
anakamera()




#bunlar da tuslarin tanimlanmasi
while calis==1:

    if keyboard.pressed(EScancodeSelect):
        if kamera==2:
            ikincicek()

        else:  
            fotocek()
    if keyboard.pressed(EScancode1):
        video()
        
          
    if keyboard.pressed(EScancodeHash):
        if bilgi==1:
            global bilgi
            bilgi=2
            kaydet()
        elif bilgi==2:
            global bilgi
            bilgi=1
            kaydet()

    if keyboard.is_down(EScancodeDownArrow):
        if kamera==2:
            appuifw.note(ru(lang(127)), 'error') 
            if bilgi==1:
                zazalt()
                e32.ao_yield()
    if keyboard.is_down(EScancodeLeftArrow):
        if kamera==2:
            appuifw.note(ru(lang(127)), 'error') 
        else:
            if bilgi==2:
                zazalt()
                e32.ao_yield()

    if keyboard.is_down(EScancodeRightArrow):
        if kamera==2:
            appuifw.note(ru(lang(127)), 'error') 
        else:
            if bilgi==2:
                zarttir()
                e32.ao_yield()                

    if keyboard.is_down(EScancodeUpArrow):
        if kamera==2:
            appuifw.note(ru(lang(127)), 'error') 
        else:
            if bilgi==1:
                zarttir()
                e32.ao_yield()

        
       
 
# kullanici girisini bekle        
    e32.ao_yield()
   
SCRIPT_LOCK.wait( )

#scriptimiz sona erdi.