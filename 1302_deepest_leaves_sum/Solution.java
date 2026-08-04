// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

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
    public int deepestLeavesSum(TreeNode root) {
        List<TreeNode> level = new ArrayList<>();
        level.add(root);
        int answer = 0;
        while (!level.isEmpty()) {
            answer = 0;
            List<TreeNode> next = new ArrayList<>();
            for (TreeNode node : level) {
                answer += node.val;
                if (node.left != null) next.add(node.left);
                if (node.right != null) next.add(node.right);
            }
            level = next;
        }
        return answer;
    }
}
