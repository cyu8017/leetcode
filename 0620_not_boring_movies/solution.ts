// LeetCode 0620 - Not Boring Movies
// https://leetcode.com/problems/not-boring-movies/

export const QUERY = `SELECT *
FROM Cinema
WHERE MOD(id, 2) = 1 AND description != 'boring'
ORDER BY rating DESC`;
