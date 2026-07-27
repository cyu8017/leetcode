<?php
// LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero
// https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function minimumOneBitOperations($n) {
        $ans = 0;
        while ($n) {
            $ans ^= $n;
            $n >>= 1;
        }
        return $ans;
    }
}
