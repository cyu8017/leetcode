<?php
// LeetCode 0320 - Generalized Abbreviation
// https://leetcode.com/problems/generalized-abbreviation/

class Solution {
    /**
     * @param String $word
     * @return String[]
     */
    function generateAbbreviations($word) {
        $result = [];
        $backtrack = function ($index, $path, $count) use (&$backtrack, $word, &$result) {
            $length = strlen($word);
            if ($index === $length) {
                $result[] = $path . ($count === 0 ? '' : (string) $count);
                return;
            }
            $backtrack($index + 1, $path, $count + 1);
            $nextPath = $path . ($count === 0 ? '' : (string) $count) . $word[$index];
            $backtrack($index + 1, $nextPath, 0);
        };
        $backtrack(0, '', 0);
        return $result;
    }
}
