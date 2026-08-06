<?php
// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

class Solution {
    /**
     * @param Integer[] $distance
     * @param Integer $start
     * @param Integer $destination
     * @return Integer
     */
    function distanceBetweenBusStops($distance, $start, $destination) {
        if ($start > $destination) [$start, $destination] = [$destination, $start];
        $clockwise = array_sum(array_slice($distance, $start, $destination - $start));
        return min($clockwise, array_sum($distance) - $clockwise);
    }
}
