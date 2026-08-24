<?php
// LeetCode 0365 - Water and Jug Problem
// https://leetcode.com/problems/water-and-jug-problem/

class Solution {
    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $target
     * @return Boolean
     */
    function canMeasureWater($x, $y, $target) {
        return $this->can_measure_water($x, $y, $target);
    }

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $target
     * @return Boolean
     */
    function can_measure_water($x, $y, $target) {
        if ($target === 0) {
            return true;
        }
        if ($x + $y < $target) {
            return false;
        }
        return $target % $this->gcd($x, $y) === 0;
    }

    private function gcd(int $a, int $b): int {
        while ($b !== 0) {
            $remainder = $a % $b;
            $a = $b;
            $b = $remainder;
        }
        return $a;
    }
}
