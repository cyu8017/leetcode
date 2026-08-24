<?php
// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

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
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return Boolean
     */
    function leafSimilar($root1, $root2) {
        $leaves = function($node) {
            $result = [];
            $dfs = function($cur) use (&$dfs, &$result) {
                if ($cur === null) return;
                if ($cur->left === null && $cur->right === null) {
                    $result[] = $cur->val;
                    return;
                }
                $dfs($cur->left);
                $dfs($cur->right);
            };
            $dfs($node);
            return $result;
        };
        $a = $leaves($root1);
        $b = $leaves($root2);
        if (count($a) !== count($b)) return false;
        $n = count($a);
        for ($i = 0; $i < $n; $i++) if ($a[$i] !== $b[$i]) return false;
        return true;
    }
}
