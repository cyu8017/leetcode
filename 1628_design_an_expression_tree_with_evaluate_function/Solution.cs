// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

using System.Collections.Generic;

public abstract class Node {
    public abstract int Evaluate();
}

public class NumNode : Node {
    private readonly int val;
    public NumNode(int val) { this.val = val; }
    public override int Evaluate() => val;
}

public class OpNode : Node {
    private readonly char op;
    private readonly Node left, right;
    public OpNode(char op, Node left, Node right) {
        this.op = op;
        this.left = left;
        this.right = right;
    }
    public override int Evaluate() {
        int a = left.Evaluate(), b = right.Evaluate();
        return op switch {
            '+' => a + b,
            '-' => a - b,
            '*' => a * b,
            '/' => a / b,
            _ => 0
        };
    }
}

public class TreeBuilder {
    public Node ExpTree(string[] postfix) {
        var stack = new Stack<Node>();
        foreach (string token in postfix) {
            if (token is "+" or "-" or "*" or "/") {
                Node right = stack.Pop();
                Node left = stack.Pop();
                stack.Push(new OpNode(token[0], left, right));
            } else {
                stack.Push(new NumNode(int.Parse(token)));
            }
        }
        return stack.Peek();
    }
}
