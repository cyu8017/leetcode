// LeetCode 1988 - Find Cutoff Score for Each School
// https://leetcode.com/problems/find-cutoff-score-for-each-school/

const char* QUERY =
    "\n"
    "SELECT school_id, MIN(IFNULL(score, -1)) AS score\n"
    "FROM Schools AS s\n"
    "LEFT JOIN Exam AS e ON s.capacity >= e.student_count\n"
    "GROUP BY school_id\n";
