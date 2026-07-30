// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

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

public class FindElements {
    private readonly HashSet<int> values = new HashSet<int>();

    public FindElements(TreeNode root) {
        void Recover(TreeNode node, int value) {
            if (node == null) return;
            node.val = value;
            values.Add(value);
            Recover(node.left, 2 * value + 1);
            Recover(node.right, 2 * value + 2);
        }
        Recover(root, 0);
    }

    public bool Find(int target) {
        return values.Contains(target);
    }
}
