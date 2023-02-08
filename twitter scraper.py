import pandas as pd
import snscrape.modules.twitter as tw

def tweets(hashtag, cant_tweets):
    '''
    Dado un termino de busqueda y una cantidad de tweets deseada
    devuelve una lista con esos tweets
    '''
    scraper = tw.TwitterSearchScraper(hashtag)
    lista = []
    for tweet in scraper.get_items():
        lista.append([tweet.date, # Fecha del Tweet
                tweet.username,   # Nombre del Usuario
                tweet.hashtags,   # Hashtags dentro del tweet
                tweet.retweetCount, # Cantidad de Retweets
                tweet.likeCount,    # Cantidad de Likes
                tweet.rawContent,   # Contenido del Tweet
                tweet.url])         # URL del Tweet
    #lista.append(tweet.hashtags)
        if len(lista) == cant_tweets:
            break
    return lista

def to_DataFrame(lista, orden, export = True):
    '''
    Convierte la lista generada en un DataFrame
    Se debe elegir una columna para que sea ordenada:
    'Fecha', 'Likes', 'Retweets'
    Puede elegir exportarlo o bien utilizarlo como df
    '''
    df = pd.DataFrame(lista)
    df = df.rename(columns={0: 'Fecha',
                        1 : 'Usuario',
                        2 : 'Hashtags',
                        3 : 'Retweets',
                        4 : 'Likes',
                        5 : 'Tweet',
                        6 : 'URL'})
                            
    
    df['Fecha'] = df['Fecha'].apply(lambda x: x.strftime("%d/%m/%y %r")) # Transforma el formato de fecha y hora a uno mas comodo para mi
    
    df = df.sort_values(orden, ascending = False)
    
    if export:
        df.to_csv('data.csv', index = False)
    else:
        return df

tweet = get_tweets('argentina campeon', 1000) # Test
df = to_DataFrame(tweet,'Likes', export=True) # Test


