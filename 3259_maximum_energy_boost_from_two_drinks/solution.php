<?php
// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

class Solution {
    function maxEnergyBoost($energyDrinkA, $energyDrinkB) {
        $n = count($energyDrinkA);
        $dpA = array_fill(0, $n, 0);
        $dpB = array_fill(0, $n, 0);
        $dpA[0] = $energyDrinkA[0];
        $dpB[0] = $energyDrinkB[0];
        if ($n === 1) return max($dpA[0], $dpB[0]);
        $dpA[1] = $energyDrinkA[1] + $dpA[0];
        $dpB[1] = $energyDrinkB[1] + $dpB[0];
        for ($i = 2; $i < $n; $i++) {
            $dpA[$i] = $energyDrinkA[$i] + max($dpA[$i - 1], $dpB[$i - 2]);
            $dpB[$i] = $energyDrinkB[$i] + max($dpB[$i - 1], $dpA[$i - 2]);
        }
        return max($dpA[$n - 1], $dpB[$n - 1]);
    }
}
