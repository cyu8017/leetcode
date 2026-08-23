// LeetCode 1988 - Find Cutoff Score for Each School
// https://leetcode.com/problems/find-cutoff-score-for-each-school/

class Solution {
    public static final String QUERY = """
SELECT school_id, MIN(IFNULL(score, -1)) AS score
FROM Schools AS s
LEFT JOIN Exam AS e ON s.capacity >= e.student_count
GROUP BY school_id
""";
}
