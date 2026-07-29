<?php
// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function clumsy($n) {
        $stack = [$n];
        $n--;
        $op = 0;
        while ($n > 0) {
            if ($op % 4 === 0) {
                $stack[] = array_pop($stack) * $n;
            } elseif ($op % 4 === 1) {
                $stack[] = intdiv(array_pop($stack), $n);
            } elseif ($op % 4 === 2) {
                $stack[] = $n;
            } else {
                $stack[] = -$n;
            }
            $n--;
            $op++;
        }
        return array_sum($stack);
    }
}
