// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

using System.Collections.Generic;

public class Node {
    public char val;
    public Node left;
    public Node right;
    public Node() { val = ' '; }
    public Node(char val) { this.val = val; }
    public Node(char val, Node left, Node right) { this.val = val; this.left = left; this.right = right; }
}

public class Solution {
    public Node ExpTree(string s) {
        var nodes = new Stack<Node>();
        var ops = new Stack<char>();
        var priority = new Dictionary<char, int> { ['+'] = 1, ['-'] = 1, ['*'] = 2, ['/'] = 2 };

        void Apply() {
            char op = ops.Pop();
            Node right = nodes.Pop(), left = nodes.Pop();
            nodes.Push(new Node(op, left, right));
        }

        foreach (char ch in s) {
            if (char.IsDigit(ch)) {
                nodes.Push(new Node(ch));
            } else if (ch == '(') {
                ops.Push(ch);
            } else if (ch == ')') {
                while (ops.Peek() != '(') Apply();
                ops.Pop();
            } else {
                while (ops.Count > 0 && ops.Peek() != '(' && priority[ops.Peek()] >= priority[ch])
                    Apply();
                ops.Push(ch);
            }
        }
        while (ops.Count > 0) Apply();
        return nodes.Pop();
    }
}
