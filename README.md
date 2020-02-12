Tested on **Python 3.5 - Django 2.2.10**

* I assumed that data in csv will be imported once and the data is always correct.
* I didn't configure project as usually (one settings, templates in common directory). Normally I would use a little different directories structure.
* I added normal view for tests purpose.
* Would use some third app to factory data but without it it will be easier to tests.
* Wasn't specified if I should write code that download csv from web so i added it to repository.


# Installation #
   1. Download repository *git clone https://github.com/publicznyprofil/rekrutacja_2020.git*
   2. Install django in your venv (requirements.txt)
   3. Create `db.sqlite3` in main repository directory 
   4. Run migration `manage.py migrate`
   5. Load data from csv into database via command `manage.py load_data_from_csv`
   6. Run server `manage.py runserver`
   7. Go to main page `localhost:8000` and see how it looks like
   
   
# Tests #
 1. Just run `manage.py test`

# How it looks in main page #
![Examle image](https://i.imgur.com/B8JxplJ.png)

# How json respone look like #
  `[{"total_clicks": 5, "date": "2020-02-11", "total_impressions": 3}]`
