<?php
// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function replaceDigits($s) {
        $chars = str_split($s);
        for ($i = 1; $i < count($chars); $i += 2) {
            $chars[$i] = chr(ord($chars[$i - 1]) + (int)$chars[$i]);
        }
        return implode("", $chars);
    }
}
