<?php
// LeetCode 1903 - Largest Odd Number in String
// https://leetcode.com/problems/largest-odd-number-in-string/

class Solution {
    function largestOddNumber($num) {
        for ($i = strlen($num) - 1; $i >= 0; $i--) {
            if ((int)$num[$i] % 2 === 1) {
                return substr($num, 0, $i + 1);
            }
        }
        return "";
    }
}
