<?php
// LeetCode 0862 - Shortest Subarray with Sum at Least K
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function shortestSubarray($nums, $k) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $dq = [];
        $ans = $n + 1;
        for ($i = 0; $i <= $n; $i++) {
            while (count($dq) && $prefix[$i] - $prefix[$dq[0]] >= $k) {
                $ans = min($ans, $i - array_shift($dq));
            }
            while (count($dq) && $prefix[$i] <= $prefix[$dq[count($dq) - 1]]) array_pop($dq);
            $dq[] = $i;
        }
        return $ans <= $n ? $ans : -1;
    }
}
