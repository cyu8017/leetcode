<?php
// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subarraysWithKDistinct($nums, $k) {
        $atMost = function ($m) use ($nums) {
            if ($m < 0) return 0;
            $count = [];
            $left = 0;
            $ans = 0;
            $n = count($nums);
            for ($right = 0; $right < $n; $right++) {
                $count[$nums[$right]] = ($count[$nums[$right]] ?? 0) + 1;
                while (count($count) > $m) {
                    $v = $nums[$left++];
                    $count[$v]--;
                    if ($count[$v] === 0) unset($count[$v]);
                }
                $ans += $right - $left + 1;
            }
            return $ans;
        };
        return $atMost($k) - $atMost($k - 1);
    }
}
