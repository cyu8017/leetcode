// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

import java.util.*;

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
    private Map<Integer, List<TreeNode>> memo = new HashMap<>();

    public List<TreeNode> allPossibleFBT(int n) {
        return build(n);
    }

    private List<TreeNode> build(int nodes) {
        if (memo.containsKey(nodes)) return memo.get(nodes);
        List<TreeNode> res = new ArrayList<>();
        if (nodes % 2 == 0) {
            memo.put(nodes, res);
            return res;
        }
        if (nodes == 1) {
            res.add(new TreeNode(0));
            memo.put(nodes, res);
            return res;
        }
        for (int left = 1; left < nodes; left += 2) {
            int right = nodes - 1 - left;
            for (TreeNode L : build(left)) {
                for (TreeNode R : build(right)) {
                    res.add(new TreeNode(0, L, R));
                }
            }
        }
        memo.put(nodes, res);
        return res;
    }
}
