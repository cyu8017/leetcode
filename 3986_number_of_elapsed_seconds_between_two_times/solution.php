<?php
// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

class Solution {
    function secondsBetweenTimes($startTime, $endTime) {
        return $this->toSeconds($endTime) - $this->toSeconds($startTime);
    }

    private function toSeconds($s) {
        $h = intval($s[0]) * 10 + intval($s[1]);
        $m = intval($s[3]) * 10 + intval($s[4]);
        $sec = intval($s[6]) * 10 + intval($s[7]);
        return $h * 3600 + $m * 60 + $sec;
    }
}
