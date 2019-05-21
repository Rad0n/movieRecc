import pandas as pd
import ast

# Load Movies Metadata
metadata = pd.read_csv("./the-movies-dataset/movies_metadata.csv", low_memory=False)

# Print the first three rows
metadata.head(3)

# Calculate C
C = metadata['vote_average'].mean()
print(C)

m = metadata['vote_count'].quantile(0.90)
print(m)


q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
q_movies.shape




def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)



# Define a new feature 'score' and calculate its value with `weighted_rating()`
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)


#Sort movies based on score calculated above
q_movies = q_movies.sort_values('score', ascending=False)



def getGenre(genreId):
# This function takes the genre id and gives recommendations
    genreId = int(genreId)

    select_movie = []
    for i in range(0,len(q_movies)):
        select_movie.append(0)
    l = 0
    for i in q_movies['genres']:

        p = ast.literal_eval(i)
        for n in p:
            if(n['id'] == genreId):
                select_movie[l] = 1
                break
            else:
                select_movie[l] = 0

        l+=1


    q_movies['selection1'] = select_movie
    q_movies_genre = q_movies.copy().loc[q_movies['selection1']==1]
    #print(q_movies_genre[['title', 'vote_count', 'vote_average', 'score']].head(15))
    return q_movies_genre

def getLang(LangId):
# This function takes the language id and gives recommendations
    LangId = str(LangId)
    select_movie = []
    for i in range(0,len(q_movies)):
        select_movie.append(0)
    l = 0
    for i in q_movies['spoken_languages']:
        #print(q_movies.loc[l])
        p = ast.literal_eval(i)


        for n in p:
            if(n['iso_639_1'] == LangId):
                select_movie[l] = 1
                break
            else:
                select_movie[l] = 0

        l+=1


    q_movies['selection2'] = select_movie
    q_movies_Lang = q_movies.copy().loc[q_movies['selection2']==1]
    return q_movies_Lang

def getYear(yearId):
# This function takes the year and gives recommendations
    yearId = int(yearId)
    select_movie = []
    for i in range(0,len(q_movies)):
        select_movie.append(0)
    l = 0
    for i in q_movies['release_date']:

        p = i[0:4]

        if(int(p) == yearId):
            select_movie[l] = 1
        else:
            select_movie[l] = 0

        l+=1


    q_movies['selection'] = select_movie
    q_movies_year = q_movies.copy().loc[q_movies['selection']==1]
    return q_movies_year

def search_movie(inp):
    str1 = str(inp)

    n = len(metadata)
    indx = -1
    l=0
    while(l<n):
        temp = metadata['original_title'].iloc[l]
        if(temp==str1):
            indx = l
            break
        l+=1
    if(indx == -1):
        return False
    else:
        return metadata.iloc[indx]


def get_popular():
    print(q_movies['title'].head(15))
    return q_movies


from tkinter import *
import requests
from io import BytesIO
from PIL import Image, ImageTk

def getInfo(df):
    #df is the data frame row for that movie
    wwin = Toplevel()
    wwin.geometry("1800x1000")
    wwin.title(df['title'])


    base_url = 'https://image.tmdb.org/t/p'
    file_size = '/w500'
    link = df['poster_path']


    url = base_url + file_size + link

    l1 = Label(wwin, text=df['title']+" ("+df['release_date'][0:4]+")", font = (None, 50), padx = 10, pady = 10, fg="black", bg="white",wraplength = 600).grid(column = 0, row = 0, sticky = W, columnspan = 3)
    l5 = Label(wwin, text = "").grid(row = 1)
    l5 = Label(wwin, text="                   ").grid(column = 1)
    l5 = Label(wwin, text="                   ").grid(column = 3)
    l5 = Label(wwin, text="                   ").grid(column = 4)
    l5 = Label(wwin, text="                   ").grid(column = 5)
    l5 = Label(wwin, text="                   ").grid(column = 6)

    l3 = Label(wwin, text = "Overview", font = (None, 30), padx = 15).grid(column = 0, row = 2, sticky = W)
    l2 = Label(wwin, text=df['overview'], justify = LEFT, bg = "white",wraplength = 600, font = (None, 20), padx = 15).grid(column = 0, columnspan = 2,row = 3, rowspan = 3, sticky = NW)
    coll = ""
    gen =""
    run = int(df['runtime'])


    l4 = None
    if(type(df['belongs_to_collection']) != float):

        coll = ast.literal_eval(df['belongs_to_collection'])['name']
        coll = "Belongs to Collection:\n"+coll
    if(type(df['genres']) != float):
        gen += "Genre:\n"
        for i in ast.literal_eval(df['genres']):
            gen += i['name'] + " "


    l4 = Label(wwin, text=coll, justify = LEFT, bg = "white",wraplength = 500, font = (None, 20), padx = 15).grid(column = 0, row = 7, sticky = W)
    l7 = Label(wwin, text=gen, justify = LEFT, bg = "white",wraplength = 500, font = (None, 20), padx = 15).grid(column = 0, row = 6, sticky = W)
    l8 = Label(wwin, text = "Runtime : "+str(run)+" minutes", font = (None, 20), padx = 15).grid(row =8, sticky = W)
    canvas = Canvas(wwin, width = 500, height = 750)
    canvas.grid(rowspan = 10,columnspan = 3,row = 0,column = 6, sticky = E)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    image = ImageTk.PhotoImage(img)
    imagesprite = canvas.create_image(250,375,image=image)
    wwin.mainloop()


#test values
