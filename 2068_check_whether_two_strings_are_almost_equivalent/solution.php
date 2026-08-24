<?php
// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution {
    /**
     * @param String $word1
     * @param String $word2
     * @return Boolean
     */
    function checkAlmostEquivalent($word1, $word2) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($word1);
        for ($i = 0; $i < $n; $i++) {
            $freq[ord($word1[$i]) - 97]++;
            $freq[ord($word2[$i]) - 97]--;
        }
        foreach ($freq as $v) if ($v > 3 || $v < -3) return false;
        return true;
    }
}
