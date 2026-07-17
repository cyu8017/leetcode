// LeetCode 1767 - Find the Subtasks That Did Not Execute
// https://leetcode.com/problems/find-the-subtasks-that-did-not-execute/

const QUERY: &str = r#"
WITH RECURSIVE subtasks AS (
    SELECT task_id, 1 AS subtask_id, subtasks_count FROM Tasks
    UNION ALL
    SELECT task_id, subtask_id + 1, subtasks_count
    FROM subtasks
    WHERE subtask_id < subtasks_count
)
SELECT s.task_id, s.subtask_id
FROM subtasks s
LEFT JOIN Executed e ON s.task_id = e.task_id AND s.subtask_id = e.subtask_id
WHERE e.task_id IS NULL;
"#;
