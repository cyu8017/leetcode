<?php
// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

class Solution {
    /**
     * @param Integer $numBottles
     * @param Integer $numExchange
     * @return Integer
     */
    function numWaterBottles($numBottles, $numExchange) {
        $total = $numBottles;
        while ($numBottles >= $numExchange) {
            $new = intdiv($numBottles, $numExchange);
            $remainder = $numBottles % $numExchange;
            $total += $new;
            $numBottles = $new + $remainder;
        }
        return $total;
    }
}
