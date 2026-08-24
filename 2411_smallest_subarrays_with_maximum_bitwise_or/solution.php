<?php
// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

class Solution {
    function smallestSubarrays($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $last = array_fill(0, 32, -1);
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($b = 0; $b < 32; $b++)
                if ((($nums[$i] >> $b) & 1) !== 0) $last[$b] = $i;
            $far = $i;
            for ($b = 0; $b < 32; $b++) $far = max($far, $last[$b]);
            $ans[$i] = $far - $i + 1;
        }
        return $ans;
    }
}
