// LeetCode 1367 - Linked List In Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

public class ListNode {
    public int val; public ListNode next;
    public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; }
}
public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {
    public bool IsSubPath(ListNode head, TreeNode root) {
        bool Match(ListNode a, TreeNode b) {
            if (a == null) return true;
            if (b == null || a.val != b.val) return false;
            return Match(a.next, b.left) || Match(a.next, b.right);
        }
        return root != null && (Match(head, root) || IsSubPath(head, root.left) || IsSubPath(head, root.right));
    }
}
