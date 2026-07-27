// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

import java.util.*;

abstract class Node {
    public abstract int evaluate();

    @Override
    public boolean equals(Object other) {
        if (other instanceof Number) return evaluate() == ((Number) other).intValue();
        if (other instanceof Node) return evaluate() == ((Node) other).evaluate();
        return false;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(evaluate());
    }
}

class NumNode extends Node {
    private final int val;
    NumNode(int val) { this.val = val; }
    public int evaluate() { return val; }
}

class OpNode extends Node {
    private final char op;
    private final Node left, right;
    OpNode(char op, Node left, Node right) {
        this.op = op;
        this.left = left;
        this.right = right;
    }
    public int evaluate() {
        int a = left.evaluate(), b = right.evaluate();
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return a / b;
            default: return 0;
        }
    }
}

class TreeBuilder {
    public Node expTree(String[] postfix) {
        Deque<Node> stack = new ArrayDeque<>();
        for (String token : postfix) {
            if ("+-*/".indexOf(token) >= 0) {
                Node right = stack.pop();
                Node left = stack.pop();
                stack.push(new OpNode(token.charAt(0), left, right));
            } else {
                stack.push(new NumNode(Integer.parseInt(token)));
            }
        }
        return stack.peek();
    }
}
