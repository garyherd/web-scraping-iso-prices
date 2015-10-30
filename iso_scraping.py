#!/usr/bin/python

from flask import Flask, render_template
import iso_models

app = Flask(__name__)


@app.route('/')
def hello_world():
    ercot = iso_models.get_ERCOT_prices()
    pjm = iso_models.get_PJM_prices()
    ny = iso_models.get_NYISO_prices()
    isone = iso_models.get_ISONE_prices()

    prices = [("ERCOT", ercot),
              ("PJM", pjm),
              ("NY", ny),
              ("ISO-NE", isone)]


    return render_template('rt_prices.html', prices=prices)


if __name__ == '__main__':
    app.run()
