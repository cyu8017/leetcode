<?php
// LeetCode 0338 - Counting Bits
// https://leetcode.com/problems/counting-bits/

class Solution {
    /**
     * @param Integer $n
     * @return Integer[]
     */
    function countBits($n) {
        return $this->count_bits($n);
    }

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function count_bits($n) {
        $result = array_fill(0, $n + 1, 0);
        for ($index = 1; $index <= $n; $index++) {
            $result[$index] = $result[$index & ($index - 1)] + 1;
        }
        return $result;
    }
}
