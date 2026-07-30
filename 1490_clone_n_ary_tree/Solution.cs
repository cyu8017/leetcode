// LeetCode 1490 - Clone N Ary Tree
// https://leetcode.com/problems/clone-n-ary-tree/

using System.Collections.Generic;
public class Node {
    public int val; public IList<Node> children;
    public Node() { children = new List<Node>(); }
    public Node(int _val) { val = _val; children = new List<Node>(); }
    public Node(int _val, IList<Node> _children) { val = _val; children = _children; }
}
public class Solution {
    public Node CloneTree(Node root) {
        if (root == null) return null;
        var kids = new List<Node>();
        foreach (var child in root.children) kids.Add(CloneTree(child));
        return new Node(root.val, kids);
    }
}
