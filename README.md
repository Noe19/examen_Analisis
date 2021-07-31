# examen_Analisis

1.PY  en este caso trabajamos en python, pues importamos las liberias  :
pip install tweepy 
 para que se guarden en couchdb donde se pone nuetras credenciales :
 '''========couchdb'=========='''
server = couchdb.Server('http://CUMBAL:12345@127.0.0.1:5984')  #('http://115.146.93.184:5984/')
try:
    db = server.create('exam31py')
except:
    db = server['M']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[5.955911,45.817993,10.49205,47.80838])  
mediante este codigo nos podemos ubicar en el mapa y generar las coordenadas almacenar en la base de datos que deseamos en enste caso fue coughdb por eso las credenciales son d este
base de datos y twitterStream.filter(locations=[5.955911,45.817993,10.49205,47.80838]) ponemos la ubicacion que deseamos extraer los datos 

2.PY 

El codigo es similar y la logica tambine en este caso solo cambia el una linea de codigo
#twitterStream.filter(track=['juegos','olimpicos'])
aqui le decimos que extraiga de twitter las palabras "juegos", olimpicos" , y las guarde en nuestra base de datos 

3.PY
En esta forma trabajamos en pyton  
buscamos una pagina en Internet donde y revisamos el html 

response = requests.get("https://resultados.as.com/resultados/juegos_olimpicos/resultados/")
soup = BeautifulSoup(response.content, "lxml")
 '''
 aqui ponemos la clase si es <spn> o <a> o <h> y la classe 
'''

equi =soup.find_all('span',class_='deporte-nombre')


'''
 aqui todo guardamos en una lista 
'''
equipos =list()
for i in equi:
    equipos.append(i.text)
print(equipos)

    
'''
aqui la guardamos en json a mongodb mediante un diccionario 
'''
for i in range(len(equipos)):
  
    a={
       '3.py':equipos[i]}
    
    my_posts.insert_one(a)
    a={}
    
    
print(equipos)
5.py
En esta trabajamos con tiktok
para esto necesitamos : tiktok-scraper user tokyo2020_brasil -t csv
en mi caso use git bash para trabajar y todo guarde en una carpeta , busque los usuarios en internet ,despues es importante subir nuestros csv a mySQL, en mi cso trabaje con XAMP
en my localshot cree una base de datos donde inserte un csv que se me genero de lo csv de tiktok, para esto debemos de antemano debemos saber como este estrucutirado si es co  comas
puntos y eso despues q especificamos todos los subimos vemos que no hay error y los mismo hacemo con todos los csv que tenemos ahora 

6.py
Despues de bajarme  y elegir de formato json o csv todo de localhost de mu mypyhpadmin abro mi mongodb local o en la nube yo lo hice en ambas 
y vamos y creamos una base de datos con  el nombre a gusto personal luego creamos una coleecion en la coleecion importamos un file y mecionamos que formato es csv o json y listo

8.py
hay dos formas d hacerlo por mi parte lo hice 
pasando todo como json y csv a mi mongo de la nube y tambien lo hice por si las dudas genere mi codigo en mongo en la nube y me conecte desde mi mongo local y de esta forma pase mi mongo local  
a mongo a la nube 

9.py
Es importante que al momento que subimos los csv su estructura es distinta , ademas en este caso tenemos la facilidad de elegir que campos necesito 
pues me los bajo de my mypyadmin formato csv 
10py 
Es importante que al momento que subimos los json  su estructura es distinta , 
pues me los bajo de my mypyadmin formato json y los subo de la misma forma diciendo que son un formato json






