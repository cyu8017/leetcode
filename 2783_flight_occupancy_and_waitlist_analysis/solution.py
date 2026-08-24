# LeetCode 2783 - Flight Occupancy and Waitlist Analysis
# https:# leetcode.com/problems/flight-occupancy-and-waitlist-analysis/

# Write your MySQL query statement below
QUERY = """
SELECT
    f.flight_id,
    LEAST(COUNT(p.passenger_id), f.capacity) AS booked_cnt,
    GREATEST(COUNT(p.passenger_id) - f.capacity, 0) AS waitlist_cnt
FROM Flights AS f
LEFT JOIN Passengers AS p USING (flight_id)
GROUP BY f.flight_id, f.capacity
ORDER BY f.flight_id
"""
