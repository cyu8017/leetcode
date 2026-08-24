<?php
// LeetCode 2119 - A Number After a Double Reversal
// https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution {
    /**
     * @param Integer $num
     * @return Boolean
     */
    function isSameAfterReversals($num) {
        return $num === 0 || $num % 10 !== 0;
    }
}
