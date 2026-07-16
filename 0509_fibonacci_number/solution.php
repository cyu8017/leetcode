<?php
// LeetCode 0509 - Fibonacci Number
// https://leetcode.com/problems/fibonacci-number/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function fib($n) {
        if ($n <= 1) {
            return $n;
        }
        $previous = 0;
        $current = 1;
        for ($index = 2; $index <= $n; $index++) {
            [$previous, $current] = [$current, $previous + $current];
        }
        return $current;
    }
}
