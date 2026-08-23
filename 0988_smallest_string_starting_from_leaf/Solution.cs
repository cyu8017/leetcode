// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class Solution {
    public string SmallestFromLeaf(TreeNode root) {
        string best = "~";
        void Dfs(TreeNode node, string path) {
            if (node == null) return;
            path = (char)('a' + node.val) + path;
            if (node.left == null && node.right == null) {
                if (string.CompareOrdinal(path, best) < 0) best = path;
                return;
            }
            Dfs(node.left, path);
            Dfs(node.right, path);
        }
        Dfs(root, "");
        return best;
    }
}
