// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

import java.util.*;

class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        return leaves(root1).equals(leaves(root2));
    }

    private List<Integer> leaves(TreeNode node) {
        List<Integer> result = new ArrayList<>();
        dfs(node, result);
        return result;
    }

    private void dfs(TreeNode cur, List<Integer> result) {
        if (cur == null) return;
        if (cur.left == null && cur.right == null) {
            result.add(cur.val);
            return;
        }
        dfs(cur.left, result);
        dfs(cur.right, result);
    }
}
