<?php
// LeetCode 0371 - Sum of Two Integers
// https://leetcode.com/problems/sum-of-two-integers/

class Solution {
    /**
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function getSum($a, $b) {
        return $this->get_sum($a, $b);
    }

    /**
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function get_sum($a, $b) {
        $mask = 0xFFFFFFFF;

        while ($b !== 0) {
            $carry = ($a & $b) << 1;
            $a = ($a ^ $b) & $mask;
            $b = $carry & $mask;
        }

        return $a <= 0x7FFFFFFF ? $a : ~($a ^ $mask);
    }
}
