<?php

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
     * @param Integer $distance
     * @return Integer
     */
    function countPairs($root, $distance) {
        $answer = 0;
        $dfs = function ($node) use (&$dfs, &$answer, $distance) {
            if ($node === null) {
                return [];
            }
            if ($node->left === null && $node->right === null) {
                return [1];
            }
            $left = $dfs($node->left);
            $right = $dfs($node->right);
            foreach ($left as $a) {
                foreach ($right as $b) {
                    if ($a + $b <= $distance) {
                        $answer++;
                    }
                }
            }
            $result = [];
            foreach (array_merge($left, $right) as $depth) {
                if ($depth + 1 < $distance) {
                    $result[] = $depth + 1;
                }
            }
            return $result;
        };
        $dfs($root);
        return $answer;
    }
}
