// LeetCode 0603 - Consecutive Available Seats
// https://leetcode.com/problems/consecutive-available-seats/

const QUERY = `
SELECT DISTINCT c1.seat_id
FROM Cinema c1
JOIN Cinema c2 ON ABS(c1.seat_id - c2.seat_id) = 1
WHERE c1.free = 1 AND c2.free = 1
ORDER BY c1.seat_id
`
