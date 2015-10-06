uwsgitop
========

``uwsgitop`` is a top-like command that uses the uWSGI Stats Server to
monitor your uwsgi application.

To use uWSGI Stat Server simply use the ``stats`` option followed by
a valid socket address, for example::

    uwsgi --module myapp --socket :3030 --stats /tmp/stats.socket

Note: If you want the stats served over HTTP you will need to also add
the ``stats-http`` option.

To start monitoring your application with ``uwsgitop`` call it with
the socket address like so::

    uwsgitop /tmp/stats.socket

Installation
------------

::

    pip install uwsgitop

Usage
-----

To display async core statistics (e.g. when using gevent) or to switch between
core statistics display mode, press `a`. To refresh the screen super fast press `f`,
and to quit, press `q`.

+--------+---------------------------------------------------------------+
| Field  |  Description                                                  |
+========+===============================================================+
| WID    | Worker ID                                                     |
+--------+---------------------------------------------------------------+
| %      | Worker usage                                                  |
+--------+---------------------------------------------------------------+
| PID    | Worker PID                                                    |
+--------+---------------------------------------------------------------+
| REQ    | How many requests worker did since worker (re)spawn           |
+--------+---------------------------------------------------------------+
| RPS    | Requests per second                                           |
+--------+---------------------------------------------------------------+
| EXC    | Exceptions                                                    |
+--------+---------------------------------------------------------------+
| STATUS | Worker is busy or free to use?                                |
+--------+---------------------------------------------------------------+
| AVG    | Average request time                                          |
+--------+---------------------------------------------------------------+
| RSS    | Worker RSS (Resident Set Size, see linux memory management)   |
+--------+---------------------------------------------------------------+
| VSZ    | Worker VSZ (Virtual Memory Size, see linux memory management) |
+--------+---------------------------------------------------------------+
| TX     | How many data was transmitted by worker                       |
+--------+---------------------------------------------------------------+
| RunT   | How long worker is working                                    |
+--------+---------------------------------------------------------------+

For more info on uWSGI Stats Server see http://projects.unbit.it/uwsgi/wiki/StatsServer
