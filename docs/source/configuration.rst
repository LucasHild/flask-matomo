Configuration
===============

Details about a route
---------------------

You can set details for a route, which will overwrite the parsed details.

.. code-block:: python

  @app.route("/users")
  @matomo.details(action_name="Users")
  def all_users():
      return render_template("users.html")


Ignore routes
-------------

If you wan't to prevent one route from being tracked, you can ignore it by adding a decorator in front of the function.

.. code-block:: python

  @app.route("/admin")
  @matomo.ignore()
  def admin():
      return render_template("admin.html")
