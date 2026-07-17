<?php
// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

class Solution {
    /**
     * @param Integer[][] $cars
     * @return Float[]
     */
    function getCollisionTimes($cars) {
        $n = count($cars);
        $ans = array_fill(0, $n, -1.0);
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            $pos = $cars[$i][0];
            $speed = $cars[$i][1];
            while (!empty($stack)) {
                $j = end($stack);
                if ($speed <= $cars[$j][1]) {
                    array_pop($stack);
                    continue;
                }
                $t = ($cars[$j][0] - $pos) / ($speed - $cars[$j][1]);
                if ($ans[$j] < 0 || $t <= $ans[$j]) {
                    $ans[$i] = $t;
                    break;
                }
                array_pop($stack);
            }
            $stack[] = $i;
        }
        return $ans;
    }
}
