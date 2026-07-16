<?php
// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

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
     * @param String $s
     * @return TreeNode|null
     */
    function str2tree($s) {
        if ($s === null || $s === "") {
            return null;
        }

        $index = 0;
        $parse = function () use ($s, &$index, &$parse) {
            if ($index >= strlen($s)) {
                return null;
            }

            $sign = 1;
            if ($s[$index] === "-") {
                $sign = -1;
                $index++;
            }

            $value = 0;
            while ($index < strlen($s) && $s[$index] >= "0" && $s[$index] <= "9") {
                $value = $value * 10 + (int)$s[$index];
                $index++;
            }

            $node = new TreeNode($sign * $value);

            if ($index < strlen($s) && $s[$index] === "(") {
                $index++;
                $node->left = $parse();
                $index++;
            }

            if ($index < strlen($s) && $s[$index] === "(") {
                $index++;
                $node->right = $parse();
                $index++;
            }

            return $node;
        };

        return $parse();
    }
}
