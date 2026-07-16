<?php
// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

class Solution {
    /**
     * @param String[] $words
     * @return String[]
     */
    function wordsAbbreviation($words) {
        return $this->words_abbreviation($words);
    }

    /**
     * @param String[] $words
     * @return String[]
     */
    function words_abbreviation($words) {
        $prefixes = array_fill(0, count($words), 1);
        $changed = true;
        while ($changed) {
            $changed = false;
            $groups = [];
            foreach ($words as $index => $word) {
                $key = $this->abbreviate($word, $prefixes[$index]);
                if (!isset($groups[$key])) {
                    $groups[$key] = [];
                }
                $groups[$key][] = $index;
            }
            foreach ($groups as $indices) {
                if (count($indices) <= 1) {
                    continue;
                }
                $changed = true;
                foreach ($indices as $index) {
                    $prefixes[$index]++;
                }
            }
        }
        $result = [];
        foreach ($words as $index => $word) {
            $result[] = $this->abbreviate($word, $prefixes[$index]);
        }
        return $result;
    }

    /**
     * @param String $word
     * @param Integer $prefix
     * @return String
     */
    private function abbreviate($word, $prefix) {
        if ($prefix + 2 >= strlen($word)) {
            return $word;
        }
        $middle = strlen($word) - $prefix - 1;
        $candidate = substr($word, 0, $prefix) . $middle . $word[strlen($word) - 1];
        return strlen($candidate) < strlen($word) ? $candidate : $word;
    }
}
