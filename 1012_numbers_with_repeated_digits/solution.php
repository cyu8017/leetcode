<?php
// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function numDupDigitsAtMostN($n) {
        $digits = array_map('intval', str_split(strval($n)));
        $m = count($digits);

        $p = function ($a, $b) {
            $res = 1;
            for ($i = 0; $i < $b; $i++) {
                $res *= $a - $i;
            }
            return $res;
        };

        $totalUnique = 0;
        for ($length = 1; $length < $m; $length++) {
            $totalUnique += 9 * $p(9, $length - 1);
        }

        $used = [];
        $broken = false;
        for ($i = 0; $i < $m; $i++) {
            $d = $digits[$i];
            for ($x = ($i === 0 ? 1 : 0); $x < $d; $x++) {
                if (isset($used[$x])) {
                    continue;
                }
                $totalUnique += $p(9 - $i, $m - $i - 1);
            }
            if (isset($used[$d])) {
                $broken = true;
                break;
            }
            $used[$d] = true;
        }
        if (!$broken) {
            $totalUnique++;
        }
        return $n - $totalUnique;
    }
}
