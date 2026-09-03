"""Generate ru.html from index.html so Google can index the Russian version.
Run after every edit to index.html:  python build.py
"""
import re
s = open('index.html', encoding='utf-8').read()
n = 0
def swap(m):
    global n; n += 1
    return m.group(1) + m.group(3) + m.group(4)
s = re.sub(r'(<(\w+)[^>]*data-he="[^"]*" data-ru="([^"]*)"[^>]*>)(?:.*?)(</\2>)', swap, s, flags=re.S)
assert n == s.count('data-ru='), (n, s.count('data-ru='))
rep = {
    '<html lang="he" dir="rtl">': '<html lang="ru" dir="ltr">',
    'let ru=false;': 'let ru=true;',
    '<use href="#f-ru"/>': '<use href="#f-il"/>',
    '<title>המטבח של אולגה – פלמני וורניקי ביתיים בעבודת יד | חיפה והקריות</title>':
        '<title>Кухня Ольги – домашние пельмени и вареники ручной лепки | Хайфа и Крайот</title>',
    'content="פלמני וורניקי ביתיים בעבודת יד, לפי מתכון של סבתא. בצק דק, מילוי נדיב, בלי חומרים משמרים. איסוף עצמי מהקריות וחיפה. הזמנה בוואטסאפ."':
        'content="Домашние пельмени и вареники ручной лепки по бабушкиному рецепту. Тонкое тесто, щедрая начинка, без консервантов. Самовывоз, Крайот и Хайфа. Заказ в WhatsApp."',
    'content="המטבח של אולגה – פלמני ביתיים כמו שסבתא הכינה"': 'content="Кухня Ольги – домашние пельмени, как у бабушки"',
    'content="פלמני וורניקי בעבודת יד, בלי חומרים משמרים. איסוף עצמי מהקריות וחיפה. מזמינים בוואטסאפ."':
        'content="Пельмени и вареники ручной лепки, без консервантов. Самовывоз, Крайот и Хайфа. Заказ в WhatsApp."',
    '<link rel="canonical" href="https://blueskaic.github.io/Olga-s-Kitchen/">': '<link rel="canonical" href="https://blueskaic.github.io/Olga-s-Kitchen/ru.html">',
    '<meta property="og:url" content="https://blueskaic.github.io/Olga-s-Kitchen/">': '<meta property="og:url" content="https://blueskaic.github.io/Olga-s-Kitchen/ru.html">',
    '<meta property="og:locale" content="he_IL"><meta property="og:locale:alternate" content="ru_RU">': '<meta property="og:locale" content="ru_RU"><meta property="og:locale:alternate" content="he_IL">',
}
for a, b in rep.items():
    assert s.count(a) == 1, a[:50]
    s = s.replace(a, b)
open('ru.html', 'w', encoding='utf-8', newline='\n').write(s)
print('ru.html ok,', n, 'strings swapped')
