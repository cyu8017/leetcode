<?php
// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

class Solution {
    /**
     * @param Integer $num
     * @return String
     */
    function convertToBase7($num) {
        return $this->convert_to_base7($num);
    }

    /**
     * @param Integer $num
     * @return String
     */
    function convert_to_base7($num) {
        if ($num === 0) {
            return "0";
        }
        $negative = $num < 0;
        $num = abs($num);
        $digits = [];
        while ($num > 0) {
            $digits[] = (string)($num % 7);
            $num = intdiv($num, 7);
        }
        $result = implode("", array_reverse($digits));
        return $negative ? "-{$result}" : $result;
    }
}
