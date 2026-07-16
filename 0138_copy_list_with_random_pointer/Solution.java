// LeetCode 0138 - Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/

import java.util.*;

class Solution {
    public Node copyRandomList(Node head) {
        return copy(head, new HashMap<>());
    }

    private Node copy(Node node, Map<Node, Node> clones) {
        if (node == null) return null;
        if (clones.containsKey(node)) return clones.get(node);
        Node clone = new Node(node.val);
        clones.put(node, clone);
        clone.next = copy(node.next, clones);
        clone.random = copy(node.random, clones);
        return clone;
    }
}
