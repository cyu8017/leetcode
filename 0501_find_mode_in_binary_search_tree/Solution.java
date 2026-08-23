// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
    public int[] findMode(TreeNode root) {
        Map<Integer, Integer> counts = new HashMap<>();
        int[] best = new int[] { 0 };
        inorder(root, counts, best);
        List<Integer> modes = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (entry.getValue() == best[0]) {
                modes.add(entry.getKey());
            }
        }
        int[] result = new int[modes.size()];
        for (int index = 0; index < modes.size(); index++) {
            result[index] = modes.get(index);
        }
        return result;
    }

    private void inorder(TreeNode node, Map<Integer, Integer> counts, int[] best) {
        if (node == null) {
            return;
        }
        inorder(node.left, counts, best);
        int count = counts.getOrDefault(node.val, 0) + 1;
        counts.put(node.val, count);
        best[0] = Math.max(best[0], count);
        inorder(node.right, counts, best);
    }
}
