from django.contrib import admin

from apps.datasets.models import DatasetInfo
#from apps.datasets.models import ChartType, DatasetChart

class DatasetInfoAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('name', 'description')
    list_editable = ('visible',)
    list_display = ('name', 'description', 'slug', 'data_file', 'visible', 'created' )
    list_filter = ('visible',)
    readonly_fields = ('modified', 'created', )
admin.site.register(DatasetInfo, DatasetInfoAdmin)

'''
class ChartTypeAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', )
    readonly_fields = ('modified', 'created', )
admin.site.register(ChartType, ChartTypeAdmin)

   
class DatasetChartAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dataset', 'variable_name', 'chart_type', 'created' )
    list_filter = ('chart_type',)
    readonly_fields = ('modified', 'created', )
admin.site.register(DatasetChart, DatasetChartAdmin)
'''