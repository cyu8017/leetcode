<?php
// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function minimumOperations($root) {
        if ($root === null) return 0;
        $ans = 0;
        $q = [$root];
        while (count($q)) {
            $sz = count($q);
            $vals = array_fill(0, $sz, 0);
            for ($i = 0; $i < $sz; $i++) {
                $node = array_shift($q);
                $vals[$i] = $node->val;
                if ($node->left !== null) $q[] = $node->left;
                if ($node->right !== null) $q[] = $node->right;
            }
            $sorted = $vals;
            sort($sorted);
            $pos = [];
            for ($i = 0; $i < $sz; $i++) $pos[$vals[$i]] = $i;
            for ($i = 0; $i < $sz; $i++) {
                if ($vals[$i] !== $sorted[$i]) {
                    $j = $pos[$sorted[$i]];
                    $tmp = $vals[$i];
                    $vals[$i] = $vals[$j];
                    $vals[$j] = $tmp;
                    $pos[$vals[$j]] = $j;
                    $pos[$vals[$i]] = $i;
                    $ans++;
                }
            }
        }
        return $ans;
    }
}
