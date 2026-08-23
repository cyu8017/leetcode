// LeetCode 2793 - Status of Flight Tickets
// https://leetcode.com/problems/status-of-flight-tickets/

class Solution {
    public static final String QUERY = """
SELECT
    passenger_id,
    IF(
        (
            RANK() OVER (
                PARTITION BY flight_id
                ORDER BY booking_time
            )
        ) <= capacity,
        'Confirmed',
        'Waitlist'
    ) AS Status
FROM
    Passengers
    JOIN Flights USING (flight_id)
ORDER BY passenger_id
""";
}
