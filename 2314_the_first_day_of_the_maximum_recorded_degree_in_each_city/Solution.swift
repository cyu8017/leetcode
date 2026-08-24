// LeetCode 2314 - The First Day Of The Maximum Recorded Degree In Each City
// https://leetcode.com/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/

let QUERY = """
WITH
    T AS (
        SELECT
            *,
            RANK() OVER (
                PARTITION BY city_id
                ORDER BY degree DESC, day
            ) AS rk
        FROM Weather
    )
SELECT city_id, day, degree
FROM T
WHERE rk = 1
ORDER BY 1
"""
