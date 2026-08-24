<?php
// LeetCode 3899 - Angles of a Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

class Solution {
    function internalAngles($sides) {
        $sides = $sides;
        sort($sides);
        $a = $sides[0];
        $b = $sides[1];
        $c = $sides[2];
        if ($a + $b <= $c) return [];
        $PI = acos(-1.0);
        $A = acos(($b * $b + $c * $c - $a * $a) / (2.0 * $b * $c)) * 180.0 / $PI;
        $B = acos(($a * $a + $c * $c - $b * $b) / (2.0 * $a * $c)) * 180.0 / $PI;
        $C = 180.0 - $A - $B;
        return [$A, $B, $C];
    }
}
