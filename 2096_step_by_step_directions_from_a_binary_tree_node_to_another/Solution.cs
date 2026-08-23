// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

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
    private bool Path(TreeNode node, int target, System.Text.StringBuilder p) {
        if (node == null) return false;
        if (node.val == target) return true;
        p.Append('L');
        if (Path(node.left, target, p)) return true;
        p[p.Length - 1] = 'R';
        if (Path(node.right, target, p)) return true;
        p.Length--;
        return false;
    }

    public string GetDirections(TreeNode root, int startValue, int destValue) {
        var ps = new System.Text.StringBuilder();
        var pd = new System.Text.StringBuilder();
        Path(root, startValue, ps);
        Path(root, destValue, pd);
        int i = 0;
        while (i < ps.Length && i < pd.Length && ps[i] == pd[i]) i++;
        return new string('U', ps.Length - i) + pd.ToString(i, pd.Length - i);
    }
}
