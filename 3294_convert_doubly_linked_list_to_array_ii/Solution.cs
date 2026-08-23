// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

using System.Collections.Generic;

public class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node() { val = 0; prev = null; next = null; }
    public Node(int x) { val = x; prev = null; next = null; }
}

public class Solution {
    public int[] ToArray(Node node) {
        while (node != null && node.prev != null) node = node.prev;
        var ans = new List<int>();
        while (node != null) {
            ans.Add(node.val);
            node = node.next;
        }
        return ans.ToArray();
    }
}
