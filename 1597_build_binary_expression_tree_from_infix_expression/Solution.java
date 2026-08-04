// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

import java.util.*;

class Node {
    char val;
    Node left;
    Node right;

    Node(char val) {
        this.val = val;
    }

    Node(char val, Node left, Node right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public Node expTree(String s) {
        Deque<Node> nodes = new ArrayDeque<>();
        Deque<Character> ops = new ArrayDeque<>();
        Map<Character, Integer> priority = Map.of('+', 1, '-', 1, '*', 2, '/', 2);
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch >= '0' && ch <= '9') {
                nodes.push(new Node(ch));
            } else if (ch == '(') {
                ops.push(ch);
            } else if (ch == ')') {
                while (ops.peek() != '(') {
                    apply(nodes, ops);
                }
                ops.pop();
            } else {
                while (!ops.isEmpty() && ops.peek() != '('
                        && priority.get(ops.peek()) >= priority.get(ch)) {
                    apply(nodes, ops);
                }
                ops.push(ch);
            }
        }
        while (!ops.isEmpty()) {
            apply(nodes, ops);
        }
        return nodes.peek();
    }

    private void apply(Deque<Node> nodes, Deque<Character> ops) {
        char op = ops.pop();
        Node right = nodes.pop();
        Node left = nodes.pop();
        nodes.push(new Node(op, left, right));
    }
}
