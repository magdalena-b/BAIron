# BAIron

## NLP

### TODO
jak na razie w folderze NLP jest moduł z placeholderem generującym tylko "Lorem Ipsum..."

## frontend

### TODO

## backend

### model bazy danych

#### Input:
- style - styl tekstu w jaki ma być wygenerowany z dostępnej listy
- first_line - pierwsza linia tekstu na podstawie której ma być generowany tekst
- ```TODO``` nie wiem czy będą jeszcze inne dane wejściowe

#### Poem:
- author - autor tekstu - Różni się od style, bo tu może być prawdziwy autor albo maszyna, jeśli jest wygenerowany przez AI
- input - FK do `Input` (opcjonalne, np. kiedy tekst jest prawdziwy)
- text - wygenerowany tekst
- views - ilość wyświetleń  (opcjonalne, automatycznie 0)
- sentiment - zaklasyfikowany sentyment  (opcjonalne, np. jak nie uda się tego zaimplementować)

#### Rate:
- poem - FK do `Poem`
- rating - liczba naturalna

#### TuringTestVote:
- poem - FK do `Poem`
- fragment - fragment tekstu na podstawie którego została podjęta decyzja (opcjonalne, np. jak nie będzie to potrzebne nigdzie)
- vote - Human/Machine

## API

`/api/generate/`

po wysłaniu jsona z danymi potrzebnymi do stworzenia `Input` zwraca jsona z wygenerowanym `Poem`

`/api/save/`

po wysłaniu jsona z danymi potrzebnymi do stworzenia `Poem` zapisuje się w bazie

`/api/poem/id/`

zwraca jsona z danymi wiersza o konkretnym id

`/api/poems/`

zwraca podstawowe (pierwsza linia i tekst) dane o [10] najczęściej wyświetlanych wierszach

`/api/poems/[style=style][&][sentiment=sentiment]`

zwraca podstawowe (pierwsza linia i tekst) dane o [10] najczęściej wyświetlanych wierszach od konkretnego autore i/lub z konkretnym sentymentem

`/api/rating/id/`

zwraca jsona z ocenami (zarówno średnia i TT) o wierszu z konkretnym id

`/api/rating/`

zwraca jsona z ocenami (zarówno średnia i TT) o wszystkich wierszach

`/api/add/rate/id/`

endpoint do dodawania z oceny [1-10] dla wiersza z konkretnym id

`/api/add/turing-test-vote/id/` 

endpoint do dodawania opinii Human/Machine dla wiersza z konkretnym id

## Uruchomienie

### model

### frontend


### Django

Pobieranie modułów do pythona: `pip install -r requirements.txt`

Najlepiej chyba zdropować za każdym razem bazę po większych zmianach (`db.sqlite3`) i usunąć migracje, jak jakieś są (`*/migrations/*` - wszystko za wyjątkiem `init.py`)

Migracje: `python manage.py makemigrations` i `python manage.py migrate`

Żeby dodać admina automatycznie dodałem komendę `python manage.py create_admin`, nie trzeba wtedy wszystkiego wpisywać - tworzy się automatycznie - login: `admin`, password: `admin`

Uruchomienie `python manage.py runserver`
