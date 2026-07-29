<?php
// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function twoSumLessThanK($nums, $k) {
        sort($nums);
        $lo = 0;
        $hi = count($nums) - 1;
        $ans = -1;
        while ($lo < $hi) {
            $total = $nums[$lo] + $nums[$hi];
            if ($total < $k) {
                $ans = max($ans, $total);
                $lo++;
            } else {
                $hi--;
            }
        }
        return $ans;
    }
}
