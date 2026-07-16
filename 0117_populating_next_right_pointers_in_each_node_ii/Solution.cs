// LeetCode 0117 - Populating Next Right Pointers in Each Node II
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

using System.Collections.Generic;

public class Node {
    public int val;
    public Node left, right, next;
    public Node(int val = 0, Node left = null, Node right = null, Node next = null) {
        this.val = val; this.left = left; this.right = right; this.next = next;
    }
}

public class Solution {
    public Node Connect(Node root) {
        if (root == null) return null;
        var queue = new Queue<Node>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            Node previous = null;
            for (int size = queue.Count; size > 0; size--) {
                Node node = queue.Dequeue();
                if (previous != null) previous.next = node;
                previous = node;
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            previous.next = null;
        }
        return root;
    }
}