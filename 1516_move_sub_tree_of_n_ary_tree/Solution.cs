// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

using System.Collections.Generic;

public class Node {
    public int val;
    public IList<Node> children;
    public Node() { val = 0; children = new List<Node>(); }
    public Node(int _val) { val = _val; children = new List<Node>(); }
    public Node(int _val, IList<Node> _children) { val = _val; children = _children; }
}

public class Solution {
    public Node MoveSubTree(Node root, Node p, Node q) {
        var parent = new Dictionary<Node, Node>();

        void Build(Node node) {
            foreach (var child in node.children) {
                parent[child] = node;
                Build(child);
            }
        }
        Build(root);

        if (parent.TryGetValue(p, out var pp) && ReferenceEquals(pp, q)) return root;

        bool IsAncestor(Node a, Node b) {
            Node cur = b;
            while (parent.ContainsKey(cur)) {
                cur = parent[cur];
                if (ReferenceEquals(cur, a)) return true;
            }
            return false;
        }

        parent.TryGetValue(p, out var pParent);
        parent.TryGetValue(q, out var qParent);

        if (IsAncestor(p, q)) {
            qParent.children.Remove(q);
            if (pParent == null) {
                root = q;
            } else {
                int idx = pParent.children.IndexOf(p);
                pParent.children[idx] = q;
            }
            q.children.Add(p);
        } else {
            if (pParent == null) {
                root = q;
            } else {
                pParent.children.Remove(p);
            }
            q.children.Add(p);
        }
        return root;
    }
}
