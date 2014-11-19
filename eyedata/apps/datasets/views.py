from __future__ import print_function

import json
import pandas

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext

from apps.datasets.models import DatasetInfo

# helper code for commonly used functions
from apps.datasets.helpers import *

#spandana_baseline_b2.0.dta
def view_list_datasets(request):
    """
    Show a list of the DatasetInfo objects
    """
    d = { 'page_title' : 'Dataset Listing' }

    # Querying models, see: https://docs.djangoproject.com/en/1.6/topics/db/queries/
    #
    d['datasets'] = DatasetInfo.objects.filter(visible=True)
    d['dataset_count'] = DatasetInfo.objects.filter(visible=True).count()
    
    return render_to_response('datasets/listing.html'\
                              , d\
                              , context_instance=RequestContext(request))
    

def view_dataset_detail(request, dataset_id):
    """
    Show Dataset detail
    """
    
    #  (1) Retrieve the dataset
    #
    try:
        dataset = DatasetInfo.objects.filter(visible=True).get(id=dataset_id)
    except DatasetInfo.DoesNotExist:
        raise Http404('Dataset not found')
    
    # (2) Set the title and dataset attributes
    # 
    d = {}
    d['page_title'] = 'Dataset: %s' % dataset.name
    d['dataset'] = dataset
    
    # (3) Do some type of processing here
    #SWITCH THIS BACK TO NOT ONCE IT WORKS CORRECTLY
    if not dataset.variable_names_json:
    #if dataset.variable_names_json:
        #
        # example of opening the file
        #
        fh = dataset.data_file  # pointer to the data_file 
        fh.open(mode='rb')  # open the file
        flines = fh.readlines() # read the lines
        fh.close()  # close the file
        
        # saving the number of file lines as a JSON string
        # save variable names
        #

        fnamearray = str(fh).split('.')
        ftype = fnamearray[-1]
        fh.open (mode='rb')
        if(ftype == 'dta'):
            data = pandas.read_stata(fh)
        elif (ftype == 'tab'):
            data = pandas.read_table(fh)
        fh.close

        print('hello hello')

        file_info = { 'num_lines' : len(flines), 'variable_names' : list(data.columns.values) }
        dataset.set_variable_names_json(file_info)
        dataset.save() 
    
    return render_to_response('datasets/detail.html'\
                              , d\
                              , context_instance=RequestContext(request))
    

# search view - renders a results page     
def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['title', 'body',])
        
        found_entries = Entry.objects.filter(entry_query).order_by('-pub_date')

    return render_to_response('search/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))
