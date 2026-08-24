<?php
// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

class Solution {
    /**
     * @param Integer[][] $lights
     * @return Integer
     */
    function brightestPosition($lights) {
        $events = [];
        foreach ($lights as $light) {
            $pos = $light[0];
            $r = $light[1];
            $events[] = [$pos - $r, 1];
            $events[] = [$pos + $r + 1, -1];
        }
        usort($events, function ($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $b[1] <=> $a[1];
        });
        $best = 0;
        $cur = 0;
        $ans = 0;
        foreach ($events as $e) {
            $cur += $e[1];
            if ($cur > $best) { $best = $cur; $ans = $e[0]; }
        }
        return $ans;
    }
}
