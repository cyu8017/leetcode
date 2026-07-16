// LeetCode 0133 - Clone Graph
// https://leetcode.com/problems/clone-graph/

using System.Collections.Generic;

public class Solution {
    public Node CloneGraph(Node node) {
        return Clone(node, new Dictionary<Node, Node>());
    }

    private Node Clone(Node node, Dictionary<Node, Node> clones) {
        if (node == null) return null;
        if (clones.TryGetValue(node, out Node copy)) return copy;
        copy = new Node(node.val);
        clones[node] = copy;
        foreach (Node neighbor in node.neighbors) copy.neighbors.Add(Clone(neighbor, clones));
        return copy;
    }
}
