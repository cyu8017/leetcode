// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        List<Integer> values = new ArrayList<>();
        inorder(root, values);

        int index = lowerBound(values, target);
        int left = index - 1;
        int right = index;
        List<Integer> result = new ArrayList<>();

        while (result.size() < k) {
            if (right >= values.size() ||
                (left >= 0 && Math.abs(values.get(left) - target) <= Math.abs(values.get(right) - target))) {
                result.add(values.get(left));
                left--;
            } else {
                result.add(values.get(right));
                right++;
            }
        }
        return result;
    }

    private void inorder(TreeNode node, List<Integer> values) {
        if (node == null) {
            return;
        }
        inorder(node.left, values);
        values.add(node.val);
        inorder(node.right, values);
    }

    private int lowerBound(List<Integer> values, double target) {
        int lo = 0;
        int hi = values.size();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (values.get(mid) < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
