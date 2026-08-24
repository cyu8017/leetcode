<?php
// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

class Solution {
    function maxBottlesDrunk($numBottles, $numExchange) {
        $ans = $numBottles;
        while ($numBottles >= $numExchange) {
            $numBottles -= $numExchange;
            $numExchange++;
            $ans++;
            $numBottles++;
        }
        return $ans;
    }
}
