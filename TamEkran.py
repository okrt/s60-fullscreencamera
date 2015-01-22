#Tam Ekran Kamera v4.6 Beta Tasarimi
#Urun: N70, N70 ME
#Dil: Uluslararası
#FullScreen Camera V4.6 Beta Building
#Produced for: N70, N70 ME
#Language: International


try:
    import miso
except:
    appuifw.note(u"cannot import miso module")

try:
    miso.set_process_priority(150)
except:
    pass    
    
import appuifw, e32, os

try:
    import camera
except:
    appuifw.note(u"Your phone is not compatible")
    os.abort()
try:
    import appswitch, location, time, messaging, sysinfo, socket, dir_iter, firmware, urllib, httplib, globalui
    from graphics import *
    from e32db import format_time
    from time import *
except:
    appuifw.note(u"There is a problem with a library file.")
kamera=1
model=firmware.phone_model
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
sikistir=0
#Kullanicinin ayarladigi bazi secenekleri dosyaya kaydet
def kaydet():
    CONFIG_DIR='E:/System/Apps/TamEkran'
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
    CONFIG_FILE='E:/System/Apps/TamEkran/mysettings.txt'
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


try:
   miso.compress_all_heaps()
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

appuifw.app.screen='full'
#Simdi yukleniyor....  

e32.ao_yield()
e32.ao_sleep(1)
startui = Image.open("E:\\System\\Apps\\TamEkran\\start.ui")
appuifw.app.body.blit(startui)  
e32.ao_yield()
startui = Image.open("E:\\System\\Apps\\TamEkran\\start2.ui")
appuifw.app.body.blit(startui) 
e32.ao_yield()
e32.ao_sleep(1)
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
def update():
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\TamEkran\\Guncelleme\\Guncelleme.app')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\TamEkran\\Guncelleme\\Guncelleme.app')

def imgviewer():
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\TamEkran\\imgviewer\\imgviewer.app')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\TamEkran\\imgviewer\\imgviewer.app')


def celllocation():
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\CellLocation\\CellLocation.app')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\CellLocation\\CellLocation.app')
def retarih():
    if adturu == "tarih":
        global value1
        value1 = tarihad
    else:
        global value1
        value1 = admetin
def cerceveyukle(cno):
    appuifw.note(ru(lang(189)))
    camera.stop_finder()
    frame=Image.open('E:\\System\\Apps\\TamEkran\\frames\\'+str(cno)+'.jpg')
    e32.ao_yield()
    framemask=Image.open('E:\\System\\Apps\\TamEkran\\frames\\'+str(cno)+'_mask.jpg')
#viewfinder duz
    maskduz=Image.new((276, 208), 'L')
    e32.ao_yield()
    global frameduz
    frameduz=frame
    global maskduz
    maskduz.blit(framemask)
#viewfinder yatay
    frameyatay=frameduz.transpose(ROTATE_270)
    global frameyatay
    e32.ao_yield()
    frameyatay=frameyatay.resize((276, 208), keepaspect=0)
    maskyatay=maskduz.transpose(ROTATE_270)
    e32.ao_yield()
    global maskyatay
    maskyatay=maskyatay.resize((276, 208), keepaspect=0)
    global cerceveekle
    cerceveekle=1
    start()
def cercevesec():
    cler=os.listdir('E:\\System\\Apps\\TamEkran\\frames')
    csayisi = len(cler)/2
    appuifw.note(ru(lang(186))+str(csayisi))
    cerceve=appuifw.query(ru(lang(187)), "number")
    if cerceve:
        if cerceve<=csayisi:    
            cerceveyukle(cerceve)
        else:
            appuifw.note(ru(lang(188))+str(csayisi))
    else:
        global cerceveekle
        cerceveekle=0
cerceveekle=0


#largepixels modunu etkinlestir ayriyetten cozunurlu belirleyip Ramde yer ac
def lp30mp():
    try:
       miso.compress_all_heaps()
    except:
       pass
    r=sysinfo.free_ram()
    r1=str(r)
    r2=int(r1)   
    r3=r2/1024
    r4=str(r3)
    r5=int(r4)
    if r4 <= "20000":
        appuifw.note(ru("You need extra RAM"))
    else:
        global lpx
        lpx=2400, 1800
        global largepixels
        largepixels=1
        appuifw.note(ru(lang(75)), 'conf')
        global katsayi
        katsayi=850

def lp29mp():
    try:
       miso.compress_all_heaps()
    except:
       pass
    r=sysinfo.free_ram()
    r1=str(r)
    r2=int(r1)   
    r3=r2/1024
    r4=str(r3)
    r5=int(r4)
    if r4 <= "20000":
        appuifw.note(ru("You need extra RAM"))    
    else:
        global lpx
        lpx=2320, 1740
        global largepixels
        largepixels=1
        appuifw.note(ru(lang(75)), 'conf')
        global katsayi
        katsayi=800

def lp28mp():
    global lpx
    lpx=2240, 1680
    global largepixels
    largepixels=1
    global katsayi
    katsayi=760
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')


def lp27mp():
    global lpx
    lpx=2160, 1620
    global largepixels
    largepixels=1
    global katsayi
    katsayi=700

    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')

def lp26mp():
    global lpx
    lpx=2080, 1560
    global largepixels
    largepixels=1
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')
    global katsayi
    katsayi=650


def lp25mp():
    global lpx
    lpx=2000, 1500
    global largepixels
    largepixels=1
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')
    global katsayi
    katsayi=600


def lp24mp():
    global lpx
    lpx=1920, 1440
    global largepixels
    largepixels=1
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')
    global katsayi
    katsayi=500

def lp23mp():
    global lpx
    lpx=1840, 1380
    global largepixels
    largepixels=1
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')
    global katsayi
    katsayi=450


def lp22mp():
    global lpx
    lpx=1760, 1320
    global largepixels
    largepixels=1
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')
    global katsayi
    katsayi=400


def lp21mp():
    global lpx
    lpx=1680, 1260
    global largepixels
    largepixels=1
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')
    global katsayi
    katsayi=300

def onlp1mp():
    global onlpx
    onlpx=800, 600
    global onlp
    onlp=1
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')   
    global katsayi
    katsayi=50    
def onlp13mp():
    global onlpx
    onlpx=1024, 768
    global onlp
    onlp=1
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf') 
    global katsayi
    katsayi=75
    
def onlp15mp():
    global onlpx
    onlpx=1200, 900
    global onlp
    onlp=1
    try:
       miso.compress_all_heaps()
    except:
       pass
    appuifw.note(ru(lang(75)), 'conf')  
    global katsayi
    katsayi=120       

def adtarih():
    global adturu
    adturu = "tarih"
    kaydet()
    appuifw.note(ru(lang(76)), 'conf')
    
def adyer():
    global adturu
    adturu = "yer"
    kaydet()
    appuifw.note(ru(lang(165)), 'conf')  

    
    


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
    
#bisiy secilmezse yapilacak ayarlari belirle    


#yer eklemeyi ac
def yer():
    if value2 == 1:
        global value2
        value2=0
        appuifw.note(ru(lang(80)), 'conf')
    else:
        global value2
        value2=1
        appuifw.note(ru(lang(81)), 'conf')
        

            
          
#metin eklemeyi ac
def metinonoff():
    if value3 == 1:
        global value3
        value3=0
        appuifw.note(ru(lang(82)), 'conf')
    else:
        global value3
        value3=1
        appuifw.note(ru(lang(83)), 'conf')

def metingir():
    global metin
    metin=appuifw.query(ru(lang(84)), "text")
    colons = metin.count(':')
    if colons > 0:
        appuifw.note(u"Cannot use ':' as part of text.", "error")
        metin=0
        global value3
        value3=0
        appuifw.note(ru(lang(82)), 'conf')
    else:
        appuifw.note(ru(lang(85)), 'conf')
    
    
#ekstradan sacmaliklar
def hakkinda():
    globalui.global_msg_query(ru("İlkTık TamEkran Kamera\nIlkTik FullScreen Camera\nSürüm:4.6 Beta\nVersion:4.6 Beta\nDeveloped by: Oğuz Kırat\nGeliştiren: Oğuz Kırat\n\n Lisans sözleşmesi ve bilgi için http://ilktik.com/tamekrankamera adresini ziyaret edin.\n For license agreement and information visit http://ilktik.com/fullscreencamera"), ru("About"))
def yardim():
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\browser\\browser.app "file://e:/system/apps/TamEkran/yardim.html"')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\browser\\browser.app "file://e:/system/apps/TamEkran/yardim.html"')



def galeri():
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\MediaGallery2\\MediaGallery2.app')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\MediaGallery2\\MediaGallery2.app')
    
zoomdegisti=0   
#joystick kullaninca zoomu arttir ya da azalt ama bi yere kadar
enyzoom=camera.max_zoom()
def zarttir():
    e32.ao_yield()
    if mzoom >= enyzoom-10:
        global mzoom
        appuifw.note(ru(lang(86)), 'error')
    else:
        global mzoom
        mzoom=mzoom+10  
        global zoomdegisti
        zoomdegisti=1          
        uygula()
        e32.ao_yield()
def zazalt():
    e32.ao_yield()
    if mzoom <= 9:
        global mzoom
        appuifw.note(ru(lang(87)), 'error')
    else:
        global mzoom
        mzoom=mzoom-10   
        global zoomdegisti
        zoomdegisti=1            
        uygula()
        e32.ao_yield()
#zoom elle girilsin istenirse
def zmod():
    enyzoom=camera.max_zoom()
    global mzoom
    mzoom=appuifw.query(ru("Zoom? 0-")+str(enyzoom), "number")    
    if mzoom:
        zooming = "aktif"
    else:
        mzoom=0        
    if mzoom >= enyzoom+1:
        global mzoom
        mzoom=enyzoom
        appuifw.note(ru(lang(89)), 'conf')
        uygula()
    else:
        uygula()
#Elle zamanlama suresini girmek istiyosa girsin
def ellezamanla():
    global bekle
    bekle=appuifw.query(ru(lang(90)), "number")
    if bekle:
        zekleme = "aktif"
        appuifw.note(ru(lang(91)), 'conf')
    else:
        bekle=0.1       
        appuifw.note(ru(lang(92)), 'conf')


# beyaz dengesi ayarlari

beyazmodlari=camera.white_balance_modes()

def whitebal1():
    global wbm
    wbm='auto'
    uygula()
    appuifw.note(ru(lang(93)), 'conf')

def whitebal2():
    if 'daylight' in beyazmodlari:
        global wbm
        wbm='daylight'
        uygula()
        appuifw.note(ru(lang(93)), 'conf')
    else: 
        appuifw.note(ru(lang(194)))  
          
def whitebal3():
    if 'cloudy' in beyazmodlari:
        global wbm
        wbm='cloydy'
        uygula()
        appuifw.note(ru(lang(93)), 'conf')
    else: 
        appuifw.note(ru(lang(194)))  
    
def whitebal4():
    if 'fluorescent' in beyazmodlari:
        global wbm
        wbm='fluorescent'
        uygula()
        appuifw.note(ru(lang(93)), 'conf')
    else: 
        appuifw.note(ru(lang(194)))  
        
def whitebal5():
    if 'tungsten' in beyazmodlari:
        global wbm
        wbm='tungsten'
        uygula()
        appuifw.note(ru(lang(93)), 'conf')
    else: 
        appuifw.note(ru(lang(194)))  
        
#cozunurluk ayarlari
def b1():
    global boyut
    boyut=(1600, 1200)
    global largepixels
    largepixels=0
    global katsayi
    katsayi=278

    appuifw.note(ru(lang(94)), 'conf')


    
def b2():
    global boyut
    boyut=(1024, 768)
    global largepixels
    largepixels=0
    global katsayi
    katsayi=150
    appuifw.note(ru(lang(94)), 'conf')

    
def b3():
    global boyut
    boyut=(800, 600)
    global largepixels
    largepixels=0
    global katsayi
    katsayi=50
    appuifw.note(ru(lang(94)), 'conf')


def b4():
    global boyut
    boyut=(640, 480)
    global largepixels
    largepixels=0
    global katsayi
    katsayi=35
    global onlp
    onlp=0
    appuifw.note(ru(lang(94)), 'conf')

def b5():
    global boyut
    boyut=(320, 240)
    global largepixels
    largepixels=0
    appuifw.note(ru(lang(94)), 'conf')
flaslar=camera.flash_modes()            
#flash ayarlari
def flon():
    if 'forced' in flaslar:
        global fmode
        fmode='forced'
    else:
        appuifw.note(ru(lang(194)))
def floff():
    global fmode
    fmode='none'
    
def flau():
    if 'auto' in flaslar:
        global fmode
        fmode='auto'
    else:
        appuifw.note(ru(lang(194)))

        
#Renk sayisi ayarlari    
def rgb12():
    global rgbmode
    rgbmode="RGB12"
    appuifw.note(ru(lang(95)), 'conf')
    
def rgb16():
    global rgbmode
    rgbmode="RGB16"
    appuifw.note(ru(lang(95)), 'conf')  
    
def rgbfull():
    global rgbmode
    rgbmode="RGB"    
    appuifw.note(ru(lang(95)), 'conf')
        
#cekim modu ayarlari
cekimmodlari=camera.exposure_modes()
def gece():
    if 'night' in cekimmodlari:
        global gmode
        gmode='night'
        uygula()
    else:
        appuifw.note(ru(lang(194)))
            
def portre():
    if 'center' in cekimmodlari:
        global gmode
        gmode='center'
        uygula()
    else:
        appuifw.note(ru(lang(194)))
        
def nrm():
    global gmode
    gmode='auto'

def nrm2():
    global gmode
    gmode='auto'
    uygula()

#zamanlayici ayarlari
def sifir():
    global bekle
    bekle=0.01
    appuifw.note(ru(lang(96)), 'conf')

def bes():
    global bekle
    bekle=5
    appuifw.note(ru(lang(91)), 'conf')

def onn():
    global bekle
    bekle=10
    appuifw.note(ru(lang(91)), 'conf')

def yirmi():
    global bekle
    bekle=20
    appuifw.note(ru(lang(91)), 'conf')

def otuz():
    global bekle
    bekle=30
    appuifw.note(ru(lang(91)), 'conf')
   
#dizi modu ayarlari ana kamera icin
dizim=0
def dizioff():
    global dizim
    dizim=0

def dizi6():
    global dizim
    dizim=5
    
def dizimodu():
    global dizim
    dizim=appuifw.query(ru(lang(160)), "number")
    if dizim:
        global dizim
        dizim=dizim-1
        zekleme = "aktif"
        appuifw.note(ru(lang(3)), 'conf')
    else:
        global dizim
        dizim=0       
        appuifw.note(ru(lang(4)), 'conf')    
    


      
def dizi4():
    global dizim
    dizim=4



def dizi2():
    global dizim
    dizim=1



 #dizi ayarlari on kamera icin   
def dizion2():
    global dizim
    dizim=2
    
def dizioncek2():
    global bekle
    zamanla=bekle
    e32.ao_sleep(bekle)
    global bekle
    bekle=0.1
    global largepixels
    largepixels=0
    ikincicek()
    ikincicek()
    global bekle
    bekle=zamanla
    
def dizion4():
    global dizim
    dizim=4


    
def dizion6():
    global dizim
    dizim=2
              

#netlik aslinda kalite ayari    
def netlik100():
    global netlik
    netlik=100
    appuifw.note(ru(lang(97)), 'conf')

def netlik70():
    global netlik
    netlik=70
    appuifw.note(ru(lang(97)), 'conf')
    
            
def netlik50():
    global netlik
    netlik=50   
    appuifw.note(ru(lang(97)), 'conf')
    
        
def netlik30():
    global netlik
    netlik=30  
    appuifw.note(ru(lang(97)), 'conf')

def netlik10():
    global netlik
    netlik=10  
    appuifw.note(ru(lang(97)), 'conf')

    
global netlik
netlik=100
    
def cikis():
    stop( )
    SCRIPT_LOCK.signal( )

def video():
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\TamEkran\\Video\\Video.app')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\TamEkran\\Video\\Video.app')
    
#dosya turu
def jepege():
    global dosyaturu
    dosyaturu=".jpg"
    kaydet()
def penege():
    global dosyaturu
    dosyaturu=".png"   
    kaydet()
   
def flekr():
    kucuk=1
    camera.stop_finder()
    start( )
    
#standart cekim modu yani nokianin kamerasi

def kucukekran():
    appuifw.app.screen='normal'
    global kucuk
    kucuk=1
    camera.stop_finder()
    camera.start_finder(vfCallback, backlight_on=1, size=(176, 240))
    global mzoom
    mzoom=0    
 


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
        camera.start_finder(vfCallback, backlight_on=1, size=(276, 208))
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
    e32.ao_sleep(bekle)
    global kln
    kln=kln+1
    camera.stop_finder()
    if redgoz==1:
        try:
            img = camera.take_photo(size=(640, 480), zoom=mzoom, flash='forced')
        except:
            pass
    try:
        global photo
        photo = camera.take_photo(mode=rgbmode, size=boyut, zoom=mzoom, flash=fmode, exposure=gmode, white_balance=wbm) 
    except:
        global photo
        photo = camera.take_photo(mode=rgbmode, size=boyut, zoom=mzoom, exposure=gmode) 

    global sikistir
    sikistir=1

    if cerceveekle==1:
        a=frameyatay.resize(boyut)
        b=maskyatay.resize(boyut)
        photo.blit(a, mask=b)

    if sb==1:
        sbshoot=Image.new(boyut, 'L')
        sbshoot.blit(photo)
        photo=sbshoot
    elif sb==2:
        sbshoot=Image.new(boyut, '1')
        sbshoot.blit(photo)
        photo=sbshoot
    canvas.blit(photo, scale=1)
    if bilgi==2:
        global photo
        photo=photo.transpose(ROTATE_90)
    tarihadi()
    e32.ao_yield()
    retarih()
    e32.ao_yield()
    oku()
    e32.ao_yield()
    if activesaving==1:
        finderstart()
    files=os.listdir(videodir)
    num = len(files) 
    global filename
    filename = videodir+value1+unicode(num+1)+dosyaturu
    if largepixels == 1:
        e32.ao_yield()
        try:
            camera.stop_finder()
            lpmodeui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\largepixelprocess.ui")
            canvas.blit(lpmodeui)
        except:
            pass
        try:    
            e32.ao_yield()
            photo=photo.resize((lpx), keepaspect=0)
            e32.ao_yield()
        except:
            appuifw.note(ru(lang(98)), 'error')
    e32.ao_sleep(0.01)

    dondur()
    e32.ao_yield()
    fotografayaz()
    e32.ao_yield()
    metinyaz()
    appuifw.note(ru(lang(99)))
    senditnow()
    global kalan
    kalan=kalan-1
    global kln
    kln=kln-1
    global sikistir
    sikistir=0
    if dizim == 0:
        if kalan==0:
            if kln==0:
                viewrestart()
    global kalan
    kalan=1
def senditnow():
    sendviablue()
    sendviamms()


def finderstart():
    global insave
    insave=0
    if kucuk == 1:
        camera.start_finder(vfCallback2, backlight_on=1, size=(176, 208))
        if dizim>=1:
            global dizim
            dizim=dizim-1
            fotocek()
            if dizim==0:
                global kalan
                kalan=1

    else:
        camera.start_finder(vfCallback2, backlight_on=1, size=(277, 208))
        appuifw.app.menu = [(ru(lang(34)), fotocek)]
        if dizim>=1:
            global dizim
            dizim=dizim-1
            fotocek()
            if dizim==0:
                global kalan
                kalan=1

def finderstart2():
    global insave
    insave=0
    if kucuk == 1:
        camera.start_finder(vfCallback3, backlight_on=1, size=(176, 208))
        if dizim>=1:
            global dizim
            dizim=dizim-1
            ikincicek()
            if dizim==0:
                global kalan
                kalan=1

    else:
        camera.start_finder(vfCallback3, backlight_on=1, size=(277, 208))
        appuifw.app.menu = [(ru(lang(34)), ikincicek)]
        if dizim>=1:
            global dizim
            dizim=dizim-1
            ikincicek()
            if dizim==0:
                global kalan
                kalan=1





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
    photo = camera.take_photo(size=(800,600), position=0)
    global kamera
    kamera=1
    menu()
    start( )

def activesave():
    global activesaving
    activesaving=1
    kaydet()
    
def passivesave():
    global activesaving
    activesaving=0
    kaydet()
        
#on kameradayken menu durumu         
def ikincimenu():    
    appuifw.app.menu = [(ru(lang(35)), anakamera), ((u'LargePixels'), ((ru(lang(4)),b4),(u'1 MP',onlp1mp),(u'1.3 MP',onlp13mp),(u'1.5 MP',onlp15mp))), ((ru(lang(15))), ((ru(lang(4)),sifir),(ru(lang(16)),bes),(ru(lang(17)),onn),(ru(lang(18)),yirmi),(ru(lang(19)),otuz),(ru(lang(20)),ellezamanla))), (ru(lang(32)), setsup), (u'EditBefore ', editbefore), (u"CellLocation", celllocation), (ru(lang(37)), galeri), (ru(lang(39)), update), (ru(lang(40)), hakkinda), (ru(lang(41)), __exit__)]

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
    global kln
    kln=kln+1
    global photo
    photo = IMG
#camera.take_photo(position=1)
    if cerceveekle==1:
        a=frameyatay.resize((640, 480))
        b=maskyatay.resize((640, 480))
        photo.blit(a, mask=b)

    if sb==1:
        sbshoot=Image.new(boyut, 'L')
        sbshoot.blit(photo)
        photo=sbshoot
    if sb==2:
        sbshoot=Image.new(boyut, '1')
        sbshoot.blit(photo)
        photo=sbshoot

    if bilgi==2:
        global photo
        photo=photo.transpose(ROTATE_90)
    tarihadi()

    files=os.listdir(videodir)
    num = len(files) 
    global filename
    filename = videodir+value1+unicode(num+1)+dosyaturu
    if onlp == 1:
        e32.ao_yield()
        try:
           miso.compress_all_heaps()
        except:
           pass
        e32.ao_sleep(2)
        try:
            e32.ao_yield()
            photo=photo.resize((onlpx), keepaspect=0)
        except:
            appuifw.note(ru(lang(98)), 'error')
    e32.ao_sleep(0.01)
    dondur()
    fotografayaz()
    metinyaz()
    appuifw.note(ru(lang(99)))
    senditnow()
    global kalan
    kalan=kalan-1
    global kln
    kln=kln-1
    if dizim == 0:
        if kalan==0:
            if kln==0:
                viewrestart2()
    global kalan
    kalan=1

    
    
#kirmizi gozu gidermek icin ust uste flas patlat
redgoz=0
def redeye():
    if redgoz==0:
        global redgoz
        redgoz=1
        appuifw.note(ru(lang(100)), 'conf')
    else:
        global redgoz
        redgoz=0
        appuifw.note(ru(lang(101)), 'conf')

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
        if cerceveekle==1:
            if bilgi==1:
                try:
                    aIm.blit(frameduz, mask=maskduz)
                except:
                    pass
            if bilgi==2:
                try:
                    aIm.blit(frameyatay, mask=maskyatay)
                except:
                    pass
        if sb==1:
            try:
                sbimg.blit(aIm)
                appuifw.app.body.blit(sbimg, scale=1)
            except:
                pass
        else:
            appuifw.app.body.blit(aIm, scale=1)
    if showshrfile==1:
        fshow=unicode(sharingnow)
        sharinnow=u""+fshow+""
        canvas.text((2,12),sharinnnow,255)

        
    if bilgi==1:
       #sol taraftaki simgeleri goster
        if here==" ":
            yercegizim=ru(lang(103))
        else:
            yerim=unicode(here)
            yercegizim=u""+yerim+""
        canvas.text((2,12),yercegizim,255)
        #zoomu cizelim lutfen
        szoom=unicode(mzoom)
        bilgim=u""+szoom+" x"
        canvas.text((2,32),bilgim,255)
        canvas.blit(dslider, target=(2,42), mask=dsmask)
        yzoom=208-(mzoom+85)
        canvas.blit(dmarker, target=(0,yzoom), mask=dmmask)

        if dizim>0:
            appuifw.app.body.blit(diziui, target=(158,81))

        if largepixels==1:
            appuifw.app.body.blit(lpmodeui, target=(158,193))
    elif bilgi==2:

       #sol taraftaki simgeleri goster
        if here==" ":
            yercegizim=ru(lang(103))
        else:
            yerim=unicode(here)
            yercegizim=u""+yerim+""
        canvas.text((2,192),yercegizim,255)
        #zoomu cizelim lutfen
        szoom=unicode(mzoom)
        bilgim=u""+szoom+" x"
        canvas.text((2,202),bilgim,255)
        canvas.blit(yslider, target=(80,198), mask=ysmask)
        xzoom=86+mzoom
        canvas.blit(ymarker, target=(xzoom,196), mask=ymmask)


        #sag taraftaki simgeleri goster  
        #Cekim modu
        if dizim>0:
            appuifw.app.body.blit(diziuiy, target=(104,2))

        if largepixels==1:
            appuifw.app.body.blit(lpmodeuiy, target=(86,2))    
    if quitto==1:
        appuifw.app.set_exit()
    IMG = aIm


def vfCallback( aIm ): 
    global IMG
    IMG = aIm
    if bilgi==0:
        appuifw.app.body.blit(uishownow)
    else:
        if cerceveekle==1:
            if bilgi==1:
                try:
                    aIm.blit(frameduz, mask=maskduz)
                except:
                    pass
            if bilgi==2:
                try:
                    aIm.blit(frameyatay, mask=maskyatay)
                except:
                    pass
        if sb==1:
            try:
                global sbimage
                sbimg=Image.new((276, 208), 'L')
                sbimg.blit(aIm)
                appuifw.app.body.blit(sbimg)
            except:
                pass
        elif sb==2:
            try:
                global sbimage
                sbimg=Image.new((276, 208), '1')
                sbimg.blit(aIm)
                appuifw.app.body.blit(sbimg)
            except:
                pass

        else:
            appuifw.app.body.blit(aIm, scale=1)
    if showshrfile==1:
        fshow=unicode(sharingnow)
        sharinnow=u""+fshow+""
        canvas.text((2,12),sharinnnow,255)

        
    if bilgi==1:
       #sol taraftaki simgeleri goster
        if here==" ":
            yercegizim=ru(lang(103))
        else:
            yerim=unicode(here)
            yercegizim=u""+yerim+""
        canvas.text((2,12),yercegizim,255)
        #zoomu cizelim lutfen
        szoom=unicode(mzoom)
        bilgim=u""+szoom+" x"
        canvas.text((2,32),bilgim,255)
        canvas.blit(dslider, target=(2,42), mask=dsmask)
        yzoom=208-(mzoom+85)
        canvas.blit(dmarker, target=(0,yzoom), mask=dmmask)

        #sag taraftaki simgeleri goster  
        #Cekim modu
       
        if gmode=="auto":
            appuifw.app.body.blit(cotoui, target=(158,30))
        elif gmode=="night":
            appuifw.app.body.blit(cnightui, target=(158,30))
        else: 
            appuifw.app.body.blit(portreui, target=(158,30))   
#flash mode
        if fmode=="auto":
            appuifw.app.body.blit(fautoui, target=(158,47))
        if fmode=="forced":
            appuifw.app.body.blit(fforcedui, target=(158,47))
        if fmode=="none":
            appuifw.app.body.blit(foffui, target=(158,47))
#beyazdengesi
        if wbm=="auto":
            appuifw.app.body.blit(wautoui, target=(158,64))

        if wbm=="daylight":
            appuifw.app.body.blit(wsunui, target=(158,64))

        if wbm=="cloudy":
            appuifw.app.body.blit(wcloudui, target=(158,64))

        if wbm=="fluorescent":
            appuifw.app.body.blit(wflourui, target=(158,64))
            
        if wbm=="tungsten":
            appuifw.app.body.blit(wtungstenui, target=(158,64))


        if dizim>0:
            appuifw.app.body.blit(diziui, target=(158,81))



#kirmizi goz
        if redgoz==1:
            appuifw.app.body.blit(redeyeonui, target=(158,176))
        else:
            appuifw.app.body.blit(redeyeoffui, target=(158,176))

        if largepixels==1:
            appuifw.app.body.blit(lpmodeui, target=(158,193))
    elif bilgi==2:

       #sol taraftaki simgeleri goster
        if here==" ":
            yercegizim=ru(lang(103))
        else:
            yerim=unicode(here)
            yercegizim=u""+yerim+""
        canvas.text((2,192),yercegizim,255)
        #zoomu cizelim lutfen
        szoom=unicode(mzoom)
        bilgim=u""+szoom+" x"
        canvas.text((2,202),bilgim,255)
        canvas.blit(yslider, target=(80,198), mask=ysmask)
        xzoom=86+mzoom
        canvas.blit(ymarker, target=(xzoom,196), mask=ymmask)


        #sag taraftaki simgeleri goster  
        #Cekim modu
       
        if gmode=="auto":
            appuifw.app.body.blit(cotouiy, target=(158,2))
        elif gmode=="night":
            appuifw.app.body.blit(cnightuiy, target=(158,2))
        else: 
            appuifw.app.body.blit(portreuiy, target=(158,2))   
#flash mode
        if fmode=="auto":
            appuifw.app.body.blit(fautouiy, target=(140,2))
        if fmode=="forced":
            appuifw.app.body.blit(fforceduiy, target=(140,2))
        if fmode=="none":
            appuifw.app.body.blit(foffuiy, target=(140,2))
#beyazdengesi
        if wbm=="auto":
            appuifw.app.body.blit(wautouiy, target=(122,2))

        if wbm=="daylight":
            appuifw.app.body.blit(wsunuiy, target=(122,2))

        if wbm=="cloudy":
            appuifw.app.body.blit(wclouduiy, target=(122,2))

        if wbm=="fluorescent":
            appuifw.app.body.blit(wflouruiy, target=(122,2))
            
        if wbm=="tungsten":
            appuifw.app.body.blit(wtungstenuiy, target=(122,2))


        if dizim>0:
            appuifw.app.body.blit(diziuiy, target=(104,2))


#kirmizi goz
        if redgoz==1:
            appuifw.app.body.blit(redeyeonuiy, target=(2,2))
        else:
            appuifw.app.body.blit(redeyeoffuiy, target=(2,2))

        if largepixels==1:
            appuifw.app.body.blit(lpmodeuiy, target=(86,2))    
    if quitto==1:
        appuifw.app.set_exit()
    IMG = aIm

def vfCallback2( aIm ):
    if quitto==1:
        appuifw.note(ru(lang(104)))
        appswitch.switch_to_bg(u"TamEkran")
    if keyboard.pressed(EScancodeSelect):
        fotocek()
    showkyt=ru(lang(105)) 
    canvas.text((2,185),showkyt,0xff0000)


    showkyt=ru(lang(106)) 
    canvas.text((2,200),showkyt,0xcccccc)
    global IMG
    if cerceveekle==1:
        if bilgi==1:
            try:
                aIm.blit(frameduz, mask=maskduz)
            except:
                pass
        if bilgi==2:
            try:
                aIm.blit(frameyatay, mask=maskyatay)
            except:
                pass
    if sb==1:
        try:
            sbimg.blit(aIm)
            appuifw.app.body.blit(sbimg, scale=1)
        except:
            pass
    elif sb==2:
        try:
            global sbimage
            sbimg=Image.new((276, 208), '1')
            sbimg.blit(aIm)
            appuifw.app.body.blit(sbimg)
        except:
             pass

    else:
        appuifw.app.body.blit(aIm, scale=1)

    IMG = aIm

def vfCallback3( aIm ):
    if quitto==1:
        appuifw.note(ru(lang(104)))
        appswitch.switch_to_bg(u"TamEkran")
    if keyboard.pressed(EScancodeSelect):
        ikincicek()
    showkyt=ru(lang(105)) 
    canvas.text((2,185),showkyt,0xff0000)
    if cerceveekle==1:
        if bilgi==1:
            try:
                aIm.blit(frameduz, mask=maskduz)
            except:
                pass
        if bilgi==2:
            try:
                aIm.blit(frameyatay, mask=maskyatay)
            except:
                pass
    if sb==1:
        try:
            sbimg.blit(aIm)
            appuifw.app.body.blit(sbimg, scale=1)
        except:
            pass
    elif sb==2:
        try:
            global sbimage
            sbimg=Image.new((276, 208), '1')
            sbimg.blit(aIm)
            appuifw.app.body.blit(sbimg)
        except:
            pass


    else:
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
def load_dictionary(filename):  
    f = file(filename, "r")  
    dict = {}  
    for line in f:  
        key, value = line.split(":")  
        dict[key.strip()] = eval(value.strip())  
    f.close()  
    return dict 

#teknik acidan bu uygulamada yer almamasi lazim celllocation ile kullanicak konum kaydetme fonksiyonu


PATH = u"E:\\System\\Apps\\CellLocation\\"
if not os.path.exists(PATH):
        os.makedirs(PATH)
        
INTERVAL = 5.0
CELL_FILE = PATH + "known_cells.txt"
CLDB_FILE = PATH + "icldb.ilktik"
LOG_FILE = PATH + "visited_cells.txt"
log = file(LOG_FILE, "a")
timer = e32.Ao_timer()   

#konum listedemi bak bakalim  

def show_location():  
    global loc
    loc = current_location()  
    if loc in known_cells:  
        global here
        here = known_cells[loc]  
    elif loc in known_cells2:  
        global here
        here = known_cells2[loc]  
    else:  
        global here
        here = " "  
    if sikistir==1:
        try:
            miso.compress_all_heaps()
        except:
            pass    
    timer.after(INTERVAL, show_location)  

#tespit et cellidleri sebekeden
def current_location():
    gsm_loc = location.gsm_location()
    return "%d/%d/%d/%d" % gsm_loc
    
  
#listeyi yukler
def load_cells2():  
    global known_cells2  
    try:  
        known_cells2 = load_dictionary(CLDB_FILE)  
    except:  
        known_cells2 = {}  

def load_cells():
    global known_cells
    try:
        known_cells = load_dictionary(CELL_FILE)
    except:
        known_cells = {}

#fotografa yazmak icin tarihi ogren 
def tarihibul():
    t = time()
    format_time(t)   # for Symbian SQL
    global tarih
    tarih = strftime('%d/%m/%Y %H:%M:%S')



def metinyaz():
    if value3 == 1:
        photo.text((20,50), u""+metin+"", fill=0xFF0000, font="title") 
    if dosyaturu==".jpg": 
        if netlik==100:   
            photo.save("" + filename + "")
        else:
            photo.save("" + filename + "", quality=netlik, compression='fast')
    else:
        photo.save("" + filename + "", bpp=24, compression='fast')    
#yer ve tarihi fotografa yaz    

def fotografayaz():
    tarihibul()
    if value2 == 1:
        photo.text((20,30), u""+here+"", fill=0xFF0000, font="title") 
        yazmatamam="tamam"
    if trhekleme == 1:
        photo.text((20,15), u""+tarih+"", fill=0xFF0000, font="title")  
    else:
         yazmatamam="tamam"

# Image Rotating
def rotkapali():
    global rotate
    rotate=0
    appuifw.note(ru(lang(108)), 'conf')

    
def rot90der():
    global rotate
    rotate = "ROTATE_90"
    appuifw.note(ru(lang(107)), 'conf')
    
def rot180der():
    global rotate
    rotate = "ROTATE_180"
    appuifw.note(ru(lang(107)), 'conf')

    
def rot270der():
    global rotate
    rotate = "ROTATE_270"    
    appuifw.note(ru(lang(107)), 'conf')

    
def rotyatay():
    global rotate
    rotate = "FLIP_LEFT_RIGHT"
    appuifw.note(ru(lang(107)), 'conf')
    

def rotdikey():
    global rotate
    rotate = "FLIP_TOP_BOTTOM"
    appuifw.note(ru(lang(107)), 'conf')
    
        
def dondur():
    if rotate == 0:
        dondurme="yapilmadi"
    if rotate == "ROTATE_90":
        photo=photo.transpose(ROTATE_90)
    if rotate == "ROTATE_180": 
        photo=photo.transpose(ROTATE_180)
    if rotate == "ROTATE_270": 
        photo=photo.transpose(ROTATE_270)
    if rotate == "FLIP_LEFT_RIGHT": 
        photo=photo.transpose(FLIP_LEFT_RIGHT)
    if rotate == "FLIP_TOP_BOTTOM":
        photo=photo.transpose(FLIP_TOP_BOTTOM)


#artik hersey tamam uygulama baslasin!!!!        
appuifw.app.exit_key_handler = __exit__
appuifw.app.title= ru(lang(1))
appuifw.app.body = appuifw.Canvas( redraw_callback = cnvCallback )
#standart degerleri gireyim de kendini sasirmasin nasi cekcek


def uygula():
    camera.stop_finder()
    try:    
        photo1 = camera.take_photo(size=(640, 480), white_balance=wbm, zoom=mzoom, exposure=gmode)
    except:
        try:    
            photo1 = camera.take_photo(size=(640, 480), zoom=mzoom, exposure=gmode)
        except:
            try:    
                photo1 = camera.take_photo(size=(640, 480), zoom=mzoom)
            except:
                pass           
                                
    if kucuk==1:
        camera.start_finder(vfCallback, backlight_on=1, size=(176, 208))
    else:
        camera.start_finder(vfCallback, backlight_on=1, size=(277, 208))
    e32.ao_yield()        
        
def sendviablue():
    e32.ao_yield()
    global onshare
    onshare=1
    global uishownow
    uishownow=syncui
    if senditblue==1:
        try:
            global bilgi
            bilgi=0
            file=(filename)
            e32.ao_yield()
            try:
                socket.bt_obex_send_file(address, channel, file)
                e32.ao_yield()   
            except:
                appuifw.note(ru(lang(110)), 'error')          
        except:
            appuifw.note(ru(lang(110)), 'error') 
        if (appuifw.query(ru(lang(111)), 'query') == True):
            devam=1
        else:
            global senditblue
            senditblue=0
            oku()
     
    global onshare
    onshare=0
    oku()
    e32.ao_yield()
    
    
def sendviamms():
    e32.ao_yield()
    if senditmms==1:
        try:
            e32.ao_yield()    
            global onshare
            onshare=1
            global bilgi
            bilgi=0
            global uishownow
            uishownow=syncui
            messaging.mms_send(number, text, filename)
            e32.ao_yield()
        except:
            appuifw.note(ru(lang(112)), 'error')
        if (appuifw.query(ru(lang(113)), 'query') == True):
            devam=1
        else:
            global senditmms
            senditmms=0
    global onshare
    onshare=0
    oku()
    e32.ao_yield()

def sendoff():
    global senditblue
    senditblue=0
    global senditmms
    senditmms=0
    appuifw.note(ru(lang(114)), 'conf')    

def sendblue():
    appuifw.note(ru(lang(115)))
    if (appuifw.query(ru(lang(116)), 'query') == True):
        appuifw.note(ru(lang(117)))
        try:
            global address
            address, services = socket.bt_obex_discover()
        except:
            appuifw.note(u"OBEX Push not available", "error")
            return
        
    if u'OBEX Object Push' in services:
            global channel
            channel = services[u'OBEX Object Push']
            global senditblue
            senditblue=1        
            appuifw.note(ru(lang(118)), 'conf') 

    else:
        appuifw.note(ru(lang(119)), 'error')
  
def sendmms():
    global number
    number=appuifw.query(ru(lang(120)), "text")
    if number:
        global text
        text=appuifw.query(ru(lang(121)), "text")
        if text:
            if (appuifw.query(ru(lang(122)), 'query') == True):
                b4()  
                global senditmms
                senditmms=1
                appuifw.note(ru(lang(123)), 'conf')
            else: 
                appuifw.note(ru(lang(124)), 'error')                
        else:
            appuifw.note(ru(lang(124)), 'error')         
    else:
        appuifw.note(ru(lang(124)), 'error') 
        
def findfile(folder, file_extension):
    p=[]
    stack = [(folder, os.listdir(folder))]
    while stack:
        folder, names = stack[-1]
        while names:
            name = names.pop()
            path = os.path.join(folder, name)
            if os.path.isfile(path):
                if name.lower().endswith(".jpg"):
                    p.append(path)
            elif os.path.isdir(path):
                stack.append((path, os.listdir(path)))
                break
        else:
            stack.pop()
    return p
    
def edeara():
    sendblue()
    if senditblue==1:
        file_extension="jpg"
        path = findfile('E:\\', file_extension.lower())
 
    # Display the path or error message if not found
        if path is None:
            appuifw.note(ru(lang(125)))
        else:
            for i in path:
	          global sharingnow
           	  sharingnow=i
	          global showshrfile
	          showshrfile=1
                  file=i
                  e32.ao_yield()
                  try:
                     socket.bt_obex_send_file(address,channel,file) 
                  except: 
                      appuifw.note(ru(lang(126))) 

def cdeara():
    sendblue()
    if senditblue==1:
        file_extension="jpg"
        path = findfile('C:\\', file_extension.lower())
 
    # Display the path or error message if not found
        if path is None:
            appuifw.note(ru(lang(125)))
        else:
            for file in path:
                socket.bt_obex_send_file(address, channel, file)
           #     except: 
            #        appuifw.note(ru(lang(126))) 
            
class Filebrowser:
    def __init__(self):
        self.script_lock = e32.Ao_lock()
        self.dir_stack = []
        self.current_dir = dir_iter.Directory_iter(e32.drive_list())

    def run(self):
        from key_codes import EKeyLeftArrow
        entries = self.current_dir.list_repr()
        if not self.current_dir.at_root:
            entries.insert(0, (u"..", u""))
        self.lb = appuifw.Listbox(entries, self.lbox_observe)
        self.lb.bind(EKeyLeftArrow, lambda: self.lbox_observe(0))
        old_title = appuifw.app.title
        self.refresh()
        self.script_lock.wait()
        appuifw.app.title = old_title
        appuifw.app.body = None
        self.lb = None

    def refresh(self):
        appuifw.app.title = u"File Browser"
        appuifw.app.menu = []
        appuifw.app.exit_key_handler = self.exit_key_handler
        appuifw.app.body = self.lb

    def do_exit(self):
        global quitto
        quitto=1
        viewrestart()

    def exit_key_handler(self):
        global quitto
        quitto=1
        viewrestart()


    def lbox_observe(self, ind = None):
        if not ind == None:
            index = ind
        else:
            index = self.lb.current()
        focused_item = 0

        if self.current_dir.at_root:
            self.dir_stack.append(index)
            self.current_dir.add(index)
        elif index == 0:                              # ".." selected
            focused_item = self.dir_stack.pop()
            self.current_dir.pop()
        elif os.path.isdir(self.current_dir.entry(index-1)):
            self.dir_stack.append(index)
            self.current_dir.add(index-1)
        else:
            item = self.current_dir.entry(index-1)
            if os.path.splitext(item)[1] == '.jpg':
                i = appuifw.popup_menu([ru("Resmi Aç"), ru("Resmi Sil")])
            else:
                i = appuifw.popup_menu([ru("Dosyayı Aç"), ru("Dosyayı Sil")])
            if i == 0:
                if os.path.splitext(item)[1].lower() == u'.jpg':
                    try:
                        appuifw.Content_handler().open(item)
                    except:
                        import sys
                        type, value = sys.exc_info() [:2]
                        appuifw.note(unicode(str(type)+'\n'+str(value)), "info")
                    #appuifw.Content_handler().open_standalone(item)
                else:
                    try:
                        appuifw.Content_handler().open(item)
                    except:
                        import sys
                        type, value = sys.exc_info() [:2]
                        appuifw.note(unicode(str(type)+'\n'+str(value)), "info")
                return
            elif i == 1:
                os.remove(item)
                focused_item = index - 1
            elif i == 2:
                socket.bt_obex_send_file(address, channel, item)
                focused_item = index - 1                

        entries = self.current_dir.list_repr()
        if not self.current_dir.at_root:
            entries.insert(0, (u"..", u""))
        self.lb.set_list(entries, focused_item)

def paylasimmerkezi():
    global bilgi
    bilgi=0
    global uishownow
    uishownow=sharecenterui
    camera.stop_finder()
    Filebrowser().run()


def cozunurlukmenusu():
    if model=="N70-1":
        appuifw.app.menu = [(ru(lang(6)), menufonk), (u'LP 3 MP(Extra RAM)',lp30mp), (u'LP 2.9 MP(Extra RAM)',lp29mp), (u'LP 2.8 MP(Not Recom.)',lp28mp), (u'LP 2.7 MP(Not Recom.)',lp27mp), (u'LP 2.6 MP',lp26mp), (u'LP 2.5 MP',lp25mp), (u'LP 2.4 MP',lp24mp), (u'LP 2.3 MP',lp23mp), (u'LP 2.2 MP',lp22mp), (u'LP 2.1 MP',lp21mp), (u'1600x1200 (2 MP)',b1), (u'1024x768',b2), (u'800x600',b3), (u'640x480',b4)]
    elif model=="N70-5":
        appuifw.app.menu = [(ru(lang(6)), menufonk), (u'LP 3 MP(Extra RAM)',lp30mp), (u'LP 2.9 MP(Extra RAM)',lp29mp), (u'LP 2.8 MP(Not Recom.)',lp28mp), (u'LP 2.7 MP(Not. Recom.)',lp27mp), (u'LP 2.6 MP',lp26mp), (u'LP 2.5 MP',lp25mp), (u'LP 2.4 MP',lp24mp), (u'LP 2.3 MP',lp23mp), (u'LP 2.2 MP',lp22mp), (u'LP 2.1 MP',lp21mp), (u'1600x1200 (2 MP)',b1), (u'1024x768',b2), (u'800x600',b3), (u'640x480',b4)]
    elif model=="N72-5":
        appuifw.app.menu = [(ru(lang(6)), menufonk), (u'LP 2.5 MP',lp25mp), (u'LP 2.4 MP',lp24mp), (u'LP 2.3 MP',lp23mp), (u'LP 2.2 MP',lp22mp), (u'LP 2.1 MP',lp21mp), (u'1600x1200 (2 MP)',b1), (u'1024x768',b2), (u'800x600',b3), (u'640x480',b4)]  
    elif model=="N90-1":
        appuifw.app.menu = [(ru(lang(6)), menufonk), (u'LP 2.5 MP',lp25mp), (u'LP 2.4 MP',lp24mp), (u'LP 2.3 MP',lp23mp), (u'LP 2.2 MP',lp22mp), (u'LP 2.1 MP',lp21mp), (u'1600x1200 (2 MP)',b1), (u'1024x768',b2), (u'800x600',b3), (u'640x480',b4)]  
    else:
        cozunurlukler=[]
        for coz in mumkunboyutlar:
            a,b=coz
            cozunur=str(a)+u"x"+str(b)
            cozunurlukler.append(cozunur)
        i=appuifw.selection_list(choices=cozunurlukler)
        global boyut     
        boyut=mumkunboyutlar[i] 
        appuifw.note(ru(lang(94)), 'conf')    

def rnknormal():
    global sb
    sb=0
def rnkgray():
    global sbimage
    sbimg=Image.new((276, 208), 'L')
    global sb
    sb=1

def rnkwb():
    global sbimage
    sbimg=Image.new((276, 208), '1')
    global sb
    sb=2

def editbefore():
    appuifw.app.menu = [(ru(lang(6)), menufonk), (ru(lang(190)), cercevesec), (ru(lang(191)), ((ru(lang(192)), rnknormal), (ru(lang(195)), rnkwb), (ru(lang(193)), rnkgray))), (ru(lang(55)), ((ru(lang(7)), metinonoff), (ru(lang(56)), metingir))), (ru(lang(57)), ((ru(lang(4)), rotkapali), (ru(lang(58)), rot90der), (ru(lang(59)), rot180der), (ru(lang(60)), rot270der), (ru(lang(61)), rotyatay), (ru(lang(62)), rotdikey))), (ru(lang(63)), ((u"%100", netlik100),(u"%70", netlik70),(u"%50", netlik50),(u"%30", netlik30),(u"%10", netlik10))), (ru(lang(64)), ((u"4.096", rgb12), (u"65.536", rgb16), (u"16.700.000", rgbfull))), (ru(lang(65)), ((ru(lang(66)), yer), (ru(lang(67)), trhekle)))]  
redgoz=0
def paylasimmenusu():
    appuifw.app.menu = [(ru(lang(6)), menufonk), (ru(lang(177)), ((ru(lang(4)),sendoff),(ru(lang(68)),sendblue),(ru(lang(69)),sendmms))), (ru(lang(70)),paylasimmerkezi)]
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
        self._iFotoTur = [ru(lang(50)), ru(lang(49)), ru(lang(164))]
        self._iKayitYeri = [ru(lang(52)), ru(lang(53))]
        self._iResimFormat = [u'JPG', u'PNG']
        ## Form fields.
        self._iFields = [( ru(lang(178)), 'combo', ( self._iCekim, 0 ) ),
                         ( ru(lang(42)), 'combo', ( self._iKayitMod, 0 ) ),
                         ( ru(lang(48)), 'combo', ( self._iFotoTur, 0 ) ),
                         ( ru(lang(51)), 'combo', ( self._iKayitYeri, 1 ) ),    
                         ( ru(lang(54)), 'combo', ( self._iResimFormat, 0 ) ),                       
                         ]
 
 
    ## Displays the form.
    def setActive( self ):
        self._iIsSaved = False
        self._iForm = appuifw.Form(self._iFields, appuifw.FFormEditModeOnly)
        self._iForm.save_hook = self._markSaved
        self._iForm.flags = appuifw.FFormAutoLabelEdit
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
 
 
    ## Return model field value..
    def getKayitModu( self ):
        ## This returns the mobile; In one case I needed to have UTF-8 encoding
        return self._iForm[1][2][1]

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
        if myForm.getKayitModu( )==0:
            activesave()
        else:
            passivesave() 
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
        (ru(lang(10)), dizimodu), 
        (ru(lang(14)), cozunurlukmenusu), 
        (ru(lang(15)), ((ru(lang(4)),sifir), (ru(lang(17)),onn), (ru(lang(20)),ellezamanla))),
        (ru(lang(21)), ((ru(lang(2)),flau), (ru(lang(3)),flon), (ru(lang(4)),floff))),  
        (ru(lang(22)), ((ru(lang(2)),nrm2), (ru(lang(23)),gece), (ru(lang(163)),portre))),
        (ru(lang(24)), ((ru(lang(2)),whitebal1), (ru(lang(25)),whitebal2), (ru(lang(26)),whitebal3), (ru(lang(27)),whitebal4), (ru(lang(28)),whitebal5))), 
        (ru(lang(29)), redeye), 
        (ru(lang(30)), zmod), (ru(lang(31)), paylasimmenusu), 
        (ru(lang(32)), setsup),
        (ru(lang(33)), editbefore),
        (ru(lang(39)), update),
        (ru(lang(40)), hakkinda)]
    else:
        appuifw.app.menu = [
        (ru(lang(8)), video), 
        (ru(lang(10)), dizimodu), 
        (ru(lang(14)), cozunurlukmenusu), 
        (ru(lang(15)), ((ru(lang(4)),sifir), (ru(lang(17)),onn), (ru(lang(20)),ellezamanla))),
        (ru(lang(21)), ((ru(lang(2)),flau), (ru(lang(3)),flon), (ru(lang(4)),floff))),  
        (ru(lang(22)), ((ru(lang(2)),nrm2), (ru(lang(23)),gece), (ru(lang(163)),portre))),
        (ru(lang(24)), ((ru(lang(2)),whitebal1), (ru(lang(25)),whitebal2), (ru(lang(26)),whitebal3), (ru(lang(27)),whitebal4), (ru(lang(28)),whitebal5))), 
        (ru(lang(29)), redeye), 
        (ru(lang(30)), zmod), (ru(lang(31)), paylasimmenusu), 
        (ru(lang(32)), setsup),
        (ru(lang(33)), editbefore),
        (ru(lang(39)), update),
        (ru(lang(40)), hakkinda)]    
#    appuifw.app.menu = [(u'Video Modu 1', video), (u'Ikinci Kaamera', ikincikamera), (u'Cozunurluk Menusu', cozunurlukmenusu), ((u'Dizi Modu'), ((u'2 Fotograf',dizi2),(u'4 Fotograf',dizi4),(u'6 Fotograf',dizi6))), ((u'Kirmizi Goz Giderme'), ((u'Acik',redeye),(u'Kapali',redeyeoff))), ((u'Zamanlayici'), ((u'Kapali',sifir),(u'5 saniye',bes),(u'10 saniye',onn),(u'20 saniye',yirmi),(u'30 saniye',otuz),(u'Elle Ayarla',ellezamanla))), ((u'Flash Modu'), ((u'Otomatik',flau),(u'Zorunlu',flon),(u'Kapali',floff))), ((u'Cekim Modu'), ((u'Otomatik',nrm2),(u'Gece',gece))), ((u'Beyaz Dengesi'), ((u'Otomatik',whitebal1),(u'Gun Isigi',whitebal2),(u'Bulutlu',whitebal3),(u'Flouresant',whitebal4),(u'Tungsten',whitebal5))), (u'Yakinlastirma', zmod), (u'Hizli Paylas Menusu', paylasimmenusu), (u'Ayarlar', setsup), (u'EditBefore', editbefore)]
 
 

#Canvas resimlerini yukle
katsayi=278
e32.ao_yield()

dslider = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sliders\\dslider.ui")
predsmask = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sliders\\dslider_mask.ui")
dsmask=Image.new(dslider.size, 'L')
dsmask.blit(predsmask)
dmarker = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sliders\\dmarker.ui")
e32.ao_yield()
predmmask = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sliders\\dmarker_mask.ui")
dmmask=Image.new(dmarker.size, 'L')
dmmask.blit(predmmask)
#yatay
e32.ao_yield()
yslider = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sliders\\yslider.ui")
preysmask = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sliders\\yslider_mask.ui")
ysmask=Image.new(yslider.size, 'L')
ysmask.blit(preysmask)
ymarker = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sliders\\ymarker.ui")
e32.ao_yield()
preymmask = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sliders\\ymarker_mask.ui")
ymmask=Image.new(dmarker.size, 'L')
ymmask.blit(preymmask)
e32.ao_yield()

lpmodeui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\lp.ui")
redeyeoffui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\redeye.ui")
redeyeonui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\blackeye.ui")
fautoui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\fauto.ui")
fforcedui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\fforced.ui")
e32.ao_yield()
redeyeonui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\blackeye.ui")
foffui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\foff.ui")
cotoui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\coto.ui")
cnightui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\cnight.ui")
e32.ao_yield()
wautoui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\wauto.ui")
wsunui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\wsun.ui")
wcloudui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\wcloud.ui")
wtungstenui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\wtungsten.ui")
wflourui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\wflour.ui")
syncui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sync.ui")
e32.ao_yield()



sharecenterui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\sharecenter.ui")
diziui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\dizi.ui")
#yatay
lpmodeuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\lp.ui")
redeyeoffuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\redeye.ui")
redeyeonuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\blackeye.ui")
fautouiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\fauto.ui")
fforceduiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\fforced.ui")
e32.ao_yield()
redeyeonuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\blackeye.ui")
foffuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\foff.ui")
cotouiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\coto.ui")
cnightuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\cnight.ui")
wautouiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\wauto.ui")
wsunuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\wsun.ui")
wclouduiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\wcloud.ui")
wtungstenuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\wtungsten.ui")
wflouruiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\wflour.ui")
e32.ao_yield()
portreuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\portre.ui")
diziuiy = Image.open("E:\\System\\Apps\\TamEkran\\ui\\yatay\\dizi.ui")
def registernow():
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\browser\\browser.app "file://e:/system/apps/TamEkran/register.html"')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\browser\\browser.app "file://e:/system/apps/TamEkran/register.html"')
    os.abort()        
def elleact():
    gserial=appuifw.query(ru("Enter serial (activation) code"), 'number')

    imei=str(sysinfo.imei())
    if len(imei)!=15:
        appuifw.note(ru("Wrong IMEI"))
        os.abort()
    hbir=imei.count(str(2))
    hiki=imei.count(str(8))
    huc=imei.count(str(1))
    hdort=imei.count(str(9))
    snobir=str(hbir)+str(hiki)+str(huc)+str(hdort)
    serialno=int(snobir)+1992
    if gserial==serial:
        try:
            e32.file_copy("E:\\System\\libs\\ilicense.py", "E:\\System\\Apps\\TamEkran\\ilicense")
        except:
            pass
        textserial="global imei\nimei="+str(imei)+"\nglobal serialno\nserialno="+str(serialno)
        f = file("E:\\System\\libs\\ilicense.py", "w") 
        print >> f, textserial
        f.close()
        appuifw.note(ru(lang(184)))
        os.abort()
    else:
        appuifw.note(ru("Wrong code"), 'error')
def signnow():
    camera.stop_finder()
    


def activate(): #function to send the data to the server.
    camera.stop_finder()
    acten = Image.open("E:\\System\\Apps\\TamEkran\\ui\\wizard\\act_en.ui")
    acttr= Image.open("E:\\System\\Apps\\TamEkran\\ui\\wizard\\act_tr.ui")
    if prgdili=='e:\\System\\Apps\\TamEkran\\langs\\Turkish.lang':
        canvas.blit(acttr)
    else:
        canvas.blit(acttr)
    global bilgi
    bilgi=0
    appuifw.app.menu=[(ru("Sign In (Giriş Yap)"), signnow), (ru("Register (Kayıt Ol)"), registernow)]



def licensecontrol():
    imei=str(sysinfo.imei())   
    if len(imei)!=15:
        appuifw.note(ru("Wrong IMEI"))
        os.abort()
   
licensecontrol()         
def ybaslat():
    miso.restart_phone()

onshare=0
wbm='auto'
gmode='auto'
mzoom=1
redgoz=0
fmode='auto'
showshrfile=0
mumkunboyutlar=camera.image_sizes()
boyut=mumkunboyutlar[0]
largepixels=0
bekle=0.1
senditblue=0
senditmms=0
rotate=0

tarihibul()
load_cells2()
load_cells()
show_location()
photo = camera.take_photo(size=(640,480), position=0)  
e32.ao_yield()
start( )
anakamera()
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
    kaydet()
    global quitto
    quitto=1
    e32.ao_sleep(0.2)
    global quitto
    quitto=1


running=1
#ozellikleri canvas uzerine ciz, az ugrasmadim bunun icin meger unicode yapmak lazimmis :P         

           


appuifw.app.exit_key_handler=quit
calis=1


#Sihirbazı başlatır ya da başlatmaz.



#bunlar da tuslarin tanimlanmasi
running=1

   
while calis==1:

    if keyboard.pressed(EScancodeSelect):
        if kamera==2:
            ikincicek()

        else:  
            fotocek()
    if keyboard.pressed(EScancode1):
        video()
        
    
    if keyboard.pressed(EScancode3):
        setsup()             
    
    if keyboard.pressed(EScancode7):
        trhekle()    

    if keyboard.pressed(EScancode6):
        if kamera==2:
            appuifw.note(ru(lang(127)), 'error') 
        else:
            redeye()
        
    if keyboard.pressed(EScancodeHash):
        if bilgi==1:
            global bilgi
            bilgi=2
            kaydet()
        elif bilgi==2:
            global bilgi
            bilgi=1
            kaydet()
    if keyboard.pressed(EScancodeStar):
        yer()

    if keyboard.pressed(EScancodeDownArrow):
        if kamera==2:
            appuifw.note(ru(lang(127)), 'error') 
        else:
            if bilgi==1:
                zazalt()

    if keyboard.pressed(EScancodeLeftArrow):
        if kamera==2:
            appuifw.note(ru(lang(127)), 'error') 
        else:
            if bilgi==2:
                zazalt()

    if keyboard.pressed(EScancodeRightArrow):
        if kamera==2:
            appuifw.note(ru(lang(127)), 'error') 
        else:
            if bilgi==2:
                zarttir()

    if keyboard.pressed(EScancodeUpArrow):
        if kamera==2:
            appuifw.note(ru(lang(127)), 'error') 
        else:
            if bilgi==1:
                zarttir()
        
    if keyboard.pressed(EScancode9):
        metinonoff()
           
    if keyboard.pressed(EScancode8):
        metingir()
        
       
    handle_redraw(())    
# yeter artik kullanici girisini bekle        
    e32.ao_yield()
   
SCRIPT_LOCK.wait( )

