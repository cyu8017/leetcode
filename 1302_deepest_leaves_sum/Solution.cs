// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

using System.Collections.Generic;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public int DeepestLeavesSum(TreeNode root) {
        var level = new List<TreeNode> { root };
        int answer = 0;
        while (level.Count > 0) {
            answer = 0;
            var next = new List<TreeNode>();
            foreach (var node in level) {
                answer += node.val;
                if (node.left != null) next.Add(node.left);
                if (node.right != null) next.Add(node.right);
            }
            level = next;
        }
        return answer;
    }
}
