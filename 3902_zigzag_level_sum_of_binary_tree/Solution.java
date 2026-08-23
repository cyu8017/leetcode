// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val; this.left = left; this.right = right;
    }
}

class Solution {
    public long[] zigzagLevelSum(TreeNode root) {
        List<Long> ans = new ArrayList<>();
        List<TreeNode> q = new ArrayList<>();
        q.add(root);
        boolean left = true;
        while (!q.isEmpty()) {
            List<TreeNode> nq = new ArrayList<>();
            for (TreeNode node : q) {
                if (node.left != null) nq.add(node.left);
                if (node.right != null) nq.add(node.right);
            }
            int m = q.size();
            long s = 0;
            for (int i = 0; i < m; i++) {
                TreeNode node = left ? q.get(i) : q.get(m - i - 1);
                TreeNode child = left ? node.left : node.right;
                if (child == null) break;
                s += node.val;
            }
            ans.add(s);
            left = !left;
            q = nq;
        }
        long[] out = new long[ans.size()];
        for (int i = 0; i < ans.size(); i++) out[i] = ans.get(i);
        return out;
    }
}
