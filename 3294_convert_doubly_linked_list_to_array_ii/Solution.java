// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

import java.util.ArrayList;
import java.util.List;

class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node() { val = 0; prev = null; next = null; }
    public Node(int x) { val = x; prev = null; next = null; }
}

class Solution {
    public int[] toArray(Node node) {
        while (node != null && node.prev != null) node = node.prev;
        var ans = new ArrayList<Integer>();
        while (node != null) {
            ans.add(node.val);
            node = node.next;
        }
        return ans.toArray();
    }
}
