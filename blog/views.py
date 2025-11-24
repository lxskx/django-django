from django.shortcuts import render

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    # ... остальные посты
]


def index(request):
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, id):
    post = next((p for p in posts if p['id'] == id), None)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    return render(
        request,
        'blog/category.html',
        {'category_slug': category_slug}
    )
