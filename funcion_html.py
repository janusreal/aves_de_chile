def iteracionHtml(photos):
    #inicializo card
    card = ''

    # claves son name["spanish"] name["english"]
    # hago la iteración del array photos y cada 
    # linea la agrego a la variable card
    for photo in photos:
        card +=  f'''
        <div class="card mb-3" style="width: 18rem;">
            <img src="{photo['images']['main']}" class="card-img-top" alt="{photo['uid']}">
            <div class="card-body">
                <h5 class="card-title">{photo['name']['spanish']}</h5>
                <p class="card-text fst-italic">{photo['name']['english']}</p>
            </div>
            <div class="card-body">
                <a href="{photo['images']['full']}" target="_blank" class="card-link">{photo['images']['full']}</a>
            </div>
        </div>'''
    return card
    