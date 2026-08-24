<?php
// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution {
    function repairCars($ranks, $cars) {
        $mn = min($ranks);
        $lo = 1;
        $hi = $mn * $cars * $cars;
        $ok = function($t) use ($ranks, $cars) {
            $done = 0;
            foreach ($ranks as $r) {
                $l = 0;
                $h = $cars;
                while ($l < $h) {
                    $mid = intdiv($l + $h + 1, 2);
                    if ($r * $mid * $mid <= $t) $l = $mid;
                    else $h = $mid - 1;
                }
                $done += $l;
                if ($done >= $cars) return true;
            }
            return $done >= $cars;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
