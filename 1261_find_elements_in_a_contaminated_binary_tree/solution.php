<?php
// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

class FindElements {
    private $values = [];

    /**
     * @param TreeNode $root
     */
    function __construct($root) {
        $recover = function ($node, $value) use (&$recover) {
            if ($node === null) return;
            $node->val = $value;
            $this->values[$value] = true;
            $recover($node->left, 2 * $value + 1);
            $recover($node->right, 2 * $value + 2);
        };
        $recover($root, 0);
    }

    /**
     * @param Integer $target
     * @return Boolean
     */
    function find($target) {
        return isset($this->values[$target]);
    }
}
