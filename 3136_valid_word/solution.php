<?php
// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

class Solution {
    function isValid($word) {
        if (strlen($word) < 3) return false;
        $hasVowel = false;
        $hasConsonant = false;
        $vs = array_fill(0, 26, false);
        foreach (str_split("aeiou") as $c) $vs[ord($c) - 97] = true;
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $c = $word[$i];
            if (ctype_alpha($c)) {
                $lower = strtolower($c);
                if ($vs[ord($lower) - 97]) $hasVowel = true;
                else $hasConsonant = true;
            } else if (!ctype_digit($c)) {
                return false;
            }
        }
        return $hasVowel && $hasConsonant;
    }
}
