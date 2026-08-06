<?php
class Solution {
    function maxProduct($root) {
        $mod = 1000000007;
        $total = 0;
        $sum = function($node) use (&$sum, &$total) {
            if (!$node) return 0;
            return $node->val + $sum($node->left) + $sum($node->right);
        };
        $total = $sum($root);
        $best = 0;
        $dfs = function($node) use (&$dfs, &$best, $total) {
            if (!$node) return 0;
            $s = $node->val + $dfs($node->left) + $dfs($node->right);
            $best = max($best, $s * ($total - $s));
            return $s;
        };
        $dfs($root);
        return $best % $mod;
    }
}
