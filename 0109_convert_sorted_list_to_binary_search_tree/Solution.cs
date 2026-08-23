// LeetCode 0109 - Convert Sorted List to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

using System.Collections.Generic;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

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
    public TreeNode SortedListToBST(ListNode head) {
        var values = new List<int>();
        while (head != null) {
            values.Add(head.val);
            head = head.next;
        }
        return Build(values, 0, values.Count - 1);
    }

    private TreeNode Build(List<int> values, int left, int right) {
        if (left > right) {
            return null;
        }
        int mid = (left + right + 1) / 2;
        var root = new TreeNode(values[mid]);
        root.left = Build(values, left, mid - 1);
        root.right = Build(values, mid + 1, right);
        return root;
    }
}
