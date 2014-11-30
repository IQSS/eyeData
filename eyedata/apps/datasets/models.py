import os

from django.db import models

from django.utils.text import slugify   # turns  "Microfinance Dataset" into "microfinance-dataset"
from model_utils.models import TimeStampedModel
from django.conf import settings
from apps.utils.json_field_reader import JSONFieldReader

class DatasetInfo(TimeStampedModel):
    """Sample model"""
    
    # Note: an 'id' field is auto-created for each model
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # FileField - see https://docs.djangoproject.com/en/1.6/ref/models/fields/#filefield
    #
    data_file = models.FileField(upload_to='eyedata_uploaded_files/%Y/%m/%d')
    
    visible = models.BooleanField(default=True)
        
    slug = models.SlugField(blank=True, help_text='auto-filled on save. url-friendly name')

    variable_names_json = models.TextField(blank=True)

    def get_file_basename(self):
        return os.path.basename(self.data_file.name)
        
    def get_variable_names_json(self):
        """
        Return saved JSON as a python object
        """
        return JSONFieldReader.get_json_string_as_python_val(self.variable_names_json)
        
    def set_variable_names_json(self, python_obj):
        """
        Save a python object as JSON
        """
        assert python_obj is not None, "The python_obj cannot be None"
        self.variable_names_json = JSONFieldReader.get_python_val_as_json_string(python_obj)
            
    
    def save(self, *args, **kwargs):
        # override the save command to create a slug
        self.slug = slugify(self.name)
        super(DatasetInfo, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Dataset info'
        

'''
class ChartType(TimeStampedModel):
    """
    Chart types
    """
    # Note: an 'id' field is auto-created for each model
    
    name = name = models.CharField(max_length=255, unique=True)
        
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)    
        
    
        
class DatasetChart(TimeStampedModel):
    """
    Example of storing JSON data for a specific:
        - Dataset
        - Variable
        - Chart type
    """
    # Note: an 'id' field is auto-created for each model
    
    dataset = models.ForeignKey(DatasetInfo)
    variable_name = models.CharField(max_length=255)
    chart_type = models.ForeignKey(ChartType)
    
    json_data = models.TextField(blank=True)
    
    def get_json_data(self):
        """
        Return saved JSON as a python object
        """
        return JSONFieldReader.get_json_string_as_python_val(self.json_data)
        
    def add_json_data(self, python_obj):
        """
        Save a python object as JSON
        """
        assert python_obj is not None, "The python_obj cannot be None"
        self.json_data = JSONFieldReader.get_python_val_as_json_string(python_obj)
    
    def __unicode__(self):
        return '%s. %s (%s)' % (self.dataset, self.variable_name, self.chart_type)
'''
