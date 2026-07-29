<?php
// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

class Solution {
    /**
     * @param String $text
     * @param String $first
     * @param String $second
     * @return String[]
     */
    function findOcurrences($text, $first, $second) {
        $words = explode(" ", $text);
        $ans = [];
        $n = count($words);
        for ($i = 0; $i < $n - 2; $i++) {
            if ($words[$i] === $first && $words[$i + 1] === $second) {
                $ans[] = $words[$i + 2];
            }
        }
        return $ans;
    }
}
