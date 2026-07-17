<?php
// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function solve($nums, $queries) {
        $mod = 1000000007;
        $n = count($nums);
        $block = intval(sqrt($n)) + 1;
        $dp = array_fill(0, $block, array_fill(0, $n, 0));
        for ($step = 1; $step < $block; $step++) {
            for ($i = $n - 1; $i >= 0; $i--) {
                $next = $i + $step < $n ? $dp[$step][$i + $step] : 0;
                $dp[$step][$i] = ($nums[$i] + $next) % $mod;
            }
        }
        $ans = [];
        foreach ($queries as $query) {
            [$start, $step] = $query;
            if ($step < $block) {
                $ans[] = $dp[$step][$start];
            } else {
                $total = 0;
                for ($i = $start; $i < $n; $i += $step) {
                    $total += $nums[$i];
                }
                $ans[] = $total % $mod;
            }
        }
        return $ans;
    }
}
