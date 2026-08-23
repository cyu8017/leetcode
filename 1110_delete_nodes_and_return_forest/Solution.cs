// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

using System.Collections.Generic;

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
    public IList<TreeNode> DelNodes(TreeNode root, int[] to_delete) {
        var deleteSet = new HashSet<int>(to_delete);
        var forest = new List<TreeNode>();
        Dfs(root, true, deleteSet, forest);
        return forest;
    }

    private TreeNode Dfs(TreeNode node, bool isRoot, HashSet<int> deleteSet, List<TreeNode> forest) {
        if (node == null) {
            return null;
        }
        bool removed = deleteSet.Contains(node.val);
        if (isRoot && !removed) {
            forest.Add(node);
        }
        node.left = Dfs(node.left, removed, deleteSet, forest);
        node.right = Dfs(node.right, removed, deleteSet, forest);
        return removed ? null : node;
    }
}
