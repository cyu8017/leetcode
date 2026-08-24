<?php
// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function numSubarrayBoundedMax($nums, $left, $right) {
        $countAtMost = function($bound) use ($nums) {
            $ans = 0;
            $cur = 0;
            foreach ($nums as $num) {
                if ($num <= $bound) {
                    $cur++;
                    $ans += $cur;
                } else {
                    $cur = 0;
                }
            }
            return $ans;
        };
        return $countAtMost($right) - $countAtMost($left - 1);
    }
}
