// LeetCode 1932 - Merge BSTs to Create Single BST
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

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

class Solution {
    public TreeNode canMerge(List<TreeNode> trees) {
        Map<Integer, TreeNode> valueToRoot = new HashMap<>();
        Map<Integer, Integer> count = new HashMap<>();
        for (TreeNode tree : trees) {
            valueToRoot.put(tree.val, tree);
            count.merge(tree.val, 1, Integer::sum);
            if (tree.left != null) count.merge(tree.left.val, 1, Integer::sum);
            if (tree.right != null) count.merge(tree.right.val, 1, Integer::sum);
        }
        TreeNode root = null;
        for (TreeNode t : trees) {
            if (count.get(t.val) == 1) {
                if (root != null) return null;
                root = t;
            }
        }
        if (root == null) return null;
        valueToRoot.remove(root.val);
        if (!merge(root, valueToRoot) || !valueToRoot.isEmpty()) return null;
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE) ? root : null;
    }

    private boolean merge(TreeNode node, Map<Integer, TreeNode> valueToRoot) {
        if (node == null) return true;
        if (node.left != null && valueToRoot.containsKey(node.left.val)) {
            node.left = valueToRoot.remove(node.left.val);
        }
        if (node.right != null && valueToRoot.containsKey(node.right.val)) {
            node.right = valueToRoot.remove(node.right.val);
        }
        return merge(node.left, valueToRoot) && merge(node.right, valueToRoot);
    }

    private boolean isValidBST(TreeNode node, long lo, long hi) {
        if (node == null) return true;
        if (node.val <= lo || node.val >= hi) return false;
        return isValidBST(node.left, lo, node.val) && isValidBST(node.right, node.val, hi);
    }
}
