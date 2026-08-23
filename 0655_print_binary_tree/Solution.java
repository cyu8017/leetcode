// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

import java.util.ArrayList;
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
    public List<List<String>> printTree(TreeNode root) {
        int h = height(root);
        int rows = h + 1;
        int cols = (1 << (h + 1)) - 1;
        List<List<String>> res = new ArrayList<>();
        for (int i = 0; i < rows; ++i) {
            List<String> row = new ArrayList<>();
            for (int j = 0; j < cols; ++j) {
                row.add("");
            }
            res.add(row);
        }
        place(root, 0, (cols - 1) / 2, h, res);
        return res;
    }

    private int height(TreeNode node) {
        if (node == null) {
            return -1;
        }
        return 1 + Math.max(height(node.left), height(node.right));
    }

    private void place(TreeNode node, int r, int c, int h, List<List<String>> res) {
        if (node == null) {
            return;
        }
        res.get(r).set(c, String.valueOf(node.val));
        if (r == h) {
            return;
        }
        int offset = 1 << (h - r - 1);
        place(node.left, r + 1, c - offset, h, res);
        place(node.right, r + 1, c + offset, h, res);
    }
}
