// LeetCode 2041 - Accepted Candidates From The Interviews
// https://leetcode.com/problems/accepted-candidates-from-the-interviews/

var QUERY = `SELECT candidate_id
FROM
    Candidates
    JOIN Rounds USING (interview_id)
WHERE years_of_exp >= 2
GROUP BY 1
HAVING SUM(score) > 15`;

module.exports = { QUERY };
