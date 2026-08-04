// LeetCode 1490 - Clone N Ary Tree
// https://leetcode.com/problems/clone-n-ary-tree/

import java.util.*;

class Node {
    public int val; public List<Node> children;
    public Node() { children = new ArrayList<>(); }
    public Node(int _val) { val = _val; children = new ArrayList<>(); }
    public Node(int _val, List<Node> _children) { val = _val; children = _children; }
}
class Solution {
    public Node cloneTree(Node root) {
        if (root == null) return null;
        var kids = new ArrayList<>();
        for (var child : root.children) kids.add(CloneTree(child));
        return new Node(root.val, kids);
    }
}
