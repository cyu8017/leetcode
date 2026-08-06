<?php
// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function isPossibleDivide($nums, $k) {
        if (count($nums) % $k !== 0) return false;
        $counts = array_count_values($nums);
        ksort($counts);
        foreach ($counts as $start => $amount) {
            if ($amount === 0) continue;
            for ($value = $start; $value < $start + $k; $value++) {
                if (($counts[$value] ?? 0) < $amount) return false;
                $counts[$value] -= $amount;
            }
        }
        return true;
    }
}
