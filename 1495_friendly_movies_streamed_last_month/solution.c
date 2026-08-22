// LeetCode 1495 - Friendly Movies Streamed Last Month
// https://leetcode.com/problems/friendly-movies-streamed-last-month/

const char* QUERY =
    "\n"
    "SELECT DISTINCT title\n"
    "FROM TVProgram p JOIN Content c ON p.content_id=c.content_id\n"
    "WHERE c.Kids_content='Y' AND c.content_type='Movies'\n"
    "  AND p.program_date >= '2020-06-01' AND p.program_date < '2020-07-01'\n";
