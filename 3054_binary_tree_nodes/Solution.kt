// LeetCode 3054 - Binary Tree Nodes
// https://leetcode.com/problems/binary-tree-nodes/

class Solution {
    companion object {
        const val QUERY = "SELECT DISTINCT\n" +
            "    t1.N AS N,\n" +
            "    IF(t1.P IS NULL, 'Root', IF(t2.P IS NULL, 'Leaf', 'Inner')) AS Type\n" +
            "FROM\n" +
            "    Tree AS t1\n" +
            "    LEFT JOIN Tree AS t2 ON t1.N = t2.p\n" +
            "ORDER BY 1;"
    }
}
