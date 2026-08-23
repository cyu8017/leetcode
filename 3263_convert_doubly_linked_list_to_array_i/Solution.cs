// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

using System.Collections.Generic;

public class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node(int val = 0, Node prev = null, Node next = null) {
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}

public class Solution {
    public int[] ToArray(Node head) {
        var ans = new List<int>();
        while (head != null) {
            ans.Add(head.val);
            head = head.next;
        }
        return ans.ToArray();
    }
}
