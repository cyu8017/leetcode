// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

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
    public Node moveSubTree(Node root, Node p, Node q) {
        Map<Node, Node> parent = new IdentityHashMap<>();

        build(root, parent);

        if (parent.get(p) == q) {
            return root;
        }

        Node pParent = parent.get(p);
        Node qParent = parent.get(q);

        if (isAncestor(p, q, parent)) {
            qParent.children.remove(q);
            if (pParent == null) {
                root = q;
            } else {
                int idx = pParent.children.indexOf(p);
                pParent.children.set(idx, q);
            }
            q.children.add(p);
        } else {
            if (pParent == null) {
                root = q;
            } else {
                pParent.children.remove(p);
            }
            q.children.add(p);
        }
        return root;
    }

    private void build(Node node, Map<Node, Node> parent) {
        for (Node child : node.children) {
            parent.put(child, node);
            build(child, parent);
        }
    }

    private boolean isAncestor(Node ancestor, Node node, Map<Node, Node> parent) {
        Node current = node;
        while (parent.containsKey(current)) {
            current = parent.get(current);
            if (current == ancestor) {
                return true;
            }
        }
        return false;
    }
}
