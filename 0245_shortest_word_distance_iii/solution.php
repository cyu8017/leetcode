<?php
// LeetCode 0245 - Shortest Word Distance III
// https://leetcode.com/problems/shortest-word-distance-iii/

class Solution {
    /**
     * @param String[] $wordsDict
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function shortestWordDistance($wordsDict, $word1, $word2) {
        if ($word1 === $word2) {
            $previous = -1;
            $best = PHP_INT_MAX;
            foreach ($wordsDict as $index => $word) {
                if ($word === $word1) {
                    if ($previous >= 0) {
                        $best = min($best, $index - $previous);
                    }
                    $previous = $index;
                }
            }
            return $best;
        }

        $index1 = -1;
        $index2 = -1;
        $best = PHP_INT_MAX;
        foreach ($wordsDict as $index => $word) {
            if ($word === $word1) {
                $index1 = $index;
                if ($index2 >= 0) {
                    $best = min($best, $index - $index2);
                }
            }
            if ($word === $word2) {
                $index2 = $index;
                if ($index1 >= 0) {
                    $best = min($best, $index - $index1);
                }
            }
        }
        return $best;
    }
}
