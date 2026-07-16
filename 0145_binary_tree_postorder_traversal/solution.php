<?php

class TreeNode {
    public int $val;
    public ?TreeNode $left;
    public ?TreeNode $right;

    function __construct(int $val = 0, ?TreeNode $left = null, ?TreeNode $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function postorderTraversal(?TreeNode $root): array {
        $result = [];
        $traverse = function (?TreeNode $node) use (&$result, &$traverse): void {
            if ($node === null) {
                return;
            }
            $traverse($node->left);
            $traverse($node->right);
            $result[] = $node->val;
        };
        $traverse($root);
        return $result;
    }
}