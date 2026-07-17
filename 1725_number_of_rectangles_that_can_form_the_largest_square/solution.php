<?php
// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution {
    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function countGoodRectangles($rectangles) {
        $best = 0;
        $count = 0;
        foreach ($rectangles as $rect) {
            $side = min($rect[0], $rect[1]);
            if ($side > $best) {
                $best = $side;
                $count = 1;
            } elseif ($side === $best) {
                $count++;
            }
        }
        return $count;
    }
}
