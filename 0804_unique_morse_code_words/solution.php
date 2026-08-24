<?php
// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    function uniqueMorseRepresentations($words) {
        $codes = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."
        ];
        $seen = [];
        foreach ($words as $word) {
            $code = "";
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) $code .= $codes[ord($word[$i]) - 97];
            $seen[$code] = true;
        }
        return count($seen);
    }
}
