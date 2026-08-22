// LeetCode 2793 - Status of Flight Tickets
// https://leetcode.com/problems/status-of-flight-tickets/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    passenger_id,\n"
    "    IF(\n"
    "        (\n"
    "            RANK() OVER (\n"
    "                PARTITION BY flight_id\n"
    "                ORDER BY booking_time\n"
    "            )\n"
    "        ) <= capacity,\n"
    "        'Confirmed',\n"
    "        'Waitlist'\n"
    "    ) AS Status\n"
    "FROM\n"
    "    Passengers\n"
    "    JOIN Flights USING (flight_id)\n"
    "ORDER BY passenger_id\n";
