// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

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
    public int[] FindMode(TreeNode root) {
        Dictionary<int, int> counts = new();
        int best = 0;
        Inorder(root, counts, ref best);
        return counts.Where(entry => entry.Value == best).Select(entry => entry.Key).ToArray();
    }

    private void Inorder(TreeNode node, Dictionary<int, int> counts, ref int best) {
        if (node == null) {
            return;
        }
        Inorder(node.left, counts, ref best);
        int count = counts.GetValueOrDefault(node.val, 0) + 1;
        counts[node.val] = count;
        best = Math.Max(best, count);
        Inorder(node.right, counts, ref best);
    }
}
