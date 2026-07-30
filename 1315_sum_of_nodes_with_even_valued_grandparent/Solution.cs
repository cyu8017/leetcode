// LeetCode 1315 - Sum Of Nodes With Even Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public int SumEvenGrandparent(TreeNode root) {
        int Dfs(TreeNode node, TreeNode parent, TreeNode grandparent) {
            if (node == null) return 0;
            int add = grandparent != null && grandparent.val % 2 == 0 ? node.val : 0;
            return add + Dfs(node.left, node, parent) + Dfs(node.right, node, parent);
        }
        return Dfs(root, null, null);
    }
}
