<?php
// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function truncateSentence($s, $k) {
        $words = preg_split('/\s+/', $s, -1, PREG_SPLIT_NO_EMPTY);
        return implode(' ', array_slice($words, 0, $k));
    }
}
