<?php
// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

class Solution {
    function minExtraChar($s, $dictionary) {
        $dict = array_flip($dictionary);
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, $n);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            $dp[$i + 1] = min($dp[$i + 1], $dp[$i] + 1);
            for ($j = $i + 1; $j <= $n; $j++) {
                $sub = substr($s, $i, $j - $i);
                if (isset($dict[$sub])) $dp[$j] = min($dp[$j], $dp[$i]);
            }
        }
        return $dp[$n];
    }
}
