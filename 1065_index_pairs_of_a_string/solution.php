<?php
// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

class Solution {
    /**
     * @param String $text
     * @param String[] $words
     * @return Integer[][]
     */
    function indexPairs($text, $words) {
        $wordSet = array_flip($words);
        $ans = [];
        $n = strlen($text);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i; $j < $n; $j++) {
                if (isset($wordSet[substr($text, $i, $j - $i + 1)])) {
                    $ans[] = [$i, $j];
                }
            }
        }
        return $ans;
    }
}
