// LeetCode 0620 - Not Boring Movies
// https://leetcode.com/problems/not-boring-movies/

const char* QUERY =
    "\n"
    "SELECT *\n"
    "FROM Cinema\n"
    "WHERE MOD(id, 2) = 1 AND description != 'boring'\n"
    "ORDER BY rating DESC\n";
