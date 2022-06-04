def look_for_verse(connection, book_name, chapter, verse, last_verse = None):
    if last_verse == None:
        sentence = f"""
        SELECT  verses.text,
                books.long_name,
                verses.chapter,
                verses.verse
        FROM    verses
        INNER JOIN books
        ON      verses.book_number = books.book_number
        /*ignore book name accent and caps*/
        WHERE   (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(books.long_name,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{book_name}' COLLATE NOCASE
        OR      books.long_name = '{book_name}' COLLATE NOCASE)
        AND     verses.chapter  = '{chapter}'
        AND     verses.verse    = '{verse}';"""
    else:
        sentence = f"""
        SELECT  verses.text,
                books.long_name,
                verses.chapter,
                verses.verse
        FROM    verses
        INNER JOIN books
        ON      verses.book_number = books.book_number
        /*ignore book name accent and caps*/
        WHERE   (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(books.long_name,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{book_name}' COLLATE NOCASE
        OR      books.long_name = '{book_name}' COLLATE NOCASE)
        AND     verses.chapter  = '{chapter}'
        AND     '{verse}'      <= verses.verse
        AND     verses.verse   <= '{last_verse}'
        ;"""
    cursor = connection.cursor()
    response = cursor.execute(sentence).fetchall()
    response_as_dicts = [{
        'text'   : verse[0],
        'book'   : verse[1],
        'chapter': verse[2],
        'verse'  : verse[3]
    } for verse in response]
    return response_as_dicts