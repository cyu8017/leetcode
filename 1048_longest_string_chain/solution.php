<?php
// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    function longestStrChain($words) {
        usort($words, function ($a, $b) {
            return strlen($a) - strlen($b);
        });
        $dp = [];
        $ans = 1;
        foreach ($words as $w) {
            $dp[$w] = 1;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $prev = substr($w, 0, $i) . substr($w, $i + 1);
                if (isset($dp[$prev])) {
                    $dp[$w] = max($dp[$w], $dp[$prev] + 1);
                }
            }
            $ans = max($ans, $dp[$w]);
        }
        return $ans;
    }
}
