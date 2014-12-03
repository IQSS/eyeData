from __future__ import print_function

import json
import pandas
import numpy as np
from scipy import stats

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

def get_variable_names(request, dataset_id): 
    try:
        dataset = DatasetInfo.objects.filter(visible=True).get(id=dataset_id)
    except DatasetInfo.DoesNotExist:
        raise Http404('Dataset not found')
    
    # (2) Set the title and dataset attributes
    # 
    d = {}
    d['page_title'] = 'Dataset: %s' % dataset.name
    d['dataset'] = dataset
    
    fh = dataset.data_file  # pointer to the data_file 
    fh.open(mode='rb')  # open the file
    flines = fh.readlines() # read the lines
    fh.close()  # close the file
    fnamearray = str(fh).split('.')
    ftype = fnamearray[-1]
    fh.open (mode='rb')
    if(ftype == 'dta'):
        data = pandas.read_stata(fh)
    elif (ftype == 'tab'):
        data = pandas.read_table(fh)
    fh.close
    
    file_info = {'variable_names' : list(data.columns.values) }

    # (3) Do some type of processing here
    #SWITCH THIS BACK TO NOT ONCE IT WORKS CORRECTLY
    #if not dataset.variable_names_json:
    #if dataset.variable_names_json:
        #
        # example of opening the file
        #
    #    fh = dataset.data_file  # pointer to the data_file 
    #    fh.open(mode='rb')  # open the file
    #    flines = fh.readlines() # read the lines
    #    fh.close()  # close the file
        
        # saving the number of file lines as a JSON string
        # save variable names
        #

    #    fnamearray = str(fh).split('.')
    #    ftype = fnamearray[-1]
    #    fh.open (mode='rb')
    #    if(ftype == 'dta'):
    #        data = pandas.read_stata(fh)
    #    elif (ftype == 'tab'):
    #        data = pandas.read_table(fh)
    #    fh.close

    #    file_info = {'variable_names' : list(data.columns.values) }
    #    dataset.set_variable_names_json(file_info)
    #    dataset.save() 
    # return HttpResponse(str(file_info), content_type="application/json")


    #     print('hello hello')

    #     file_info = {'variable_names' : list(data.columns.values) }
    #     dataset.set_variable_names_json(file_info)
    #     dataset.save() 

    return HttpResponse(json.dumps(file_info), content_type="application/json")



def get_variable_info(request, dataset_id, variable_name):     
    try:
        dataset = DatasetInfo.objects.filter(visible=True).get(id=dataset_id)
    except DatasetInfo.DoesNotExist:
        raise Http404('Dataset not found')
    
    # (2) Set the title and dataset attributes
    # 
    d = {}
    d['page_title'] = 'Dataset: %s' % dataset.name
    d['dataset'] = dataset
    
    fh = dataset.data_file
    fnamearray = str(fh).split('.')
    ftype = fnamearray[-1]
    fh.open (mode='rb')
    if(ftype == 'dta'):
        data = pandas.read_stata(fh)
    elif (ftype == 'tab'):
        data = pandas.read_table(fh)
    fh.close

    if variable_name in data:
        data['storer'] = 1
        counts = data.groupby(variable_name).count()
        counts.reset_index(inplace=True)
        print("hello")
        if (not isinstance(counts[variable_name][0], basestring)): 
            counts = counts[np.isfinite(counts[variable_name])]
        if len(counts.index) <= 15: 
            file_info = { 'x' : list(counts[variable_name]), 'y': list(counts['storer']), 'graph type': 'bar', 'graph title' : d['page_title'], 'x_axis' : variable_name, 'y_axis': 'Quantity'}
        else:  
            if (not isinstance(counts[variable_name][0], basestring)): 
                counts = counts[np.isfinite(counts[variable_name])] 
            data = data[np.isfinite(data[variable_name])]
            density = stats.kde.gaussian_kde(data[variable_name])
            x = list(data[variable_name].unique())
            y = []
            for val in x: 
                y.append(list(density(val))[0])
            file_info = {'x' : x, 'y': y, 'graph type': 'density', 'graph title' : d['page_title'], 'x_axis' : variable_name, 'y_axis': 'Quantity'}

    else:
        file_info = {'x': [0], 'y': [0], 'gaph type': 'invalid', 'graph title': 'invalid','x_axis' : variable_name, 'y_axis': 'Quantity'} 


    # (3) Do some type of processing here
    #SWITCH THIS BACK TO NOT ONCE IT WORKS CORRECTLY

    #string_variable = "dataset." + variable_name + "_info_json"
    #if not dataset.variable_names_json or dataset.variable_names_json:
    #current_json = dataset.variable_name_info_json 

    #if not current_json.weight or current_json.weight: 
    #if dataset.variable_names_json:
    
    #check if weight is in json!!!!!!!!!!!!

    #if not dataset.variable_names_json or dataset.variable_names_json:
        #
        # example of opening the file
        #
    #    fh = dataset.data_file  # pointer to the data_file 
    #    fh.open(mode='rb')  # open the file
    #    flines = fh.readlines() # read the lines
    #    fh.close()  # close the file
        
        # saving the number of file lines as a JSON string
        # save variable names
        #

    #    fnamearray = str(fh).split('.')
    #    ftype = fnamearray[-1]
    #    fh.open (mode='rb')
    #    if(ftype == 'dta'):
    #        data = pandas.read_stata(fh)
        # elif (ftype == 'tab'):
        #     data = pandas.read_table(fh)
        # fh.close

        # if variable_name in data:
        #     counts = data.groupby(variable_name).count()
        #     counts['storer'] = 1
        #     counts.reset_index(inplace=True)
        #     if counts.count <= 15: 
        #         file_info = { 'x' : counts[variable_name], 'y': counts['storer'], 'graph type': 'bar', 'graph title' : d['page_title'], 'x_axis' : variable_name, 'y_axis': 'Quantity'}
        #     else: 
        #         density = stats.kde.gaussian_kde(data[variable_name])
        #         x = list(data[variable_name].unique())
        #         y = []
        #         for val in x: 
        #             y.append(list(density(val))[0])
        #         file_info = {'x' : x, 'y': y, 'graph type': 'density', 'graph title' : d['page_title'], 'x_axis' : variable_name, 'y_axis': 'Quantity'}

        # else:
        #     counts = ["invalid variable name"] 

#        file_info = { 'x' : counts, 'y': counts, 'graph type': 'bar', 'graph title' : d['page_title'], 'x_axis' : variable_name, 'y_axis': 'Quantity'}

        # need to convert to list so json encode
        #file_info = { 'x' : list(counts), 'y': list(counts), 'graph type': 'bar', 'graph title' : d['page_title'], 'x_axis' : variable_name, 'y_axis': 'Quantity'}
        #file_info = {'graph title' : d['page_title'], 'x_axis' : variable_name, 'y_axis': 'Quantity'}
        #file_info = { 'num_lines' : len(flines), 'variable_names' : list(data.columns.values) }
        #file_info = dataset.get_variable_name_info_json
        #file_info[0][variable_name] = {'x' : arr, 'y': counts, 'graph type': 'bar', 'graph title' : d['page_title'], 'x_axis' : variable_name, 'y_axis': 'Quantity'}

        #setter = "dataset.set_" + variable_name + "info_json"
        #dataset.set_variable_name_info_json(file_info)
        #string_variable = file_info
        #dataset.save() 

    #return render_to_response('datasets/info.html', d, context_instance=RequestContext(request))
    #return HttpResponse(str(file_info), content_type="application/json")
    
    return HttpResponse(json.dumps(file_info), content_type="application/json")


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
