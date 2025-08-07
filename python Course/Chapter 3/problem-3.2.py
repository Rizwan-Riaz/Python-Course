letter = ''''Hello <|Name|>
You Are Selected 
Dated <|Date|>'''

print(letter.replace("<|Name|>","Rizwan").replace("<|Date|>","20 Dec 2025"))