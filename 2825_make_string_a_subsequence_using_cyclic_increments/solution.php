<?php
// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution {
    function canMakeSubsequence($str1, $str2) {
        $j = 0;
        $n1 = strlen($str1);
        $n2 = strlen($str2);
        for ($i = 0; $i < $n1 && $j < $n2; $i++) {
            $a = ord($str1[$i]) - 97;
            $b = ord($str2[$j]) - 97;
            if ($a === $b || ($a + 1) % 26 === $b) $j++;
        }
        return $j === $n2;
    }
}
