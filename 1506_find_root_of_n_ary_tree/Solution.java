// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

import java.util.*;

class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int val) {
        this.val = val;
        this.children = new ArrayList<>();
    }

    public Node(int val, List<Node> children) {
        this.val = val;
        this.children = children;
    }
}

class Solution {
    public Node findRoot(List<Node> tree) {
        int value = 0;
        Map<Integer, Node> nodes = new HashMap<>();
        for (Node node : tree) {
            nodes.put(node.val, node);
            value ^= node.val;
            for (Node child : node.children) {
                value ^= child.val;
            }
        }
        return nodes.get(value);
    }
}
