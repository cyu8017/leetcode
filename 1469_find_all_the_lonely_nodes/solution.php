<?php
class Solution {
    function getLonelyNodes($root) {
        $ans = [];
        $dfs = function($node) use (&$dfs, &$ans) {
            if (!$node) return;
            if (boolval($node->left) xor boolval($node->right)) {
                $ans[] = ($node->left ?: $node->right)->val;
            }
            $dfs($node->left);
            $dfs($node->right);
        };
        $dfs($root);
        return $ans;
    }
}
