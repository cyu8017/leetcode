<?php
// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

class Solution {
    function numberOfRounds($loginTime, $logoutTime) {
        $toMin = function ($t) {
            [$h, $m] = array_map('intval', explode(':', $t));
            return $h * 60 + $m;
        };
        $start = $toMin($loginTime);
        $end = $toMin($logoutTime);
        if ($end < $start) {
            $end += 24 * 60;
        }
        $start = intdiv($start + 14, 15) * 15;
        $end = intdiv($end, 15) * 15;
        return max(0, intdiv($end - $start, 15));
    }
}
