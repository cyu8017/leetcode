// LeetCode 2041 - Accepted Candidates From the Interviews
// https://leetcode.com/problems/accepted-candidates-from-the-interviews/

const char* QUERY =
    "\n"
    "SELECT candidate_id\n"
    "FROM\n"
    "    Candidates\n"
    "    JOIN Rounds USING (interview_id)\n"
    "WHERE years_of_exp >= 2\n"
    "GROUP BY 1\n"
    "HAVING SUM(score) > 15\n";
