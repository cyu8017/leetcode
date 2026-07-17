<?php
// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

class Solution {
    /**
     * @param String $word1
     * @param String $word2
     * @return String
     */
    function mergeAlternately($word1, $word2) {
        $out = '';
        $len1 = strlen($word1);
        $len2 = strlen($word2);
        $i = 0;
        $j = 0;
        while ($i < $len1 || $j < $len2) {
            if ($i < $len1) {
                $out .= $word1[$i++];
            }
            if ($j < $len2) {
                $out .= $word2[$j++];
            }
        }
        return $out;
    }
}
