// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private Map<Integer, Integer> height = new HashMap<>();
    private Map<Integer, Integer> level = new HashMap<>();
    private Map<Integer, List<Integer>> levelMax = new HashMap<>();

    public int[] treeQueries(TreeNode root, int[] queries) {
        dfs(root, 0);
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int q = queries[i];
            int d = level.get(q), h = height.get(q);
            List<Integer> top = levelMax.get(d);
            if (top.get(0) == h) {
                if (top.size() > 1) ans[i] = d + top.get(1);
                else ans[i] = d - 1;
            } else {
                ans[i] = d + top.get(0);
            }
        }
        return ans;
    }

    private int dfs(TreeNode node, int d) {
        if (node == null) return -1;
        level.put(node.val, d);
        int h = 1 + Math.max(dfs(node.left, d + 1), dfs(node.right, d + 1));
        height.put(node.val, h);
        List<Integer> arr = levelMax.computeIfAbsent(d, k -> new ArrayList<>());
        if (arr.isEmpty()) arr.add(h);
        else if (h >= arr.get(0)) {
            if (arr.size() == 1) arr.add(arr.get(0));
            else arr.set(1, arr.get(0));
            arr.set(0, h);
        } else if (arr.size() == 1 || h > arr.get(1)) {
            if (arr.size() == 1) arr.add(h);
            else arr.set(1, h);
        }
        return h;
    }
}

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
