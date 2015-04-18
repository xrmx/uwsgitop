Run your uWSGI server with the stats server enabled, Ex.:

uwsgi --module myapp --socket :3030 --stats /tmp/stats.socket

Then connect uwsgitop to the stats socket

uwsgitop /tmp/stats.socket

To display async core statistics (e.g. when using gevent) or to switch between
core statistics display mode, press 'a'.

To refresh the screen super fast, press 'f'.

To quit, press 'q'.



 Field  |  Description    |
--------|:---------------:|
WID    | Worker ID       |
%      | Worker usage    |
PID    | Worker PID      |
REQ    | How many requests worker did since worker (re)spawn |
RPS    | Requests per second |
EXC    | Exceptions  |
STATUS | Worker is busy or free to use? |
AVG    | Average request time |
RSS    | Worker RSS (Resident Set Size, see linux memory management) |
VSZ    | Worker VSZ (Virtual Memory Size, see linux memory management)|
TX     | How many data was transmitted by worker|
RunT   | How long worker is working|


more info on http://projects.unbit.it/uwsgi/wiki/StatsServer
