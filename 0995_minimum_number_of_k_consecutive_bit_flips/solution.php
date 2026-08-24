<?php
// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minKBitFlips($nums, $k) {
        $n = count($nums);
        $flip = array_fill(0, $n, 0);
        $ans = 0;
        $flipped = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i >= $k) $flipped ^= $flip[$i - $k];
            if ($nums[$i] === $flipped) {
                if ($i + $k > $n) return -1;
                $ans++;
                $flipped ^= 1;
                $flip[$i] = 1;
            }
        }
        return $ans;
    }
}
