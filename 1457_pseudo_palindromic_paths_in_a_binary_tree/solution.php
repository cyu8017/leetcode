<?php
class Solution {
    function pseudoPalindromicPaths($root) {
        $dfs = function($node, $mask) use (&$dfs) {
            if (!$node) return 0;
            $mask ^= 1 << $node->val;
            if (!$node->left && !$node->right) return ($mask & ($mask - 1)) === 0 ? 1 : 0;
            return $dfs($node->left, $mask) + $dfs($node->right, $mask);
        };
        return $dfs($root, 0);
    }
}
