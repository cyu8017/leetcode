// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

using System.Collections.Generic;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class Solution {
    public int CountPairs(TreeNode root, int distance) {
        int answer = 0;
        List<int> Dfs(TreeNode node) {
            if (node == null) return new List<int>();
            if (node.left == null && node.right == null) return new List<int> { 1 };
            var left = Dfs(node.left);
            var right = Dfs(node.right);
            foreach (int a in left)
                foreach (int b in right)
                    if (a + b <= distance) answer++;
            var result = new List<int>();
            foreach (int depth in left)
                if (depth + 1 < distance) result.Add(depth + 1);
            foreach (int depth in right)
                if (depth + 1 < distance) result.Add(depth + 1);
            return result;
        }
        Dfs(root);
        return answer;
    }
}
