<?php
// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

class Solution {
    /**
     * @param String[] $words
     * @return String
     */
    function longestWord($words) {
        $wordSet = array_flip($words);
        $best = '';

        foreach ($words as $word) {
            $prefix = $word;
            $valid = true;
            while ($prefix !== '') {
                if (!isset($wordSet[$prefix])) {
                    $valid = false;
                    break;
                }
                $prefix = substr($prefix, 0, -1);
            }

            if ($valid && (strlen($word) > strlen($best) || (strlen($word) === strlen($best) && $word < $best))) {
                $best = $word;
            }
        }

        return $best;
    }
}
