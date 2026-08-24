// LeetCode 1303 - Find The Team Size
// https://leetcode.com/problems/find-the-team-size/

const QUERY: &str = r#"
SELECT employee_id, COUNT(*) OVER (PARTITION BY team_id) AS team_size
FROM Employee
"#;
