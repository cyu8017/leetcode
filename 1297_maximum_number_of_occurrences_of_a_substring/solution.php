<?php
// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

class Solution {
    /**
     * @param String $s
     * @param Integer $maxLetters
     * @param Integer $minSize
     * @param Integer $maxSize
     * @return Integer
     */
    function maxFreq($s, $maxLetters, $minSize, $maxSize) {
        $counts = [];
        $n = strlen($s);
        for ($i = 0; $i <= $n - $minSize; $i++) {
            $sub = substr($s, $i, $minSize);
            if (count(array_unique(str_split($sub))) <= $maxLetters) {
                $counts[$sub] = ($counts[$sub] ?? 0) + 1;
            }
        }
        return empty($counts) ? 0 : max($counts);
    }
}
