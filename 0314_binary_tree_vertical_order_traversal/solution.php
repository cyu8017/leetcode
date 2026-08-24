<?php
// LeetCode 0314 - Binary Tree Vertical Order Traversal
// https://leetcode.com/problems/binary-tree-vertical-order-traversal/

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
     * @param TreeNode|null $root
     * @return Integer[][]
     */
    function verticalOrder($root) {
        if ($root === null) {
            return [];
        }

        $columns = [];
        $queue = [[$root, 0]];
        $minCol = 0;
        $maxCol = 0;
        while (!empty($queue)) {
            [$node, $column] = array_shift($queue);
            $minCol = min($minCol, $column);
            $maxCol = max($maxCol, $column);
            if (!isset($columns[$column])) {
                $columns[$column] = [];
            }
            $columns[$column][] = $node->val;
            if ($node->left !== null) {
                $queue[] = [$node->left, $column - 1];
            }
            if ($node->right !== null) {
                $queue[] = [$node->right, $column + 1];
            }
        }

        $result = [];
        for ($column = $minCol; $column <= $maxCol; $column++) {
            $result[] = $columns[$column] ?? [];
        }
        return $result;
    }
}
