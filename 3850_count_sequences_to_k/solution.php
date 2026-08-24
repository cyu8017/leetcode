<?php
// LeetCode 3850 - Count Sequences to K
// https://leetcode.com/problems/count-sequences-to-k/

class Solution {
    public $nums;
    public $k;
    public $f;
    function gcd($a, $b) {
        while ($b !== 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
    function dfs($i, $p, $q) {
        if ($i === count($this->nums)) return ($p === $this->k && $q === 1) ? 1 : 0;
        $key = $i . ',' . $p . ',' . $q;
        if (isset($this->f[$key])) return $this->f[$key];
        $res = $this->dfs($i + 1, $p, $q);
        $x = $this->nums[$i];
        $g1 = $this->gcd($p * $x, $q);
        $res += $this->dfs($i + 1, intdiv($p * $x, $g1), intdiv($q, $g1));
        $g2 = $this->gcd($p, $q * $x);
        $res += $this->dfs($i + 1, intdiv($p, $g2), intdiv($q * $x, $g2));
        $this->f[$key] = $res;
        return $res;
    }
    function countSequences($nums, $k) {
        $this->nums = $nums;
        $this->k = $k;
        $this->f = [];
        return $this->dfs(0, 1, 1);
    }
}
