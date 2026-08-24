<?php
// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

class Solution {
    function maxFreeTime($eventTime, $startTime, $endTime) {
        $n = count($startTime);
        $gaps = array_fill(0, $n + 1, 0);
        $gaps[0] = $startTime[0];
        for ($i = 1; $i < $n; $i++) $gaps[$i] = $startTime[$i] - $endTime[$i - 1];
        $gaps[$n] = $eventTime - $endTime[$n - 1];
        $ans = 0;
        foreach ($gaps as $g) if ($g > $ans) $ans = $g;
        $leftMax = array_fill(0, $n + 1, 0);
        $rightMax = array_fill(0, $n + 1, 0);
        for ($i = 0; $i <= $n; $i++) {
            $leftMax[$i] = $gaps[$i];
            if ($i > 0 && $leftMax[$i - 1] > $leftMax[$i]) $leftMax[$i] = $leftMax[$i - 1];
        }
        for ($i = $n; $i >= 0; $i--) {
            $rightMax[$i] = $gaps[$i];
            if ($i < $n && $rightMax[$i + 1] > $rightMax[$i]) $rightMax[$i] = $rightMax[$i + 1];
        }
        for ($i = 0; $i < $n; $i++) {
            $dur = $endTime[$i] - $startTime[$i];
            $merged = $gaps[$i] + $gaps[$i + 1];
            $bestOther = 0;
            if ($i > 0 && $leftMax[$i - 1] > $bestOther) $bestOther = $leftMax[$i - 1];
            if ($i + 2 <= $n && $rightMax[$i + 2] > $bestOther) $bestOther = $rightMax[$i + 2];
            $cand = $merged;
            if ($bestOther >= $dur) $cand = $merged + $dur;
            if ($cand > $ans) $ans = $cand;
        }
        return $ans;
    }
}
