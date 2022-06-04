SELECT  books.long_name,
        verses.text,
        verses.chapter,
        verses.verse
FROM    verses
INNER JOIN books
ON      verses.book_number = books.book_number
/*ignore book name accent and caps*/
WHERE   REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(books.long_name,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = 'genesis' COLLATE NOCASE
OR      books.long_name = 'genesis' COLLATE NOCASE
AND     verses.chapter  = '1'
AND     verses.verse    = '1';