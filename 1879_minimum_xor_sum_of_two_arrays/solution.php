<?php
// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minimumXORSum($nums1, $nums2) {
        $n = count($nums1);
        $size = 1 << $n;
        $dp = array_fill(0, $size, PHP_INT_MAX);
        $dp[0] = 0;

        for ($mask = 0; $mask < $size; $mask++) {
            $i = substr_count(decbin($mask), '1');
            if ($i >= $n) {
                continue;
            }
            for ($j = 0; $j < $n; $j++) {
                if ($mask & (1 << $j)) {
                    continue;
                }
                $nextMask = $mask | (1 << $j);
                $cost = $dp[$mask] + ($nums1[$i] ^ $nums2[$j]);
                if ($cost < $dp[$nextMask]) {
                    $dp[$nextMask] = $cost;
                }
            }
        }

        return $dp[$size - 1];
    }
}
