# api_query
First project:
Using an existing publicly available REST API on the internet of your choice (for example Github) and show how you would authenticate (if necessary) against this API and then utilise a part of the API to fetch some information and format it appropriately for storage in data store of your choice.
 
#########################

This app will query https://api.openweathermap.org for weather data for specific cities. It can insert the data into a database. It assumes that you have MariaDB installed, without root password.

api_query.py contains one function: owm. It takes the city name as parameter and returns: City name, country code, temperature in C, weather description, and time of last update.
The result is also printed to console:
python3.6
Python 3.6.7 (default, Dec  5 2018, 15:02:05)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from api_query import owm
>>> owm('Berlin')
('Berlin', 'DE', '3.2C', 'Clear', '2019-04-02 01:47:24')
>>>

db.py contains 2 functions: add_to_db and query_db.

add_to_db imports api_query and calls owm function. It adds the output to a database. It creates the db and table if they are missing. The function prints where the info was inserted and what was the line number.
The table looks like this:
+-------------+-----------+---------+--------+---------+---------------------+
| query_index | city      | country | temp_C | weather | last_update         |
+-------------+-----------+---------+--------+---------+---------------------+
|           1 | London    | GB      |      4 | Clouds  | 2019-04-02 00:35:12 |
|           2 | Prague    | CZ      |      3 | Clear   | 2019-04-02 00:37:29 |
|           3 | Paris     | FR      |     13 | Clear   | 2019-04-02 00:32:44 |
|           4 | Moscow    | RU      |     -2 | Clear   | 2019-04-02 00:29:59 |
|           5 | New York  | US      |      5 | Clear   | 2019-04-02 00:39:12 |
|           6 | Las Vegas | US      |     23 | Clear   | 2019-04-02 00:35:42 |
|           7 | Tokyo     | JP      |      9 | Clouds  | 2019-04-02 00:41:50 |
|           8 | London    | GB      |      4 | Clouds  | 2019-04-02 00:35:12 |
|           9 | New York  | US      |      5 | Clear   | 2019-04-02 00:39:12 |
|          10 | Paris     | FR      |     13 | Clear   | 2019-04-02 00:47:49 |
|          11 | Bucharest | RO      |     11 | Clear   | 2019-04-02 00:53:43 |
|          12 | Brno      | CZ      |      2 | Clear   | 2019-04-02 01:32:11 |
|          13 | Warsaw    | PL      |      1 | Clear   | 2019-04-02 01:35:58 |
|          14 | Warsaw    | PL      |      1 | Clear   | 2019-04-02 01:35:58 |
+-------------+-----------+---------+--------+---------+---------------------+

query_db takes as argument the name of a city and returns all the information for that city from the db.
Sample output:
>>> query_db("London")
(1, 'London', 'GB', 4, 'Clouds', '2019-04-02 00:35:12')
(8, 'London', 'GB', 4, 'Clouds', '2019-04-02 00:35:12')
>>>


