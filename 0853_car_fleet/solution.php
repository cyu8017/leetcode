<?php
// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

class Solution {
    /**
     * @param Integer $target
     * @param Integer[] $position
     * @param Integer[] $speed
     * @return Integer
     */
    function carFleet($target, $position, $speed) {
        $n = count($position);
        $cars = [];
        for ($i = 0; $i < $n; $i++) $cars[] = [$position[$i], $speed[$i]];
        usort($cars, function($a, $b) { return $b[0] <=> $a[0]; });
        $fleets = 0;
        $maxTime = 0;
        foreach ($cars as $car) {
            $time = ($target - $car[0]) / $car[1];
            if ($time > $maxTime) {
                $fleets++;
                $maxTime = $time;
            }
        }
        return $fleets;
    }
}
