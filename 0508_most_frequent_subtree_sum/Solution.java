// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

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
    public int[] findFrequentTreeSum(TreeNode root) {
        Map<Integer, Integer> counts = new HashMap<>();
        subtreeSum(root, counts);
        if (counts.isEmpty()) {
            return new int[0];
        }
        int best = 0;
        for (int count : counts.values()) {
            best = Math.max(best, count);
        }
        List<Integer> frequent = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (entry.getValue() == best) {
                frequent.add(entry.getKey());
            }
        }
        frequent.sort(Integer::compareTo);
        int[] result = new int[frequent.size()];
        for (int index = 0; index < frequent.size(); index++) {
            result[index] = frequent.get(index);
        }
        return result;
    }

    private int subtreeSum(TreeNode node, Map<Integer, Integer> counts) {
        if (node == null) {
            return 0;
        }
        int total = node.val + subtreeSum(node.left, counts) + subtreeSum(node.right, counts);
        counts.put(total, counts.getOrDefault(total, 0) + 1);
        return total;
    }
}
