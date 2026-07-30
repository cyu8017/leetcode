// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

using System.Collections.Generic;

public class Node {
    public int val;
    public IList<Node> children;
    public Node() { children = new List<Node>(); }
    public Node(int _val) { val = _val; children = new List<Node>(); }
    public Node(int _val, IList<Node> _children) { val = _val; children = _children; }
}

public class Solution {
    public Node FindRoot(List<Node> tree) {
        int value = 0;
        var nodes = new Dictionary<int, Node>();
        foreach (var node in tree) {
            nodes[node.val] = node;
            value ^= node.val;
            foreach (var child in node.children) value ^= child.val;
        }
        return nodes[value];
    }
}
