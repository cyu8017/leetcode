<?php
// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

class Solution {
    function maximumStrongPairXor($nums) {
        sort($nums);
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            for ($j = $i; $j < $n && $nums[$j] <= 2 * $x; $j++) {
                $xorr = $x ^ $nums[$j];
                if ($xorr > $ans) $ans = $xorr;
            }
        }
        return $ans;
    }
}
