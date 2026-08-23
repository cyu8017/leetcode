// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

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
    public int[] FindFrequentTreeSum(TreeNode root) {
        Dictionary<int, int> counts = new();
        SubtreeSum(root, counts);
        if (counts.Count == 0) {
            return Array.Empty<int>();
        }
        int best = counts.Values.Max();
        return counts
            .Where(entry => entry.Value == best)
            .Select(entry => entry.Key)
            .OrderBy(value => value)
            .ToArray();
    }

    private int SubtreeSum(TreeNode node, Dictionary<int, int> counts) {
        if (node == null) {
            return 0;
        }
        int total = node.val + SubtreeSum(node.left, counts) + SubtreeSum(node.right, counts);
        counts[total] = counts.GetValueOrDefault(total, 0) + 1;
        return total;
    }
}
