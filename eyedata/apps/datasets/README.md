
### Installing basic example of a model with a reference to a file

#### Create database table

- From the Terminal, go into the project directory and run ```syncdb```

```
cd ~\eyeData\eyedata
workon eyedata
python manage.py syncdb
```

#### Load test data

- From the same Terminal, run the ```loaddata``` command

```
python manage.py loaddata apps/datasets/fixtures/test_data.json
```

You should see a message that reads:

```
Installed 2 object(s) from 1 fixture(s)
```

#### Run the development server

- From the same Terminal

```
python manage.py runserver
```

#### View model data

- Go to the list datasets page: http://127.0.0.1:8000/datasets/list-datasets/
- Click on one of the dataset names (e.g. "Microfinance Hyderabad")

#### "Wiring" for a dataset detail page

1. The url definition: [```/datasets/dataset-detail/{{ dataset_id }}/```](https://github.com/IQSS/eyeData/blob/master/eyedata/apps/datasets/urls.py#L8)
2. Points to the ```view_dataset_detail``` function](https://github.com/IQSS/eyeData/blob/master/eyedata/apps/datasets/views.py#L28)
3. The function has access the file itself.  See [lines 52-62](https://github.com/IQSS/eyeData/blob/master/eyedata/apps/datasets/views.py#L28) for an example of opening the file and saving some text (JSON) to the database.
4. The dataset is sent to a [template for display](https://github.com/IQSS/eyeData/blob/master/eyedata/templates/datasets/detail.html).




