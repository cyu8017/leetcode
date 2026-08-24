<?php
// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution {
    function shortestBeautifulSubstring($s, $k) {
        $ans = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ones = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($s[$j] === '1') $ones++;
                if ($ones === $k) {
                    $cand = substr($s, $i, $j - $i + 1);
                    if ($ans === '' || strlen($cand) < strlen($ans) || (strlen($cand) === strlen($ans) && $cand < $ans))
                        $ans = $cand;
                    break;
                }
                if ($ones > $k) break;
            }
        }
        return $ans;
    }
}
