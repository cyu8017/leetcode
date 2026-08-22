// LeetCode 2026 - Low-Quality Problems
// https://leetcode.com/problems/low-quality-problems/

const char* QUERY =
    "\n"
    "SELECT problem_id\n"
    "FROM Problems\n"
    "WHERE likes / (likes + dislikes) < 0.6\n"
    "ORDER BY problem_id\n";
