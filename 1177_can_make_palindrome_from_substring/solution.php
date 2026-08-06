<?php
// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

class Solution {
    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function canMakePaliQueries($s, $queries) {
        $prefix = [0];
        $mask = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $mask ^= 1 << (ord($s[$i]) - 97);
            $prefix[] = $mask;
        }
        $ans = [];
        foreach ($queries as [$left, $right, $k]) {
            $bits = $prefix[$right + 1] ^ $prefix[$left];
            $ans[] = (substr_count(decbin($bits), '1') >> 1) <= $k;
        }
        return $ans;
    }
}
