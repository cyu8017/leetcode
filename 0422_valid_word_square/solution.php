<?php
// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

class Solution {
    /**
     * @param String[] $words
     * @return Boolean
     */
    function validWordSquare($words) {
        return $this->valid_word_square($words);
    }

    /**
     * @param String[] $words
     * @return Boolean
     */
    function valid_word_square($words) {
        foreach ($words as $row => $word) {
            $length = strlen($word);
            for ($col = 0; $col < $length; $col++) {
                if ($col >= count($words)) {
                    return false;
                }
                if ($row >= strlen($words[$col])) {
                    return false;
                }
                if ($words[$col][$row] !== $word[$col]) {
                    return false;
                }
            }
        }
        return true;
    }
}
