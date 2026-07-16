<?php
// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

class Solution {
    /**
     * @param Integer $num
     * @return Boolean
     */
    function checkPerfectNumber($num) {
        return $this->check_perfect_number($num);
    }

    /**
     * @param Integer $num
     * @return Boolean
     */
    function check_perfect_number($num) {
        if ($num <= 1) {
            return false;
        }
        $total = 1;
        $limit = (int)sqrt($num);
        for ($divisor = 2; $divisor <= $limit; $divisor++) {
            if ($num % $divisor === 0) {
                $total += $divisor;
                $pair = intdiv($num, $divisor);
                if ($pair !== $divisor) {
                    $total += $pair;
                }
            }
        }
        return $total === $num;
    }
}
