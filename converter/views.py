from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from converter.forms import BalanceForm
from converter.models import ExchangeRate


def convert(request):
    if request.method == "POST":
        form = BalanceForm(request.POST)
        if form.is_valid():
            rate = ExchangeRate.objects.get(o_currency=form.cleaned_data['o_currency'], t_currency=form.cleaned_data['t_currency'])
        balanse = form.cleaned_data['balance']
        result = float(balanse)*float(rate)
        return HttpResponseRedirect('')
    else:
        return render(request, 'base.html', {'form': BalanceForm()})











# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
