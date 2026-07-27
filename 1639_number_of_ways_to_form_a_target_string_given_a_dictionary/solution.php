<?php
// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution {
    /**
     * @param String[] $words
     * @param String $target
     * @return Integer
     */
    function numWays($words, $target) {
        $MOD = 1000000007;
        $m = strlen($words[0]);
        $tlen = strlen($target);
        $dp = array_fill(0, $tlen + 1, 0);
        $dp[0] = 1;
        for ($j = 0; $j < $m; $j++) {
            $count = array_fill(0, 26, 0);
            foreach ($words as $word) {
                $count[ord($word[$j]) - 97]++;
            }
            for ($i = min($j + 1, $tlen); $i > 0; $i--) {
                $dp[$i] = ($dp[$i] + $dp[$i - 1] * $count[ord($target[$i - 1]) - 97]) % $MOD;
            }
        }
        return $dp[$tlen];
    }
}
