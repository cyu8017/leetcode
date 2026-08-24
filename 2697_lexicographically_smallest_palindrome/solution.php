<?php
// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution {
    function makeSmallestPalindrome($s) {
        $arr = str_split($s);
        $n = count($arr);
        for ($i = 0; $i < intdiv($n, 2); $i++) {
            $c = $arr[$i] < $arr[$n - 1 - $i] ? $arr[$i] : $arr[$n - 1 - $i];
            $arr[$i] = $arr[$n - 1 - $i] = $c;
        }
        return implode("", $arr);
    }
}
