<?php
// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

class Solution {
    private $ans = 0.0;

    /**
     * @param TreeNode $root
     * @return Float
     */
    function maximumAverageSubtree($root) {
        $this->ans = 0.0;
        $this->dfs($root);
        return $this->ans;
    }

    private function dfs($node) {
        if ($node === null) return [0, 0];
        [$ls, $lc] = $this->dfs($node->left);
        [$rs, $rc] = $this->dfs($node->right);
        $sum = $ls + $rs + $node->val;
        $cnt = $lc + $rc + 1;
        $this->ans = max($this->ans, $sum / $cnt);
        return [$sum, $cnt];
    }
}
