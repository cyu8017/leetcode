// LeetCode 2783 - Flight Occupancy and Waitlist Analysis
// https://leetcode.com/problems/flight-occupancy-and-waitlist-analysis/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    f.flight_id,\n"
    "    LEAST(COUNT(p.passenger_id), f.capacity) AS booked_cnt,\n"
    "    GREATEST(COUNT(p.passenger_id) - f.capacity, 0) AS waitlist_cnt\n"
    "FROM Flights AS f\n"
    "LEFT JOIN Passengers AS p USING (flight_id)\n"
    "GROUP BY f.flight_id, f.capacity\n"
    "ORDER BY f.flight_id\n";
