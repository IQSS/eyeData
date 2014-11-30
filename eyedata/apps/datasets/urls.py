from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.datasets.views',
    
    url(r'^get-vars/(?P<dataset_id>\d{1,8})/$', 'get_variable_names', name="get_variable_names"),

    url(r'^variable-detail/(?P<dataset_id>\d{1,8})/(?P<variable_name>\w+)/$', 'get_variable_info', name="get_variable_info"),

    url(r'^dataset-detail/(?P<dataset_id>\d{1,8})/$', 'view_dataset_detail', name="view_dataset_detail"),
    
    url(r'^', 'view_list_datasets', name="view_list_datasets"),



)
