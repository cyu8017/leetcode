// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

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
    private int answer;

    public int countPairs(TreeNode root, int distance) {
        answer = 0;
        dfs(root, distance);
        return answer;
    }

    private List<Integer> dfs(TreeNode node, int distance) {
        if (node == null) {
            return Collections.emptyList();
        }
        if (node.left == null && node.right == null) {
            return Collections.singletonList(1);
        }
        List<Integer> left = dfs(node.left, distance);
        List<Integer> right = dfs(node.right, distance);
        for (int a : left) {
            for (int b : right) {
                if (a + b <= distance) {
                    answer++;
                }
            }
        }
        List<Integer> depths = new ArrayList<>();
        for (int depth : left) {
            if (depth + 1 < distance) {
                depths.add(depth + 1);
            }
        }
        for (int depth : right) {
            if (depth + 1 < distance) {
                depths.add(depth + 1);
            }
        }
        return depths;
    }
}
