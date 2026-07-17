// LeetCode 1767 - Find the Subtasks That Did Not Execute
// https://leetcode.com/problems/find-the-subtasks-that-did-not-execute/

class Solution {
    companion object {
        const val QUERY = "WITH RECURSIVE subtasks AS (\n" +
            "    SELECT task_id, 1 AS subtask_id, subtasks_count FROM Tasks\n" +
            "    UNION ALL\n" +
            "    SELECT task_id, subtask_id + 1, subtasks_count\n" +
            "    FROM subtasks\n" +
            "    WHERE subtask_id < subtasks_count\n" +
            ")\n" +
            "SELECT s.task_id, s.subtask_id\n" +
            "FROM subtasks s\n" +
            "LEFT JOIN Executed e ON s.task_id = e.task_id AND s.subtask_id = e.subtask_id\n" +
            "WHERE e.task_id IS NULL;\n"
    }
}
