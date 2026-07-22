// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

using System;
using System.Collections.Generic;

public class Node {
    public char val;
    public Node left;
    public Node right;
    public Node(char val = '\0', Node left = null, Node right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public bool CheckEquivalence(Node root1, Node root2) {
        var a = new int[26];
        var b = new int[26];
        Count(root1, a);
        Count(root2, b);
        for (int i = 0; i < 26; i++) if (a[i] != b[i]) return false;
        return true;
    }

    // Harness may pass serialized trees as strings via Python; this overload supports that shape.
    public bool CheckEquivalence(string root1, string root2) {
        return CheckEquivalence(Parse(root1), Parse(root2));
    }

    private static void Count(Node node, int[] cnt) {
        if (node == null) return;
        if (node.val == '+') {
            Count(node.left, cnt);
            Count(node.right, cnt);
        } else {
            cnt[node.val - 'a']++;
        }
    }

    private static Node Parse(string data) {
        if (string.IsNullOrEmpty(data) || data == "[]") return null;
        string inner = data;
        if (inner[0] == '[') inner = inner.Substring(1, inner.Length - 2);
        var vals = inner.Length == 0 ? Array.Empty<string>() : inner.Split(',');
        var nodes = new Node[vals.Length];
        for (int i = 0; i < vals.Length; i++) {
            if (vals[i] == "null") nodes[i] = null;
            else nodes[i] = new Node(vals[i][0]);
        }
        int kid = 1;
        foreach (var node in nodes) {
            if (node == null) continue;
            if (kid < nodes.Length) node.left = nodes[kid++];
            if (kid < nodes.Length) node.right = nodes[kid++];
        }
        return nodes.Length == 0 ? null : nodes[0];
    }
}
