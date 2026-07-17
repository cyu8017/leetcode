<?php
// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function sumBase($n, $k) {
        $total = 0;
        while ($n > 0) {
            $total += $n % $k;
            $n = intdiv($n, $k);
        }
        return $total;
    }
}
