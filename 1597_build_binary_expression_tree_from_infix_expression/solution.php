<?php

class Node {
    public $val;
    public $left;
    public $right;

    function __construct($val = ' ', $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    /**
     * @param String $s
     * @return Node
     */
    function expTree($s) {
        $nodes = [];
        $ops = [];
        $priority = ['+' => 1, '-' => 1, '*' => 2, '/' => 2];

        $apply = function () use (&$nodes, &$ops) {
            $op = array_pop($ops);
            $right = array_pop($nodes);
            $left = array_pop($nodes);
            $nodes[] = new Node($op, $left, $right);
        };

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if ($ch >= '0' && $ch <= '9') {
                $nodes[] = new Node($ch);
            } elseif ($ch === '(') {
                $ops[] = $ch;
            } elseif ($ch === ')') {
                while (end($ops) !== '(') {
                    $apply();
                }
                array_pop($ops);
            } else {
                while (!empty($ops) && end($ops) !== '('
                    && $priority[end($ops)] >= $priority[$ch]) {
                    $apply();
                }
                $ops[] = $ch;
            }
        }
        while (!empty($ops)) {
            $apply();
        }
        return $nodes[0];
    }
}
