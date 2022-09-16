#Traductor. Aurora Gómez 2022.
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from googletrans import Translator, constants
import tkinter.font as font

languages = {
    'af': 'Afrikáans',
    'sq': 'Albanés',
    'am': 'Amhárico',
    'ar': 'Árabe',
    'hy': 'Armenio',
    'az': 'Azerí',
    'eu': 'Vasco',
    'be': 'Bielorruso',
    'bn': 'Bengalí',
    'bs': 'Bosnio',
    'bg': 'Búlgaro',
    'ca': 'Catalán',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chino (simplificado)',
    'zh-tw': 'Chino (tradicional)',
    'co': 'Corso',
    'hr': 'Croata',
    'cs': 'Checo',
    'da': 'Danés',
    'nl': 'Neerlandés',
    'en': 'Inglés',
    'eo': 'Esperanto',
    'et': 'Estonio',
    'tl': 'Filipino',
    'fi': 'Finés',
    'fr': 'Francés',
    'fy': 'Frisio',
    'gl': 'Gaélico',
    'ka': 'Georgiano',
    'de': 'Alemán',
    'el': 'Griego',
    'gu': 'Gujaratí',
    'ht': 'Criollo haitiano',
    'ha': 'Hausa',
    'haw': 'Hawaiano',
    'iw': 'Hebreo',
    'he': 'Hebreo',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Húngaro',
    'is': 'Islandés',
    'ig': 'Igbo',
    'id': 'Indonesio',
    'ga': 'Irlandés',
    'it': 'Italiano',
    'ja': 'Japonés',
    'jw': 'Javanés',
    'kn': 'Canarés',
    'kk': 'Kazajo',
    'km': 'Khmer',
    'ko': 'Coreano',
    'ku': 'Kurdo (kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latín',
    'lv': 'Letón',
    'lt': 'Lituano',
    'lb': 'Luxemburgués',
    'mk': 'Macedonio',
    'mg': 'Malgache',
    'ms': 'Malayo',
    'ml': 'Malayalam',
    'mt': 'Maltés',
    'mi': 'Maorí',
    'mr': 'Marathi',
    'mn': 'Mongol',
    'my': 'Myanmar',
    'ne': 'Nepalí',
    'no': 'Noruego',
    'or': 'Odia',
    'ps': 'Pashto',
    'fa': 'Persa',
    'pl': 'Polaco',
    'pt': 'Portugués',
    'pa': 'Punjabi',
    'ro': 'Rumano',
    'ru': 'Ruso',
    'sm': 'Samoa',
    'gd': 'Gaelico escocés',
    'sr': 'Serbio',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Eslovaco',
    'sl': 'Esloveno',
    'so': 'Somalí',
    'es': 'Español',
    'su': 'Sundanés',
    'sw': 'Swahili',
    'sv': 'Sueco',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Tailandés',
    'tr': 'Turco',
    'uk': 'Ucraniano',
    'ur': 'Urdu',
    'ug': 'Uigur',
    'uz': 'Uzbeco',
    'vi': 'Vietnamita',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'}

idioma1 = ""
idioma2 = ""
translator = Translator()
ventana = Tk()
ventana.geometry("920x300")
ventana.resizable(width=False, height=False)
ventana.title('Translate')
myFont = font.Font(family='Times New Roman',size=12)
myFont2 = font.Font(family='Times New Roman',size=13)
style = ttk.Style()
style.configure('TButton', font=('Times New Roman', 12))
texto1 = Text(ventana, font=myFont2, width=47, height=11)
texto2 = Text(ventana, font=myFont2, width=50, height=11)
combo1 = ttk.Combobox(ventana,state="readonly",font=myFont,width=20,values=['Automático','Inglés','Español','Francés','Portugués', 'Alemán', 'Italiano', 'Catalán', 'Rumano', 'Latín', 'Japonés', 'Chino', 'Coreano', 'Árabe',
        'Neerlandés', 'Afrikáans', 'Hebreo', 'Griego', 'Noruego', 'Sueco', 'Danés', 'Islandés', 'Finés', 'Ruso', 'Ucraniano', 'Turco', 'Indonesio', 'Checo', 'Esperanto', 'Hindi', 'Urdu', 'Persa', 'Filipino'])
combo2 = ttk.Combobox(ventana,state="readonly",font=myFont,width=20,values=['Inglés','Español','Francés', 'Portugués', 'Alemán', 'Italiano', 'Catalán', 'Latín','Japonés', 'Chino', 'Coreano', 'Árabe',
        'Neerlandés', 'Afrikáans', 'Hebreo', 'Griego', 'Noruego', 'Sueco', 'Danés', 'Islandés', 'Finés', 'Ruso', 'Ucraniano', 'Turco', 'Indonesio', 'Checo', 'Esperanto','Hindi','Urdu','Persa', 'Filipino'])
label = Label(ventana,font=myFont2,text="")
def primero():
    global idioma1
    idioma1 = combo1.get()
    if idioma1 == "Automático":
        idioma1 = "autom"
    elif idioma1 == "Inglés":
        idioma1 = "en"
    elif idioma1 == "Español":
        idioma1 = "es"
    elif idioma1 == "Francés":
        idioma1 = "fr"
    elif idioma1 == "Portugués":
        idioma1 = "pt"
    elif idioma1 == "Filipino":
        idioma1 = "tl"
    elif idioma1 == "Alemán":
        idioma1 = "de"
    elif idioma1 == "Italiano":
        idioma1 = "it"
    elif idioma1 == "Catalán":
        idioma1 = "ca"
    elif idioma1 == "Rumano":
        idioma1 = "ro"
    elif idioma1 == "Latín":
        idioma1 = "la"
    elif idioma1 == "Japonés":
        idioma1 = "ja"
    elif idioma1 == "Chino":
        idioma1 = "zh-cn"
    elif idioma1 == "Coreano":
        idioma1 = "ko"
    elif idioma1 == "Neerlandés":
        idioma1 = "nl"
    elif idioma1 == "Afrikáans":
        idioma1 = "af"
    elif idioma1 == "Árabe":
        idioma1 = "ar"
    elif idioma1 == "Hebreo":
        idioma1 = "he"
    elif idioma1 == "Griego":
        idioma1 = "el"
    elif idioma1 == "Noruego":
        idioma1 = "no"
    elif idioma1 == "Sueco":
        idioma1 = "sv"
    elif idioma1 == "Danés":
        idioma1 = "da"
    elif idioma1 == "Islandés":
        idioma1 = "is"
    elif idioma1 == "Finés":
        idioma1 = "fi"
    elif idioma1 == "Ruso":
        idioma1 = "ru"
    elif idioma1 == "Ucraniano":
        idioma1 = "uk"
    elif idioma1 == "Turco":
        idioma1 = "tr"
    elif idioma1 == "Indonesio":
        idioma1 = "id"
    elif idioma1 == "Checo":
        idioma1 = "cs"
    elif idioma1 == "Esperanto":
        idioma1 = "eo"
    elif idioma1 == "Hindi":
        idioma1 = "hi"
    elif idioma1 == "Urdu":
        idioma1 = "ur"
    elif idioma1 == "Persa":
        idioma1 = "fa"
def segundo():
    global idioma2
    idioma2 = combo2.get()
    if idioma2 == "Inglés":
        idioma2 = "en"
    elif idioma2 == "Español":
        idioma2 = "es"
    elif idioma2 == "Francés":
        idioma2 = "fr"
    elif idioma2 == "Portugués":
        idioma2 = "pt"
    elif idioma2 == "Filipino":
        idioma2 = "tl"
    elif idioma2 == "Alemán":
        idioma2 = "de"
    elif idioma2 == "Italiano":
        idioma2 = "it"
    elif idioma2 == "Catalán":
        idioma2 = "ca"
    elif idioma2 == "Rumano":
        idioma2 = "ro"
    elif idioma2 == "Latín":
        idioma2 = "la"
    elif idioma2 == "Japonés":
        idioma2 = "ja"
    elif idioma2 == "Chino":
        idioma2 = "zh-cn"
    elif idioma2 == "Coreano":
        idioma2 = "ko"
    elif idioma2 == "Neerlandés":
        idioma2 = "nl"
    elif idioma2 == "Afrikáans":
        idioma2 = "af"
    elif idioma2 == "Árabe":
        idioma2 = "ar"
    elif idioma2 == "Hebreo":
        idioma2 = "he"
    elif idioma2 == "Griego":
        idioma2 = "el"
    elif idioma2 == "Noruego":
        idioma2 = "no"
    elif idioma2 == "Sueco":
        idioma2 = "sv"
    elif idioma2 == "Danés":
        idioma2 = "da"
    elif idioma2 == "Islandés":
        idioma2 = "is"
    elif idioma2 == "Finés":
        idioma2 = "fi"
    elif idioma2 == "Ruso":
        idioma2 = "ru"
    elif idioma2 == "Ucraniano":
        idioma2 = "uk"
    elif idioma2 == "Turco":
        idioma2 = "tr"
    elif idioma2 == "Indonesio":
        idioma2 = "id"
    elif idioma2 == "Checo":
        idioma2 = "cs"
    elif idioma2 == "Esperanto":
        idioma2 = "eo"
    elif idioma2 == "Hindi":
        idioma2 = "hi"
    elif idioma2 == "Urdu":
        idioma2 = "ur"
    elif idioma2 == "Persa":
        idioma2 = "fa"

def ttlang():
    global translator
    primero()
    segundo()
    global idioma1
    global idioma2
    global texto1
    global texto2
    global label
    traduciendo = texto1.get('1.0',END)
    if idioma1 == "autom":
        translation = translator.translate(traduciendo, dest=idioma2)
        traduccion = f"{translation.text}"
        idioma = f"{translation.src}"
        label['text'] = "Traducido del " + languages[idioma]
        texto2.delete('1.0',END)
        texto2.insert('1.0',traduccion)
    else:
        translation = translator.translate(traduciendo, src=idioma1,dest=idioma2)
        traduccion = f"{translation.text}"
        label['text'] = ""
        texto2.delete('1.0',END)
        texto2.insert('1.0',traduccion)

def change():
    global texto1
    global texto2
    l3 = combo1.get()
    l4 = combo2.get()
    t2 = texto2.get('1.0',END)
    combo1.set(l4)
    if l3 == "Automático":
        l3 = "Inglés"
        combo2.set(l3)
    else:
        combo2.set(l3)
    texto1.delete('1.0',END)
    texto2.delete('1.0',END)
    texto1.insert('1.0', t2)
    ttlang()
    
    
traduce = ttk.Button(ventana,text="Traducir", command=ttlang)
switch = ttk.Button(ventana, text="<->", command=change)
combo1.current(0)
combo2.current(1)
combo1.place(x=10,y=30)
combo2.place(x=450,y=30)
texto1.place(x=10, y=60)
texto2.place(x=450,y=60)
traduce.place(x=650,y=28)
switch.place(x=750,y=28)
label.place(x=195,y=30)

ventana.mainloop()