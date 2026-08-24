<?php
// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function averageOfLevels($root) {
        $result = [];
        if ($root == null) return $result;
        $queue = [$root];
        while ($queue) {
            $count = count($queue);
            $total = 0;
            for ($i = 0; $i < $count; ++$i) {
                $node = array_shift($queue);
                $total += $node->val;
                if ($node->left) $queue[] = $node->left;
                if ($node->right) $queue[] = $node->right;
            }
            $result[] = $total / $count;
        }
        return $result;
    }
}
