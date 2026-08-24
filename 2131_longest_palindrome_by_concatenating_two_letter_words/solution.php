<?php
// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    function longestPalindrome($words) {
        $freq = [];
        foreach ($words as $w) $freq[$w] = ($freq[$w] ?? 0) + 1;
        $ans = 0;
        $center = false;
        foreach ($freq as $w => $c) {
            $rev = $w[1] . $w[0];
            if ($w[0] === $w[1]) {
                $ans += intdiv($c, 2) * 4;
                if ($c % 2 !== 0) $center = true;
            } else if ($w < $rev) {
                $ans += min($c, $freq[$rev] ?? 0) * 4;
            }
        }
        if ($center) $ans += 2;
        return $ans;
    }
}
