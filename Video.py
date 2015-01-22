#Video recorder module for TE

import e32, camera, appuifw, key_codes, os, appswitch, time, location, miso, sysinfo, firmware
from graphics import *
from time import *
from e32db import format_time
appuifw.app.screen='full'

try:
    import miso
except:
    appuifw.note(u"cannot import miso module")

try:
    miso.set_process_priority(150)
except:
    pass    
try:
   appswitch.end_app(u"FullScreen")
except:
   pass   
   

try:
   appswitch.end_app(u"TamEkran")
except:
   pass   
   


try:
   appswitch.end_app(u"Kamera")
except:
   pass   
   
   
try:
   appswitch.end_app(u"Camera")
except:
   pass   
   
def ru(x):return x.decode('utf-8')
control_light=0
videodir=u"e:\\Videos\\"
adturu="metin"
admetni="Video"
dosyaturu=".mp4"
tevideodir="e:\\Images\\"
teadturu="metin"
teadmetni="Photo"
tedosyaturu=".jpg"
onrecord=0
teactivesaving=1
firstrun=0
bilgi=1
def oku():
    CONFIG_FILE='E:/System/Apps/TamEkran/mysettings.txt'
    try:
        f=open(CONFIG_FILE,'rt')
        try:
            content = f.read()
            config=eval(content)
            f.close()
            global teadmetni
            teadmetni=config.get('variable1','')
            global adturu
            teadturu=config.get('variable2','')
            global videodir
            tevideodir=config.get('variable3','')
            global dosyaturu
            tedosyaturu=config.get('variable4','')            
            global admetni
            admetni=config.get('variable5','')
            global adturu
            adturu=config.get('variable6','')
            global videodir
            videodir=config.get('variable7','')
            global dosyaturu
            dosyaturu=config.get('variable8','')
            global prgdili
            prgdili=config.get('variable9','')
            global teactivesaving
            teactivesaving=config.get('variable10','')            
            #TE verileri al because of onlar da kaydedilemk zorunda
            global firstrun
            firstrun=config.get('variable11','')          
            global bilgi
            bilgi=config.get('variable12','')   
        except:
            print 'dosya okunamiyor'
    except:
        print 'dosya acilamiyor'




def kaydet():
    CONFIG_DIR='E:/System/Apps/TamEkran/'
    CONFIG_FILE=os.path.join(CONFIG_DIR,'mysettings.txt')
    if not os.path.isdir(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
        CONFIG_FILE=os.path.join(CONFIG_DIR,'mysettings.txt')      
    config={}
    config['variable1']= teadmetni
    config['variable2']= teadturu
    config['variable3']= tevideodir
    config['variable4']= tedosyaturu
    #Variables of video recorderin
    config['variable5']= admetni
    config['variable6']= adturu
    config['variable7']= videodir
    config['variable8']= dosyaturu
    config['variable9']= prgdili
    config['variable10']= teactivesaving
    config['variable11']= firstrun
    config['variable12']= bilgi          
    f=open(CONFIG_FILE,'wt')
    f.write(repr(config))
    f.close()
    oku()
    
 
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
 
        os.path.walk(self.dir,iter,self)
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
    
zaman=0    


timer = e32.Ao_timer()     
INTERVAL = 1.0 
mzoom=0 


def zarttir():
    if mzoom >= 61:
        global mzoom
        appuifw.note(ru(lang(86)), 'error')
    else:
        global mzoom
        mzoom=mzoom+10    
        uygula()

def zazalt():
    if mzoom <= 9:
        global mzoom
        appuifw.note(ru(lang(87)), 'error')
    else:
        global mzoom
        mzoom=mzoom-10    
        uygula()
        
def uygula():
    camera.stop_finder()
    photo = camera.take_photo(zoom=mzoom, position=0)
    photo.save("c:\\system\\temp.jpg", quality=10, compression='fast')
    camera.start_finder(vfCallback, backlight_on=1, size=(320, 240))

def onad():
    global admetni
    admetni=appuifw.query(ru(lang(130)), "text")
    kaydet()
    
def admetin():
    global adturu
    adturu = "metin"
    kaydet()
    onad()    
    
def adtarih():
    global adturu
    adturu = "tarih"
    kaydet()
    appuifw.note(ru(lang(131)), 'conf')

def ikincikamera():
    global kamera
    kamera=2
    camera.stop_finder()
    photo = camera.take_photo(position=1)
    photo.save("c:\\system\\temp.jpg", quality=10, compression='fast')
    camera.start_finder(vfCallback, backlight_on=1, size=(320, 240))
    ikincimenu()
    canvas.bind(key_codes.EKeyUpArrow, kullanilamaz)
    canvas.bind(key_codes.EKeyDownArrow, kullanilamaz)
def anakamera():
    global kamera
    kamera=1
    camera.stop_finder()
    photo = camera.take_photo(position=0)
    photo.save("c:\\system\\temp.jpg", quality=10, compression='fast')
    camera.start_finder(vfCallback, backlight_on=1, size=(320, 240))
    menu()
    canvas.bind(key_codes.EKeyUpArrow, zarttir)
    canvas.bind(key_codes.EKeyDownArrow, zazalt)
    
def adbelirle():
    if adturu=="metin":
        global value1
        value1 = admetni
    else:
        global value1
        value1 = tarihad

def tarihadi():
    t = time()
    format_time(t)   # for Symbian SQL
    global tarihad
    tarihad = strftime('%d %m %Y %H %M %S')

def empidort():
    global dosyaturu
    dosyaturu=".mp4"
    kaydet()
    
def ucgepe():
    global dosyaturu
    dosyaturu=".3gp"
    kaydet()


def hafizakarti():
    global videodir
    videodir=u"e:\\Videos\\"
    kaydet()
    appuifw.note(ru(lang(132)), 'conf')
    
def telhafizasi():
    global videodir
    videodir=u"c:\\Nokia\\Videos\\"
    kaydet()
    appuifw.note(ru(lang(133)), 'conf')    
        
def goruntu():
    if onrecord==1:
        stop_video()
    camera.stop_finder()
    camera.release()
    app_lock.signal()
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\TamEkran\\TamEkran.app')
    try:
       appswitch.end_app(u"Video")
    except:
       pass
        

zaman=0
  
bilgi=1
def vfCallback( aIm ):
    global IMG
    if bilgi==0:
        appuifw.app.body.blit(uishownow)
    else:
        appuifw.app.body.blit(aIm,scale=1)
    if showshrfile==1:
        fshow=unicode(sharingnow)
        sharinnow=u""+fshow+""
        canvas.text((2,12),sharinnnow,255)
    if bilgi==1:
        if onrecord==1:
            appuifw.app.body.blit(vidrecui, target=(2,12))
    IMG = aIm
        
        
        
 
def cnvCallback( aRect=None ):
    if IMG != None:
        appuifw.app.body.clear( )
        appuifw.app.body.blit( IMG )


try:
    if not os.path.exists(videodir):  
        os.makedirs(videodir)
    else:
        pass
except:
    appuifw.note(ru(lang(134)), "error")  
 
def finder_cb(im):
    global control_light
    if control_light==1:
        im.point((240, 120), outline = (255, 0, 0), width = 25) 
    else:
        im.point((240, 120), outline = (0, 255, 0), width = 25) 
    canvas.blit(im)

def video_callback(err,current_state):
    global control_light   
    if current_state == camera.EPrepareComplete:
        global control_light
        control_light=1
    else:
        pass 

def start_video():
    global control_light
    control_light = 1 
    files=os.listdir(videodir)
    num = len(files) 
    filename = videodir+value1+unicode(num+1)+dosyaturu
    camera.start_record(filename,video_callback)  
    global onrecord
    onrecord=1     
    appuifw.app.menu = [(ru(lang(135)), stop_video)]
    canvas.bind(key_codes.EKeyUpArrow, kullanilamaz)
    canvas.bind(key_codes.EKeySelect, stop_video)
    canvas.bind(key_codes.EKeyDownArrow, kullanilamaz)
    
def stop_video():
    global control_light
    control_light = 0    
    camera.stop_record()
    global onrecord
    onrecord=0
    menu()
    canvas.bind(key_codes.EKeyUpArrow, zarttir)
    canvas.bind(key_codes.EKeyDownArrow, zazalt)
    canvas.bind(key_codes.EKeySelect, start_video)



#CellLocation Starts Here
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
        
        
#CellLocation Tamamlandi.

        
def quit():
    if onrecord==1:
        stop_video()
    camera.stop_finder()
    camera.release()
    app_lock.signal()
    try:
       appswitch.end_app(u"Video")
    except:
       pass
       
model=firmware.phone_model
     
def menu():
    if camera.cameras_available()==2:
        appuifw.app.menu = [(ru(lang(136)), start_video), (ru(lang(9)), ikincikamera), (ru(lang(137)), ((ru(lang(138)), onad), (ru(lang(139)), adtarih))), (ru(lang(140)), ((u'MP4', empidort), (u'3GP', ucgepe))), (ru(lang(141)), ((ru(lang(142)), telhafizasi), (ru(lang(143)), hafizakarti))), (ru(lang(144)), goruntu)]
    else:
        appuifw.app.menu = [(ru(lang(136)), start_video), (ru(lang(137)), ((ru(lang(138)), onad), (ru(lang(139)), adtarih))), (ru(lang(140)), ((u'MP4', empidort), (u'3GP', ucgepe))), (ru(lang(141)), ((ru(lang(142)), telhafizasi), (ru(lang(143)), hafizakarti))), (ru(lang(144)), goruntu)]
    

def ikincimenu():
    appuifw.app.menu = [(ru(lang(136)), start_video), (ru(lang(35)), anakamera), (ru(lang(137)), ((ru(lang(138)), onad), (ru(lang(139)), adtarih))), (ru(lang(140)), ((u'MP4', empidort), (u'3GP', ucgepe))), (ru(lang(141)), ((ru(lang(142)), telhafizasi), (ru(lang(143)), hafizakarti))), (ru(lang(144)), goruntu)]

def kullanilamaz():
    appuifw.note(ru(lang(161)), 'error')

canvas = appuifw.Canvas()
appuifw.app.body = canvas
calis=1

vidrecui = Image.open("E:\\System\\Apps\\TamEkran\\ui\\vidrec.ui")
startui = Image.open("E:\\System\\Apps\\TamEkran\\start.ui")
sharingnow=startui
showshrfile=0
bilgi=1    
oku()
tarihadi()
adbelirle()
load_cells2()
load_cells()
show_location()
menu()
camera.start_finder(vfCallback, backlight_on=1, size=(640, 480))
canvas.bind(key_codes.EKeySelect, start_video)
canvas.bind(key_codes.EKeyUpArrow, zarttir)
canvas.bind(key_codes.EKeyDownArrow, zazalt)
appuifw.app.title = ru(lang(145))
appuifw.app.exit_key_handler = quit
app_lock = e32.Ao_lock()
app_lock.wait()
