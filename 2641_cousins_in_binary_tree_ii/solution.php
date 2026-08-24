<?php
// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

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
    function replaceValueInTree($root) {
        if ($root === null) return null;
        $root->val = 0;
        $q = [$root];
        while (count($q) > 0) {
            $sz = count($q);
            $levelSum = 0;
            $level = [];
            for ($i = 0; $i < $sz; $i++) {
                $node = array_shift($q);
                $level[] = $node;
                if ($node->left) $levelSum += $node->left->val;
                if ($node->right) $levelSum += $node->right->val;
            }
            foreach ($level as $node) {
                $cousin = $levelSum;
                if ($node->left) $cousin -= $node->left->val;
                if ($node->right) $cousin -= $node->right->val;
                if ($node->left) { $node->left->val = $cousin; $q[] = $node->left; }
                if ($node->right) { $node->right->val = $cousin; $q[] = $node->right; }
            }
        }
        return $root;
    }
}
