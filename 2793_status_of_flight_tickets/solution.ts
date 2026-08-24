// LeetCode 2793 - Status Of Flight Tickets
// https://leetcode.com/problems/status-of-flight-tickets/

export const QUERY = `SELECT
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
ORDER BY passenger_id`;
