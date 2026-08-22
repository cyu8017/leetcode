// LeetCode 1308 - Running Total for Different Genders
// https://leetcode.com/problems/running-total-for-different-genders/

const char* QUERY =
    "\n"
    "SELECT gender, day,\n"
    "       SUM(score_points) OVER (PARTITION BY gender ORDER BY day) AS total\n"
    "FROM Scores\n"
    "ORDER BY gender, day\n";
