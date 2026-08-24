<?php
// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function widthOfBinaryTree($root) {
        if ($root == null) return 0;
        $queue = [[$root, 0]];
        $best = 0;
        while ($queue) {
            $left = $queue[0][1];
            $size = count($queue);
            for ($i = 0; $i < $size; ++$i) {
                $item = array_shift($queue);
                $node = $item[0];
                $idx = $item[1];
                $best = max($best, $idx - $left + 1);
                if ($node->left) $queue[] = [$node->left, $idx * 2];
                if ($node->right) $queue[] = [$node->right, $idx * 2 + 1];
            }
        }
        return $best;
    }
}
