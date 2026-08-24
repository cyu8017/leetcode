<?php
// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution {
    /**
     * @param Integer[][] $events
     * @return Integer
     */
    function maxTwoEvents($events) {
        usort($events, fn($a, $b) => $a[0] <=> $b[0]);
        $n = count($events);
        $suffix = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) $suffix[$i] = max($suffix[$i + 1], $events[$i][2]);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans = max($ans, $events[$i][2]);
            $lo = $i + 1;
            $hi = $n;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($events[$mid][0] > $events[$i][1]) $hi = $mid;
                else $lo = $mid + 1;
            }
            if ($lo < $n) $ans = max($ans, $events[$i][2] + $suffix[$lo]);
        }
        return $ans;
    }
}
