// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/

using System;
using System.Collections.Generic;

public class Node {
    public int val;
    public IList<Node> children;
    public Node() { children = new List<Node>(); }
    public Node(int _val) { val = _val; children = new List<Node>(); }
    public Node(int _val, IList<Node> _children) { val = _val; children = _children; }
}

public class Solution {
    public int Diameter(Node root) {
        int answer = 0;
        int Depth(Node node) {
            int longest = 0, second = 0;
            foreach (var child in node.children) {
                int value = Depth(child) + 1;
                if (value > longest) { second = longest; longest = value; }
                else if (value > second) second = value;
            }
            answer = Math.Max(answer, longest + second);
            return longest;
        }
        if (root != null) Depth(root);
        return answer;
    }
}
