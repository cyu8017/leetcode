<?php
// LeetCode 0343 - Integer Break
// https://leetcode.com/problems/integer-break/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function integerBreak($n) {
        return $this->integer_break($n);
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function integer_break($n) {
        if ($n <= 3) {
            return $n - 1;
        }

        $product = 1;
        while ($n > 4) {
            $product *= 3;
            $n -= 3;
        }

        return $product * $n;
    }
}
