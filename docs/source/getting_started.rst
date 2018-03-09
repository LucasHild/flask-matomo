Getting Started
===============

Installation
------------

To install Flask-Matomo::

  pip install flask-matomo

Simple integration
------------------

.. code-block:: python

  from flask import Flask, render_template
  from flask_matomo import *

  app = Flask(__name__)
  matomo = Matomo(app, matomo_url="https://matomo.mydomain.com",
                  id_site=5, token_auth="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

  @app.route("/")
  def index():
    return render_template("index.html")

  if __name__ == "__main__":
    app.run()

In the code above:

#. The ``Matomo`` object is created by passing in the Flask application and arguments to configure Matomo.
#. The ``matomo_url`` parameter is the url to your Matomo installation.
#. The ``id_site`` parameter is the id of your site. This is used if you track several websites with on Matomo installation. It can be found if you open your Matomo dashboard, change to site you want to track and look for ``&idSite=`` in the url.
#. The ``token_auth`` parameter can be found in the area API in the settings of Matomo. It is required for tracking the ip address.
