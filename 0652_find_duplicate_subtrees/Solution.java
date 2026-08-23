// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
    private final Map<String, Integer> counts = new HashMap<>();
    private final List<TreeNode> result = new ArrayList<>();

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        counts.clear();
        result.clear();
        serialize(root);
        return result;
    }

    private String serialize(TreeNode node) {
        if (node == null) {
            return "#";
        }
        String key = node.val + "," + serialize(node.left) + "," + serialize(node.right);
        int count = counts.getOrDefault(key, 0) + 1;
        counts.put(key, count);
        if (count == 2) {
            result.add(node);
        }
        return key;
    }
}
