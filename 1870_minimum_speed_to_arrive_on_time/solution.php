<?php
// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

class Solution {
    /**
     * @param Integer[] $dist
     * @param Float $hour
     * @return Integer
     */
    function minSpeedOnTime($dist, $hour) {
        $n = count($dist);
        if ($n - 1 >= $hour) {
            return -1;
        }

        $canArrive = function (int $speed) use ($dist, $n, $hour): bool {
            $time = 0.0;
            for ($i = 0; $i < $n - 1; $i++) {
                $time += intdiv($dist[$i] + $speed - 1, $speed);
            }
            $time += $dist[$n - 1] / $speed;
            return $time <= $hour;
        };

        if (!$canArrive(10000000)) {
            return -1;
        }

        $lo = 1;
        $hi = 10000000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($canArrive($mid)) {
                $hi = $mid;
            } else {
                $lo = $mid + 1;
            }
        }

        return $lo;
    }
}
