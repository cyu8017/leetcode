<?php
// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

class Solution {
    function longestWord($words) {
        sort($words);
        $built = ['' => true];
        $best = '';
        foreach ($words as $word) {
            $prefix = substr($word, 0, strlen($word) - 1);
            if (isset($built[$prefix])) {
                $built[$word] = true;
                if (strlen($word) > strlen($best)) $best = $word;
            }
        }
        return $best;
    }
}
