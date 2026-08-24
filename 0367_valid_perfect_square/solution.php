<?php
// LeetCode 0367 - Valid Perfect Square
// https://leetcode.com/problems/valid-perfect-square/

class Solution {
    /**
     * @param Integer $num
     * @return Boolean
     */
    function isPerfectSquare($num) {
        return $this->is_perfect_square($num);
    }

    /**
     * @param Integer $num
     * @return Boolean
     */
    function is_perfect_square($num) {
        $left = 1;
        $right = $num;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            $square = $mid * $mid;
            if ($square === $num) {
                return true;
            }
            if ($square < $num) {
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }

        return false;
    }
}
