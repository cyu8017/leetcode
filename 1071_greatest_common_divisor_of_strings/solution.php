<?php
// LeetCode 1071 - Greatest Common Divisor of Strings
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution {
    /**
     * @param String $str1
     * @param String $str2
     * @return String
     */
    function gcdOfStrings($str1, $str2) {
        if ($str1 . $str2 !== $str2 . $str1) {
            return "";
        }
        $a = strlen($str1);
        $b = strlen($str2);
        while ($b !== 0) {
            $t = $b;
            $b = $a % $b;
            $a = $t;
        }
        return substr($str1, 0, $a);
    }
}
