<?php
// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

class Solution {
    function nextClosestTime($time) {
        $digits = [$time[0] => true, $time[1] => true, $time[3] => true, $time[4] => true];
        $start = intval(substr($time, 0, 2), 10) * 60 + intval(substr($time, 3, 2), 10);
        for ($delta = 1; $delta <= 24 * 60; $delta++) {
            $mins = ($start + $delta) % (24 * 60);
            $hh = intdiv($mins, 60);
            $mm = $mins % 60;
            $c0 = (string)intdiv($hh, 10);
            $c1 = (string)($hh % 10);
            $c2 = (string)intdiv($mm, 10);
            $c3 = (string)($mm % 10);
            if (isset($digits[$c0]) && isset($digits[$c1]) && isset($digits[$c2]) && isset($digits[$c3])) {
                return $c0 . $c1 . ':' . $c2 . $c3;
            }
        }
        return $time;
    }
}
