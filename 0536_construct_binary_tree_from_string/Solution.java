// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    private int index;

    public TreeNode str2tree(String s) {
        if (s == null || s.isEmpty()) {
            return null;
        }
        index = 0;
        return parse(s);
    }

    private TreeNode parse(String s) {
        if (index >= s.length()) {
            return null;
        }

        int sign = 1;
        if (s.charAt(index) == '-') {
            sign = -1;
            index++;
        }

        int value = 0;
        while (index < s.length() && Character.isDigit(s.charAt(index))) {
            value = value * 10 + (s.charAt(index) - '0');
            index++;
        }

        TreeNode node = new TreeNode(sign * value);

        if (index < s.length() && s.charAt(index) == '(') {
            index++;
            node.left = parse(s);
            index++;
        }

        if (index < s.length() && s.charAt(index) == '(') {
            index++;
            node.right = parse(s);
            index++;
        }

        return node;
    }
}
