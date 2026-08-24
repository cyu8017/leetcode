<?php
// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

class Solution {
    function minmaxGasDist($stations, $k) {
        $can = function ($dist) use ($stations, $k) {
            $needed = 0;
            for ($i = 1; $i < count($stations); $i++)
                $needed += (int)floor(($stations[$i] - $stations[$i - 1]) / $dist);
            return $needed <= $k;
        };
        $lo = 0.0;
        $hi = $stations[count($stations) - 1] - $stations[0];
        while ($hi - $lo > 1e-6) {
            $mid = ($lo + $hi) / 2.0;
            if ($can($mid)) $hi = $mid;
            else $lo = $mid;
        }
        return $hi;
    }
}
