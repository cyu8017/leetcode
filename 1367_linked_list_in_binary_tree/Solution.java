// LeetCode 1367 - Linked List In Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

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

class Solution {
    public boolean isSubPath(ListNode head, TreeNode root) {
        if (root == null) return false;
        return match(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right);
    }

    private boolean match(ListNode a, TreeNode b) {
        if (a == null) return true;
        if (b == null || a.val != b.val) return false;
        return match(a.next, b.left) || match(a.next, b.right);
    }
}
