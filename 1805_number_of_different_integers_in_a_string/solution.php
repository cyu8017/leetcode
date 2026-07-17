<?php
// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function numDifferentIntegers($word) {
        $seen = [];
        if (preg_match_all('/\d+/', $word, $matches)) {
            foreach ($matches[0] as $match) {
                $seen[(int)$match] = true;
            }
        }
        return count($seen);
    }
}
