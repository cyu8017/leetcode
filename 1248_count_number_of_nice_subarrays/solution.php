<?php
// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function numberOfSubarrays($nums, $k) {
        $atMost = function ($k) use ($nums) {
            if ($k < 0) return 0;
            $left = $odd = $ans = 0;
            $n = count($nums);
            for ($right = 0; $right < $n; $right++) {
                $odd += $nums[$right] & 1;
                while ($odd > $k) {
                    $odd -= $nums[$left] & 1;
                    $left++;
                }
                $ans += $right - $left + 1;
            }
            return $ans;
        };
        return $atMost($k) - $atMost($k - 1);
    }
}
