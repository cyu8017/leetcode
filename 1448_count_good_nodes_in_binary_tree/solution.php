<?php
class Solution {
    function goodNodes($root) {
        $visit = function($node, $maximum) use (&$visit) {
            if (!$node) return 0;
            $good = $node->val >= $maximum ? 1 : 0;
            $maximum = max($maximum, $node->val);
            return $good + $visit($node->left, $maximum) + $visit($node->right, $maximum);
        };
        return $visit($root, PHP_INT_MIN);
    }
}
