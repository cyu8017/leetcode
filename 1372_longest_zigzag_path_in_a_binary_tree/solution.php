<?php
class Solution {
    private $ans = 0;
    function longestZigZag($root) {
        $this->ans = 0;
        $this->dfs($root);
        return $this->ans;
    }
    private function dfs($node) {
        if (!$node) return [-1, -1];
        $l = $this->dfs($node->left);
        $r = $this->dfs($node->right);
        $a = $l[1] + 1;
        $b = $r[0] + 1;
        $this->ans = max($this->ans, $a, $b);
        return [$a, $b];
    }
}
