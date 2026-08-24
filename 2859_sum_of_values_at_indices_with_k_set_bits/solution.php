<?php
// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

class Solution {
    function sumIndicesWithKSetBits($nums, $k) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $i;
            $bits = 0;
            while ($x) {
                $bits += $x & 1;
                $x >>= 1;
            }
            if ($bits === $k) $ans += $nums[$i];
        }
        return $ans;
    }
}
