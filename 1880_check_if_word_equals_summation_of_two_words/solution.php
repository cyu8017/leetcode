<?php
// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    private function value($word) {
        $digits = '';
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $digits .= (string)(ord($word[$i]) - ord('a'));
        }
        return (int)$digits;
    }

    /**
     * @param String $firstWord
     * @param String $secondWord
     * @param String $targetWord
     * @return Boolean
     */
    function isSumEqual($firstWord, $secondWord, $targetWord) {
        return $this->value($firstWord) + $this->value($secondWord) === $this->value($targetWord);
    }
}
