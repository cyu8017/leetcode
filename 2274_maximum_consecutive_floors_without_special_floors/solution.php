<?php
// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

class Solution {
    function maxConsecutive($bottom, $top, $special) {
        sort($special);
        $ans = $special[0] - $bottom;
        for ($i = 1; $i < count($special); $i++)
            $ans = max($ans, $special[$i] - $special[$i - 1] - 1);
        $ans = max($ans, $top - $special[count($special) - 1]);
        return $ans;
    }
}
