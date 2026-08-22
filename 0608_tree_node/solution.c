// LeetCode 0608 - Tree Node
// https://leetcode.com/problems/tree-node/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    id,\n"
    "    CASE\n"
    "        WHEN p_id IS NULL THEN 'Root'\n"
    "        WHEN id IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Inner'\n"
    "        ELSE 'Leaf'\n"
    "    END AS type\n"
    "FROM Tree\n";
