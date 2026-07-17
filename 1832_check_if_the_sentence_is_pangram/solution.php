<?php
// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution {
    /**
     * @param String $sentence
     * @return Boolean
     */
    function checkIfPangram($sentence) {
        return count(array_unique(str_split($sentence))) === 26;
    }
}
