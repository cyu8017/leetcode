<?php
// LeetCode 1009 - Complement of Base 10 Integer
// https://leetcode.com/problems/complement-of-base-10-integer/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function bitwiseComplement($n) {
        if ($n === 0) {
            return 1;
        }
        $mask = (1 << (int)floor(log($n, 2) + 1)) - 1;
        return $n ^ $mask;
    }
}
