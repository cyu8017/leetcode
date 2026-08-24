<?php
// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution {
    /**
     * @param Integer[] $time
     * @param Integer $totalTrips
     * @return Integer
     */
    function minimumTime($time, $totalTrips) {
        $mn = $time[0];
        foreach ($time as $t) $mn = min($mn, $t);
        $lo = 1;
        $hi = $mn * $totalTrips;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $trips = 0;
            $ok = false;
            foreach ($time as $t) {
                $trips += intdiv($mid, $t);
                if ($trips >= $totalTrips) { $ok = true; break; }
            }
            if ($ok) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
