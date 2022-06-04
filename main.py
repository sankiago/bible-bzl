from logic import connect_with_db, look_for_verse

bible_connection = connect_with_db('NTV.SQLite3')
verses = look_for_verse(bible_connection, 'genesis','1','1','4')
for verse in verses:
    print(verse)