<?php
// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

class Solution {
    function maxFreeTime($eventTime, $k, $startTime, $endTime) {
        $n = count($startTime);
        $gaps = array_fill(0, $n + 1, 0);
        $gaps[0] = $startTime[0];
        for ($i = 1; $i < $n; $i++) $gaps[$i] = $startTime[$i] - $endTime[$i - 1];
        $gaps[$n] = $eventTime - $endTime[$n - 1];
        $window = $k + 1;
        $sum = 0;
        for ($i = 0; $i < $window && $i < count($gaps); $i++) $sum += $gaps[$i];
        $ans = $sum;
        for ($i = $window; $i < count($gaps); $i++) {
            $sum += $gaps[$i] - $gaps[$i - $window];
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
