<?php
// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

class Solution {
    /**
     * @param Integer $num
     * @return Integer
     */
    function smallestNumber($num) {
        $neg = $num < 0;
        if ($neg) $num = -$num;
        if ($num === 0) return 0;
        $digits = [];
        while ($num > 0) {
            $digits[] = $num % 10;
            $num = intdiv($num, 10);
        }
        if ($neg) {
            rsort($digits);
            $ans = 0;
            foreach ($digits as $d) $ans = $ans * 10 + $d;
            return -$ans;
        }
        sort($digits);
        if ($digits[0] === 0) {
            for ($i = 1; $i < count($digits); $i++) {
                if ($digits[$i] !== 0) {
                    $t = $digits[0];
                    $digits[0] = $digits[$i];
                    $digits[$i] = $t;
                    break;
                }
            }
        }
        $res = 0;
        foreach ($digits as $d) $res = $res * 10 + $d;
        return $res;
    }
}
