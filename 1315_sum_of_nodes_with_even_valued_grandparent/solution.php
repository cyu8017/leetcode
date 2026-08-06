<?php
class Solution {
    function sumEvenGrandparent($root) {
        $dfs = function($node, $parent, $grandparent) use (&$dfs) {
            if (!$node) return 0;
            $add = ($grandparent && $grandparent->val % 2 === 0) ? $node->val : 0;
            return $add + $dfs($node->left, $node, $parent) + $dfs($node->right, $node, $parent);
        };
        return $dfs($root, null, null);
    }
}
