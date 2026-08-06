<?php
// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function subtractProductAndSum($n) {
        $product = 1;
        $total = 0;
        while ($n) {
            $digit = $n % 10;
            $n = intdiv($n, 10);
            $product *= $digit;
            $total += $digit;
        }
        return $product - $total;
    }
}
