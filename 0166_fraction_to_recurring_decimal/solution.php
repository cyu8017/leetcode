<?php
// LeetCode 0166 - Fraction to Recurring Decimal
// https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution {
    function fractionToDecimal(int $numerator, int $denominator): string {
        if ($numerator === 0) return "0";
        $sign = (($numerator < 0) !== ($denominator < 0)) ? "-" : "";
        $numerator = abs($numerator);
        $denominator = abs($denominator);
        $integer = intdiv($numerator, $denominator);
        $remainder = $numerator % $denominator;
        if ($remainder === 0) return $sign . $integer;

        $parts = [$sign . $integer, "."];
        $seen = [];
        while ($remainder !== 0) {
            if (isset($seen[$remainder])) {
                array_splice($parts, $seen[$remainder], 0, "(");
                $parts[] = ")";
                break;
            }
            $seen[$remainder] = count($parts);
            $remainder *= 10;
            $parts[] = (string) intdiv($remainder, $denominator);
            $remainder %= $denominator;
        }
        return implode("", $parts);
    }
}
