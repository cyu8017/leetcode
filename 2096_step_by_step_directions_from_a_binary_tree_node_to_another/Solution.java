// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val; this.left = left; this.right = right;
    }
}

class Solution {
    private boolean path(TreeNode node, int target, StringBuilder p) {
        if (node == null) return false;
        if (node.val == target) return true;
        p.append('L');
        if (path(node.left, target, p)) return true;
        p.setCharAt(p.length() - 1, 'R');
        if (path(node.right, target, p)) return true;
        p.setLength(p.length() - 1);
        return false;
    }

    public String getDirections(TreeNode root, int startValue, int destValue) {
        StringBuilder ps = new StringBuilder();
        StringBuilder pd = new StringBuilder();
        path(root, startValue, ps);
        path(root, destValue, pd);
        int i = 0;
        while (i < ps.length() && i < pd.length() && ps.charAt(i) == pd.charAt(i)) i++;
        StringBuilder ans = new StringBuilder();
        for (int k = 0; k < ps.length() - i; k++) ans.append('U');
        ans.append(pd.substring(i));
        return ans.toString();
    }
}
