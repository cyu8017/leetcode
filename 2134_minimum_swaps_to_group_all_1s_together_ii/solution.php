<?php
// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minSwaps($nums) {
        $ones = 0;
        foreach ($nums as $x) $ones += $x;
        if ($ones === 0) return 0;
        $n = count($nums);
        $window = 0;
        for ($i = 0; $i < $ones; $i++) $window += $nums[$i];
        $best = $window;
        for ($i = 0; $i < $n; $i++) {
            $window -= $nums[$i];
            $window += $nums[($i + $ones) % $n];
            $best = max($best, $window);
        }
        return $ones - $best;
    }
}
