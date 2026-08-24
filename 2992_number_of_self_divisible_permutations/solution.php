<?php
// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

class Solution {
    private $ans;
    private $used;
    private $n;

    private function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    private function dfs($pos) {
        if ($pos > $this->n) { $this->ans++; return; }
        for ($v = 1; $v <= $this->n; $v++) {
            if ($this->used[$v]) continue;
            if ($this->gcd($v, $pos) !== 1) continue;
            $this->used[$v] = true;
            $this->dfs($pos + 1);
            $this->used[$v] = false;
        }
    }

    function selfDivisiblePermutationCount($n) {
        $this->n = $n;
        $this->ans = 0;
        $this->used = array_fill(0, $n + 1, false);
        $this->dfs(1);
        return $this->ans;
    }
}
