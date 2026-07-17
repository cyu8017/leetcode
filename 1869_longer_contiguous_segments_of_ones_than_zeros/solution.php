<?php
// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function checkZeroOnes($s) {
        $maxZeros = 0;
        $maxOnes = 0;
        $zeros = 0;
        $ones = 0;

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '0') {
                $zeros++;
                $ones = 0;
                $maxZeros = max($maxZeros, $zeros);
            } else {
                $ones++;
                $zeros = 0;
                $maxOnes = max($maxOnes, $ones);
            }
        }

        return $maxOnes > $maxZeros;
    }
}
