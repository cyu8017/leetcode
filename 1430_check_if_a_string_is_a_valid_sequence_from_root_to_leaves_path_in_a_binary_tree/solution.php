<?php
class Solution {
    function isValidSequence($root, $arr) {
        $visit = function($node, $index) use (&$visit, $arr) {
            if (!$node || $index === count($arr) || $node->val !== $arr[$index]) return false;
            if (!$node->left && !$node->right) return $index === count($arr) - 1;
            return $visit($node->left, $index + 1) || $visit($node->right, $index + 1);
        };
        return $visit($root, 0);
    }
}
