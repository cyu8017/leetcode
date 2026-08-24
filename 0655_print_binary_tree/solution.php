<?php
// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function printTree($root) {
        $heightFn = function($node) use (&$heightFn) {
            return $node == null ? -1 : 1 + max($heightFn($node->left), $heightFn($node->right));
        };
        $h = $heightFn($root);
        $rows = $h + 1;
        $cols = (1 << ($h + 1)) - 1;
        $res = [];
        for ($i = 0; $i < $rows; ++$i) $res[$i] = array_fill(0, $cols, "");
        $place = function($node, $r, $c) use (&$place, &$res, $h) {
            if ($node == null) return;
            $res[$r][$c] = strval($node->val);
            if ($r === $h) return;
            $offset = 1 << ($h - $r - 1);
            $place($node->left, $r + 1, $c - $offset);
            $place($node->right, $r + 1, $c + $offset);
        };
        $place($root, 0, intdiv($cols - 1, 2));
        return $res;
    }
}
