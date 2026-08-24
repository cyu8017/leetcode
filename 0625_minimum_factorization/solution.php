<?php
// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

class Solution {
    function smallestFactorization($num) {
        if ($num < 10) return $num;
        $digits = [];
        for ($digit = 9; $digit >= 2; --$digit) {
            while ($num % $digit === 0) {
                $digits[] = $digit;
                $num = intdiv($num, $digit);
            }
        }
        if ($num !== 1) return 0;
        $result = 0;
        for ($i = count($digits) - 1; $i >= 0; --$i) {
            $result = $result * 10 + $digits[$i];
            if ($result > 2147483647) return 0;
        }
        return $result;
    }
}
