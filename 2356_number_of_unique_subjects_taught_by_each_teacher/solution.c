// LeetCode 2356 - Number of Unique Subjects Taught by Each Teacher
// https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

const char* QUERY =
    "\n"
    "SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt\n"
    "FROM Teacher\n"
    "GROUP BY 1\n";
