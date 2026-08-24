<?php
// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

class Solution {
    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function interchangeableRectangles($rectangles) {
        $gcd = function ($a, $b) {
            while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
            return $a;
        };
        $freq = [];
        $ans = 0;
        foreach ($rectangles as $rect) {
            $g = $gcd($rect[0], $rect[1]);
            $key = intdiv($rect[0], $g) . "/" . intdiv($rect[1], $g);
            $f = $freq[$key] ?? 0;
            $ans += $f;
            $freq[$key] = $f + 1;
        }
        return $ans;
    }
}
