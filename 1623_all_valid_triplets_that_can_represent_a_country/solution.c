// LeetCode 1623 - All Valid Triplets That Can Represent a Country
// https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country/

const char* QUERY =
    "\n"
    "SELECT s1.student_name AS member_A, s2.student_name AS member_B, s3.student_name AS member_C\n"
    "FROM SchoolA s1\n"
    "CROSS JOIN SchoolB s2\n"
    "CROSS JOIN SchoolC s3\n"
    "WHERE s1.student_id <> s2.student_id AND s1.student_id <> s3.student_id AND s2.student_id <> s3.student_id\n"
    "  AND s1.student_name <> s2.student_name AND s1.student_name <> s3.student_name AND s2.student_name <> s3.student_name;\n";
