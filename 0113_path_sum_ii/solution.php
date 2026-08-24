<?php
class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function pathSum($root, $targetSum) {
        $result = [];
        $visit = function ($node, $remaining, $path) use (&$visit, &$result) {
            if ($node === null) return;
            $path[] = $node->val;
            if ($node->left === null && $node->right === null) {
                if ($node->val === $remaining) $result[] = $path;
                return;
            }
            $visit($node->left, $remaining - $node->val, $path);
            $visit($node->right, $remaining - $node->val, $path);
        };
        $visit($root, $targetSum, []);
        return $result;
    }
}
