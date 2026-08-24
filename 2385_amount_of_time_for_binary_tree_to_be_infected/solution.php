<?php
// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

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
    private $g = [];

    function amountOfTime($root, $start) {
        $this->g = [];
        $this->build($root, null);
        $ans = 0;
        $vis = [$start => true];
        $q = [[$start, 0]];
        while (count($q) > 0) {
            [$cur, $d] = array_shift($q);
            $ans = max($ans, $d);
            foreach ($this->g[$cur] ?? [] as $nxt) {
                if (!isset($vis[$nxt])) {
                    $vis[$nxt] = true;
                    $q[] = [$nxt, $d + 1];
                }
            }
        }
        return $ans;
    }

    private function build($node, $parent) {
        if ($node === null) return;
        if ($parent !== null) {
            $this->g[$node->val][] = $parent->val;
            $this->g[$parent->val][] = $node->val;
        }
        $this->build($node->left, $node);
        $this->build($node->right, $node);
    }
}
