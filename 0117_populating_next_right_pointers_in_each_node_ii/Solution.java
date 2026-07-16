// LeetCode 0117 - Populating Next Right Pointers in Each Node II
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

import java.util.*;

class Node {
    public int val;
    public Node left, right, next;
    public Node() {}
    public Node(int val) { this.val = val; }
    public Node(int val, Node left, Node right, Node next) {
        this.val = val; this.left = left; this.right = right; this.next = next;
    }
}

class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        Queue<Node> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            Node previous = null;
            for (int size = queue.size(); size > 0; size--) {
                Node node = queue.poll();
                if (previous != null) previous.next = node;
                previous = node;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            previous.next = null;
        }
        return root;
    }
}