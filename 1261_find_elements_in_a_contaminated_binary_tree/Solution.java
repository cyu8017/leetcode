// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

import java.util.*;

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

class FindElements {
    private final Set<Integer> values = new HashSet<>();

    public FindElements(TreeNode root) {
        recover(root, 0);
    }

    private void recover(TreeNode node, int value) {
        if (node == null) return;
        node.val = value;
        values.add(value);
        recover(node.left, 2 * value + 1);
        recover(node.right, 2 * value + 2);
    }

    public boolean find(int target) {
        return values.contains(target);
    }
}
