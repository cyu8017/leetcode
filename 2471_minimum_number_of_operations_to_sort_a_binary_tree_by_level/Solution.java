// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;

class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class Solution {
    public int minimumOperations(TreeNode root) {
        if (root == null) return 0;
        int ans = 0;
        var q = new ArrayDeque<TreeNode>();
        q.offer(root);
        while (q.size() > 0) {
            int sz = q.size();
            int[] vals = new int[sz];
            for (int i = 0; i < sz; i++) {
                TreeNode node = q.poll();
                vals[i] = node.val;
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            int[] sorted = vals.clone();
            Arrays.sort(sorted);
            var pos = new HashMap<Integer, Integer>();
            for (int i = 0; i < sz; i++) pos.put(vals[i], i);
            for (int i = 0; i < sz; i++) {
                if (vals[i] != sorted[i]) {
                    int j = pos.get(sorted[i]);
                    (vals[i], vals[j]) = (vals[j], vals[i]);
                    pos.put(vals[j], j);
                    pos.put(vals[i], i);
                    ans++;
                }
            }
        }
        return ans;
    }
}
