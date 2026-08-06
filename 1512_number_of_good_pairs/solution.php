<?php
// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numIdenticalPairs($nums) {
        $counts = [];
        foreach ($nums as $num) {
            $counts[$num] = ($counts[$num] ?? 0) + 1;
        }
        $ans = 0;
        foreach ($counts as $c) {
            $ans += intdiv($c * ($c - 1), 2);
        }
        return $ans;
    }
}
