<?php
// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

class Solution {
    function reverseOnlyLetters($s) {
        $arr = str_split($s);
        $i = 0;
        $j = count($arr) - 1;
        $isLetter = function ($c) {
            return ($c >= 'a' && $c <= 'z') || ($c >= 'A' && $c <= 'Z');
        };
        while ($i < $j) {
            while ($i < $j && !$isLetter($arr[$i])) $i++;
            while ($i < $j && !$isLetter($arr[$j])) $j--;
            $tmp = $arr[$i];
            $arr[$i] = $arr[$j];
            $arr[$j] = $tmp;
            $i++;
            $j--;
        }
        return implode("", $arr);
    }
}
