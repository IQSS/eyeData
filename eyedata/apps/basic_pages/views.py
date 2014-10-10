from __future__ import print_function

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext


def view_homepage(request):
    d = {}
    #d['page_title'] = 'Phthisis Ravens: TB Project'
    d['home_page'] = True
    
    return render_to_response('home/homepage.html'\
                              , d\
                              , context_instance=RequestContext(request))


def view_about_page(request):
    d = {}
    d['about_page'] = True
    return render_to_response('about.html'\
                              , d\
                              , context_instance=RequestContext(request))


def view_support_page(request):
  d = {}
  d['support_page'] = True
  return render_to_response('support.html'\
                            , d\
                            , context_instance=RequestContext(request))




