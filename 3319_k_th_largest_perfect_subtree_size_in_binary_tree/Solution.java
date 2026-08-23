// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

import java.util.ArrayList;
import java.util.Collections;
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
    private List<Integer> sizes;

    /** returns {height, size, isPerfect} */
    private int[] dfs(TreeNode node) {
        if (node == null) return new int[] {0, 0, 1};
        int[] L = dfs(node.left);
        int[] R = dfs(node.right);
        int sz = L[1] + R[1] + 1;
        boolean perf = L[2] == 1 && R[2] == 1 && L[0] == R[0];
        if (perf) sizes.add(sz);
        return new int[] {Math.max(L[0], R[0]) + 1, sz, perf ? 1 : 0};
    }

    public int kthLargestPerfectSubtree(TreeNode root, int k) {
        sizes = new ArrayList<>();
        dfs(root);
        sizes.sort(Collections.reverseOrder());
        if (k > sizes.size()) return -1;
        return sizes.get(k - 1);
    }
}
