<?php
// LeetCode 3855 - Sum of K Digit Numbers in a Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

class Solution {
    function qpow($a, $n, $mod) {
        $a %= $mod;
        $res = 1;
        while ($n > 0) {
            if ($n & 1) $res = $res * $a % $mod;
            $a = $a * $a % $mod;
            $n >>= 1;
        }
        return $res;
    }
    function sumOfNumbers($l, $r, $k) {
        $MOD = 1000000007;
        $n = $r - $l + 1;
        $sum = (int)((($l + $r) * $n / 2) % $MOD);
        $part1 = $this->qpow($n % $MOD, $k - 1, $MOD);
        $part2 = ($this->qpow(10, $k, $MOD) - 1 + $MOD) % $MOD;
        $inv9 = $this->qpow(9, $MOD - 2, $MOD);
        $ans = $sum;
        $ans = $ans * $part1 % $MOD;
        $ans = $ans * $part2 % $MOD;
        $ans = $ans * $inv9 % $MOD;
        return $ans;
    }
}
