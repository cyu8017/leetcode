// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

class Node {
    char val;
    Node left;
    Node right;
    Node(char val) { this.val = val; }
}

class Solution {
    public boolean checkEquivalence(Node root1, Node root2) {
        int[] a = new int[26], b = new int[26];
        count(root1, a);
        count(root2, b);
        for (int i = 0; i < 26; i++) if (a[i] != b[i]) return false;
        return true;
    }

    public boolean checkEquivalence(String root1, String root2) {
        return checkEquivalence(parse(root1), parse(root2));
    }

    private void count(Node node, int[] out) {
        if (node == null) return;
        if (node.val == '+') {
            count(node.left, out);
            count(node.right, out);
        } else {
            out[node.val - 'a']++;
        }
    }

    private Node parse(String data) {
        if (data == null) return null;
        String inner = data.trim();
        if (inner.startsWith("[")) inner = inner.substring(1, inner.length() - 1);
        if (inner.isEmpty()) return null;
        String[] vals = inner.split(",");
        Node[] nodes = new Node[vals.length];
        for (int i = 0; i < vals.length; i++) {
            String v = vals[i].trim();
            nodes[i] = v.equals("null") ? null : new Node(v.charAt(0));
        }
        int kid = 1;
        for (Node node : nodes) {
            if (node == null) continue;
            if (kid < nodes.length) node.left = nodes[kid++];
            if (kid < nodes.length) node.right = nodes[kid++];
        }
        return nodes[0];
    }
}
