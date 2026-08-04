// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        Set<Integer> values = new HashSet<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        if (root1 != null) stack.push(root1);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            values.add(node.val);
            if (node.left != null) stack.push(node.left);
            if (node.right != null) stack.push(node.right);
        }
        stack.clear();
        if (root2 != null) stack.push(root2);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (values.contains(target - node.val)) return true;
            if (node.left != null) stack.push(node.left);
            if (node.right != null) stack.push(node.right);
        }
        return false;
    }
}
