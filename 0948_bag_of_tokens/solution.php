<?php
// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

class Solution {
    function bagOfTokensScore($tokens, $power) {
        sort($tokens);
        $i = 0;
        $j = count($tokens) - 1;
        $score = 0;
        $ans = 0;
        while ($i <= $j) {
            if ($power >= $tokens[$i]) {
                $power -= $tokens[$i++];
                $score++;
                $ans = max($ans, $score);
            } elseif ($score > 0) {
                $power += $tokens[$j--];
                $score--;
            } else break;
        }
        return $ans;
    }
}
