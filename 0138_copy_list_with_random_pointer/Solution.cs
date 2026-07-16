// LeetCode 0138 - Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/

using System.Collections.Generic;

public class Solution {
    public Node CopyRandomList(Node head) {
        return Copy(head, new Dictionary<Node, Node>());
    }

    private Node Copy(Node node, Dictionary<Node, Node> clones) {
        if (node == null) return null;
        if (clones.TryGetValue(node, out Node copy)) return copy;
        copy = new Node(node.val);
        clones[node] = copy;
        copy.next = Copy(node.next, clones);
        copy.random = Copy(node.random, clones);
        return copy;
    }
}
