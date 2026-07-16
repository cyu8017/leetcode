<?php
// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution {
    /**
     * @param String $s
     * @param String[] $dictionary
     * @return String
     */
    function findLongestWord($s, $dictionary) {
        return $this->find_longest_word($s, $dictionary);
    }

    /**
     * @param String $s
     * @param String[] $dictionary
     * @return String
     */
    function find_longest_word($s, $dictionary) {
        $best = "";
        foreach ($dictionary as $word) {
            if (!$this->isSubsequence($s, $word)) {
                continue;
            }
            if (strlen($word) > strlen($best) || (strlen($word) === strlen($best) && $word < $best)) {
                $best = $word;
            }
        }
        return $best;
    }

    /**
     * @param String $source
     * @param String $word
     * @return Boolean
     */
    private function isSubsequence($source, $word) {
        $index = 0;
        $length = strlen($word);
        $sourceLength = strlen($source);
        for ($i = 0; $i < $sourceLength; $i++) {
            if ($index < $length && $word[$index] === $source[$i]) {
                $index++;
            }
        }
        return $index === $length;
    }
}
