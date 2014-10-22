from __future__ import print_function

import json

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext


def view_homepage(request):
    d = {}
    
    # Get Data
    # Analyze with Pandas
    # Visualize data with D3 (or use vincent to wrap)
    
    
    #d['page_title'] = 'Phthisis Ravens: TB Project'
    d['worker_data'] = json.dumps({"1":525,"2":725,"3":658,"4":206,"5":270,"9":24})

    d['home_page'] = True
    
    return render_to_response('home/homepage.html'\
                              , d\
                              , context_instance=RequestContext(request))



def view_json_example(request):

    # generate some JSON
    json_str = """{"1":525,"2":725,"3":658,"4":206,"5":270,"9":24})"""
    return HttpResponse(json_str, content_type="application/json")


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

def view_example_page(request):
  d = {}
  d['example_age'] = True;
  return render_to_response('graph.html' \
                            ,d \
                            , context_instance=RequestContext(request))




