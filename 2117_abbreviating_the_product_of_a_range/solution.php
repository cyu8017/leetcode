<?php
// LeetCode 2117 - Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/

class Solution {
    /**
     * @param Integer $left
     * @param Integer $right
     * @return String
     */
    function abbreviateProduct($left, $right) {
        $twos = 0;
        $fives = 0;
        for ($i = $left; $i <= $right; $i++) {
            $x = $i;
            while ($x % 2 === 0) { $twos++; $x = intdiv($x, 2); }
            while ($x % 5 === 0) { $fives++; $x = intdiv($x, 5); }
        }
        $zeros = min($twos, $fives);
        $MOD = "100000000000";
        $prod = "1";
        $extra2 = $twos - $zeros;
        $extra5 = $fives - $zeros;
        $logSum = 0.0;
        for ($i = $left; $i <= $right; $i++) {
            $x = $i;
            while ($x % 2 === 0) $x = intdiv($x, 2);
            while ($x % 5 === 0) $x = intdiv($x, 5);
            $prod = bcmul($prod, (string)$x);
            $prod = bcmod($prod, $MOD);
            $logSum += log10($x);
        }
        for ($i = 0; $i < $extra2; $i++) {
            $prod = bcmul($prod, "2");
            $prod = bcmod($prod, $MOD);
            $logSum += log10(2.0);
        }
        for ($i = 0; $i < $extra5; $i++) {
            $prod = bcmul($prod, "5");
            $prod = bcmod($prod, $MOD);
            $logSum += log10(5.0);
        }
        $fullLog = 0.0;
        for ($i = $left; $i <= $right; $i++) $fullLog += log10($i);
        $digits = (int)floor($fullLog) + 1;
        if ($digits <= 10) {
            $p = "1";
            for ($i = $left; $i <= $right; $i++) $p = bcmul($p, (string)$i);
            return $p;
        }
        $frac = $logSum - floor($logSum);
        $prefix = (int)floor(pow(10.0, $frac + 4));
        $suffix = (int)bcmod($prod, "100000");
        return $prefix . "e" . $zeros . str_pad((string)$suffix, 5, "0", STR_PAD_LEFT);
    }
}
