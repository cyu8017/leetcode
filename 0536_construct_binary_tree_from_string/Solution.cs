// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

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
    private int index;

    public TreeNode Str2tree(string s) {
        if (string.IsNullOrEmpty(s)) {
            return null;
        }
        index = 0;
        return Parse(s);
    }

    private TreeNode Parse(string s) {
        if (index >= s.Length) {
            return null;
        }

        int sign = 1;
        if (s[index] == '-') {
            sign = -1;
            index++;
        }

        int value = 0;
        while (index < s.Length && char.IsDigit(s[index])) {
            value = value * 10 + (s[index] - '0');
            index++;
        }

        TreeNode node = new TreeNode(sign * value);

        if (index < s.Length && s[index] == '(') {
            index++;
            node.left = Parse(s);
            index++;
        }

        if (index < s.Length && s[index] == '(') {
            index++;
            node.right = Parse(s);
            index++;
        }

        return node;
    }
}
