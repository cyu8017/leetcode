<?php
// LeetCode 3783 - Mirror Distance of an Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution {
    function mirrorDistance($n) {
        $reverse = function($x) {
            $y = 0;
            for (; $x > 0; $x = intdiv($x, 10)) $y = $y * 10 + $x % 10;
            return $y;
        };
        return abs($n - $reverse($n));
    }
}
