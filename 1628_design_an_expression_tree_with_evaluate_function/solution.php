<?php
// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

class Node {
    public $val;
    public $left = null;
    public $right = null;

    function __construct($val, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }

    function evaluate() {
        if (!in_array($this->val, ["+", "-", "*", "/"], true)) {
            return intval($this->val);
        }
        $a = $this->left->evaluate();
        $b = $this->right->evaluate();
        if ($this->val === "+") {
            return $a + $b;
        }
        if ($this->val === "-") {
            return $a - $b;
        }
        if ($this->val === "*") {
            return $a * $b;
        }
        return intdiv($a, $b);
    }
}

class TreeBuilder {
    /**
     * @param String[] $postfix
     * @return Node
     */
    function expTree($postfix) {
        $stack = [];
        foreach ($postfix as $token) {
            $node = new Node($token);
            if (in_array($token, ["+", "-", "*", "/"], true)) {
                $node->right = array_pop($stack);
                $node->left = array_pop($stack);
            }
            $stack[] = $node;
        }
        return $stack[count($stack) - 1];
    }
}
