<?php
// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

class Solution {
    function countCompleteDayPairs($hours) {
        $cnt = array_fill(0, 24, 0);
        $ans = 0;
        foreach ($hours as $x) {
            $ans += $cnt[(24 - $x % 24) % 24];
            $cnt[$x % 24]++;
        }
        return $ans;
    }
}
