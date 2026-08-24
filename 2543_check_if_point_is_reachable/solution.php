<?php
// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/

class Solution {
    function isReachable($targetX, $targetY) {
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $g = $gcd($targetX, $targetY);
        while ($g % 2 === 0) $g = intdiv($g, 2);
        return $g === 1;
    }
}
