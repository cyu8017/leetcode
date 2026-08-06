<?php
// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

class Solution {
    /**
     * @param String $text1
     * @param String $text2
     * @return Integer
     */
    function longestCommonSubsequence($text1, $text2) {
        $m = strlen($text1);
        $n = strlen($text2);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $m; $i++) {
            $prev = 0;
            for ($j = 1; $j <= $n; $j++) {
                $cur = $dp[$j];
                if ($text1[$i - 1] === $text2[$j - 1]) {
                    $dp[$j] = $prev + 1;
                } else {
                    $dp[$j] = max($dp[$j], $dp[$j - 1]);
                }
                $prev = $cur;
            }
        }
        return $dp[$n];
    }
}
