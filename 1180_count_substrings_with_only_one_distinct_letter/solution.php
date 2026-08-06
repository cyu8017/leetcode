<?php
// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function countLetters($s) {
        $ans = $length = 1;
        $n = strlen($s);
        for ($i = 1; $i < $n; $i++) {
            $length = ($s[$i] === $s[$i - 1]) ? $length + 1 : 1;
            $ans += $length;
        }
        return $ans;
    }
}
