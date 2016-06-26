from django.shortcuts import render
from jurblog.models import NewsEntry, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



from django.shortcuts import get_object_or_404, render_to_response


def index(request):
    entries = NewsEntry.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(entries,3)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    return render_to_response('jurblog/index.html', {'entries': entries}, request.FILES)

def category(request, slug):
    category = get_object_or_404(Category,
                                           slug=slug)
    entries = category.entries.published()
    return render(request, 'jurblog/index.html', {'entries': entries})

def archive_year(request, year):
    entries = NewsEntry.objects.filter(draft=False,
                                       published_at__year=year)
    return render_to_response('jurblog/index.html', {'entries': entries})

def archive_month(request, year, month):
    entries = NewsEntry.objects.filter(draft=False,
                                       published_at__year=year,
                                       published_at__month=month)
    return render_to_response('jurblog/index.html', {'entries': entries})

def archive_day(request, year, month, day):
    entries = NewsEntry.objects.filter(draft=False,
                                       published_at__year=year,
                                       published_at__month=month,
                                       published_at__day=day)
    return render_to_response('jurblog/index.html', {'entries': entries})

def details(request, year, month, day, slug):
    entry = get_object_or_404(NewsEntry, draft=False,
                                         published_at__year=year,
                                         published_at__month=month,
                                         published_at__day=day,
                                         slug=slug)
    return render_to_response('jurblog/blog_details.html', {'entry': entry})
