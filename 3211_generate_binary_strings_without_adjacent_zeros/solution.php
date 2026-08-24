<?php
// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

class Solution {
    private $n;
    private $ans;
    private $t;

    function validStrings($n) {
        $this->n = $n;
        $this->ans = [];
        $this->t = [];
        $this->dfs(0);
        return $this->ans;
    }

    private function dfs($i) {
        if ($i >= $this->n) { $this->ans[] = implode('', $this->t); return; }
        for ($j = 0; $j < 2; $j++) {
            if (($j === 0 && ($i === 0 || $this->t[$i - 1] === '1')) || $j === 1) {
                $this->t[] = (string)$j;
                $this->dfs($i + 1);
                array_pop($this->t);
            }
        }
    }
}
