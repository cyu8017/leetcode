// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

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
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> nodes = new HashMap<>();
        Set<Integer> child = new HashSet<>();
        for (int[] d : descriptions) {
            int p = d[0], c = d[1], isLeft = d[2];
            nodes.putIfAbsent(p, new TreeNode(p));
            nodes.putIfAbsent(c, new TreeNode(c));
            if (isLeft == 1) nodes.get(p).left = nodes.get(c);
            else nodes.get(p).right = nodes.get(c);
            child.add(c);
        }
        for (Map.Entry<Integer, TreeNode> kv : nodes.entrySet())
            if (!child.contains(kv.getKey())) return kv.getValue();
        return null;
    }
}
