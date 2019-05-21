import tkinter
from tkinter import *
import langgenre

window = tkinter.Tk()

window.title("MOVIES FOR YOU")
window.geometry("1800x1000")

from functools import partial

def gen_horror():
    win1 = tkinter.Tk()
    win1.geometry("300x300")
    win1.title("Horror movies for you")
    horror_movies = langgenre.getGenre(27)
    for i in range (15):
        tkinter.Button(win1, command=partial(langgenre.getInfo, horror_movies.iloc[i]) ,text=horror_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)


    # tkinter.Label(win,text="bhu").grid(row=0,column=1)
def gen_action():
    win2 = tkinter.Tk()
    win2.geometry("300x300")
    win2.title("Action movies for you")
    action_movies = langgenre.getGenre(28)
    for i in range (15):
        tkinter.Button(win2, command=partial(langgenre.getInfo, action_movies.iloc[i]) ,text=action_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)


def gen_thrill():
    win3= tkinter.Tk()
    win3.geometry("300x300")
    win3.title("Thriller movies for you")
    thrill_movies = langgenre.getGenre(53)
    for i in range (15):
        tkinter.Button(win3, command=partial(langgenre.getInfo, thrill_movies.iloc[i]) ,text=thrill_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)


def gen_adventure():
    win4 = tkinter.Tk()
    win4.geometry("300x300")
    win4.title("Adventure movies for you")
    adventure_movies = langgenre.getGenre(12)
    for i in range (15):
        tkinter.Button(win4, command=partial(langgenre.getInfo, adventure_movies.iloc[i]) ,text=adventure_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)


def gen_comedy():
    win5 = tkinter.Tk()
    win5.geometry("300x300")
    win5.title("Comedy movies for you")
    comedy_movies = langgenre.getGenre(35)


    for i in range (15):
        tkinter.Button(win5, command=partial(langgenre.getInfo, comedy_movies.iloc[i]) ,text=comedy_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def show_popular():
    win6 = tkinter.Tk()
    win6.geometry("300x300")
    win6.title("Popular movies for you")
    popular_movies = langgenre.get_popular()

    for i in range (15):
        tkinter.Button(win6, command=partial(langgenre.getInfo, popular_movies.iloc[i]) ,text=popular_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def gen_ani():
    win15 = tkinter.Tk()
    win15.geometry("300x600")
    win15.title("Animation movies for you")
    ani_movies = langgenre.getGenre(16)


    for i in range (25):
        tkinter.Button(win15, command=partial(langgenre.getInfo, ani_movies.iloc[i]) ,text=ani_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)


def gen_family():
    win16 = tkinter.Tk()
    win16.geometry("300x300")
    win16.title("Family movies for you")
    family_movies = langgenre.getGenre(10751)


    for i in range (15):
        tkinter.Button(win16, command=partial(langgenre.getInfo, family_movies.iloc[i]) ,text=family_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def gen_drama():
    win17 = tkinter.Tk()
    win17.geometry("300x300")
    win17.title("Drama movies for you")
    drama_movies = langgenre.getGenre(18)


    for i in range (15):
        tkinter.Button(win17, command=partial(langgenre.getInfo, drama_movies.iloc[i]) ,text=drama_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def gen_sci():
    win17 = tkinter.Tk()
    win17.geometry("300x300")
    win17.title("Drama movies for you")
    sci_movies = langgenre.getGenre(878)


    for i in range (15):
        tkinter.Button(win17, command=partial(langgenre.getInfo, sci_movies.iloc[i]) ,text=sci_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def lang_english():
    win7 = tkinter.Tk()
    win7.geometry("300x300")
    win7.title("Popular English movies for you")
    eng_movies = langgenre.getLang('en')

    for i in range (15):
        tkinter.Button(win7, command=partial(langgenre.getInfo, eng_movies.iloc[i]) ,text=eng_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def lang_spanish():
    win8 = tkinter.Toplevel()
    win8.geometry("300x400")
    win8.title("Popular Spanish movies for you")
    span_movies = langgenre.getLang('es')

    for i in range (15):
        tkinter.Button(win8, command=partial(langgenre.getInfo, span_movies.iloc[i]) ,text=span_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def lang_french():
    win9 = tkinter.Tk()
    win9.geometry("300x300")
    win9.title("Popular French movies for you")
    french_movies = langgenre.getLang('fr')

    for i in range (15):
        tkinter.Button(win9, command=partial(langgenre.getInfo, french_movies.iloc[i]) ,text=french_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)



def lang_russian():
    win10 = tkinter.Tk()
    win10.geometry("300x300")
    win10.title("Popular Russian movies for you")
    russian_movies = langgenre.getLang('ru')

    for i in range (15):
        tkinter.Button(win10, command=partial(langgenre.getInfo, russian_movies.iloc[i]) ,text=russian_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def lang_italian():
    win11 = tkinter.Tk()
    win11.geometry("300x300")
    win11.title("Popular Italian movies for you")
    it_movies = langgenre.getLang('it')
    for i in range (15):
        tkinter.Button(win11, command=partial(langgenre.getInfo, it_movies.iloc[i]) ,text=it_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def lang_japanese():
    win12 = tkinter.Tk()
    win12.geometry("300x300")
    win12.title("Popular Japanese movies for you")
    jap_movies = langgenre.getLang('ja')
    for i in range (15):
        tkinter.Button(win12, command=partial(langgenre.getInfo, jap_movies.iloc[i]) ,text=jap_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def lang_latin():
    win13 = tkinter.Tk()
    win13.geometry("300x300")
    win13.title("Popular Latin movies for you")
    lat_movies = langgenre.getLang('la')
    for i in range (15):
        tkinter.Button(win13, command=partial(langgenre.getInfo, lat_movies.iloc[i]) ,text=lat_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)

def lang_hindi():
    win14 = tkinter.Tk()
    win14.geometry("300x300")
    win14.title("Popular Hindi movies for you")
    hin_movies = langgenre.getLang('hi')

    for i in range (15):
        tkinter.Button(win14, command=partial(langgenre.getInfo, hin_movies.iloc[i]) ,text=hin_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)
def notFound():
    windowp = tkinter.Tk()
    windowp.title("ERROR")
    windowp.geometry("400x250")
    tkinter.Label(windowp, text="Title not Found", fg="red", font = (None, 60)).pack(side = LEFT)

def titleSearch():
    inp = ent_title.get()
    data = langgenre.search_movie(inp)

    langgenre.getInfo(data)

ent_title = Entry(window)
tkinter.Label(window, text="Search by Title", fg="red", font = (None, 20)).grid(row=0, column=2, sticky = E)
ent_title.grid(row=0, column=3)
tkinter.Button(window, text="Go", command = titleSearch).grid(row=0, column=4, sticky = W)

def yrNotFound():
    windowp = tkinter.Tk()
    windowp.title("ERROR")
    windowp.geometry("400x250")
    tkinter.Label(windowp, text="Year not valid", fg="red", font = (None, 60)).pack(side = LEFT)

def year_data():
    inp = ent.get()
    try:
        val = int(inp)
    except ValueError:
        yrNotFound()
        return

    win14 = tkinter.Tk()
    win14.geometry("300x550")
    win14.title("Movies from "+ str(inp))

    yr_movies = langgenre.getYear(int(inp))
    for i in range (25):
        tkinter.Button(win14, command=partial(langgenre.getInfo, yr_movies.iloc[i]) ,text=yr_movies.iloc[i]['title'], width=35, height=1).grid(row=i, columnspan=2)


ent = Entry(window)
tkinter.Label(window, text="Search by Year", fg="red", font = (None, 20)).grid(row=0, column=5, sticky = E)
ent.grid(row=0, column=6)
tkinter.Button(window, text="Go", command = year_data).grid(row=0, column=7, sticky = W)


tkinter.Label(window, text="Search by Genre", fg="blue", font = (None, 20)).grid(row=4, column=2)

from PIL import Image, ImageTk

image = Image.open("./Unknown.jpeg")
photo = ImageTk.PhotoImage(image)
tkinter.Button(window, width=250, height=163, image=photo, command = gen_action).grid(row=5, column=2)
tkinter.Label(window, text="Action", fg="purple").grid(row=6, column=2)


image1 = Image.open("./ghost.jpg")
photo1 = ImageTk.PhotoImage(image1)
tkinter.Button(window, text="Horror", command=gen_horror, width=250, height=163, image=photo1).grid(row=5, column=3)
tkinter.Label(window, text="Horror", fg="purple").grid(row=6, column=3)


image2 = Image.open("./thrill.jpeg")
photo2 = ImageTk.PhotoImage(image2)
tkinter.Button(window, text="Thrill", width=250, height=163, image=photo2,command = gen_thrill).grid(row=5, column=4)
tkinter.Label(window, text="Thrill", fg="purple").grid(row=6, column=4)


#image3 = Image.open("./images.jpeg")
image3 = Image.open("./adventure.png")
image3 = image3.resize((250, 200), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)
tkinter.Button(window, text="Adventure", width=250, height=163, image=photo3,command = gen_adventure).grid(row=5, column=5)
tkinter.Label(window, text="Adventure", fg="purple").grid(row=6, column=5)

image4 = Image.open("./images-1.jpeg")
photo4 = ImageTk.PhotoImage(image4)
tkinter.Button(window, text="Comedy", width=250, height=163, image=photo4,command = gen_comedy).grid(row=5, column=6)
tkinter.Label(window, text="Comedy", fg="purple").grid(row=6, column=6)


image5 = Image.open("./images-2.jpeg")
photo5 = ImageTk.PhotoImage(image5)
tkinter.Button(window, text="popular movies", width=250, height=200, image=photo5,command = show_popular).grid(row=7, column=2)
tkinter.Label(window, text="WHAT'S TRENDING", fg="purple").grid(row=8, column=2)

image14 = Image.open("./animation.jpg")
image14 = image14.resize((250,200), Image.ANTIALIAS)
photo14 = ImageTk.PhotoImage(image14)
tkinter.Button(window, text="popular movies", width=250, height=200, image = photo14,command = gen_ani).grid(row=7, column=3)
tkinter.Label(window, text="Animation", fg="purple").grid(row=8, column=3)

image15 = Image.open("./family.jpeg")
image15 = image15.resize((250, 200), Image.ANTIALIAS)
photo15 = ImageTk.PhotoImage(image15)
tkinter.Button(window, text="Family", width=250, height=163, image = photo15, command = gen_family).grid(row=7, column=4)
tkinter.Label(window, text="Family", fg="purple").grid(row=8, column=4)

image16 = Image.open("./drama.jpg")
image16 = image16.resize((250,200), Image.ANTIALIAS)
photo16 = ImageTk.PhotoImage(image16)
tkinter.Button(window, text="Drama", width=250, height=200, image = photo16,command = gen_drama).grid(row=7, column=5)
tkinter.Label(window, text="Drama", fg="purple").grid(row=8, column=5)



image17 = Image.open("./scific.jpg")
image17 = image17.resize((250,200), Image.ANTIALIAS)
photo17 = ImageTk.PhotoImage(image17)
tkinter.Button(window, text="Science Fiction", width=250, height=200, image = photo17,command = gen_sci).grid(row=7, column=6)
tkinter.Label(window, text="Science Fiction", fg="purple").grid(row=8, column=6)

tkinter.Label(window, text="Search by Language", fg="green", font = (None, 20)).grid(row=10, column=2)

image6 = Image.open("./english.jpeg")
photo6 = ImageTk.PhotoImage(image6)
tkinter.Button(window, text="English", width=250, height=130, image=photo6,command = lang_english).grid(row=11, column=2)


image7 = Image.open("./hindi.png")
photo7 = ImageTk.PhotoImage(image7)
tkinter.Button(window, text="Hindi", width=240, height=130, image=photo7,command = lang_hindi).grid(row=11, column=3)


image8 = Image.open("./spanish.png")
photo8 = ImageTk.PhotoImage(image8)
tkinter.Button(window, text="Espanol", width=240, height=130, image=photo8,command = lang_spanish).grid(row=11, column=4)


image9 = Image.open("./images-3.jpeg")
photo9 = ImageTk.PhotoImage(image9)
tkinter.Button(window, text="French", width=240, height=130, image=photo9,command = lang_french).grid(row=11, column=5)


image10 = Image.open("./russian.png")
photo10 = ImageTk.PhotoImage(image10)
tkinter.Button(window, text="Russian", width=240, height=130, image=photo10,command = lang_russian).grid(row=12, column=2)


image11 = Image.open("./itit.jpg")
photo11 = ImageTk.PhotoImage(image11)
tkinter.Button(window, text="Italian", width=240, height=130, image=photo11 ,command = lang_italian).grid(row=12, column=3)


image12 = Image.open("./japan.png")
photo12 = ImageTk.PhotoImage(image12)
tkinter.Button(window, text="Japanese", width=240, height=130, image=photo12,command = lang_japanese).grid(row=12,column=4)


image13 = Image.open("./latin.jpg")
photo13 = ImageTk.PhotoImage(image13)
tkinter.Button(window, text="Latin", width=240, height=130, image=photo13,command = lang_latin).grid(row=12, column=5)

window.mainloop()
