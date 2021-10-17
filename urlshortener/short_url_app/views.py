from django.shortcuts import redirect, render
from .forms import ShortUrlForm
from .utils import Generate
from .models import ShortUrlModel

gen = Generate()


def short_url_view(request):
    context = {}
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)

        if form.is_valid():
            long_url = form.cleaned_data['url']
            context['long_url'] = long_url

            try:
                # check for pre-existing shortening and return that
                existing_data = ShortUrlModel.objects.get(long_url=long_url)
                short_url = existing_data.short_url
                context['short_url'] = short_url

            except Exception:
                # Create new shortening if one doesn't exist
                short_url = gen.short_url()
                context['short_url'] = short_url

                new_url = ShortUrlModel(long_url=long_url, short_url=short_url)
                new_url.save()

            complete_url = request.build_absolute_uri('/') + short_url
            context['complete_url'] = complete_url

        else:
            context['errors'] = form.errors

    else:
        form = ShortUrlForm()

    data = ShortUrlModel.objects.all()
    context['form'] = form
    context['data'] = data
    return render(request, 'index.html', context)


def redirect_view(_, short_url):
    data = ShortUrlModel.objects.get(short_url=short_url)
    return redirect(data.long_url)

