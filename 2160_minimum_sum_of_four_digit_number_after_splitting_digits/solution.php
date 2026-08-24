<?php
// LeetCode 2160 - Minimum Sum of Four Digit Number After Splitting Digits
// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution {
    /**
     * @param Integer $num
     * @return Integer
     */
    function minimumSum($num) {
        $d = [intdiv($num, 1000), intdiv($num, 100) % 10, intdiv($num, 10) % 10, $num % 10];
        sort($d);
        return 10 * $d[0] + $d[2] + 10 * $d[1] + $d[3];
    }
}
