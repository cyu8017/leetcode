<?php
// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

class Solution {
    /**
     * @param string[] $words
     * @return string[]
     */
    function findAllConcatenatedWordsInADict($words) {
        return $this->find_all_concatenated_words_in_a_dict($words);
    }

    /**
     * @param string[] $words
     * @return string[]
     */
    function find_all_concatenated_words_in_a_dict($words) {
        usort($words, function ($left, $right) {
            return strlen($left) <=> strlen($right);
        });
        $wordSet = array_flip($words);
        $result = [];

        $canForm = function ($word, $dictionary) {
            if ($word === "") {
                return true;
            }
            $length = strlen($word);
            $dp = array_fill(0, $length + 1, false);
            $dp[0] = true;
            for ($end = 1; $end <= $length; $end++) {
                for ($start = 0; $start < $end; $start++) {
                    if ($dp[$start] && isset($dictionary[substr($word, $start, $end - $start)])) {
                        $dp[$end] = true;
                        break;
                    }
                }
            }
            return $dp[$length];
        };

        foreach ($words as $word) {
            unset($wordSet[$word]);
            if ($canForm($word, $wordSet)) {
                $result[] = $word;
            }
            $wordSet[$word] = true;
        }
        return $result;
    }
}
