<?php
// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

class Solution {
    /**
     * @param String[] $words
     * @return String[]
     */
    function findWords($words) {
        return $this->find_words($words);
    }

    /**
     * @param String[] $words
     * @return String[]
     */
    function find_words($words) {
        $rows = [
            array_flip(str_split('qwertyuiop')),
            array_flip(str_split('asdfghjkl')),
            array_flip(str_split('zxcvbnm')),
        ];

        $onOneRow = function ($word) use ($rows) {
            $letters = [];
            $length = strlen($word);
            for ($index = 0; $index < $length; $index++) {
                $char = $word[$index];
                if (ctype_alpha($char)) {
                    $letters[strtolower($char)] = true;
                }
            }
            foreach ($rows as $row) {
                $matches = true;
                foreach (array_keys($letters) as $letter) {
                    if (!isset($row[$letter])) {
                        $matches = false;
                        break;
                    }
                }
                if ($matches) {
                    return true;
                }
            }
            return false;
        };

        $result = [];
        foreach ($words as $word) {
            if ($onOneRow($word)) {
                $result[] = $word;
            }
        }
        return $result;
    }
}
