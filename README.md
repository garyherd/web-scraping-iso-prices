# ISO Web Scraper

A simple scraper for getting Real Time LMP prices from
* ERCOT
* PJM
* ISONE
* NYISO

It uses [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) and [Flask](http://flask.pocoo.org/) libraries to extract data and render a simple page. I built it as a kind of prototype for the developers at my company working on a larger project.

## Using/Installing the application

You can view it [here](http://garyherd.pythonanywhere.com/)

To install it to a local machine:

* Install Python 3.5 (I haven't tested with 2.7)
* `git clone https://github.com/garyherd/web-scraping-iso-prices.git`
* Install and activate a virtual environment. I did this on a Windows machine:
    * Navigate into project folder
    * From cmd prompt type:
        ```
        >python -m venv venv
        >venv\Scripts\activate
        >pip install -r requirements.txt
        ``` 
* To run it on a local webserver:
  * From the cmd prompt type: `python iso_scraping.py`
  * Open up a web browser and go to [http://localhost:5000](http://localhost:5000)