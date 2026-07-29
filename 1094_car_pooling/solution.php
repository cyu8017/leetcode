<?php
// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

class Solution {
    /**
     * @param Integer[][] $trips
     * @param Integer $capacity
     * @return Boolean
     */
    function carPooling($trips, $capacity) {
        $diff = array_fill(0, 1001, 0);
        foreach ($trips as $trip) {
            $diff[$trip[1]] += $trip[0];
            $diff[$trip[2]] -= $trip[0];
        }
        $cur = 0;
        foreach ($diff as $x) {
            $cur += $x;
            if ($cur > $capacity) {
                return false;
            }
        }
        return true;
    }
}
