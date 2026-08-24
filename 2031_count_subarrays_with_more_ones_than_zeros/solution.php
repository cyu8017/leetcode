<?php
// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function subarraysWithMoreZerosThanOnes($nums) {
        $MOD = 1000000007;
        $n = count($nums);
        $bit = array_fill(0, 2 * $n + 7, 0);
        $add = function ($i, $v) use (&$bit) {
            $len = count($bit);
            for (; $i < $len; $i += $i & -$i) $bit[$i] += $v;
        };
        $sum = function ($i) use (&$bit) {
            $s = 0;
            for (; $i > 0; $i -= $i & -$i) $s += $bit[$i];
            return $s;
        };
        $offset = $n + 1;
        $pref = 0;
        $ans = 0;
        $add($offset, 1);
        foreach ($nums as $x) {
            $pref += ($x === 1) ? 1 : -1;
            $idx = $pref + $offset;
            $ans = ($ans + $sum($idx - 1)) % $MOD;
            $add($idx, 1);
        }
        return $ans;
    }
}
