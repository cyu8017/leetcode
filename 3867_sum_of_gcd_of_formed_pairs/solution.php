<?php
// LeetCode 3867 - Sum of GCD of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

class Solution {
    function Gcd($a, $b) {
        while ($b !== 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
    function gcdSum($nums) {
        $n = count($nums);
        $prefixGcd = [];
        $mx = 0;
        for ($i = 0; $i < $n; $i++) {
            $mx = max($mx, $nums[$i]);
            $prefixGcd[$i] = $this->Gcd($nums[$i], $mx);
        }
        sort($prefixGcd);
        $ans = 0;
        for ($i = 0; $i < intdiv($n, 2); $i++) $ans += $this->Gcd($prefixGcd[$i], $prefixGcd[$n - $i - 1]);
        return $ans;
    }
}
