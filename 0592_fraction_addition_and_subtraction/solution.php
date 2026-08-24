<?php
// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution {
    function fractionAddition($expression) {
        $gcd = function($a, $b) {
            $a = abs($a); $b = abs($b);
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $numerator = 0;
        $denominator = 1;
        $i = 0;
        $len = strlen($expression);
        while ($i < $len) {
            $sign = 1;
            if ($expression[$i] === "+" || $expression[$i] === "-") {
                if ($expression[$i] === "-") $sign = -1;
                ++$i;
            }
            $a = 0;
            while ($i < $len && $expression[$i] >= "0" && $expression[$i] <= "9") {
                $a = $a * 10 + (ord($expression[$i]) - 48);
                ++$i;
            }
            $a *= $sign;
            ++$i;
            $b = 0;
            while ($i < $len && $expression[$i] >= "0" && $expression[$i] <= "9") {
                $b = $b * 10 + (ord($expression[$i]) - 48);
                ++$i;
            }
            $numerator = $numerator * $b + $a * $denominator;
            $denominator *= $b;
            $g = $gcd($numerator, $denominator);
            $numerator = intdiv($numerator, $g);
            $denominator = intdiv($denominator, $g);
        }
        return $numerator . "/" . $denominator;
    }
}
