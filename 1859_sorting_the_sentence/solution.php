<?php
// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function sortSentence($s) {
        $tokens = preg_split('/\s+/', $s, -1, PREG_SPLIT_NO_EMPTY);
        $ordered = array_fill(0, count($tokens), '');

        foreach ($tokens as $token) {
            $position = (int)substr($token, -1) - 1;
            $ordered[$position] = substr($token, 0, -1);
        }

        return implode(' ', $ordered);
    }
}
