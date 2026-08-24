<?php
// LeetCode 3733 - Minimum Time to Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

class Solution {
    function minimumTime($d, $r) {
        $ok = function($T) use ($d, $r) {
            $w0 = $T - intdiv($T, $r[0]);
            $w1 = $T - intdiv($T, $r[1]);
            return $w0 + $w1 >= $d[0] + $d[1];
        };
        $lo = 1;
        $hi = 9007199254740991;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
