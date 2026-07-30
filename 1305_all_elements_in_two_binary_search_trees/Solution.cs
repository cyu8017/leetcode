// LeetCode 1305 - All Elements In Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

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
    public IList<int> GetAllElements(TreeNode root1, TreeNode root2) {
        var a = Inorder(root1);
        var b = Inorder(root2);
        var answer = new List<int>();
        int i = 0, j = 0;
        while (i < a.Count || j < b.Count) {
            if (j == b.Count || (i < a.Count && a[i] <= b[j])) answer.Add(a[i++]);
            else answer.Add(b[j++]);
        }
        return answer;
    }
    List<int> Inorder(TreeNode root) {
        var result = new List<int>();
        void Dfs(TreeNode node) {
            if (node == null) return;
            Dfs(node.left);
            result.Add(node.val);
            Dfs(node.right);
        }
        Dfs(root);
        return result;
    }
}
