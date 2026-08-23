// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> closestNodes(TreeNode root, List<Integer> queries) {
        List<Integer> vals = new ArrayList<>();
        inorder(root, vals);
        List<List<Integer>> ans = new ArrayList<>();
        for (int q : queries) {
            int j = lowerBound(vals, q);
            int mx = j < vals.size() ? vals.get(j) : -1;
            int mn = -1;
            if (j < vals.size() && vals.get(j) == q) mn = q;
            else if (j > 0) mn = vals.get(j - 1);
            ans.add(Arrays.asList(mn, mx));
        }
        return ans;
    }

    private void inorder(TreeNode node, List<Integer> vals) {
        if (node == null) return;
        inorder(node.left, vals);
        vals.add(node.val);
        inorder(node.right, vals);
    }

    private int lowerBound(List<Integer> vals, int q) {
        int lo = 0, hi = vals.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (vals.get(mid) < q) lo = mid + 1;
            else hi = mid;
        }
        return lo;
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
