// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

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

public class CBTInserter {
    private readonly TreeNode root;
    private readonly Queue<TreeNode> parents = new();

    public CBTInserter(TreeNode root) {
        this.root = root;
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        while (q.Count > 0) {
            TreeNode node = q.Dequeue();
            if (node.left != null) q.Enqueue(node.left);
            else {
                parents.Enqueue(node);
                break;
            }
            if (node.right != null) q.Enqueue(node.right);
            else {
                parents.Enqueue(node);
                break;
            }
        }
        while (q.Count > 0) parents.Enqueue(q.Dequeue());
    }

    public int Insert(int val) {
        TreeNode parent = parents.Peek();
        TreeNode child = new TreeNode(val);
        if (parent.left == null) parent.left = child;
        else {
            parent.right = child;
            parents.Dequeue();
        }
        parents.Enqueue(child);
        return parent.val;
    }

    public TreeNode GetRoot() {
        return root;
    }
}
