<?php
// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution {
    /**
     * @param String $word1
     * @param String $word2
     * @return String
     */
    function largestMerge($word1, $word2) {
        $len1 = strlen($word1);
        $len2 = strlen($word2);
        $i = 0;
        $j = 0;
        $out = '';
        while ($i < $len1 && $j < $len2) {
            if (strcmp(substr($word1, $i), substr($word2, $j)) > 0) {
                $out .= $word1[$i];
                $i++;
            } else {
                $out .= $word2[$j];
                $j++;
            }
        }
        return $out . substr($word1, $i) . substr($word2, $j);
    }
}
