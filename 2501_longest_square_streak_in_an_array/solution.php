<?php
// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

class Solution {
    function longestSquareStreak($nums) {
        $set = [];
        foreach ($nums as $x) $set[$x] = true;
        $best = -1;
        foreach ($nums as $x) {
            $length = 0;
            $cur = $x;
            while (isset($set[$cur])) {
                $length++;
                if ($cur > 100000) break;
                $next = $cur * $cur;
                if ($next === $cur) break;
                $cur = $next;
            }
            if ($length >= 2 && $length > $best) $best = $length;
        }
        return $best;
    }
}
