// LeetCode 1421 - NPV Queries
// https://leetcode.com/problems/npv-queries/

const char* QUERY = R"SQL(
SELECT q.id, q.year, COALESCE(n.npv, 0) AS npv
FROM Queries q
LEFT JOIN NPV n ON n.id = q.id AND n.year = q.year
)SQL";
