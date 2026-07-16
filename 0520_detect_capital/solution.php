<?php
// LeetCode 0520 - Detect Capital
// https://leetcode.com/problems/detect-capital/

class Solution {
    /**
     * @param String $word
     * @return Boolean
     */
    function detectCapitalUse($word) {
        return $this->detect_capital_use($word);
    }

    /**
     * @param String $word
     * @return Boolean
     */
    function detect_capital_use($word) {
        return $word === strtoupper($word)
            || $word === strtolower($word)
            || $word === ucfirst(strtolower($word));
    }
}
