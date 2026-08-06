<?php
// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer[][]
     */
    function minimumAbsDifference($arr) {
        sort($arr);
        $best = PHP_INT_MAX;
        $n = count($arr);
        for ($i = 0; $i < $n - 1; $i++) $best = min($best, $arr[$i + 1] - $arr[$i]);
        $ans = [];
        for ($i = 0; $i < $n - 1; $i++) {
            if ($arr[$i + 1] - $arr[$i] === $best) $ans[] = [$arr[$i], $arr[$i + 1]];
        }
        return $ans;
    }
}
