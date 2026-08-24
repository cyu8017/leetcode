<?php
// LeetCode 0342 - Power of Four
// https://leetcode.com/problems/power-of-four/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function isPowerOfFour($n) {
        return $this->is_power_of_four($n);
    }

    /**
     * @param Integer $n
     * @return Boolean
     */
    function is_power_of_four($n) {
        return $n > 0 && ($n & ($n - 1)) === 0 && $n % 3 === 1;
    }
}
