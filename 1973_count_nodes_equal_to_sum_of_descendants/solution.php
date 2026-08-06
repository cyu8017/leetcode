<?php
// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

class Solution {
    private $ans = 0;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function equalToDescendants($root) {
        $this->ans = 0;
        $this->dfs($root);
        return $this->ans;
    }

    private function dfs($node) {
        if ($node === null) {
            return 0;
        }
        $total = $this->dfs($node->left) + $this->dfs($node->right);
        if ($total === $node->val) {
            $this->ans++;
        }
        return $total + $node->val;
    }
}
