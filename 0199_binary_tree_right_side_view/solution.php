<?php

// LeetCode 0199 - Binary Tree Right Side View
class TreeNode {
    public $val;
    public $left;
    public $right;

    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function rightSideView($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $queue = [$root];
        while (!empty($queue)) {
            $levelSize = count($queue);
            for ($i = 0; $i < $levelSize; $i++) {
                $node = array_shift($queue);
                if ($i === $levelSize - 1) {
                    $result[] = $node->val;
                }
                if ($node->left !== null) {
                    $queue[] = $node->left;
                }
                if ($node->right !== null) {
                    $queue[] = $node->right;
                }
            }
        }
        return $result;
    }
}