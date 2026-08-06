<?php
class Solution {
    private $ans = 0;
    function maxSumBST($root) {
        $this->ans = 0;
        $this->dfs($root);
        return $this->ans;
    }
    private function dfs($node) {
        if (!$node) return [true, PHP_INT_MAX, PHP_INT_MIN, 0];
        [$a, $lx, $lh, $ls] = $this->dfs($node->left);
        [$b, $rx, $rh, $rs] = $this->dfs($node->right);
        if ($a && $b && $lh < $node->val && $node->val < $rx) {
            $s = $ls + $rs + $node->val;
            $this->ans = max($this->ans, $s);
            return [true, min($lx, $node->val), max($rh, $node->val), $s];
        }
        return [false, 0, 0, 0];
    }
}
