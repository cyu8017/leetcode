// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

public class Solution {
    public TreeNode SubtreeWithAllDeepest(TreeNode root) {
        (int depth, TreeNode node) Dfs(TreeNode node) {
            if (node == null) return (0, null);
            var (ld, ln) = Dfs(node.left);
            var (rd, rn) = Dfs(node.right);
            if (ld > rd) return (ld + 1, ln);
            if (rd > ld) return (rd + 1, rn);
            return (ld + 1, node);
        }
        return Dfs(root).node;
    }
}
