<?php
// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

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
    private function path($node, $target, &$p) {
        if ($node === null) return false;
        if ($node->val === $target) return true;
        $p[] = 'L';
        if ($this->path($node->left, $target, $p)) return true;
        $p[count($p) - 1] = 'R';
        if ($this->path($node->right, $target, $p)) return true;
        array_pop($p);
        return false;
    }

    /**
     * @param TreeNode $root
     * @param Integer $startValue
     * @param Integer $destValue
     * @return String
     */
    function getDirections($root, $startValue, $destValue) {
        $ps = [];
        $pd = [];
        $this->path($root, $startValue, $ps);
        $this->path($root, $destValue, $pd);
        $i = 0;
        while ($i < count($ps) && $i < count($pd) && $ps[$i] === $pd[$i]) $i++;
        return str_repeat('U', count($ps) - $i) . implode('', array_slice($pd, $i));
    }
}
