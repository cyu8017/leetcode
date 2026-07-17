<?php
// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function halvesAreAlike($s) {
        $vowels = 'aeiouAEIOU';
        $n = strlen($s);
        $mid = intdiv($n, 2);
        $balance = 0;
        for ($i = 0; $i < $n; $i++) {
            if (strpos($vowels, $s[$i]) !== false) {
                $balance += $i < $mid ? 1 : -1;
            }
        }
        return $balance === 0;
    }
}
