<?php
// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

class Solution {
    function buttonWithLongestTime($events) {
        $bestT = $events[0][1];
        $bestI = $events[0][0];
        $n = count($events);
        for ($i = 1; $i < $n; $i++) {
            $t = $events[$i][1] - $events[$i - 1][1];
            if ($t > $bestT || ($t === $bestT && $events[$i][0] < $bestI)) {
                $bestT = $t;
                $bestI = $events[$i][0];
            }
        }
        return $bestI;
    }
}
