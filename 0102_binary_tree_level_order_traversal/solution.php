<?php
// LeetCode 0102 - Binary Tree Level Order Traversal
// https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    /**
     * @param TreeNode $root
     * @return Integer[][]
     */
    function levelOrder($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $queue = [$root];

        while (!empty($queue)) {
            $size = count($queue);
            $level = [];
            for ($i = 0; $i < $size; $i++) {
                $node = array_shift($queue);
                $level[] = $node->val;
                if ($node->left !== null) {
                    $queue[] = $node->left;
                }
                if ($node->right !== null) {
                    $queue[] = $node->right;
                }
            }
            $result[] = $level;
        }

        return $result;
    }
}
