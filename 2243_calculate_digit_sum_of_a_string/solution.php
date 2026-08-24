<?php
// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution {
    function digitSum($s, $k) {
        while (strlen($s) > $k) {
            $next = '';
            $n = strlen($s);
            for ($i = 0; $i < $n; $i += $k) {
                $sum = 0;
                $end = min($i + $k, $n);
                for ($j = $i; $j < $end; $j++) $sum += ord($s[$j]) - 48;
                $next .= (string)$sum;
            }
            $s = $next;
        }
        return $s;
    }
}
