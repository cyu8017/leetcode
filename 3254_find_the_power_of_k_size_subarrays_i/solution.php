<?php
// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution {
    function resultsArray($nums, $k) {
        $n = count($nums);
        $ans = array_fill(0, $n - $k + 1, 0);
        for ($i = 0; $i <= $n - $k; $i++) {
            $ok = true;
            for ($j = $i + 1; $j < $i + $k; $j++) {
                if ($nums[$j] !== $nums[$j - 1] + 1) { $ok = false; break; }
            }
            $ans[$i] = $ok ? $nums[$i + $k - 1] : -1;
        }
        return $ans;
    }
}
