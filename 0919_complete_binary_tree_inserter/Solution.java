// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

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

class CBTInserter {
    private final TreeNode root;
    private final Queue<TreeNode> parents = new ArrayDeque<>();

    public CBTInserter(TreeNode root) {
        this.root = root;
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            if (node.left != null) q.offer(node.left);
            else {
                parents.offer(node);
                break;
            }
            if (node.right != null) q.offer(node.right);
            else {
                parents.offer(node);
                break;
            }
        }
        while (!q.isEmpty()) parents.offer(q.poll());
    }

    public int insert(int val) {
        TreeNode parent = parents.peek();
        TreeNode child = new TreeNode(val);
        if (parent.left == null) parent.left = child;
        else {
            parent.right = child;
            parents.poll();
        }
        parents.offer(child);
        return parent.val;
    }

    public TreeNode getRoot() {
        return root;
    }
}
