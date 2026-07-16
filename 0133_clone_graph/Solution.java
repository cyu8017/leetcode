// LeetCode 0133 - Clone Graph
// https://leetcode.com/problems/clone-graph/

import java.util.*;

class Solution {
    public Node cloneGraph(Node node) {
        return clone(node, new HashMap<>());
    }

    private Node clone(Node node, Map<Node, Node> clones) {
        if (node == null) return null;
        if (clones.containsKey(node)) return clones.get(node);
        Node copy = new Node(node.val);
        clones.put(node, copy);
        for (Node neighbor : node.neighbors) copy.neighbors.add(clone(neighbor, clones));
        return copy;
    }
}
