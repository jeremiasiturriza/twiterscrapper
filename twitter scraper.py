import pandas as pd
import snscrape.modules.twitter as tw

def tweets(hashtag, cant_tweets):
    '''
    Dado un hashtag y una cantidad de tweets deseada
    devuelve una lista con esos tweets
    '''
    scraper = tw.TwitterSearchScraper(hashtag)
    lista = []
    for tweet in scraper.get_items():
        lista.append([tweet.date, 
                tweet.username, 
                tweet.hashtags,
                tweet.retweetCount,
                tweet.likeCount,
                tweet.rawContent,
                tweet.url])
    #lista.append(tweet.hashtags)
        if len(lista) == cant_tweets:
            break
    return lista

a = tweets('python', 300)

def convertir_a_DataFrame(lista):
    '''
    Convierte la lista generada en un DataFrame
    '''
    df = pd.DataFrame(lista)
    df = df.rename(columns={0: 'Fecha',
                        1 : 'Usuario',
                        2 : 'Hashtags',
                        3 : 'Retweets',
                        4 : 'Likes',
                        5 : 'Tweet',
                        6 : 'URL'})
                            
    
    df['Fecha'] = df['Fecha'].apply(lambda x: x.strftime("%d/%m/%y %r"))
    df = df.sort_values(['Likes', 'Fecha'], ascending = [False, False])
    df.to_csv('data.csv', index = False)


