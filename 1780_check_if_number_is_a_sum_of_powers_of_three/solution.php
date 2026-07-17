<?php
// LeetCode 1780 - Check if Number is a Sum of Powers of Three
// https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function checkPowersOfThree($n) {
        while ($n > 0) {
            if ($n % 3 === 2) {
                return false;
            }
            $n = intdiv($n, 3);
        }
        return true;
    }
}
