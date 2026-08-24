<?php
// LeetCode 0991 - Broken Calculator
// https://leetcode.com/problems/broken-calculator/

class Solution {
    /**
     * @param Integer $startValue
     * @param Integer $target
     * @return Integer
     */
    function brokenCalc($startValue, $target) {
        $ans = 0;
        while ($target > $startValue) {
            if ($target % 2 === 1) $target++;
            else $target = intdiv($target, 2);
            $ans++;
        }
        return $ans + $startValue - $target;
    }
}
