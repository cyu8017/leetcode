// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

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
    public IList<int> ClosestKValues(TreeNode root, double target, int k) {
        List<int> values = new List<int>();
        Inorder(root, values);

        int lo = 0;
        int hi = values.Count;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (values[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        int left = lo - 1;
        int right = lo;
        List<int> result = new List<int>();
        while (result.Count < k) {
            if (right >= values.Count ||
                (left >= 0 && System.Math.Abs(values[left] - target) <= System.Math.Abs(values[right] - target))) {
                result.Add(values[left]);
                left--;
            } else {
                result.Add(values[right]);
                right++;
            }
        }
        return result;
    }

    private void Inorder(TreeNode node, List<int> values) {
        if (node == null) {
            return;
        }
        Inorder(node.left, values);
        values.Add(node.val);
        Inorder(node.right, values);
    }
}
