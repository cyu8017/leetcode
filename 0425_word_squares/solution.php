<?php
// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

class Solution {
    /**
     * @param String[] $words
     * @return String[][]
     */
    function wordSquares($words) {
        return $this->word_squares($words);
    }

    /**
     * @param String[] $words
     * @return String[][]
     */
    function word_squares($words) {
        sort($words);
        $length = strlen($words[0]);
        $prefixMap = ['' => $words];
        foreach ($words as $word) {
            for ($index = 0; $index < strlen($word); $index++) {
                $prefix = substr($word, 0, $index + 1);
                if (!isset($prefixMap[$prefix])) {
                    $prefixMap[$prefix] = [];
                }
                $prefixMap[$prefix][] = $word;
            }
        }

        $squares = [];
        $current = [];
        $this->buildWordSquares($prefixMap, $length, 0, $current, $squares);
        return $squares;
    }

    /**
     * @param array<string, String[]> $prefixMap
     * @param int $length
     * @param int $row
     * @param String[] $current
     * @param String[][] $squares
     */
    private function buildWordSquares($prefixMap, $length, $row, &$current, &$squares) {
        if ($row === $length) {
            $squares[] = $current;
            return;
        }

        $prefix = '';
        foreach ($current as $word) {
            $prefix .= $word[$row];
        }
        foreach ($prefixMap[$prefix] ?? [] as $candidate) {
            $current[] = $candidate;
            $this->buildWordSquares($prefixMap, $length, $row + 1, $current, $squares);
            array_pop($current);
        }
    }
}
