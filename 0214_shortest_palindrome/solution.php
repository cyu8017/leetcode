<?php
// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

class Solution {
    function shortestPalindrome($s) {
        if ($s === '') {
            return '';
        }
        $combined = $s . '#' . strrev($s);
        $lps = 0;
        $pi = array_fill(0, strlen($combined), 0);
        for ($i = 1; $i < strlen($combined); $i++) {
            while ($lps > 0 && $combined[$i] !== $combined[$lps]) {
                $lps = $pi[$lps - 1];
            }
            if ($combined[$i] === $combined[$lps]) {
                $lps++;
            }
            $pi[$i] = $lps;
        }
        $prefixLen = $pi[strlen($combined) - 1];
        return strrev(substr($s, $prefixLen)) . $s;
    }
}
