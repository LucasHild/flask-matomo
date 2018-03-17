Configuration
===============

Ignore Routes
-------------

If you wan't to prevent one route from being tracked, you can ignore it by adding a decorator in front of the function.

.. code-block:: python

  @app.route("/admin")
  @matomo.ignore()
  def admin():
      return render_template("admin.html")
