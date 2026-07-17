<?php
// LeetCode 1771 - Maximize Palindrome Length From Subsequences
// https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

class Solution {
    /**
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function longestPalindrome($word1, $word2) {
        $s = $word1 . $word2;
        $n = strlen($s);
        $n1 = strlen($word1);
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        $ans = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $dp[$i][$i] = 1;
            for ($j = $i + 1; $j < $n; $j++) {
                if ($s[$i] === $s[$j]) {
                    $dp[$i][$j] = ($j === $i + 1) ? 2 : $dp[$i + 1][$j - 1] + 2;
                    if ($i < $n1 && $n1 <= $j) {
                        $ans = max($ans, $dp[$i][$j]);
                    }
                } else {
                    $dp[$i][$j] = max($dp[$i + 1][$j], $dp[$i][$j - 1]);
                }
            }
        }
        return $ans;
    }
}
