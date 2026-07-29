<?php
// LeetCode 1015 - Smallest Integer Divisible by K
// https://leetcode.com/problems/smallest-integer-divisible-by-k/

class Solution {
    /**
     * @param Integer $k
     * @return Integer
     */
    function smallestRepunitDivByK($k) {
        if ($k % 2 === 0 || $k % 5 === 0) {
            return -1;
        }
        $rem = 0;
        for ($length = 1; $length <= $k; $length++) {
            $rem = ($rem * 10 + 1) % $k;
            if ($rem === 0) {
                return $length;
            }
        }
        return -1;
    }
}
