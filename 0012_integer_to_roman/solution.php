<?php
// LeetCode 0012 - Integer to Roman
// https://leetcode.com/problems/integer-to-roman/

class Solution {
    /**
     * @param Integer $num
     * @return String
     */
    function intToRoman($num) {
        $values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
        $symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        $result = "";

        for ($i = 0; $i < count($values); $i++) {
            while ($num >= $values[$i]) {
                $result .= $symbols[$i];
                $num -= $values[$i];
            }
        }

        return $result;
    }
}
