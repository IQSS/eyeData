from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.datasets.views',

    url(r'^list-datasets/$', 'view_list_datasets', name="view_list_datasets"),

    url(r'^dataset-detail/(?P<dataset_id>\d{1,8})/$', 'view_dataset_detail', name="view_dataset_detail"),
    
)
