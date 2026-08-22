// LeetCode 1294 - Weather Type in Each Country
// https://leetcode.com/problems/weather-type-in-each-country/

const char* QUERY =
    "\n"
    "SELECT c.country_name,\n"
    "       CASE\n"
    "           WHEN AVG(w.weather_state) <= 15 THEN 'Cold'\n"
    "           WHEN AVG(w.weather_state) >= 25 THEN 'Hot'\n"
    "           ELSE 'Warm'\n"
    "       END AS weather_type\n"
    "FROM Countries c\n"
    "JOIN Weather w ON w.country_id = c.country_id\n"
    "WHERE w.day BETWEEN '2019-11-01' AND '2019-11-30'\n"
    "GROUP BY c.country_id, c.country_name\n";
