// LeetCode 0620 - Not Boring Movies
// https://leetcode.com/problems/not-boring-movies/

const char* QUERY = R"SQL(
SELECT *
FROM Cinema
WHERE MOD(id, 2) = 1 AND description != 'boring'
ORDER BY rating DESC
)SQL";
