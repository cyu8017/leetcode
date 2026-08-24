<?php
// LeetCode 0461 - Hamming Distance
// https://leetcode.com/problems/hamming-distance/

class Solution {
    /**
     * @param int $x
     * @param int $y
     * @return int
     */
    function hammingDistance($x, $y) {
        return $this->hamming_distance($x, $y);
    }

    /**
     * @param int $x
     * @param int $y
     * @return int
     */
    function hamming_distance($x, $y) {
        $value = $x ^ $y;
        $count = 0;
        while ($value !== 0) {
            $count += $value & 1;
            $value >>= 1;
        }
        return $count;
    }
}
