<?php
// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

class Solution {
    function kthPalindrome($queries, $intLength) {
        $half = ($intLength + 1) >> 1;
        $start = 1;
        for ($i = 1; $i < $half; $i++) $start *= 10;
        $total = $start * 9;
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $q = $queries[$i];
            if ($q > $total) { $ans[$i] = -1; continue; }
            $left = $start + $q - 1;
            $pal = $left;
            $x = $left;
            if ($intLength % 2 !== 0) $x = intdiv($x, 10);
            while ($x > 0) { $pal = $pal * 10 + $x % 10; $x = intdiv($x, 10); }
            $ans[$i] = $pal;
        }
        return $ans;
    }
}
