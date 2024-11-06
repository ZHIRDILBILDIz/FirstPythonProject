# Игра начинается здесь:
label start:

    # показывает изображение с названием room
    scene Backdrop_Airplane
    with fade

    stop music fadeout 3.0
    play music Normal

    '''
    Как же давно я мечтал поступить в МФТИ и наконец-то я лечу туда.

    Надеюсь друзья и учителя не обманули, и это правда лучший вуз.

    Интересно какими будут мои одногруппники?

    Какими будут мои учителя?

    Хорошее ли там общежитие?"

    Всё ли у меня будет хорошо?

    Справлюсь ли я с учёбой?

    Надо отвлечься на что-то, а то я доконаю себя этими вопросами.
    '''

    menu:
        "На что отвлечься?"

        "Посмотреть в иллюминатор.":
            stop music fadeout 3.0
            jump LookWindow

        "Послушать музыку.":
            jump ListenMusic

            stop music fadeout 3.0
        "Лечь спать.":
            stop music fadeout 3.0
            jump NotLookWindow

    return

label LookWindow:
    scene Sky_From_Airplane
    with fade

    stop music fadeout 3.0
    play music Relax

    '''
    Завараживающее зрелище.

    Подо мной будто пушистое белое море, где облака растянулись до самого горизонта, словно мягкие волны.

    А сверху — солнце, яркое и тёплое, заливает всё вокруг мягким светом, от которого облака кажутся почти светящимися.

    В этой картине нет ничего лишнего — только белоснежные облака и бескрайняя синь неба.

    От этого вида внутри разливается спокойствие, будто мир стал проще и чище.

    Кажется, что я лечу в каком-то другом, безмятежном мире, где нет суеты, только тишина и бесконечный простор, залитый солнечным светом.
    '''

    play music Attention
    $ renpy.pause(3)
    stop music

    Attention_Airplane '''
        Уважаемые пассажиры, наш самолёт начал снижение и вскоре мы будем приземляться.

        Просим вас убедиться, что ваши ремни безопасности застёгнуты.

        Пожалуйста, приведите спинки кресел в вертикальное положение, уберите откидные столики и откройте шторки на иллюминаторах.

        Благодарим за внимание.
    '''

    scene Backdrop_Airplane
    with fade

    "Эхх, скоро посадка..."

    jump Airport
    return

label ListenMusic:
    stop music fadeout 2.0
    play music A_Rock_To_The_Head
    "КИШ Камнем по голове"

    stop music fadeout 2.0
    play music Eat_Meat_Men
    "КИШ Ели мясо мужики"

    stop music fadeout 2.0
    play music Fool_And_Polnias
    "КИШ Дурак и молния"

    stop music fadeout 2.0
    play music Sorcerers_Doll
    "КИШ Кукла колдуна"

    stop music fadeout 2.0
    play music Woodsman
    "КИШ Лесник"

    play music Attention
    $ renpy.pause(3)
    stop music

    Attention_Airplane '''
        Уважаемые пассажиры, наш самолёт начал снижение и вскоре мы будем приземляться.

        Просим вас убедиться, что ваши ремни безопасности застёгнуты.

        Пожалуйста, приведите спинки кресел в вертикальное положение, уберите откидные столики и откройте шторки на иллюминаторах.

        Благодарим за внимание.
    '''

    scene Backdrop_Airplane
    with fade
    

    "Эхх, скоро посадка..."

    jump Airport
    return

label NotLookWindow:
    scene Backdrop_Airplane
    with fade
    show Steward_Normal

    Steward "Извините"

    Steward "Кхм-кхм."

    Mark "Аааа?"

    Steward "Извините мы уже приземлились, вам необходимо покинуть самолёт."

    Mark "Да? М-м, спасибо, что разбудили меня."

    hide Steward_Normal

    "Такой хороший сон был, жаль."

    jump Airport
    return
