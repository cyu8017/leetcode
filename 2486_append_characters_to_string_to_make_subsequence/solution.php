<?php
// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution {
    function appendCharacters($s, $t) {
        $j = 0;
        $sn = strlen($s);
        $tn = strlen($t);
        for ($i = 0; $i < $sn && $j < $tn; $i++) {
            if ($s[$i] === $t[$j]) $j++;
        }
        return $tn - $j;
    }
}
