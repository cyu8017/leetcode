<?php
// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution {
    function maximumStrongPairXor($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i; $j < $n; $j++) {
                $x = $nums[$i];
                $y = $nums[$j];
                if (abs($x - $y) <= min($x, $y)) {
                    $xorr = $x ^ $y;
                    if ($xorr > $ans) $ans = $xorr;
                }
            }
        return $ans;
    }
}
